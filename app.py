"""
Aplicação web Flask para simulação de distribuição granulométrica de minerais detríticos.
Baseado no artigo de Resentini et al. (2013) [Computers & Geosciences 59 (2013) 90-97].
"""

from flask import Flask, render_template, request, session, make_response
import pandas as pd
from data_store import MINERAL_PROPERTIES, PROVENANCE_COMPOSITIONS
from calculations import calculate_mineral_distribution, generate_plots

app = Flask(__name__)
app.secret_key = 'minsorting_secret_key'  # Necessário para session

@app.route('/', methods=['GET'])
def index():
    """Renderiza a página inicial com o formulário."""
    return render_template(
        'index.html',
        mineral_properties=MINERAL_PROPERTIES,
        provenance_compositions=PROVENANCE_COMPOSITIONS.keys()
    )

@app.route('/', methods=['POST'])
def calculate():
    """Processa o formulário e calcula os resultados."""
    try:
        # Recupera dados do formulário
        dm = float(request.form['dm'])
        sigma = float(request.form['sigma'])
        fluid_type = request.form['fluid_type']
        provenance = request.form['provenance']
        density_option = request.form['density_option']
        
        # Processa densidades fine-tuning se necessário
        fine_tuning_densities = None
        if density_option == 'fine_tuning':
            fine_tuning_densities = {}
            for mineral in MINERAL_PROPERTIES:
                field_name = f'density_fine_tuning_{mineral}'
                if field_name in request.form:
                    fine_tuning_densities[mineral] = float(request.form[field_name])
        
        # Calcula distribuição
        results_df = calculate_mineral_distribution(
            dm, sigma, fluid_type, provenance,
            density_option, fine_tuning_densities
        )
        
        # Gera gráficos
        plots = generate_plots(results_df)
        
        # Guarda apenas os parâmetros de entrada na session
        session['input_params'] = {
            'dm': dm,
            'sigma': sigma,
            'fluid_type': fluid_type,
            'provenance': provenance,
            'density_option': density_option,
            'fine_tuning_densities': fine_tuning_densities
        }
        
        # Renderiza página de resultados
        return render_template(
            'results.html',
            results_table=results_df.to_html(classes='table table-striped', index=True),
            plots=plots,
            input_params=session['input_params']
        )
    
    except Exception as e:
        return render_template(
            'index.html',
            error=str(e),
            mineral_properties=MINERAL_PROPERTIES,
            provenance_compositions=PROVENANCE_COMPOSITIONS.keys()
        )

@app.route('/export_csv')
def export_csv():
    """Exporta os resultados como arquivo CSV."""
    try:
        # Recupera parâmetros da session
        input_params = session.get('input_params')
        if not input_params:
            return "Nenhum resultado disponível para exportação", 400
        
        # Recupera parâmetros
        dm = input_params['dm']
        sigma = input_params['sigma']
        fluid_type = input_params['fluid_type']
        provenance = input_params['provenance']
        density_option = input_params['density_option']
        fine_tuning_densities = input_params.get('fine_tuning_densities')
        
        # Recalcula o DataFrame
        results_df = calculate_mineral_distribution(
            dm, sigma, fluid_type, provenance,
            density_option, fine_tuning_densities
        )
        
        # Cria resposta CSV
        response = make_response(results_df.to_csv())
        response.headers['Content-Disposition'] = 'attachment; filename=results.csv'
        response.headers['Content-Type'] = 'text/csv'
        
        return response
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True) 