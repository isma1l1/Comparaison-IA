## Utilisateur
Here is an analog electronics circuit. 
Determine the input-output relationship of the filter shown. Explain your reasoning.
*(image of an operational amplifier circuit with a capacitor at the inverting input and a resistor in the feedback loop)*

---

## IA
Based on the circuit diagram provided, this is an **Inverting Differentiator** (or more specifically, a high-pass filter configuration).

Here is the breakdown of the input-output relationship and the reasoning behind it.

---

### 1. Circuit Identification
The circuit consists of an operational amplifier (op-amp) with:
* A **capacitor** ($C$) at the input path.
* A **resistor** ($R$) in the feedback path.
* The non-inverting input ($+$) connected to **ground**.
* The input signal $e$ applied to the inverting input ($-$) through the capacitor.

---

### 2. Theoretical Reasoning
To find the relationship between the input voltage $e(t)$ and the output voltage $s(t)$, we apply the two fundamental rules of ideal op-amps:
1.  **Virtual Ground:** Since the non-inverting terminal is grounded, the inverting terminal is also at $0V$ (virtual ground).
2.  **High Input Impedance:** No current flows into the op-amp terminals. Therefore, the current flowing through the capacitor ($i_C$) must be equal to the current flowing through the feedback resistor ($i_R$).

#### Step-by-Step Derivation:
* **Current through the capacitor:** The current through a capacitor is defined by the rate of change of voltage across it. Since one side is at $e$ and the other is at $0V$:
$$i_C = C \frac{de}{dt}$$

* **Current through the resistor:** The current flows from the virtual ground ($0V$) toward the output $s$:
$$i_R = \frac{0 - s}{R} = -\frac{s}{R}$$

* **Equating the currents ($i_C = i_R$):**
$$C \frac{de}{dt} = -\frac{s}{R}$$

---

### 3. The Input-Output Relationship
By isolating the output signal $s$, we get the time-domain equation:

$$s(t) = -RC \frac{de(t)}{dt}$$

In the frequency domain (using Laplace transforms where $\frac{d}{dt}$ becomes $j\omega$ or $s$), the transfer function $H(j\omega)$ is:

$$H(j\omega) = \frac{S(j\omega)}{E(j\omega)} = -j\omega RC$$

---

### 4. Conclusion
* **Function:** This circuit acts as a **differentiator**. The output voltage is proportional to the rate of change (derivative) of the input voltage.
* **Inversion:** The negative sign indicates a **180° phase shift** (inversion).
* **Filter Type:** This is a basic **High-Pass Filter**. It blocks DC signals (where $\frac{de}{dt} = 0$) and produces an output that increases in magnitude as the frequency of the input signal increases.

> **Note:** In practical applications, a small resistor is often added in series with the capacitor to prevent high-frequency noise from saturating the op-amp, as a "pure" differentiator is highly sensitive to noise.
