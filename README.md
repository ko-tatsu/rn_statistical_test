# rn_statistical_test

A small Python project for experimenting with statistical tests of pseudo-random number sequences.

This repository was originally created in **December 2019** as an early Python learning project.  
The original idea and simple structure are intentionally preserved, while obvious bugs, spelling mistakes, and unused code were cleaned up in 2026.

## What this script does

The script generates pseudo-random numbers with Python's `random.random()` and evaluates the generated sequence using two simple statistical tests:

- **Delay-k test** — checks serial dependence between values separated by `k`
- **Chi-square equiprobability test** — checks whether values are approximately uniformly distributed across bins

## Requirements

- Python 3
- SciPy

Install the dependency with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python rn_sta_test.py
```

The default settings are:

- Number of random values: `10,000`
- Delay parameter: `k = 1`
- Number of bins: `10`
- Significance level: `alpha = 0.05`

## Background

This repository is preserved as a record of an early Python/statistics learning exercise.

The 2019 version contained the original implementation. In 2026, the project was lightly cleaned up while retaining the same purpose and basic approach.

## Notes

This code is intended for educational and experimental use. It is not a comprehensive random-number test suite.
