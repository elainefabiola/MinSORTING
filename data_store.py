"""
Módulo contendo constantes e dados para a aplicação MinSORTING.
Baseado no artigo de Resentini et al. (2013) [Computers & Geosciences 59 (2013) 90-97].
"""

import numpy as np

# Propriedades dos fluidos (Tabela 1)
FLUID_PROPERTIES = {
    "Freshwater": {"density": 1.0, "viscosity": 0.01},
    "Seawater": {"density": 1.025, "viscosity": 0.0105},
    "Air": {"density": 0.001, "viscosity": 0.00018},
}

# Propriedades dos minerais (Fig. 4b e texto)
MINERAL_PROPERTIES = {
    "Q": {"name": "Quartz", "standard_density": 2.65, "min_density": 2.65, "max_density": 2.65, "calc_density": 2.65},
    "F": {"name": "Feldspar", "standard_density": 2.61, "min_density": 2.58, "max_density": 2.67, "calc_density": 2.61},
    "Lv": {"name": "Volcanic Lithics", "standard_density": 2.60, "min_density": 2.40, "max_density": 2.80, "calc_density": 2.60},
    "Lc": {"name": "Carbonate Lithics", "standard_density": 2.75, "min_density": 2.71, "max_density": 2.80, "calc_density": 2.75},
    "Ls": {"name": "Sedimentary Lithics", "standard_density": 2.65, "min_density": 2.50, "max_density": 2.75, "calc_density": 2.65},
    "Lm": {"name": "Metamorphic Lithics", "standard_density": 2.75, "min_density": 2.70, "max_density": 2.80, "calc_density": 2.75},
    "Lu": {"name": "Ultramafic Lithics", "standard_density": 2.85, "min_density": 2.60, "max_density": 3.00, "calc_density": 2.85},
    "mica": {"name": "Mica", "standard_density": 2.90, "min_density": 2.80, "max_density": 3.00, "calc_density": 2.40},
    "Op": {"name": "Opaques", "standard_density": 4.95, "min_density": 4.90, "max_density": 5.00, "calc_density": 4.95},
    "Zrn": {"name": "Zircon", "standard_density": 4.65, "min_density": 4.65, "max_density": 4.65, "calc_density": 4.65},
    "Tur": {"name": "Tourmaline", "standard_density": 3.15, "min_density": 3.10, "max_density": 3.20, "calc_density": 3.15},
    "Rt": {"name": "Rutile", "standard_density": 4.25, "min_density": 4.25, "max_density": 4.25, "calc_density": 4.25},
    "Ttn": {"name": "Titanite", "standard_density": 3.50, "min_density": 3.50, "max_density": 3.50, "calc_density": 3.50},
    "Ap": {"name": "Apatite", "standard_density": 3.20, "min_density": 3.20, "max_density": 3.20, "calc_density": 3.20},
    "Mnz": {"name": "Monazite", "standard_density": 5.15, "min_density": 5.15, "max_density": 5.15, "calc_density": 5.15},
    "Amp": {"name": "Amphibole", "standard_density": 3.20, "min_density": 3.20, "max_density": 3.20, "calc_density": 3.20},
    "Ep": {"name": "Epidote", "standard_density": 3.45, "min_density": 3.45, "max_density": 3.45, "calc_density": 3.45},
    "Grt": {"name": "Garnet", "standard_density": 4.00, "min_density": 3.90, "max_density": 4.10, "calc_density": 4.00},
    "Px": {"name": "Pyroxene", "standard_density": 3.30, "min_density": 3.30, "max_density": 3.30, "calc_density": 3.30},
    "Ol": {"name": "Olivine", "standard_density": 3.35, "min_density": 3.35, "max_density": 3.35, "calc_density": 3.35},
    "Spl": {"name": "Spinel", "standard_density": 4.45, "min_density": 4.45, "max_density": 4.45, "calc_density": 4.45},
    "Cld": {"name": "Chloritoid", "standard_density": 3.65, "min_density": 3.65, "max_density": 3.65, "calc_density": 3.65},
    "St": {"name": "Staurolite", "standard_density": 3.75, "min_density": 3.75, "max_density": 3.75, "calc_density": 3.75},
    "Ky": {"name": "Kyanite", "standard_density": 3.60, "min_density": 3.60, "max_density": 3.60, "calc_density": 3.60},
    "And": {"name": "Andalusite", "standard_density": 3.15, "min_density": 3.15, "max_density": 3.15, "calc_density": 3.15},
    "Sil": {"name": "Sillimanite", "standard_density": 3.00, "min_density": 2.80, "max_density": 3.25, "calc_density": 2.55},
    "&HM": {"name": "Other Heavy Minerals", "standard_density": 3.20, "min_density": 3.00, "max_density": 3.50, "calc_density": 3.20}
}

# Lista de abreviações na ordem da Tabela 2/Fig 7
MINERAL_ORDER = ["Q", "F", "Lv", "Lc", "Ls", "Lm", "Lu", "mica", "Op", "Zrn", "Tur", "Rt", "Ttn", "Ap", "Mnz", "Amp", "Ep", "Grt", "Px", "Ol", "Spl", "Cld", "St", "Ky", "And", "Sil", "&HM"]

