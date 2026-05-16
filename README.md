This is an attempt to replicate a result by Cremieux on X which found that testosterone levels are going up in the USA, contrary to conventional wisdom.  It just displays testosterone data from the CDC over the years 2011 to 2023.  It's just an exercise for me in basic data retrieval and analysis.

Original post by Cremieux https://www.cremieux.xyz/p/why-are-testosterone-levels-rising


The data was taken from here.  
https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx

You need to download the XPT files.  And you need laboratory files and demographic files.  

For the laboratory files go to the 'all laboratory data' page and then search for 'TST' and download the XPT files for the appropriate years.  Presumably that's for testosterone, although the years after 2011 are called 'sex steroid hormone' rather than testosterone.  

You also need demographic data to read this stuff apparently.  It's simpler.  Just go to the 'all demographics data' page and just download the appropriate years.  

If you couldn't find those pages here they are
All laboratory data page https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory
All demographics data page https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics



Get Python Pandas
pip install pandas pyreadstat

then run 
python nhanes_all_years.py


### More information.

CDC & NHANES Overview
NHANES (National Health and Nutrition Examination Survey) is the CDC’s flagship program for monitoring the health and nutrition of the U.S. civilian population. Run by the National Center for Health Statistics (NCHS), it releases nationally representative data in two-year cycles under Continuous NHANES (since 1999).
Data & Methodology
Source: Public-use files from https://wwwn.cdc.gov/nchs/nhanes/
Files used (per cycle):

Laboratory: TST_G.xpt (2011–2012, labeled “Total Testosterone”) and TST_H/I/L.xpt (later cycles, labeled “Sex Steroid Hormone” panel)
Demographics: DEMO_*.xpt (age, sex, survey weights)

Key variable: LBXTST (total testosterone in ng/dL), measured consistently via ID-LC-MS/MS.
Analysis steps:

Merge lab and demographics files on SEQN
Filter to men aged 20+
Apply survey weights (e.g. WTMEC2YR) for national estimates
Calculate weighted means

Tools: Python + pandas + pyreadstat
Note: 2021–2023 files required encoding="latin1" due to a minor encoding incompatibility (common with newer NHANES .xpt releases).