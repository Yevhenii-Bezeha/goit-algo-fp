# Monte Carlo Integration of f(x) = x^2

## Overview
This project calculates the definite integral of the function \( f(x) = x^2 \) over the interval \([0, 2]\) using the Monte Carlo method and verifies the result by comparing it with the analytical solution obtained via the `scipy.integrate.quad` function.

## Methodology
1. **Monte Carlo Integration**:
   - Generate `N` random points \( (x, y) \) within the bounding box \([a, b] \times [0, f(b)]\).
   - Count the number of points that fall under the curve \( y \leq f(x) \).
   - Estimate the integral as:
     \[
     I \approx \frac{\text{points under curve}}{N} \times (b - a) \times f(b)
     \]

2. **Analytical Integration**:
   - The definite integral of \( f(x) = x^2 \) from \( 0 \) to \( 2 \) is computed using SciPy’s `quad` function, which provides a precise numerical result.

## Results
- **Monte Carlo Method**: The estimated integral value fluctuates around **2.67**, depending on the number of random points used.
- **Analytical Result**: The exact integral computed using `quad` is **2.66667** with a negligible numerical error.
- **Comparison**:
  - The Monte Carlo estimation closely matches the analytical result.
  - Increasing the number of points improves accuracy.

## Conclusion
The Monte Carlo method provides an effective approximation of the integral, with accuracy improving as the number of samples increases. The results validate the correctness of the implementation and demonstrate the reliability of Monte Carlo integration for numerical computations.

