# Gaussian Particle Swarm Optimization Sample

Langage : Python

## Abstract

### Purpose

Optimize following function :
```math
F(x_1,x2) = {x_1}^2 + {x_2}^2, S_0 = {(x_1, x_2)| |x_1| \le 5, |x_2| \le 5}
```
### Update Rule

```math
v^i_j(n + 1) = wv^i_j(n) + \rho_1\mathrm{rand}(p^i_j - x^i_j(n)) + \rho_2\mathrm{rand}(l^i_j - x^i_j(n)) \\
x^i_j(n + 1) = x^i_j(n) + v^i_j(n)
where
\mathrm{rand}(x) ~ N(x, 1)
```

### Graph Structure

Complete Graph

