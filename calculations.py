"""
Módulo contendo a lógica de cálculo para a aplicação MinSORTING.
Implementa as fórmulas de decantação e modelagem de distribuição granulométrica.
"""

import numpy as np
import pandas as pd
from scipy import stats
from data_store import (
    FLUID_PROPERTIES, MINERAL_PROPERTIES, MINERAL_ORDER,
    PROVENANCE_COMPOSITIONS, GRAVITY, PHI_TO_MM, MM_TO_PHI
)

def calculate_bulk_density(provenance_composition, calc_densities):
    """
    Calcula a densidade bulk do sedimento.
    
    Args:
        provenance_composition (dict): Composição da proveniência em porcentagem
        calc_densities (dict): Densidades de cálculo para cada mineral
    
    Returns:
        float: Densidade bulk em g/cm³
    """
    return sum(
        provenance_composition[mineral] * calc_densities[mineral]
        for mineral in provenance_composition
    ) / 100

def get_settling_equations(fluid_type, dm):
    """
    Seleciona as equações apropriadas baseado no tipo de fluido e tamanho.
    
    Args:
        fluid_type (str): Tipo de fluido ('Freshwater', 'Seawater', 'Air')
        dm (float): Diâmetro médio em phi
    
    Returns:
        tuple: Funções para calcular velocidade de decantação e size-shift
    """
    if fluid_type in ['Freshwater', 'Seawater']:
        if dm > 3.5:  # Stokes law
            def settling_velocity(d, rho_p, rho_f, mu):
                return (GRAVITY * (rho_p - rho_f) * d**2) / (18 * mu)
            
            def size_shift(rho_p, rho_ref=2.65):
                return np.log2(np.sqrt(rho_p / rho_ref))
        else:  # Cheng equation
            def settling_velocity(d, rho_p, rho_f, mu):
                return (GRAVITY * (rho_p - rho_f) * d**2) / (18 * mu * (1 + 0.15 * d))
            
            def size_shift(rho_p, rho_ref=2.65):
                return np.log2(np.sqrt(rho_p / rho_ref))
    else:  # Air
        def settling_velocity(d, rho_p, rho_f, mu):
            return (GRAVITY * (rho_p - rho_f) * d**2) / (18 * mu)
        
        def size_shift(rho_p, rho_ref=2.65):
            return np.log2(np.sqrt(rho_p / rho_ref))
    
    return settling_velocity, size_shift

