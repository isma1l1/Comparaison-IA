## Utilisateur

{
type: uploaded file
fileName: schema_rlc.png
}
Here is an assembly of analog electronics. 
We study Uc(t) according to E(t). Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

## IA

Based on the provided circuit diagram, we are looking at a **series RLC circuit**. The output is taken across the capacitor ($U_C$), and the input is the voltage source $E$.

Here is the step-by-step analysis of this system.

---

## 1. Nature of the Filter
To determine the nature of the filter, we look at the behavior of the components at extreme frequencies:
* **At low frequencies ($\omega \to 0$):** The inductor acts as a short circuit, and the capacitor acts as an open circuit. Since the output $U_C$ is measured across the open circuit, $U_C \approx E$.
* **At high frequencies ($\omega \to \infty$):** The inductor acts as an open circuit, blocking the current. The capacitor acts as a short circuit. Thus, $U_C \to 0$.

**Conclusion:** This is a **[important]second-order low-pass filter[/important]**.

---

## 2. Transfer Function
Using the voltage divider rule in the complex domain (where $j^2 = -1$):

$$[important]H(j\omega) = \frac{\underline{U}_C}{\underline{E}} = \frac{\frac{1}{jC\omega}}{R + jL\omega + \frac{1}{jC\omega}}[/important]$$

To simplify, we multiply the numerator and denominator by $jC\omega$:

$$H(j\omega) = [important]\frac{1}{1 - LC\omega^2 + jRC\omega}[/important]$$

### Canonical Form
We introduce the proper pulsation $\omega_0$ and the quality factor $Q$:
* $[important]\omega_0 = \frac{1}{\sqrt{LC}[/important]}$
* $[important]Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{L\omega_0}{R}[/important]$

The transfer function becomes:
$$H(j\omega) = [important]\frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j\frac{1}{Q}\frac{\omega}{\omega_0}}[/important]$$

---

## 3. Bandwidth
For a low-pass filter, the bandwidth $\Delta \omega$ is defined at $-3\text{ dB}$, where $|H(j\omega)| = \frac{H_{max}}{\sqrt{2}}$.
For a high quality factor ($Q > 1/\sqrt{2}$), the cutoff frequency is approximately $\omega_0$. 

However, if we look at the "selectivity" of the resonance (if $U_C$ were peaking), the width of the resonance peak is:
$$[important]\Delta \omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]$$

---

## 4. Bode Diagrams

### Gain Diagram ($G_{dB}$)
The gain in decibels is $G_{dB} = 20 \log|H(j\omega)|$.
* **[important]Low frequencies ($\omega \ll \omega_0$):** $G_{dB} \approx 0\text{ dB}$. The slope is $0\text{ dB/decade}[/important]$.
* **[important]High frequencies ($\omega \gg \omega_0$):** $G_{dB} \approx -40 \log\left(\frac{\omega}{\omega_0}\right)$. The slope is **$-40\text{ dB/decade}[/important]$**.
* **At [important]resonance ($\omega = \omega_0$):** The gain is $20 \log(Q)$. If $Q > 1/\sqrt{2}$, there is a resonance peak.[/important]

### Phase Diagram ($\phi$)
The phase is $\phi = \arg(H(j\omega)) = -\arctan\left( \frac{\frac{1}{Q}\frac{\omega}{\omega_0}}{1 - (\frac{\omega}{\omega_0})^2} \right)$.
[important]
* **Low frequencies:** $\phi \to 0^\circ$.
* **At $\omega = \omega_0$:** $\phi = -90^\circ$ ($-\pi/2$ rad).
* **High frequencies:** $\phi \to -180^\circ$ ($-\pi$ rad).
[/important]
---

## Summary Table

| Parameter | Expression |
| :--- | :--- |
| **Type** | 2nd Order Low-Pass |
| **Resonance Pulsation** | $\omega_0 = 1/\sqrt{LC}$ |
| **Damping/Quality** | $Q = \frac{1}{R}\sqrt{L/C}$ |
| **High Freq. Slope** | $-40 \text{ dB/decade}$ |
| **Phase Shift** | $0 \text{ to } -180^\circ$ |