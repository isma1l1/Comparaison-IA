## Utilisateur
Here is an analog electronic circuit.
Identify the type of filter shown without performing any calculations, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, given a cutoff frequency ω₀ = 10⁴ rad/s and a high-frequency gain of 20 dB.
*(image of an analog electronic circuit with R, C, R', and an operational amplifier)*

---
## IA
### Analysis of the Circuit

---
#### **1. Type of Filter**
The circuit is a **Sallen-Key topology**, specifically a **second-order low-pass filter**. This is identified by:
- The use of an operational amplifier (op-amp) in a non-inverting configuration.
- The presence of two reactive components (R, C and R', C) in the feedback and input paths.
- The arrangement of the resistors and capacitors, which is typical for a low-pass response.

---
#### **2. Transfer Function in Canonical Form**
For a Sallen-Key low-pass filter, the transfer function in canonical form is:

\[
H(s) = \frac{H_0 \cdot \omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}
\]

Where:
- \( H_0 \) is the **DC gain** (low-frequency gain).
- \( \omega_0 \) is the **cutoff frequency**.
- \( \zeta \) is the **damping ratio**.

For a **Butterworth response** (maximally flat magnitude), \( \zeta = \frac{1}{\sqrt{2}} \).

---
#### **3. High-Frequency Gain**
The high-frequency gain of a Sallen-Key low-pass filter is **0 dB** (or 1 in linear scale) because the op-amp is in a non-inverting configuration, and the feedback network attenuates high-frequency signals. However, the problem states a **high-frequency gain of 20 dB**, which is unusual for a standard Sallen-Key low-pass filter.

This suggests that the circuit might be a **non-inverting amplifier with a low-pass filter**, where the high-frequency gain is determined by the feedback network. For a non-inverting amplifier, the gain is:

\[
H_{\infty} = 1 + \frac{R'}{R}
\]

Given \( H_{\infty} = 20 \, \text{dB} \), which is \( 10 \) in linear scale:

\[
1 + \frac{R'}{R} = 10 \implies \frac{R'}{R} = 9 \implies R' = 9R
\]

For \( R = 1 \, \text{k}\Omega \):

\[
R' = 9 \times 1 \, \text{k}\Omega = 9 \, \text{k}\Omega
\]

---
#### **4. Cutoff Frequency**
The cutoff frequency \( \omega_0 \) for a Sallen-Key low-pass filter is given by:

\[
\omega_0 = \frac{1}{\sqrt{R R' C^2}}
\]

Given \( \omega_0 = 10^4 \, \text{rad/s} \) and \( R = 1 \, \text{k}\Omega \), \( R' = 9 \, \text{k}\Omega \):

\[
10^4 = \frac{1}{\sqrt{10^3 \times 9 \times 10^3 \times C^2}} = \frac{1}{\sqrt{9 \times 10^6 \times C^2}} = \frac{1}{3 \times 10^3 \times C}
\]

Solving for \( C \):

\[
C = \frac{1}{3 \times 10^3 \times 10^4} = \frac{1}{3 \times 10^7} \approx 33.33 \, \text{nF}
\]

---
### Summary of Results
- **Type of Filter:** Sallen-Key second-order low-pass filter.
- **Transfer Function (Canonical Form):**
  \[
  H(s) = \frac{H_0 \cdot \omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}
  \]
  (For Butterworth, \( \zeta = \frac{1}{\sqrt{2}} \), \( H_0 = 1 \).)
- **Values:**
  - \( R' = 9 \, \text{k}\Omega \)
  - \( C \approx 33.33 \, \text{nF} \)
