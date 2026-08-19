## Utilisateur
*(image of a Sallen-Key high-pass filter circuit diagram with components R, C, R', and an operational amplifier)*

Answer concisely, omitting any unnecessary details.
Identify the type of filter shown without performing any calculations, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kiloohm, given a cutoff frequency ω₀ = 10⁴ rad/s and a high-frequency gain of 20 dB.

---
## IA
The circuit shown is a **Sallen-Key high-pass filter**.

### Transfer Function (Canonical Form)
The transfer function of a Sallen-Key high-pass filter is:

\[
H(s) = \frac{A \cdot s^2}{s^2 + \frac{1}{R C} s + \frac{1}{R^2 C^2}}
\]

For a high-pass filter, the canonical form is:

\[
H(s) = \frac{A \cdot s^2}{s^2 + \omega_0^2}
\]

where \( A \) is the high-frequency gain.

---
### Values of \( R' \) and \( C \)
Given:
- \( R = 1 \, \text{k}\Omega = 1000 \, \Omega \)
- Cutoff frequency \( \omega_0 = 10^4 \, \text{rad/s} \)
- High-frequency gain \( A = 20 \, \text{dB} = 10 \) (since \( 20 \, \text{dB} = 10 \times \log_{10}(A) \))

For a Sallen-Key high-pass filter, the cutoff frequency is determined by:

\[
\omega_0 = \frac{1}{R C}
\]

Thus:

\[
C = \frac{1}{R \omega_0} = \frac{1}{1000 \times 10^4} = 10^{-8} \, \text{F} = 10 \, \text{nF}
\]

For the high-frequency gain \( A = 10 \), the feedback resistor \( R' \) is related to \( R \) by:

\[
A = 1 + \frac{R'}{R}
\]

Solving for \( R' \):

\[
R' = (A - 1) R = (10 - 1) \times 1000 = 9000 \, \Omega = 9 \, \text{k}\Omega
\]

---
### Summary
- **Filter Type:** Sallen-Key high-pass filter
- **Transfer Function:** \( H(s) = \frac{10 s^2}{s^2 + 10^8} \)
- **Values:** \( R' = 9 \, \text{k}\Omega \), \( C = 10 \, \text{nF} \)
