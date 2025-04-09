import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from model import black_scholes

# Streamlit app title
st.title("Black-Scholes European Call Option Calculator")

# Input fields for the parameters
K = st.number_input("Strike Price (K):", min_value=0.0, value=100.0, step=1.0)
T = st.number_input("Time to Maturity (T, in years):", min_value=0.0, value=1.0, step=0.1)
r = st.number_input("Risk-Free Interest Rate (r):", min_value=0.0, value=0.05, step=0.01, format="%.2f")

# Sliders for Stock Price (S) and Volatility (σ)
S_min, S_max = st.slider("Stock Price Range (S):", min_value=0.0, max_value=500.0, value=(50.0, 150.0), step=1.0)
sigma_min, sigma_max = st.slider("Volatility Range (σ):", min_value=0.0, max_value=1.0, value=(0.1, 0.5), step=0.01)

# Helper function to create a range with floating-point steps
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

# Generate matrix of option prices
if st.button("Generate Option Price Heatmap"):
    try:
        # Create ranges for stock prices and volatilities
        stock_prices = [round(S, 2) for S in range(int(S_min), int(S_max) + 1, 10)]
        volatilities = [round(sigma, 2) for sigma in frange(sigma_min, sigma_max, 0.05)]

        # Create a DataFrame to store the option prices
        data = []
        for sigma in volatilities:
            row = [black_scholes(S, K, T, r, sigma) for S in stock_prices]
            data.append(row)

        df = pd.DataFrame(data, index=volatilities, columns=stock_prices)

        # Display the heatmap with annotations
        st.write("Option Price Heatmap (Rows: Volatility, Columns: Stock Price):")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=stock_prices, yticklabels=volatilities, ax=ax)
        ax.set_xlabel("Stock Price (S)")
        ax.set_ylabel("Volatility (σ)")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")
