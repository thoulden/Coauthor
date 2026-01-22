#!/usr/bin/env python3
"""
Process NBER working paper data to calculate average coauthors per year.
Uses official NBER metadata in Stata (.dta) format.
"""

import json
from pathlib import Path

import pandas as pd


def main():
    data_dir = Path(__file__).parent.parent / 'data'

    print("Loading NBER data...")

    # Load author data (paper -> author name, multiple rows per paper)
    auths = pd.read_stata(data_dir / 'auths.dta')
    print(f"Loaded {len(auths):,} author records")

    # Load date data (paper -> issue_date)
    dates = pd.read_stata(data_dir / 'date.dta')
    dates['year'] = pd.to_datetime(dates['issue_date']).dt.year
    print(f"Loaded {len(dates):,} papers")

    # Count authors per paper
    author_counts = auths.groupby('paper').size().reset_index(name='num_authors')

    # Merge with dates
    merged = dates.merge(author_counts, on='paper', how='left')

    # Filter to 2005 onwards and exclude papers with no authors
    start_year = 2005
    merged = merged[(merged['year'] >= start_year) & (merged['num_authors'].notna())]

    # Calculate stats by year
    stats = merged.groupby('year').agg(
        paper_count=('paper', 'count'),
        total_authors=('num_authors', 'sum'),
        average_coauthors=('num_authors', 'mean')
    ).reset_index()

    # Convert to dict format
    results = {}
    for _, row in stats.iterrows():
        year = int(row['year'])
        results[year] = {
            'average_coauthors': round(row['average_coauthors'], 3),
            'paper_count': int(row['paper_count']),
            'total_authors': int(row['total_authors'])
        }

    # Save results
    output_file = data_dir / 'coauthor_stats.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_file}")
    print(f"\nAverage coauthors per paper by year ({start_year}-{max(results.keys())}):")
    print("-" * 55)
    for year in sorted(results.keys()):
        s = results[year]
        print(f"{year}: {s['average_coauthors']:.2f} authors/paper ({s['paper_count']:,} papers)")

    total_papers = sum(r['paper_count'] for r in results.values())
    total_authors = sum(r['total_authors'] for r in results.values())
    print(f"\nTotal papers analyzed: {total_papers:,}")
    print(f"Total author appearances: {total_authors:,}")


if __name__ == '__main__':
    main()
