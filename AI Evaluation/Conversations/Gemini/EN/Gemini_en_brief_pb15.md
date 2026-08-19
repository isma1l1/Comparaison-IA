## Utilisateur
Answer concisely, omitting any unnecessary details. 
Identify the type of filter shown without performing any calculations, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kiloohm, given a cutoff frequency ω₀ = 10⁴ rad/s and a high-frequency gain of 20 dB.
*(image of an active high-pass filter circuit diagram featuring an operational amplifier, an input resistor R, an input capacitor C, and a feedback resistor R')*

## IA
## Filter Analysis

### 1. Filter Type
This is an **active high-pass filter** (specifically an inverting amplifier configuration where the input impedance decreases as frequency increases).

---

### 2. Canonical Transfer Function
The transfer function $H(j\omega)$ for this high-pass filter is:
$$H(j\omega) = -A_{\infty} \frac{j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$$
Where:
* $A_{\infty} = \frac{R'}{R}$ (High-frequency gain magnitude)
* $\omega_0 = \frac{1}{RC}$ (Cutoff frequency)

---

### 3. Component Values
Given: $R = 1 \text{ k}\Omega$, $\omega_0 = 10^4 \text{ rad/s}$, and $G_{dB} = 20 \text{ dB}$.

* **Calculate $R'$:**
    A gain of $20 \text{ dB}$ corresponds to a linear magnitude of $10$.
    $$A_{\infty} = \frac{R'}{R} = 10 \implies R' = 10 \times 1 \text{ k}\Omega = \mathbf{10 \text{ k}\Omega}$$

* **Calculate $C$:**
    Using the cutoff frequency formula:
    $$C = \frac{1}{R\omega_0} = \frac{1}{10^3 \times 10^4} = 10^{-7} \text{ F} = \mathbf{100 \text{ nF}}$$
