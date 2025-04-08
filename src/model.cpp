#include <iostream>
#include <cmath>
#include <cstdlib> // For std::atof


// Function to calculate the cumulative normal distribution
double normalCDF(double x) {
    // For standard normal, the CDF is equivalent to 0.5 * (1 + erf(x / sqrt(2)))
    return 0.5 * std::erfc(-x * std::sqrt(0.5));
}

// Black-Scholes formula for a European call option
double blackScholes(double S, double K, double T, double r, double sigma) {
    double d1 = (std::log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * std::sqrt(T));
    double d2 = d1 - sigma * std::sqrt(T);
    return S * normalCDF(d1) - K * std::exp(-r * T) * normalCDF(d2);
}

int main(int argc, char* argv[]) {
    if (argc != 6) {
        std::cerr << "Usage: " << argv[0] << " <S> <K> <T> <r> <sigma>" << std::endl;
        return 1;
    }

    // Parse command-line arguments
    double S = std::atof(argv[1]);      // Current stock price
    double K = std::atof(argv[2]);      // Strike price
    double T = std::atof(argv[3]);      // Time to maturity (in years)
    double r = std::atof(argv[4]);      // Risk-free interest rate
    double sigma = std::atof(argv[5]);  // Volatility

    // Calculate the call option price
    double callPrice = blackScholes(S, K, T, r, sigma);
    std::cout << "European Call Option Price: " << callPrice << std::endl;

    return 0;
}