# Composições de proveniência (Tabela 2)
PROVENANCE_COMPOSITIONS = {
    "Undissected Magmatic Arc": {"Q": 3.23, "F": 27.90, "Lv": 47.00, "Lc": 0.40, "Ls": 0.40, "Lm": 0.40, "Lu": 0.00, "mica": 0.80, "Op": 2.02, "Zrn": 0.00, "Tur": 0.00, "Rt": 0.00, "Ttn": 0.02, "Ap": 0.02, "Mnz": 0.00, "Amp": 0.40, "Ep": 0.10, "Grt": 0.00, "Px": 15.40, "Ol": 0.00, "Spl": 0.00, "Cld": 0.00, "St": 0.00, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 1.91},
    "Dissected Magmatic Arc": {"Q": 34.89, "F": 39.70, "Lv": 1.10, "Lc": 0.60, "Ls": 0.80, "Lm": 3.00, "Lu": 0.00, "mica": 4.50, "Op": 1.52, "Zrn": 0.06, "Tur": 0.06, "Rt": 0.00, "Ttn": 0.20, "Ap": 0.20, "Mnz": 0.05, "Amp": 9.30, "Ep": 1.90, "Grt": 0.00, "Px": 0.40, "Ol": 0.10, "Spl": 0.00, "Cld": 0.00, "St": 0.00, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 1.62},
    "Ophiolite": {"Q": 4.98, "F": 7.40, "Lv": 8.10, "Lc": 9.40, "Ls": 0.80, "Lm": 3.70, "Lu": 47.50, "mica": 0.10, "Op": 0.71, "Zrn": 0.00, "Tur": 0.00, "Rt": 0.00, "Ttn": 0.00, "Ap": 0.01, "Mnz": 0.00, "Amp": 1.90, "Ep": 1.20, "Grt": 0.00, "Px": 11.30, "Ol": 0.60, "Spl": 1.40, "Cld": 0.00, "St": 0.00, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 0.90},
    "Recycled Clastic": {"Q": 75.96, "F": 14.00, "Lv": 0.00, "Lc": 1.50, "Ls": 5.00, "Lm": 2.00, "Lu": 0.00, "mica": 1.00, "Op": 0.02, "Zrn": 0.10, "Tur": 0.10, "Rt": 0.10, "Ttn": 0.01, "Ap": 0.01, "Mnz": 0.00, "Amp": 0.00, "Ep": 0.00, "Grt": 0.10, "Px": 0.00, "Ol": 0.00, "Spl": 0.00, "Cld": 0.00, "St": 0.10, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 0.00},
    "Undissected Continental Block": {"Q": 2.43, "F": 0.40, "Lv": 2.00, "Lc": 65.40, "Ls": 24.90, "Lm": 4.80, "Lu": 0.00, "mica": 0.00, "Op": 0.02, "Zrn": 0.01, "Tur": 0.01, "Rt": 0.01, "Ttn": 0.00, "Ap": 0.01, "Mnz": 0.00, "Amp": 0.00, "Ep": 0.00, "Grt": 0.01, "Px": 0.00, "Ol": 0.00, "Spl": 0.00, "Cld": 0.00, "St": 0.00, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 0.00},
    "Transitional Continental Block": {"Q": 36.69, "F": 12.80, "Lv": 1.70, "Lc": 1.10, "Ls": 1.50, "Lm": 33.10, "Lu": 0.00, "mica": 8.30, "Op": 0.24, "Zrn": 0.01, "Tur": 0.02, "Rt": 0.11, "Ttn": 0.01, "Ap": 0.01, "Mnz": 0.01, "Amp": 1.00, "Ep": 1.20, "Grt": 0.70, "Px": 0.20, "Ol": 0.00, "Spl": 0.00, "Cld": 0.10, "St": 0.10, "Ky": 0.10, "And": 0.10, "Sil": 0.00, "&HM": 0.90},
    "Dissected Continental Block": {"Q": 42.81, "F": 32.80, "Lv": 1.20, "Lc": 2.20, "Ls": 0.50, "Lm": 7.40, "Lu": 0.00, "mica": 4.50, "Op": 0.95, "Zrn": 0.06, "Tur": 0.04, "Rt": 0.11, "Ttn": 0.04, "Ap": 0.17, "Mnz": 0.02, "Amp": 4.50, "Ep": 1.20, "Grt": 1.20, "Px": 0.00, "Ol": 0.00, "Spl": 0.00, "Cld": 0.00, "St": 0.10, "Ky": 0.10, "And": 0.10, "Sil": 0.00, "&HM": 0.00},
    "Subcreted Axial Belt": {"Q": 25.39, "F": 3.60, "Lv": 1.70, "Lc": 15.30, "Ls": 12.90, "Lm": 38.00, "Lu": 0.00, "mica": 0.50, "Op": 1.20, "Zrn": 0.02, "Tur": 0.02, "Rt": 0.01, "Ttn": 0.02, "Ap": 0.10, "Mnz": 0.01, "Amp": 0.20, "Ep": 0.40, "Grt": 0.00, "Px": 0.00, "Ol": 0.00, "Spl": 0.00, "Cld": 0.13, "St": 0.00, "Ky": 0.00, "And": 0.00, "Sil": 0.00, "&HM": 0.50},
    "Subducted Axial Belt": {"Q": 48.76, "F": 15.30, "Lv": 0.30, "Lc": 0.10, "Ls": 0.00, "Lm": 15.10, "Lu": 0.00, "mica": 0.50, "Op": 13.40, "Zrn": 0.03, "Tur": 0.04, "Rt": 0.10, "Ttn": 0.09, "Ap": 0.17, "Mnz": 0.02, "Amp": 0.40, "Ep": 2.50, "Grt": 2.10, "Px": 0.00, "Ol": 0.00, "Spl": 0.00, "Cld": 0.00, "St": 0.00, "Ky": 0.20, "And": 0.00, "Sil": 0.10, "&HM": 0.69}
}

# Constantes físicas
GRAVITY = 9.81  # m/s²
PHI_TO_MM = lambda phi: 2 ** (-phi)  # Conversão de phi para mm
MM_TO_PHI = lambda mm: -np.log2(mm)  # Conversão de mm para phi 