# Basic Black-Scholes Implementation

```bash
bazel build //src:black_scholes
./bazel-bin/src/black_scholes
```

```bash
g++ -o black_scholes src/model.cpp -std=c++20 -lm
./black_scholes
```