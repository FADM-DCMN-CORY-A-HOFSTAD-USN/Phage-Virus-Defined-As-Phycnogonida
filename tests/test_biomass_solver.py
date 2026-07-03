"""
Phage-Virus-Defined-As-Phycnogonida: Section 12 Regression Test Suite
Filename: tests/test_biomass_solver.py
"""

import pytest
import numpy as np
from src.biomass_solver import NitrogenBiomassSolver

def test_biomass_growth_logistical_saturation_limits():
    """Verifies that dV/dt correctly decelerates as the vesicle hits boundary saturation points."""
    shape = (4, 4, 4)
    grid = np.zeros(shape, dtype=np.float32)
    solver = NitrogenBiomassSolver(grid)
    
    # Evaluate a baseline stable volume vs a critical, near-rupture volume track
    metrics_stable = solver.evaluate_nitrogen_limiting_growth(current_volume_v=500.0, available_nitrogen_pool=85.0, target_strain="Colossendeis")
    metrics_saturated = solver.evaluate_nitrogen_limiting_growth(current_volume_v=4800.0, available_nitrogen_pool=85.0, target_strain="Colossendeis")
    
    assert metrics_stable["containment_risk_status"] == "BOUNDED_STABLE"
    assert metrics_saturated["containment_risk_status"] == "CRITICAL_THREAT_DETECTED"
    # Proliferation derivative must diminish near capacity
    assert metrics_saturated["biomass_growth_derivative_dv_dt"] < metrics_stable["biomass_growth_derivative_dv_dt"]

def test_alkaline_degradation_target_extraction():
    """Confirms the database map correctly pulls specific target pH levels across strains."""
    shape = (4, 4, 4)
    grid = np.zeros(shape, dtype=np.float32)
    solver = NitrogenBiomassSolver(grid)
    
    profile_dodecolopoda = solver.evaluate_nitrogen_limiting_growth(100.0, 50.0, "Dodecolopoda")
    profile_achelia = solver.evaluate_nitrogen_limiting_growth(100.0, 50.0, "Achelia")
    
    assert profile_dodecolopoda["required_degradation_ph"] == 8.55
    assert profile_achelia["required_degradation_ph"] == 8.15
