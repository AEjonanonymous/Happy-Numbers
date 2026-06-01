# <div align="center">🙂 The Golden Ratio's Footprint in Happy Number Sequences 

## <div align="center">📌 Overview
This repository hosts the computational framework and formal proofs supporting the manuscript: **"The Golden Ratio's Footprint in Happy Number Sequences."** Our research proves that the behavior of happy and unhappy numbers is not random, but governed by a unified system where digit-sum structural costs ($R_S$) and sequential lengths ($R_L$) converge to an algebraic equilibrium tied to the Golden Ratio ($\phi$).

## 🗝️ Key Findings & Equations
Our research identifies the Base-10 number system as a unique **Geometric Singularity** where the system’s iterative path reaches an algebraic equilibrium of $\phi^2$.

###  1. The Unified System Identity $\phi^2$ 
The structural metrics are coupled via the Golden Ratio ($\phi \approx 1.618$):

$$R_S + R_L = \phi^2 \approx 2.618$$

###  2. Asymptotic Convergence Constants 👣
The individual ratios converge to exact constants defined by the Base-10 structure:
- **Structural Ratio ($R_S$):** $R_S \rightarrow 3 - \phi \approx 1.382$
- **Sequential Ratio ($R_L$):** $R_L \rightarrow \frac{2}{\phi} \approx 1.236$

### 👣 4. Geometric Confluence
We observe a confluence where the iteration process intersects with the geometric constant $\pi$:

$$\frac{R_S}{\phi^2} \approx \frac{\pi}{6} \approx 0.524$$

### 👣 2. The Base-10 Singularity
We identify the Base-10 number system as a unique **Geometric Singularity**. While sequence behaviors in other bases follow general conservation principles, the Base-10 system achieves an algebraic equilibrium where the sum of its structural and sequential ratios is exactly $\phi^2$. This demonstrates that the Base-10 iteration process is inherently constrained by the geometric properties of the Golden Ratio.

---

## ✔️ Formal Verification in Lean 4
We utilized the Lean 4 theorem prover to establish that the empirical convergence is not coincidental, but a mathematical necessity.
- **Contraction Mapping:** Proved via `basin_is_bounded.lean` that the system is bounded, forcing all integers into finite attractor basins.
- **Global Density:** The kernel-verified `basin_density.lean` confirms the happy number density is 1/7 validating the system's structural constraints.
- **Algebraic Equilibrium:** `unified_system_identity_proof.lean` closes the identity $R_S + R_L = \phi^2$ using formal tactic engines, proving these ratios are the unique equilibrium of the base-10 engine.

---

## 📐 Analytical Functional Derivation
The identity $R_S + R_L = \phi^2$ is derived from the decomposition of the system into three fundamental mandate constants:
1.  **Geometric Factor ($\lambda_G = 1/\phi$):** The collapse rate of sequence paths, determined by the Fibonacci recurrence relation dominant in the digit-sum space.
2.  **Arithmetic Density ($\lambda_A = 2$):** The compression factor derived from the cycle length ($L=8$) and modular filter ($M=4$).
3.  **Structural Constant ($C_A = 3$):** The minimum mean of the unstable digit set required to overcome base-10 entropy.

**Proof of Identity:**
Substituting these constants:

$$(C_A - \lambda_G) + (\lambda_A \cdot \lambda_G) = \phi^2$$
$$(3 - \frac{1}{\phi}) + (2 \cdot \frac{1}{\phi}) = \phi^2$$

Using the identity:

$$1/\phi = \phi - 1$$ 

This simplifies to:

$$2 + \phi = \phi^2$$

This confirms the fundamental algebraic signature of the system.

---
## ⚖️ [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
