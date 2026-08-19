## Utilisateur
We study Uc(t) as a function of E(t) in a series RLC circuit. Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

## IA
We’re looking at a **series RLC circuit** and the output is the capacitor voltage \( U_c(t) \), while the input is \( E(t) \). Let’s go step by step.

---

# 1) Nature of the filter

In a **series RLC circuit**, the total impedance is:
\[
[important]Z(\omega) = R + j\omega L + \frac{1}{j\omega C}[/important]
\]

The output is taken **across the capacitor**, whose impedance is:
\[
Z_C = \frac{1}{j\omega C}
\]

At different frequencies:
- **Low frequency (\(\omega \to 0\))**: capacitor behaves like an open circuit → voltage across it is **large** → output ≈ input  
- **High frequency (\(\omega \to \infty\))**: capacitor behaves like a short circuit → voltage across it → 0  
- Around resonance: energy exchanges between \(L\) and \(C\)

👉 Therefore, this circuit behaves as a:

**➡️ [important]Low-pass filter[/important]**

---

# 2) Transfer function \( H(j\omega) \)

Using the [important]voltage divider[/important]:

\[
[important]H(j\omega) = \frac{U_c}{E} = \frac{Z_C}{Z}[/important]
\]

\[
H(j\omega) = \frac{\frac{1}{j\omega C}}{R + j\omega L + \frac{1}{j\omega C}}
\]

Multiply numerator and denominator by \( j\omega C \):

\[
H(j\omega) = [important]\frac{1}{1 + j\omega RC - \omega^2 LC}[/important]
\]

---

# 3) Canonical form

Define:
- Resonant pulsation:
\[
[important]\omega_0 = \frac{1}{\sqrt{LC}}[/important]
\]
- Quality factor:
\[
[important]Q = \frac{1}{R} \sqrt{\frac{L}{C}}[/important]
\]

Then:

\[
H(j\omega) = \frac{1}{1 + j\frac{\omega}{\omega_0 Q} - \left(\frac{\omega}{\omega_0}\right)^2}
\]

---

# 4) Bandwidth

For a **second-order system**, bandwidth is:

\[
[important]\Delta \omega = \frac{\omega_0}{Q}[/important]
\]

Substitute \(Q\):

\[
\Delta \omega = [important]\frac{R}{L}[/important]
\]

👉 So the **bandwidth** is:
\[
\boxed{\Delta \omega = \frac{R}{L}}
\]

---

# 5) Bode diagram (gain)

### Magnitude behavior:

- **[important]Low frequencies (\(\omega \ll \omega_0\))**  
  \(H \approx 1\) → gain ≈ 0 dB  [/important]

- **At [important]resonance (\(\omega = \omega_0\))**  
  Possible peak if \(Q > \frac{1}{\sqrt{2}}\)[/important]

- **[important]High frequencies (\(\omega \gg \omega_0\))**  
  \[
  H \sim \frac{1}{\omega^2}
  \]
  → slope = **−40 dB/decade**[/important]

---

# 6) Bode diagram (phase)

Phase of:
\[
H(j\omega) = \frac{1}{1 + j\omega RC - \omega^2 LC}
\]

Behavior:
[important]
- **Low frequency** → phase ≈ 0°  
- **At resonance** → phase ≈ −90°  
- **High frequency** → phase → −180°
[/important]
---

# 7) Summary

- **Filter type**: Low-pass (2nd order)
- **Transfer function**:
\[
H(j\omega) = \frac{1}{1 + j\omega RC - \omega^2 LC}
\]
- **Resonant frequency**:
\[
\omega_0 = \frac{1}{\sqrt{LC}}
\]
- **Bandwidth**:
\[
\Delta \omega = \frac{R}{L}
\]
- **Bode gain**:
  - Flat at low freq
  - −40 dB/dec at high freq
- **Phase**:
  - 0° → −180°

---

If you want, I can sketch the Bode plots or show how the resonance peak depends on \(Q\).