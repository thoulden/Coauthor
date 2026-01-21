# Coauthorship Trends in Economics

Tracking the average number of coauthors on NBER (National Bureau of Economic Research) working papers over time.

## Key Finding

The average number of authors per NBER working paper increased by **15%** between 2015 and 2021, rising from 2.67 to 3.06 authors per paper. This trend reflects the growing importance of collaboration in economics research.

## Live Site

View the interactive visualization at: **[GitHub Pages URL]** (enable GitHub Pages in repo settings, pointing to `/docs`)

## Data

| Year | Avg. Authors | Papers | Total Authors |
|------|-------------|--------|---------------|
| 2015 | 2.67 | 1,020 | 2,723 |
| 2016 | 2.61 | 1,175 | 3,067 |
| 2017 | 2.74 | 1,164 | 3,191 |
| 2018 | 2.76 | 1,236 | 3,406 |
| 2019 | 2.87 | 1,185 | 3,401 |
| 2020 | 3.03 | 1,713 | 5,196 |
| 2021 | 3.06 | 1,311 | 4,010 |

Notable: 2020 saw both increased paper output (likely COVID-19 related research) and higher collaboration rates.

## Data Source

Paper metadata is from the [nberwp R package](https://github.com/bldavies/nberwp), which compiles and cleans official metadata from the [National Bureau of Economic Research](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata).

## Project Structure

```
Coauthor/
├── data/
│   ├── papers.csv           # NBER paper metadata (id, year, month, title)
│   ├── paper_authors.csv    # Paper-author relationships
│   └── coauthor_stats.json  # Processed statistics by year
├── scripts/
│   └── process_data.py      # Data processing script
├── docs/
│   └── index.html           # Static website
└── README.md
```

## Running the Analysis

```bash
# Process the data and generate statistics
python3 scripts/process_data.py
```

## Methodology

1. NBER working papers (prefix `w`) are filtered from the dataset
2. For each paper, the number of distinct authors is counted
3. Papers are grouped by publication year
4. Average coauthors = total author appearances / number of papers

## License

Data is from NBER public metadata. Code is MIT licensed.
