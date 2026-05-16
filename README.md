# NHANES Testosterone Trend (2011–2023)

This project replicates the analysis shared by **Crémieux** on X showing that mean testosterone levels in U.S. men have been **rising** from 2011 to 2023 — contrary to the common narrative of declining testosterone.

It is a simple personal exercise in downloading, merging, and analyzing public CDC data.

**Original post**: [Why Have Testosterone Levels Been Rising?](https://www.cremieux.xyz/p/why-are-testosterone-levels-rising)

---

### Data Source

All data comes from the **CDC’s National Health and Nutrition Examination Survey (NHANES)** — Continuous NHANES (since 1999).

- **Laboratory files** (`TST_*.xpt`): Contain total testosterone (`LBXTST`)
  - 2011–2012: Labeled “Total Testosterone”
  - 2013 onward: Labeled “Sex Steroid Hormone” panel
- **Demographics files** (`DEMO_*.xpt`): Age, sex, and survey weights

**Direct pages**:
- [All Laboratory Data](https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory)
- [All Demographics Data](https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics)

---

### Setup & Running

1. Download the relevant `.xpt` files (TST + DEMO for each cycle) into one folder.
2. Install required packages:

```bash
pip install pandas pyreadstat

```bash
python nhanes_all_years.py
