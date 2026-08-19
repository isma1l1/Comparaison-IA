## Utilisateur
Here is an analog electronic circuit.
Identify the type of filter shown without performing any calculations, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, given a cutoff frequency ω₀ = 10⁴ rad/s and a high-frequency gain of 20 dB.
*(image of an op-amp circuit with a resistor R and capacitor C in series at the input, feeding the inverting input, with feedback resistor R', and the non-inverting input grounded)*

## IA
From the topology alone: the input signal goes through a **series capacitor into the inverting input**, with a feedback resistor \(R'\). That’s the classic signature of an **active first-order high-pass filter (inverting)**.

---

### 1) Transfer function

For an inverting op-amp:
\[
H(s) = -\frac{Z_f}{Z_{in}}
\]

Here:
- \(Z_f = R'\)
- \(Z_{in} = R + \frac{1}{sC}\)

So the transfer function becomes:

\[
H(s) = -\frac{R'}{R + \frac{1}{sC}} = -\frac{R' \, sC}{1 + sRC}
\]

In canonical high-pass form:

\[
H(s) = -\frac{R'}{R} \cdot \frac{s/\omega_0}{1 + s/\omega_0}
\]

where:
\[
\omega_0 = \frac{1}{RC}
\]

---

### 2) Identify parameters

- **Cutoff frequency**:
  \[
  \omega_0 = \frac{1}{RC}
  \]

- **High-frequency gain**:
  \[
  |H(\infty)| = \frac{R'}{R}
  \]

---

### 3) Compute values

#### Given:
- \(R = 1\,\text{k}\Omega\)
- \(\omega_0 = 10^4 \, \text{rad/s}\)
- Gain = \(20\,\text{dB} \Rightarrow 10^{20/20} = 10\)

---

#### (a) Find \(R'\)

\[
\frac{R'}{R} = 10 \Rightarrow R' = 10R = 10 \times 1\,\text{k}\Omega = 10\,\text{k}\Omega
\]

---

#### (b) Find \(C\)

\[
\omega_0 = \frac{1}{RC} \Rightarrow C = \frac{1}{R \omega_0}
\]

\[
C = \frac{1}{(1000)(10^4)} = 10^{-7}\,\text{F} = 100\,\text{nF}
\]

---

### ✅ Final answers

- **Filter type:** First-order **inverting active high-pass filter**
- **Transfer function:**
  \[
  H(s) = -\frac{R'}{R} \cdot \frac{s/\omega_0}{1 + s/\omega_0}
  \]
- **Component values:**
  - \(R' = 10\,\text{k}\Omega\)
  - \(C = 100\,\text{nF}\)

---

If you want, I can sketch the Bode plot or explain the intuition behind why the capacitor placement creates a high-pass response.
```
