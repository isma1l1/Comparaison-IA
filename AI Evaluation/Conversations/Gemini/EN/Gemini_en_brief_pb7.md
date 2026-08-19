## User

Respond in a concise manner by deleting any unnecessary remarks. We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA

A standard difference amplifier uses an operational amplifier (op-amp) with two matched resistor pairs to amplify the difference between two input voltages ($V_1$ and $V_2$).

### 1. Circuit Assumptions and Definitions

* **Resistor Matching:** Let the input resistors be $R_1$ and the feedback/ground resistors be $R_2$.
* **Ideal Op-Amp Behavior:** * No current enters the op-amp input terminals ($I_+ = I_- = 0$).
* Negative feedback maintains the virtual short condition: $V_+ = V_-$.



---

### 2. Derivation

**Step 1: Determine the voltage at the non-inverting node ($V_+$)**
The network at the non-inverting input is a simple voltage divider driven by $V_2$:


$$V_+ = V_2 \left( \frac{R_2}{R_1 + R_2} \right)$$

**Step 2: Apply Kirchhoff's Current Law (KCL) at the inverting node ($V_-$)**
Since no current enters the op-amp, the current flowing from $V_1$ through the input resistor equals the current flowing through the feedback resistor to $V_{out}$:


$$\frac{V_1 - V_-}{R_1} = \frac{V_- - V_{out}}{R_2}$$

**Step 3: Substitute $V_- = V_+$ and simplify**
Rearranging the KCL equation for $V_{out}$:


$$\frac{V_1}{R_1} + \frac{V_{out}}{R_2} = V_- \left( \frac{1}{R_1} + \frac{1}{R_2} \right)$$

$$V_{out} = R_2 \left[ V_- \left( \frac{R_1 + R_2}{R_1 R_2} \right) - \frac{V_1}{R_1} \right] = V_- \left( \frac{R_1 + R_2}{R_1} \right) - \frac{R_2}{R_1}V_1$$

Substitute the expression for $V_+$ (since $V_- = V_+$):


$$V_{out} = \left[ V_2 \left( \frac{R_2}{R_1 + R_2} \right) \right] \left( \frac{R_1 + R_2}{R_1} \right) - \frac{R_2}{R_1}V_1$$

The $(R_1 + R_2)$ terms cancel out:


$$V_{out} = \frac{R_2}{R_1}V_2 - \frac{R_2}{R_1}V_1$$

---

### 3. Input-Output Relationship

Factoring out the resistor ratio yields the final ideal transfer function:

$$V_{out} = \frac{R_2}{R_1}(V_2 - V_1)$$

The output voltage is directly proportional to the difference between the two input voltages, scaled by the gain factor $\frac{R_2}{R_1}$.
