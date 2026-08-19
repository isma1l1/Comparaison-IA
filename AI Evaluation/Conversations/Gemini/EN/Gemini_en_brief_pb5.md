## Utilisateur

Respond in a concise manner by deleting any unnecessary remarks. 
We study Uc(t) as a function of E(t) in a series RLC circuit. Determines the nature of the represented filter, calculates the transfer function, gives the expression of the bandwidth width and traces the Bode diagrams in gain and phase. Explain your reasoning.

---

## IA

In a series RLC circuit where the output is taken across the capacitor ($U_c$), the system acts as a **[important]Low-Pass Filter[/important]**.

### 1. Transfer Function
Using the voltage divider rule in the complex domain:
$$[important]\underline{H}(j\omega) = \frac{\underline{U}_c}{\underline{E}} = \frac{\frac{1}{jC\omega}}{R + jL\omega + \frac{1}{jC\omega}}[/important]$$

Multiplying by $jC\omega$ and normalizing with $[important]\omega_0 = \frac{1}{\sqrt{LC}}[/important]$ and $[important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]$:
$$[important]\underline{H}(j\omega) = \frac{1}{1 - (\frac{\omega}{\omega_0})^2 + j\frac{1}{Q}\frac{\omega}{\omega_0}}[/important]$$

---

### 2. Nature of the Filter
* **At low frequencies ($\omega \to 0$):** $|\underline{H}| \to 1$ (0 dB). The signal passes.
* **At high frequencies ($\omega \to \infty$):** $|\underline{H}| \to 0$ ($-\infty$ dB). The signal is blocked.
* **Conclusion:** It is a **[important]2nd order[/important] low-pass filter**.

---

### 3. Bandwidth
The bandwidth $\Delta\omega$ is defined at the $-3\text{ dB}$ cutoff. For a high-quality factor ($Q > 1/\sqrt{2}$), the bandwidth around the resonance peak is:
$$[important]\Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]$$

---

### 4. Bode Diagrams

| Feature | Gain Diagram ($G_{dB}$) | Phase Diagram ($\phi$) |
| :--- | :--- | :--- |
| [/mportant]**Low Freq** | Flat at $0\text{ dB}$ | Starts at $0$[/important] |
| **[important]At $\omega_0$** | Peak of $+20\log(Q)\text{ dB}$ | Crossing at $-\pi/2$[/important] ($-90^\circ$) |
| **[important]High Freq** | Slope of $-40\text{ dB/decade}$ | Tends toward $-\pi$[/important] ($-180^\circ$) |

* **Gain Reasoning:** The $1/\omega^2$ dependence at high frequencies results in a quadratic roll-off ($-40\text{ dB/dec}$).
* **Phase Reasoning:** The denominator transitions from purely real (positive) to purely real (negative), passing through purely imaginary at resonance.
