#!/usr/bin/env python3
"""
Process NBER working paper data to calculate average coauthors per year.
"""

import csv
import json
from collections import defaultdict
from pathlib import Path


def load_papers(filepath):
    """Load papers.csv and return dict of paper_id -> year."""
    papers = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            paper_id = row['paper']
            # Only include working papers (w prefix), not historical (h prefix)
            if paper_id.startswith('w'):
                papers[paper_id] = int(row['year'])
    return papers


def load_paper_authors(filepath):
    """Load paper_authors.csv and return dict of paper_id -> list of authors."""
    paper_authors = defaultdict(list)
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            paper_id = row['paper']
            author_id = row['author']
            paper_authors[paper_id].append(author_id)
    return paper_authors


def calculate_coauthors_by_year(papers, paper_authors, start_year=2015):
    """Calculate average number of coauthors per paper by year."""
    yearly_stats = defaultdict(lambda: {'total_authors': 0, 'paper_count': 0})

    for paper_id, year in papers.items():
        if year >= start_year:
            num_authors = len(paper_authors.get(paper_id, []))
            if num_authors > 0:  # Only count papers with author data
                yearly_stats[year]['total_authors'] += num_authors
                yearly_stats[year]['paper_count'] += 1

    # Calculate averages
    results = {}
    for year in sorted(yearly_stats.keys()):
        stats = yearly_stats[year]
        if stats['paper_count'] > 0:
            avg = stats['total_authors'] / stats['paper_count']
            results[year] = {
                'average_coauthors': round(avg, 3),
                'paper_count': stats['paper_count'],
                'total_authors': stats['total_authors']
            }

    return results


def main():
    data_dir = Path(__file__).parent.parent / 'data'

    print("Loading historical data...")
    papers = load_papers(data_dir / 'papers.csv')
    paper_authors = load_paper_authors(data_dir / 'paper_authors.csv')

    print(f"Loaded {len(papers)} working papers")
    print(f"Loaded {sum(len(v) for v in paper_authors.values())} author links")

    # Calculate stats for 2015 onwards
    print("\nCalculating average coauthors by year (2015+)...")
    results = calculate_coauthors_by_year(papers, paper_authors, start_year=2015)

    # Save results
    output_file = data_dir / 'coauthor_stats.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_file}")
    print("\nAverage coauthors per paper by year:")
    print("-" * 50)
    for year, stats in results.items():
        print(f"{year}: {stats['average_coauthors']:.2f} authors/paper ({stats['paper_count']} papers)")


if __name__ == '__main__':
    main()
