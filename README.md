# Coauthorship Trends in Economics

Tracking the average number of coauthors on NBER (National Bureau of Economic Research) working papers over time.

## Key Finding

The average number of authors per NBER working paper increased by **51%** between 2005 and 2025, rising from 2.13 to 3.22 authors per paper. This trend reflects the growing importance of collaboration in economics research.

## Live Site

View the interactive visualization at: **[GitHub Pages URL]** (enable GitHub Pages in repo settings, pointing to `/docs`)

## Data

| Year | Avg. Authors | Papers | Year | Avg. Authors | Papers |
|------|-------------|--------|------|-------------|--------|
| 2005 | 2.13 | 891 | 2016 | 2.61 | 1,175 |
| 2006 | 2.16 | 904 | 2017 | 2.74 | 1,164 |
| 2007 | 2.23 | 904 | 2018 | 2.76 | 1,236 |
| 2008 | 2.29 | 912 | 2019 | 2.87 | 1,185 |
| 2009 | 2.33 | 1,000 | 2020 | 3.04 | 1,713 |
| 2010 | 2.35 | 1,025 | 2021 | 3.07 | 1,311 |
| 2011 | 2.44 | 1,065 | 2022 | 3.11 | 1,191 |
| 2012 | 2.48 | 945 | 2023 | 3.13 | 1,197 |
| 2013 | 2.50 | 1,110 | 2024 | 3.21 | 1,308 |
| 2014 | 2.53 | 1,045 | 2025 | 3.22 | 1,227 |
| 2015 | 2.67 | 1,020 | | | |

Notable: 2020 saw both increased paper output (likely COVID-19 related research) and higher collaboration rates.

## Data Source

Official NBER working paper metadata from the [National Bureau of Economic Research](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata).

## Project Structure

```
Coauthor/
├── data/
│   ├── auths.dta            # Author data (paper -> author name)
│   ├── date.dta             # Publication dates (paper -> issue_date)
│   └── coauthor_stats.json  # Processed statistics by year
├── scripts/
│   └── process_data.py      # Data processing script
├── docs/
│   └── index.html           # Static website
└── README.md
```

## Running the Analysis

```bash
# Requires pandas
pip install pandas

# Process the data and generate statistics
python3 scripts/process_data.py
```

## Methodology

1. Load NBER working paper metadata (Stata format)
2. For each paper, count the number of distinct authors
3. Group papers by publication year
4. Calculate: average coauthors = total author appearances / number of papers

## License

Data is from NBER public metadata. Code is MIT licensed.
