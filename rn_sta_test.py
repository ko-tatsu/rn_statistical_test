import math
import random

from scipy import stats


N = 10000
DELAY_K = 1
NUM_BINS = 10
ALPHA = 0.05


def generate_random_numbers(n):
    """Generate n pseudo-random numbers in the interval [0, 1)."""
    return [random.random() for _ in range(n)]


def delay_k_test(values, k=DELAY_K, alpha=ALPHA):
    """Perform a delay-k test for serial dependence."""
    n = len(values)
    sum_product = sum(
        values[i] * values[(i + k) % n]
        for i in range(n)
    )

    z = (12.0 / n * sum_product - 3.0) * math.sqrt(n / 13.0)
    critical_value = stats.norm.ppf(1.0 - alpha / 2.0)
    passed = abs(z) < critical_value

    print("######### delay-k statistical test #########")
    print(f"N: {n}")
    print(f"k: {k}")
    print(f"z value: {z:.6f}")
    print(f"critical value (two-sided, alpha={alpha}): ±{critical_value:.6f}")
    print("Result:", "PASS" if passed else "FAIL")
    print()

    return z, passed


def equiprobability_test(values, num_bins=NUM_BINS, alpha=ALPHA):
    """Perform a chi-square equiprobability test."""
    n = len(values)
    counts = [0] * num_bins

    for value in values:
        index = min(int(value * num_bins), num_bins - 1)
        counts[index] += 1

    expected = n / num_bins
    chi_square = sum(
        (observed - expected) ** 2 / expected
        for observed in counts
    )

    degrees_of_freedom = num_bins - 1
    critical_value = stats.chi2.isf(alpha, degrees_of_freedom)
    passed = chi_square < critical_value

    print("######### equiprobability statistical test #########")
    print(f"N: {n}")
    print(f"number of bins: {num_bins}")
    print("histogram:")
    for i, count in enumerate(counts):
        print(f"  bin {i}: {count}")
    print(f"expected count per bin: {expected:.2f}")
    print(f"chi-square value: {chi_square:.6f}")
    print(f"critical value (alpha={alpha}, df={degrees_of_freedom}): {critical_value:.6f}")
    print("Result:", "PASS" if passed else "FAIL")
    print()

    return chi_square, passed


def main():
    print("Generate random numbers")
    values = generate_random_numbers(N)

    delay_k_test(values)
    equiprobability_test(values)

    print("Test end")


if __name__ == "__main__":
    main()
