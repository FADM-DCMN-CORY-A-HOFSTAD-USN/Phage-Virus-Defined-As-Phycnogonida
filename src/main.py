"""
Phage-Virus-Defined-As-Phycnogonida: Master Core Runner & Orchestrator
Filename: src/main.py
Author: Archival Software Component

This script orchestrates the full multi-modal tracking pipeline: it ingests 
dynamic scanner calibrations, compiles sequential DICOM folders into a 3D grid, 
 scrubs high-frequency noise using PyCUDA, calculates Section 10 multi-planar 
bone dynamics, maps Section 11 tritium radiotoxicity vectors, and generates 
automated clinical support documents.
"""

import os
import sys
import numpy as np

# Core Pipeline Engineering Ingestions
from config_loader import ConfigurationLoader
from core_registration_engine import MultiModalRegistrationEngine
from dicom_series_aggregator import DICOMSeriesAggregator
from anisotropic_filter import AnisotropicFilterEngine
from skeletal_dynamics import MultiPlanarSkeletalDynamics
from radiotoxic_kinetics import RadiotoxicKineticsEngine
from ai_diagnostic_app import AIDiagnosticSupportApp
from univac_bridge import UnivacTaxonomyBridge

def setup_runtime_directories() -> str:
    """
    Validates workspace infrastructure and creates a mock clinical 
    cross-section folder if local testing streams are bare.
    """
    mock_dir = "dicom_input_series"
    if not os.path.exists(mock_dir):
        os.makedirs(mock_dir, exist_ok=True)
        print(f"[INFO] Synthesizing automated test cross-sections at: ./{mock_dir}")
        from tests.test_series_aggregator import write_mock_slice
        # Generate out-of-order baseline slices mimicking real medical directories
        write_mock_slice(mock_dir, "slice_z30.dcm", z_position=3.0, pixel_value=150)
        write_mock_slice(mock_dir, "slice_z00.dcm", z_position=0.0, pixel_value=120)
        write_mock_slice(mock_dir, "slice_z15.dcm", z_position=1.5, pixel_value=135)
    return mock_dir

