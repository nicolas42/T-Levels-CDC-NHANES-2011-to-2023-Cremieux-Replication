import pandas as pd
import pyreadstat

cycles = {
    "2011-2012": ("TST_G.xpt", "DEMO_G.xpt"),
    "2013-2014": ("TST_H.xpt", "DEMO_H.xpt"),
    "2015-2016": ("TST_I.xpt", "DEMO_I.xpt"),
    "2021-2023": ("TST_L.xpt", "DEMO_L.xpt"),
}

results = []

for year, (tst_file, demo_file) in cycles.items():
    try:
        # Special handling for 2021-2023.  
        # For some reason, 2021 used latin1 encoding because the CDC sucks.
        if year == "2021-2023":
            tst, _ = pyreadstat.read_xport(tst_file, encoding="latin1")
            demo, _ = pyreadstat.read_xport(demo_file, encoding="latin1")
        else:
            tst, _ = pyreadstat.read_xport(tst_file)
            demo, _ = pyreadstat.read_xport(demo_file)
        
        merged = pd.merge(tst, demo, on="SEQN", how="inner")
        men = merged[(merged['RIAGENDR'] == 1) & (merged['RIDAGEYR'] >= 20)].copy()
        
        # Auto-detect weight column
        weight_var = None
        for w in ['WTMEC2YR', 'WTSAF2YR', 'WTPH2YR', 'WTMEC4YR']:
            if w in men.columns:
                weight_var = w
                break
                
        if weight_var is None:
            print(f"Warning: No weight for {year}")
            continue
            
        men = men.dropna(subset=['LBXTST', weight_var])
        
        weighted_mean = (men['LBXTST'] * men[weight_var]).sum() / men[weight_var].sum()
        
        results.append({
            "Cycle": year,
            "Weighted Mean T (ng/dL)": round(weighted_mean, 1),
            "N (men 20+)": len(men),
            "Weight": weight_var
        })
        
    except Exception as e:
        print(f"Error with {year}: {e}")

summary = pd.DataFrame(results)
print("\n=== Total Testosterone Trend - Men 20+ (NHANES) ===")
print(summary)