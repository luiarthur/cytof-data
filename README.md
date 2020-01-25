# README

This repository contains the CyTOF cord blood (CB) data used in the paper [A
Bayesian Feature Allocation Model for Identification of Cell Subpopulations
Using Cytometry Data][1].

- `Makefile`
    - Run `make` to generate the transformed data
      (i.e. `data/cb/cb_transformed.csv`)
- `src/transform.py`
    - The script that transforms the raw data and saves to
      `data/cb/cb_transformed.csv`.
- `data/`
    - `cb/`
        - Contains the cord blood data used in this work. See `README.md`
          in that directory.
    - `synthetic/`
        - Contains the synthetic data used in this work. See `README.md`
          in that directory.

[1]: #