def main():
    print("==================================================================")
    print("      PHAGE-VIRUS-DEFINED-AS-PHYCNOGONIDA: MASTER CORE RUNNER     ")
    print("==================================================================")

    # ... [Configuration matrices and directory setup processes complete] ...
    
    print("[INFO] Spawning Univac IX Database Connectivity Bridge...")
    univac_db = UnivacTaxonomyBridge("config/univac_taxonomy.db")
    univac_db.initialize_database_schema("src/populate_taxonomy.sql")
    
    # Suppose your periodic table detector reads an optical hue of #FF4500
    # The system dynamically pulls the matched constraints straight from SQL rows
    target_hex_key = "#FF4500"
    matched_profile = univac_db.query_vector_by_optical_hex(target_hex_key)
    
    if matched_profile["status"] == "MATCH_FOUND":
        print(f"[SUCCESS] Univac IX mapped color key {target_hex_key} directly to: {matched_profile['scientific_name']}")
        # Dynamically overwrite global pipeline constraints matching the database row
        chitin_bounds = matched_profile["bounds"]
    else:
        chitin_bounds = [140.0, 690.0] # Default fallback threshold matrix
        
    univac_db.close_connection()
    
    # Proceed to serial folder aggregation, PyCUDA filtering, and Section 10/11 math...
 
    # 1. Ingest dynamic hardware calibration profiles and constraints
    config = ConfigurationLoader("config/config_matrices.json")
    if not config.load_and_validate_matrices():
        print("[CRITICAL ERROR] Scanner matrix profiles absent. Halting execution pipeline.")
        return
        
    xray_trans, xray_scale, _ = config.extract_carestream_affine_vectors()
    mri_phase, _, global_constraints = config.extract_ge_mri_profiles()
    
    # 2. Compile disorganized folder cross-sections into sorted 3D array grids
    input_directory = setup_runtime_directories()
    aggregator = DICOMSeriesAggregator(input_directory)
    compiled_volume = aggregator.compile_3d_volume()
    volume_shape = aggregator.spatial_metadata["volume_shape"]
    
    # 3. Compute 4x4 coordinate transforms and warp multi-modal geometries
    mock_2d_projection = np.zeros((volume_shape, volume_shape), dtype=np.float32)
    engine = MultiModalRegistrationEngine(mock_2d_projection, compiled_volume)
    engine.configure_affine_parameters(
        scale=tuple(xray_scale), 
        rotation=(0.0, 0.0, float(mri_phase)), 
        translation=tuple(xray_trans)
    )
    warped_volume = engine.execute_volume_warp()
    
    # 4. Filter high-frequency noise using edge-preserving 3D diffusion kernels
    print("[INFO] Initializing parallel spatial noise scrubbing filters...")
    filter_engine = AnisotropicFilterEngine(volume_shape)
    filtered_volume = filter_engine.execute_filter(warped_volume, iterations=2)
    
    # 5. Evaluate Section 10 multi-planar bone Dynamics (Sagittal, Coronal, Axial)
    print("[INFO] Computing Section 10 Multi-Planar Skeletal Fluid Transit Profiles...")
    skeletal_tracker = MultiPlanarSkeletalDynamics(filtered_volume, voxel_spacing_mm=(0.5, 0.5, 1.0))
    mock_baseline = np.full_like(filtered_volume, 180.0)
    skeletal_metrics = skeletal_tracker.evaluate_realtime_density_shifts(mock_baseline)
    print(f"  [SKELETAL FLUX] Total Marrow Depletion: {skeletal_metrics['marrow_depletion_voxels']} voxels")
    
    # 6. Execute Section 11 Radiotoxic Kinetics Engine
    print("[INFO] Calculating Section 11 Isotopic Tritium Effusion Trajectories...")
    radiotoxic_engine = RadiotoxicKineticsEngine(volume_shape)
    
    # Establish nitrogen-limiting reagent consumption multiplier
    simulated_nitrogen_rate = float(global_constraints.get("restricted_adc_threshold", 0.7)) * 5.0
    tritium_flux_map = radiotoxic_engine.calculate_tritium_effusion_profile(filtered_volume, simulated_nitrogen_rate)
    
    # Isolate bone marrow tracks to measure deep-field radiation impact
    marrow_mask = filtered_volume < 180.0
    radiation_impact = radiotoxic_engine.evaluate_hematopoietic_suppression_index(tritium_flux_map, marrow_mask)
    print(f"  [ISOTOPIC FLUX] Net Marrow Absorbed Energy: {radiation_impact['net_marrow_dose_bq']:.4f} Bq")
    print(f"  [ISOTOPIC FLUX] Hematopoietic Status Tier : {radiation_impact['suppression_status']}")
    
    # 7. Package clinical metrics and export structured diagnostic support document
    print("[INFO] Running automated AI Diagnostic Support report coordination...")
    validation_mask = filtered_volume > 140.0
    metrics = engine.calculate_attenuation_vectors(validation_mask)
    
    ai_app = AIDiagnosticSupportApp(docs_dir="docs", reports_dir="reports")
    ai_app.ingest_documentation_vault()
    evaluation_profile = ai_app.process_and_evaluate_metrics(metrics)
    
    # Inject radiotoxic state values directly into final log variables
    evaluation_profile["recommended_action"] += f" | Radiation Countermeasure: {radiation_impact['recommended_action_blueprint']}"
    
    generated_report = ai_app.export_diagnosis_support_file(evaluation_profile)
    print("==================================================================")
    print(f"[SUCCESS] Core execution loop closed cleanly. Support log saved: {generated_report}")
    print("==================================================================")

if __name__ == "__main__":
    main()