def calculate_mineral_distribution(
    dm, sigma, fluid_type, provenance_name,
    density_option='standard', fine_tuning_densities=None
):
    """
    Calcula a distribuição granulométrica para cada mineral.
    
    Args:
        dm (float): Diâmetro médio em phi
        sigma (float): Sorting em phi
        fluid_type (str): Tipo de fluido
        provenance_name (str): Nome da proveniência
        density_option (str): 'standard' ou 'fine_tuning'
        fine_tuning_densities (dict): Densidades ajustadas se density_option='fine_tuning'
    
    Returns:
        pd.DataFrame: DataFrame com a distribuição granulométrica
    """
    # Recupera propriedades do fluido
    fluid_props = FLUID_PROPERTIES[fluid_type]
    rho_f = fluid_props['density']
    mu = fluid_props['viscosity']
    
    # Recupera composição da proveniência
    provenance_composition = PROVENANCE_COMPOSITIONS[provenance_name]
    
    # Determina densidades de cálculo
    calc_densities = {}
    if density_option == 'standard':
        calc_densities = {
            mineral: MINERAL_PROPERTIES[mineral]['calc_density']
            for mineral in provenance_composition
        }
    else:
        calc_densities = fine_tuning_densities.copy()
        # Aplica ajustes específicos
        if 'mica' in calc_densities:
            calc_densities['mica'] -= 0.5
        if 'Sil' in calc_densities:
            calc_densities['Sil'] -= 0.45
    
    # Calcula densidade bulk
    bulk_density = calculate_bulk_density(provenance_composition, calc_densities)
    
    # Seleciona equações apropriadas
    settling_velocity, size_shift = get_settling_equations(fluid_type, dm)
    
    # Calcula parâmetros para cada mineral
    mineral_params = {}
    for mineral, percentage in provenance_composition.items():
        if percentage > 0:  # Ignora minerais com 0%
            # Calcula size-shift
            ss = size_shift(calc_densities[mineral])
            # Calcula dm para o mineral
            dm_mineral = dm - ss
            # Calcula sigma para o mineral
            d_min = PHI_TO_MM(dm - sigma)
            d_max = PHI_TO_MM(dm + sigma)
            v_min = settling_velocity(d_min, bulk_density, rho_f, mu)
            v_max = settling_velocity(d_max, bulk_density, rho_f, mu)
            d_min_mineral = MM_TO_PHI(v_min)
            d_max_mineral = MM_TO_PHI(v_max)
            sigma_mineral = (d_max_mineral - d_min_mineral) / 2
            
            mineral_params[mineral] = {
                'dm': dm_mineral,
                'sigma': sigma_mineral,
                'percentage': percentage
            }
    
    # Gera intervalos de phi
    phi_intervals = np.arange(-2, 4.5, 0.25)
    
    # Calcula distribuição para cada mineral
    results = []
    for phi in phi_intervals:
        row = {'phi': phi, 'mm': PHI_TO_MM(phi)}
        total_percentage = 0
        
        for mineral, params in mineral_params.items():
            # Calcula proporção do mineral no intervalo
            proportion = stats.norm.cdf(phi + 0.125, params['dm'], params['sigma']) - \
                        stats.norm.cdf(phi - 0.125, params['dm'], params['sigma'])
            percentage = proportion * params['percentage']
            row[mineral] = percentage
            total_percentage += percentage
        
        row['total'] = total_percentage
        results.append(row)
    
    # Cria DataFrame
    df = pd.DataFrame(results)
    df = df.set_index('phi')
    
    # Adiciona linha de totais
    totals = df.sum()
    df.loc['total'] = totals
    
    return df

def generate_plots(results_df):
    """
    Gera gráficos Plotly para visualização dos resultados.
    
    Args:
        results_df (pd.DataFrame): DataFrame com os resultados
    
    Returns:
        dict: Dicionário com os gráficos em formato JSON
    """
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Remove a linha de totais para os gráficos
    plot_df = results_df.drop('total')
    
    # Gráfico de distribuição cumulativa
    fig1 = go.Figure()
    
    # Adiciona minerais principais
    main_minerals = ['Q', 'F', 'Zrn', 'Grt']
    for mineral in main_minerals:
        if mineral in plot_df.columns:
            cumulative = plot_df[mineral].cumsum()
            fig1.add_trace(go.Scatter(
                x=plot_df.index,
                y=cumulative,
                name=MINERAL_PROPERTIES[mineral]['name'],
                mode='lines'
            ))
    
    # Adiciona distribuição total
    fig1.add_trace(go.Scatter(
        x=plot_df.index,
        y=plot_df['total'].cumsum(),
        name='Bulk Sediment',
        mode='lines',
        line=dict(dash='dash')
    ))
    
    fig1.update_layout(
        title='Distribuição Cumulativa',
        xaxis_title='Phi (φ)',
        yaxis_title='Porcentagem Acumulada',
        showlegend=True
    )
    
    # Gráfico de barras comparativo
    fig2 = make_subplots(rows=1, cols=2, subplot_titles=('Composição de Entrada', 'Composição de Saída'))
    
    # Composição de entrada
    input_data = results_df.loc['total'].drop('total')
    fig2.add_trace(
        go.Bar(
            x=input_data.index,
            y=input_data.values,
            name='Entrada',
            marker_color='blue'
        ),
        row=1, col=1
    )
    
    # Composição de saída (média dos intervalos)
    output_data = plot_df.mean()
    fig2.add_trace(
        go.Bar(
            x=output_data.index,
            y=output_data.values,
            name='Saída',
            marker_color='red'
        ),
        row=1, col=2
    )
    
    fig2.update_layout(
        title='Comparação de Composições',
        showlegend=False,
        height=500
    )
    
    return {
        'cumulative': fig1.to_json(),
        'comparison': fig2.to_json()
    } 