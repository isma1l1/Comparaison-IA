## Utilisateur

We consider a differential assembly in electronics. Establish the expression of Vout based on the input voltages and resistors. Explain your reasoning.

## IA

To establish the expression for the output voltage of a differential amplifier (also known as a difference amplifier), we typically analyze a standard operational amplifier (op-amp) circuit with four resistors.

### The Circuit Configuration
A standard differential assembly consists of:
[important]
* Two input voltages: $V_1$ (connected to the inverting terminal via $R_1$) and $V_2$ (connected to the non-inverting terminal via $R_3$).
* Four resistors: $R_1, R_2, R_3, \text{and } R_4$.
[/important]
---

### Step-by-Step Derivation


To find $V_{out}$, we assume an **[important]ideal[/important] op-amp**, which implies two key rules:
1.  **[important]Infinite Input Impedance[/important]:** No current flows into the op-amp input terminals ($I_+ = I_- = 0$).
2.  **Virtual Short Circuit:** In a negative feedback configuration, the voltages at the input terminals are equal ($[important]V_+ = V_-[/important]$).

#### 1. Calculate the Voltage at the Non-Inverting Terminal ($V_+$)
The non-inverting terminal is essentially a voltage divider formed by $V_2$, $R_3$, and $R_4$:
$$[important]V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

#### 2. Calculate the Voltage at the Inverting Terminal ($V_-$)
Using [important]Kirchhoff's Current Law[/important] (KCL) at the inverting node, the sum of currents entering the node is zero. Since no current enters the op-amp:
$$[important]\frac{V_1 - V_-}{R_1} + \frac{V_{out} - V_-}{R_2} = 0[/important]$$

#### 3. Apply the Virtual Short ($[important]V_+ = V_-[/important]$)
Substitute the expression for $V_+$ into the KCL equation:
$$[important]\frac{V_1}{R_1} + \frac{V_{out}}{R_2} = V_- \left( \frac{1}{R_1} + \frac{1}{R_2} \right)[/important]$$
$$[important]\frac{V_1}{R_1} + \frac{V_{out}}{R_2} = \left( V_2 \cdot \frac{R_4}{R_3 + R_4} \right) \left( \frac{R_1 + R_2}{R_1 R_2} \right)[/important]$$

#### 4. Solve for $V_{out}$
Isolating $V_{out}$ gives us the general expression:
$$[important]V_{out} = V_2 \left( \frac{R_4}{R_3 + R_4} \right) \left( \frac{R_1 + R_2}{R_1} \right) - V_1 \left( \frac{R_2}{R_1} \right)[/important]$$

---

### The Balanced Condition
In most practical applications, the resistors are chosen such that the ratios are balanced:
$$\frac{R_2}{R_1} = \frac{R_4}{R_3}$$

When this condition is met, the formula simplifies beautifully. Let $k = \frac{R_2}{R_1}$. The expression becomes:

$$[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]$$

### Summary of Reasoning
* **[important]Superposition[/important]:** The circuit acts as an inverting amplifier for $V_1$ and a non-inverting amplifier (with a preliminary voltage divider) for $V_2$.
* **Soustraction:** By setting the resistor ratios equal, the circuit subtracts the two input signals and multiplies the result by a gain factor.
* **Common Mode Rejection:** This specific setup is designed to ignore voltages that are common to both inputs (noise) and only amplify the difference between them.
