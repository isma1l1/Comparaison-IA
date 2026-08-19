## Utilisateur
Here is an assembly of analog electronics.  
We study Uc(t) according to E(t). Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

## IA
This is a **series R–L–C circuit** with the output taken across the capacitor \(U_C\). That already tells us a lot about the filter behavior.

---

## 1) Nature of the filter

At low frequency:
- \(Z_C = \frac{1}{j\omega C} \to \infty\) → capacitor behaves like an open circuit  
- So almost all the input voltage appears across the capacitor → \(U_C \approx E\)

At high frequency:
- \(Z_C \to 0\) → capacitor behaves like a short circuit  
- So \(U_C \approx 0\)

👉 This is therefore a **[important]2nd-order low-pass filter[/important]**.

---

## 2) Transfer function \(H(j\omega)\)

Using impedance divider:
[important]
- \(Z_R = R\)
- \(Z_L = j\omega L\)
- \(Z_C = \frac{1}{j\omega C}\)
[/important]
\[
[important]H(j\omega) = \frac{U_C}{E} = \frac{Z_C}{Z_R + Z_L + Z_C}[/important]
\]

Substitute:

\[
H(j\omega) = \frac{\frac{1}{j\omega C}}{R + j\omega L + \frac{1}{j\omega C}}
\]

Multiply numerator and denominator by \(j\omega C\):

\[
H(j\omega) = [important]\frac{1}{1 - \omega^2 LC + j\omega RC}[/important]
\]

---

## 3) Canonical form

Define:

- Resonance pulsation:  
\[
[important]\omega_0 = \frac{1}{\sqrt{LC}}[/important]
\]

- Damping factor:  
\[
[important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]
\]

Then:

\[
H(j\omega) = [important]\frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j \frac{\omega}{\omega_0}\frac{1}{Q}}[/important]
\]

---

## 4) Bandwidth

For a series RLC circuit:

\[
[important]\Delta \omega = \frac{R}{L}[/important]
\]

and in frequency:

\[
\Delta f = \frac{R}{2\pi L}
\]

Also:

\[
[important]Q = \frac{\omega_0}{\Delta \omega}[/important]
\]

---

## 5) Bode diagram (qualitative)

### Gain (magnitude)
[important]
- Low frequency (\(\omega \ll \omega_0\)):  
  \( |H| \approx 1 \) → **0 dB**
[/important]
- Around [important]resonance:
  - If \(Q > \frac{1}{\sqrt{2}}\): resonance peak[/important]
  - If heavily damped: smooth transition

- [important]High frequency (\(\omega \gg \omega_0\)):  
  \[
  |H| \sim \frac{1}{\omega^2} \Rightarrow -40\ \text{dB/dec}[/important]
  \]

👉 So:
- Flat at 0 dB
- Possible peak
- Then slope = **−40 dB/dec**

---

### Phase
[important]
- Low frequency:  
  \( \phi \approx 0^\circ \)

- At resonance:  
  \( \phi = -90^\circ \)

- High frequency:  
  \( \phi \to -180^\circ \)
[/important]
---

## 6) Summary

- **Type:** 2nd-order low-pass filter  
- **Transfer function:**  
  \[
  H(j\omega) = \frac{1}{1 - \omega^2 LC + j\omega RC}
  \]
- **Resonance:** \( \omega_0 = \frac{1}{\sqrt{LC}} \)  
- **Bandwidth:** \( \Delta \omega = \frac{R}{L} \)  
- **Slope:** −40 dB/dec at high frequency  
- **Phase:** 0° → −180°

---

If you want, I can sketch the actual Bode plots or show how the resonance peak changes with \(R\).