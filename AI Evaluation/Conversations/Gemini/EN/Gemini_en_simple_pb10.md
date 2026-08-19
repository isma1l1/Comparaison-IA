## Utilisateur
We are studying a classic non-inverting summing circuit in which the four resistors have the same value R. Determine Vs as a function of V1 and V2. Explain your reasoning.

---

## IA
To find the output voltage $V_s$ for a non-inverting summing circuit where all resistors have the same value $R$, we need to look at the circuit in two parts: the **voltage divider** at the non-inverting input and the **non-inverting amplifier** stage.

---

### 1. Find the Voltage at the Non-Inverting Terminal ($V_+$)
The input stage consists of two voltage sources, $V_1$ and $V_2$, each connected to the non-inverting terminal through a resistor $R$. Since the op-amp is "ideal," no current flows into the input terminals (infinite input impedance).

We can use **Superposition** or **Nodal Analysis** at the non-inverting node ($V_+$):

$$\frac{V_1 - V_+}{R} + \frac{V_2 - V_+}{R} = 0$$

Multiplying by $R$:
$$(V_1 - V_+) + (V_2 - V_+) = 0$$
$$V_1 + V_2 = 2V_+$$
[[important]$$V_+ = \frac{V_1 + V_2}{2}$$[\important]]

This shows that the voltage at the non-inverting terminal is simply the **average** of the two input voltages.

---

### 2. Determine the Op-Amp Gain
The rest of the circuit is a standard non-inverting amplifier configuration. The gain $A_v$ is determined by the feedback resistor ($R_f$) and the resistor to ground ($R_g$). In your case, both are equal to $R$.

The formula for non-inverting gain is:
$$A_v = 1 + \frac{R_f}{R_g}$$

Substituting $R$ for both values:
[[important]$$A_v = 1 + \frac{R}{R} = 1 + 1 = 2$$[\important]]

---

### 3. Calculate the Final Output ($V_s$)
The output of a non-inverting amplifier is the product of the input voltage at the terminal ($V_+$) and the gain ($A_v$):
[[important]
$$V_s = A_v \cdot V_+$$
$$V_s = 2 \cdot \left( \frac{V_1 + V_2}{2} \right)$$[\important]]

### The Solution
When we simplify the expression, the factors of 2 cancel out:
[[important]
$$V_s = V_1 + V_2$$[\important]]

---

### Summary of Reasoning
* **Input Stage:** The two input resistors act as a passive averager, creating a voltage of $\frac{V_1 + V_2}{2}$ at the non-inverting pin.
* **Gain Stage:** The feedback network creates a gain of exactly $2$.
* **Result:** The gain of 2 perfectly compensates for the division by 2 in the input stage, resulting in an output that is the direct sum of the input voltages.
