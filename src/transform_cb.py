import numpy as np
import pandas as pd

cb_dir = 'data/cb'

# Read cutoffs from file
cutoffs = pd.read_csv('{}/cb_cutoffs.csv'.format(cb_dir))

# Read raw CB expressions from file
cb_raw = pd.read_csv('{}/cb_raw.csv'.format(cb_dir))

def transform(i):
    mask_raw = cb_raw.sample_id == i
    mask_cutoffs = cutoffs.sample_id == i
    cbi = np.log(cb_raw[mask_raw] / cutoffs[mask_cutoffs].iloc[0])
    cbi.sample_id = i
    return cbi.replace(-np.inf, np.nan)

# Transform each sample
cb = pd.concat([transform(i) for i in cutoffs.sample_id])

# Write transformed data to csv
cb.to_csv('{}/cb_transformed.csv'.format(cb_dir), index=False)
