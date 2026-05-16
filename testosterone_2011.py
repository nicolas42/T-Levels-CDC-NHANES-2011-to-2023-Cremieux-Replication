import pandas as pd
import pyreadstat

# Load the two files
tst, _ = pyreadstat.read_xport("TST_G.xpt")
demo, _ = pyreadstat.read_xport("DEMO_G.xpt")

# Merge them
merged = pd.merge(tst, demo, on="SEQN", how="inner")

# Filter to men aged 20+
men = merged[(merged['RIAGENDR'] == 1) & (merged['RIDAGEYR'] >= 20)].copy()

# Basic stats (unweighted first - quick look)
print("=== 2011-2012 Men Aged 20+ ===")
print(f"Sample size: {len(men)}")
print(f"Unweighted mean total T (ng/dL): {men['LBXTST'].mean():.1f}")
print(f"Median: {men['LBXTST'].median():.1f}")
print("\nQuick summary:")
print(men['LBXTST'].describe())

# Weighted mean (more accurate for US population)
weight_var = "WTMEC2YR"   # This is the correct weight for this cycle
men = men.dropna(subset=['LBXTST', weight_var])

weighted_mean = (men['LBXTST'] * men[weight_var]).sum() / men[weight_var].sum()
print(f"\nWeighted mean total T (ng/dL): {weighted_mean:.1f}")