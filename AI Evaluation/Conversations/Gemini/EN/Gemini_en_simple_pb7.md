## Utilisateur

We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA

To find the input-output relationship of a standard difference amplifier (also known as a differential amplifier) with matched resistor pairs, we can analyze the circuit using the ideal op-amp characteristics and the principle of superposition.

---

## 1. Circuit Configuration and Assumptions

Let's define the components of the standard difference amplifier:

* **Inputs:** $V_1$ is connected to the inverting input side, and $V_2$ is connected to the non-inverting input side.
* **Resistors:** * The inverting path has resistors $R_1$ (input) and $R_2$ (feedback).
* The non-inverting path has resistors $R_3$ (input to $V_2$) and $R_4$ (to ground).


* **Matched Pairs Condition:** For a standard difference amplifier, the resistor pairs are matched such that:

$$\frac{R_2}{R_1} = \frac{R_4}{R_3}$$



### Ideal Op-Amp Characteristics

1. **Virtual Short:** The voltages at the inverting ($V_-$) and non-inverting ($V_+$) terminals are equal ($V_- = V_+$).
2. **Zero Input Current:** No current flows into the op-amp input terminals ($I_- = I_+ = 0$).

---

## 2. Derivation Using Superposition

Because the circuit is linear, we can determine the output voltage $V_{out}$ by calculating the individual effects of $V_1$ and $V_2$ independently, and then summing them together ($V_{out} = V_{out1} + V_{out2}$).

### Step A: Effect of $V_2$ (Inverting input $V_1 = 0$)

When $V_1$ is grounded, the circuit behaves as a non-inverting amplifier.

1. First, find the voltage $V_+$ at the non-inverting terminal using the voltage divider rule:

$$V_+ = V_2 \left( \frac{R_4}{R_3 + R_4} \right)$$


2. The output due to $V_2$ is given by the standard non-inverting amplifier formula:

$$V_{out2} = V_+ \left( 1 + \frac{R_2}{R_1} \right) = V_2 \left( \frac{R_4}{R_3 + R_4} \right) \left( 1 + \frac{R_2}{R_1} \right)$$



### Step B: Effect of $V_1$ (Non-inverting input $V_2 = 0$)

When $V_2$ is grounded, no current flows through $R_3$ and $R_4$, meaning $V_+ = 0$. By the virtual short condition, $V_- = 0$ as well.

The circuit now behaves exactly like a standard inverting amplifier:


$$V_{out1} = -V_1 \left( \frac{R_2}{R_1} \right)$$

### Step C: Total Output

Combining both components yields the general transfer function:


$$V_{out} = V_2 \left( \frac{R_4}{R_3 + R_4} \right) \left( \frac{R_1 + R_2}{R_1} \right) - V_1 \left( \frac{R_2}{R_1} \right)$$

---

## 3. Applying the Matched Resistor Condition

To simplify this for a standard difference amplifier, we apply the matching condition $\frac{R_4}{R_3} = \frac{R_2}{R_1}$, which can also be written as $R_3 = R_1$ and $R_4 = R_2$.

Let's substitute $R_3 = R_1$ and $R_4 = R_2$ into the $V_{out2}$ term:


$$V_{out2} = V_2 \left( \frac{R_2}{R_1 + R_2} \right) \left( \frac{R_1 + R_2}{R_1} \right)$$

Notice that the $(R_1 + R_2)$ terms cancel out perfectly:


$$V_{out2} = V_2 \left( \frac{R_2}{R_1} \right)$$

Now, substitute this back into the total output equation:


$$V_{out} = V_2 \left( \frac{R_2}{R_1} \right) - V_1 \left( \frac{R_2}{R_1} \right)$$

---

## 4. Final Input-Output Relationship

Factoring out the common resistance ratio gives the final input-output relationship:

$$V_{out} = \frac{R_2}{R_1} (V_2 - V_1)$$

> **Conclusion:** The output voltage is directly proportional to the difference between the two input voltages ($V_2 - V_1$). The voltage gain of the system is determined entirely by the ratio of the matched resistor pairs, denoted as $A_d = \frac{R_2}{R_1}$.
