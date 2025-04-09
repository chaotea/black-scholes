import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes formula.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the stock

    Returns:
    float: Price of the European call option
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

def main():
    print("Black-Scholes European Call Option Calculator")
    try:
        S = float(input("Enter current stock price (S): "))
        K = float(input("Enter strike price (K): "))
        T = float(input("Enter time to maturity in years (T): "))
        r = float(input("Enter risk-free interest rate (r): "))
        sigma = float(input("Enter volatility (sigma): "))

        # Calculate call option price
        call_price = black_scholes(S, K, T, r, sigma)
        print(f"\nThe price of the European call option is: {call_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()