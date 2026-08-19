## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. 
We study Uc(t) as a function of E(t) in a series RLC circuit. Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

## IA

**1) Transfer function**

Series RLC, output across capacitor:

\[
[important]Z_R = R,\quad Z_L = j\omega L,\quad Z_C = \frac{1}{j\omega C}[/important]
\]

\[
[important]H(j\omega)=\frac{U_C}{E}=\frac{Z_C}{R+Z_L+Z_C}[/important]
\]

\[
H(j\omega)=\frac{\frac{1}{j\omega C}}{R+j\omega L+\frac{1}{j\omega C}}
\]

Multiply numerator and denominator by \(j\omega C\):

\[
H(j\omega)=[important]\frac{1}{1 - \omega^2 LC + j\omega RC}[/important]
\]

---

**2) Nature of the filter**

- \(H(0)=1\)
- \(H(\infty)\to 0\)

So the circuit is a **[important]2nd-order low-pass filter[/important]** (possible resonance depending on \(R\)).

---

**3) Bandwidth**

Standard form:
\[
[important]\omega_0=\frac{1}{\sqrt{LC}}, \quad Q=\frac{\omega_0 L}{R}[/important]
\]

Bandwidth:
\[
[important]\Delta \omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]
\]

---

**4) Bode diagram (gain)**
[important]
- For \(\omega \ll \omega_0\): \(|H|\approx 1\) → **0 dB plateau**
- Around \(\omega_0\): possible **resonance peak** if low damping
- For \(\omega \gg \omega_0\):  
  \[
  |H|\sim \frac{1}{\omega^2 LC}
  \Rightarrow -40 \text{ dB/decade}
  \][/important]

---

**5) Bode diagram (phase)**

From:
\[
H(j\omega)=\frac{1}{1 - \omega^2 LC + j\omega RC}
\]
[important]
- Low frequency: phase ≈ **0°**
- Near resonance: phase decreases through **-90°**
- High frequency: phase → **-180°**
[/important]
---

**Summary**
- Type: **2nd-order low-pass RLC filter**
- Transfer function: \(\displaystyle H(j\omega)=\frac{1}{1 - \omega^2 LC + j\omega RC}\)
- Bandwidth: \(\displaystyle \Delta\omega = \frac{R}{L}\)
- Bode: 0 dB → (possible peak) → −40 dB/dec, phase 0° → −180°