# <div align="center">🙂 The Golden Ratio's Footprint in Happy Number Sequences 

## <div align="center">📌 Overview
This repository hosts the computational framework and formal proofs supporting the manuscript 📝: **The Golden Ratio's Footprint in Happy Number Sequences.pdf"** Our research proves that the behavior of happy and unhappy numbers is not random, but governed by a unified system where digit-sum structural costs ($R_S$) and sequential lengths ($R_L$) converge to an algebraic equilibrium tied to the Golden Ratio ($\phi$).

## 💻 Empirical Models & Web Applications
We modeled the digit-sum engine using custom Python scripts and web-based utilities to analyze 50,000,000 integers. These tools calculate the Total Digit Sum ($\Sigma_D$) and Sequence Length ($L_S$) to observe the emergent convergence of $R_S$ and $R_L$.
- **Python Scripts:** `happy_number_sum.py`, `happy_number_step.py`
- **Web Applications:** `SumAnalyzer.html`, `StepAnalyzer.html`


## 🗝️ Key Findings & Equations
Our research identifies the Base-10 number system as a unique **Geometric Singularity** where the system’s iterative path reaches an algebraic equilibrium of $\phi^2$.

### $\phi^2$ The Unified System Identity 
The structural metrics are coupled via the Golden Ratio ($\phi \approx 1.618$):

$$R_S + R_L = \phi^2 \approx 2.618$$

### 👣 Asymptotic Convergence Constants 
The individual ratios converge to exact constants defined by the Base-10 structure:
- **Structural Ratio ($R_S$):** $R_S \rightarrow 3 - \phi \approx 1.382$
- **Sequential Ratio ($R_L$):** $R_L \rightarrow \frac{2}{\phi} \approx 1.236$

### ⊡ Geometric Confluence 
We observe a confluence where the iteration process intersects with the geometric constant $\pi$:

$$\frac{R_S}{\phi^2} \approx \frac{\pi}{6} \approx 0.524$$

### 🕳️ The Base-10 Singularity 
We identify the Base-10 number system as a unique **Geometric Singularity**. While sequence behaviors in other bases follow general conservation principles, the Base-10 system achieves an algebraic equilibrium where the sum of its structural and sequential ratios is exactly $\phi^2$. This demonstrates that the Base-10 iteration process is inherently constrained by the geometric properties of the Golden Ratio.

---

## ✅ Formal Verification in Lean 4
This repository includes a formal verification suite that bridges empirical observation with mathematical necessity. The file `StepAnalyzer_SumAnalyzer.lean` is central to this work; it defines in Lean the digit-sum engine and metrics used to verify that the logic in our Lean proofs is consistent with the logic in our Python models and web applications.
- **Verification of Contraction:** `basin_is_bounded.lean` proves the system is a contraction mapping with a finite attractor basin.
- **Attractor Density:** `basin_density.lean` provides a formal kernel-verified calculation of the global attractor density (1/7).
- **Identity Proof:** `unified_system_identity_proof.lean` utilizes the Lean 4 tactic engine to close the goal for the identity $R_S + R_L = \phi^2$, proving these ratios are the unique algebraic equilibrium of the system.

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
## ⚖️ [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) [![Lean 4 Verified](https://img.shields.io/badge/Lean-4-blue.svg)](https://lean-lang.org/)

**Copyright © 2026 Jonathan $f(n)$ Reed.** 
