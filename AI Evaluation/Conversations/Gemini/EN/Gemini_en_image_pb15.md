## Utilisateur

Here is an analog electronic circuit.
Identify the type of filter shown without performing any calculations, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, given a cutoff frequency ω₀ = 10⁴ rad/s and a high-frequency gain of 20 dB.
*(image of an active high-pass filter circuit using an operational amplifier in an inverting configuration with a resistor R and capacitor C in series at the input and a feedback resistor R')*

## IA

Based on the circuit diagram provided, we are looking at an operational amplifier (op-amp) in an **inverting configuration**.

### 1. Circuit Identification
Without formal calculation, we can identify this as a **First-Order Active High-Pass Filter**.

* **Low Frequencies:** At $ \omega \to 0 $, the capacitor $ C $acts as an open circuit. No current flows from the source$ e $, so the output $s$ is zero.
* **High Frequencies:** At $ \omega \to \infty $, the capacitor $ C $acts as a short circuit (a wire). The circuit behaves like a standard inverting amplifier with a gain determined by$ -R'/R $.
* **Conclusion:** Since it blocks low frequencies and passes high frequencies, it is a high-pass filter.

---

### 2. Transfer Function (Canonical Form)
The transfer function $H(j\omega) = \frac{\underline{s}}{\underline{e}}$ for an active high-pass filter is expressed as:

$$H(j\omega) = A_{\infty} \frac{j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$$

Where:
* **$ A_{\infty} $** is the high-frequency gain: $A_{\infty} = -\frac{R'}{R}$
* **$ \omega_0 $** is the cutoff frequency: $\omega_0 = \frac{1}{(R+R_{series})C}$. However, in this specific topology where $R$ and $ C $are in series at the input, the cutoff frequency is$ \omega_0 = \frac{1}{RC} $.

---

### 3. Component Value Calculations
We are given:
* $R = 1 \text{ k}\Omega$
* $\omega_0 = 10^4 \text{ rad/s}$
* $G_{dB} = 20 \text{ dB}$ (High-frequency gain magnitude)

#### Finding $ R' $
The gain magnitude in decibels is defined as $20 \log_{10}(|A_{\infty}|)$.
$$20 = 20 \log_{10} \left( \frac{R'}{R} \right)$$
$$1 = \log_{10} \left( \frac{R'}{R} \right) \implies \frac{R'}{R} = 10^1 = 10$$
$$R' = 10 \times R = 10 \times 1 \text{ k}\Omega = \mathbf{10 \text{ k}\Omega}$$

#### Finding $C$
Using the formula for the cutoff frequency:
$$\omega_0 = \frac{1}{RC}$$
$$C = \frac{1}{R \cdot \omega_0}$$
$$C = \frac{1}{10^3 \cdot 10^4} = 10^{-7} \text{ F}$$
$$C = \mathbf{100 \text{ nF}}$$

---

### Summary of Results
| Parameter | Value |
| :--- | :--- |
| **Filter Type** | First-Order Active High-Pass |
| **Resistor $ R' $** | $10 \text{ k}\Omega$ |
| **Capacitor $ C $** | $100 \text{ nF}$ |
