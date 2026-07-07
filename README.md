# 🧬 Phage-Virus-Defined-As-Phycnogonida

This repository houses the structural, mathematical, and data-ingestion bridge models designed to map, track, and validate the morphological and biophysical convergence between historical 2D phage virus silhouettes and modern 3D cebidiomorphic *Pycnogonida* (sea spider) parasitic vectors.

Adobe Podcasts and PDF documents for BIOCHEM 1090 are located on the Adobe Document Cloud (please use the link).
https://acrobat.adobe.com/link/spaces/urn:aaid:sc:US:a163d2bd-1898-4895-8abc-7a2727b12f87

## 📐 Computational Mapping and Structural Alignment Core

The active logic suite coordinates raw medical imaging data inputs directly with specialized cross-disciplinary guidelines to overcome a century-old resolution blindspot:

*   **Config Ingestion (`config_loader.py`):** Automatically reads affine 4x4 coordinate warp matrices, Dixon phase offsets, and spectral fat-saturation calibrations from Carestream X-ray systems and GE Medical 3T MRI sequences.
*   **Series Stacking Aggregator (`dicom_series_aggregator.py`):** Scans input folders, parses absolute physical `ImagePositionPatient` coordinate tags, stacks files sequentially along the Z-axis, and builds normalized 3D array grids.
*   **Parallel Spatial Noise Scrubber (`anisotropic_filter.py`):** Deploys a parallelized PyCUDA 3D Perona-Malik anisotropic diffusion filtering kernel to clean high-frequency scanner noise while keeping sharp edge boundaries intact.
*   **Section 10 Multi-Planar Flow Engine (`skeletal_dynamics.py`):** Calculates multi-axis finite difference gradients and 3D Laplacian flux vectors to quantify longitudinal bone-marrow mineral leaching and tissue density variations.
*   **Section 11 Isotopic Effusion Vector Engine (`radiotoxic_kinetics.py`):** Computes time-dependent, multi-directional cellular tritium activity maps ($Bq/mm^3$) and tracks marrow absorbed energy to predict secondary hematopoietic suppression.
*   **AI Reporting Support App (`ai_diagnostic_app.py`):** Cross-references live 3D voxel density metrics against text-based research guidelines, automatically exporting structured diagnostic validation support sheets into your local `/reports/` directory on every execution pass.

---

## 🚀 Quick-Start Execution Loop

To deploy this integrated code layout, construct all folder systems, populate your logic scripts, and run the master validation processing loop locally, execute these shell commands:

```bash
# 1. Run the local automated repository infrastructure builder
python build_repo.py

# 2. Add the dynamic source locations to your system path variables
export PYTHONPATH=\(PYTHONPATH:\)(pwd)/src

# 3. Fire the master data processing pipeline orchestrator loop
python src/main.py
```
