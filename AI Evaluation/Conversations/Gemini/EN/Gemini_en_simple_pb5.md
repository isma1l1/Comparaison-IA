## Utilisateur

We study Uc(t) as a function of E(t) in a series RLC circuit. Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

## IA

In an RLC series circuit where the output is taken across the capacitor $C$, we are analyzing a classic second-order system. Here is the breakdown of its behavior and characteristics.

---

### 1. Nature of the Filter
By analyzing the behavior of the components at extreme frequencies, we can determine the filter type:
* **Low Frequencies ($\omega \to 0$):** The capacitor acts as an **open circuit** ($Z_C \to \infty$). The output voltage $U_c$ equals the input voltage $E$.
* **High Frequencies ($\omega \to \infty$):** The capacitor acts as a **short circuit** ($Z_C \to 0$). The output voltage $U_c$ drops to zero.

Since it passes low frequencies and attenuates high frequencies, this is a **[important]Low-Pass Filter[/important]**.

---

### 2. Transfer Function
Using the voltage divider rule in the complex domain (where $j^2 = -1$):

$$[important]H(j\omega) = \frac{\underline{U}_c}{\underline{E}} = \frac{\frac{1}{jC\omega}}{R + jL\omega + \frac{1}{jC\omega}}[/important]$$

Multiplying the numerator and denominator by $jC\omega$, we get the canonical form:

$$H(j\omega) = [important]\frac{1}{1 - LC\omega^2 + jRC\omega}[/important]$$

To simplify, we define the natural resonance frequency $\omega_0$ and the quality factor $Q$:
* $[important]\omega_0 = \frac{1}{\sqrt{LC}}[/important]$
* $[important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]$

The transfer function becomes:
$$H(j\omega) = [important]\frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j\frac{1}{Q}\frac{\omega}{\omega_0}}[/important]$$

---

### 3. Bandwidth ($\Delta\omega$)
For a low-pass filter, the bandwidth is traditionally defined as the frequency range $[0, \omega_c]$ where the gain is within **-3 dB** of the maximum gain. 

If $Q$ is high (specifically $Q > 1/\sqrt{2}$), there is a resonance peak. However, the standard "width" of the resonance (often associated with the band-pass behavior of current) is given by:

$$[important]\Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]$$

*Note: For the capacitor voltage specifically, the actual -3 dB cutoff frequency $\omega_c$ requires solving $|H(j\omega)| = \frac{1}{\sqrt{2}}$, which depends on the specific value of $Q$.*

---

### 4. Bode Diagrams

#### Gain Diagram ($G_{dB}$)
The gain in decibels is $20\log_{10}|H(j\omega)|$.
[important]
* **$\omega \ll \omega_0$:** The gain is approximately **0 dB** (horizontal asymptote).
* **$\omega = \omega_0$:** The gain is $20\log_{10}(Q)$. If $Q > 1/\sqrt{2}$, a resonance peak appears.
* **$\omega \gg \omega_0$:** The term $(\omega/\omega_0)^2$ dominates. The slope becomes **-40 dB/decade**.
[/important]
#### Phase Diagram ($\phi$)
The phase is $\arg(H(j\omega)) = -\arctan\left(\frac{\frac{1}{Q}\frac{\omega}{\omega_0}}{1 - (\frac{\omega}{\omega_0})^2}\right)$.
[important]
* **$\omega \ll \omega_0$:** Phase starts at **0°**.
* **$\omega = \omega_0$:** Phase is exactly **-90°** ($-\pi/2$).
* **$\omega \gg \omega_0$:** Phase asymptotes toward **-180°** ($-\pi$).
[/important]
---

### Summary Table

| Feature | Value / Characteristic |
| :--- | :--- |
| **Filter Type** | [important]2nd Order[/important] Low-Pass |
| **Max Gain** | $1$ (or $Q$ if resonance occurs) |
| **Cutoff Slope** | -40 dB/decade |
| **Phase Shift** | $0$ to $-\pi$ |

What are the specific values for $R$, $L$, and $C$ in your study, or are we keeping this strictly theoretical?