# Basic Black-Scholes Implementation

In C++:
```bash
bazel build //src:black_scholes
./bazel-bin/src/black_scholes
```

```bash
g++ -o black_scholes src/model.cpp -std=c++20 -lm
./black_scholes
```

For Python frontend:
```bash
python3 -m streamlit run frontend/frontend.py
```