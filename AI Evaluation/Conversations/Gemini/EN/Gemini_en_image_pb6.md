## Utilisateur
Here is an assembly of analog electronics. 
Establish the expression of Vout according to the input tensions. Explain your reasoning.
*(image of a differential amplifier circuit featuring an operational amplifier, two input voltages Vin1 and Vin2, and resistors R1, R2, Rf, and Rg)*

## IA
This circuit is a **Differential Amplifier** (also known as a subtractor). It uses an Operational Amplifier (Op-Amp) to amplify the difference between two input voltages, $V_{in1}$ and $V_{in2}$.

To find the expression for $V_{out}$, we assume an **[important]ideal[/important] Op-Amp**, which gives us two key rules:
1.  **[important]Infinite Input Impedance[/important]:** No current enters the (+) or (-) input terminals.
2.  **Virtual Short Circuit:** If there is [important]negative feedback[/important] (which $R_f$ provides), the voltage at the inverting input ($V_-$) is equal to the voltage at the non-inverting input ($V_+$).

---

### Step 1: Calculate $V_+$ (Non-inverting terminal)
The non-inverting input is connected to a [important]voltage divider [/important]formed by $V_{in2}$, $R_2$, and $R_g$. Since no current flows into the Op-Amp, we use the standard voltage divider formula:

$$[important]V_+ = V_{in2} \cdot \left( \frac{R_g}{R_2 + R_g} \right)[/important]$$

### Step 2: Apply KCL at $V_-$ (Inverting terminal)

According to the virtual short principle, $[important]V_- = V_+[/important]$. We apply [important]Kirchhoff’s Current Law[/important] (KCL) at the node $V_-$. The sum of currents leaving the node is zero:

$$[important]\frac{V_- - V_{in1}}{R_1} + \frac{V_- - V_{out}}{R_f} = 0[/important]$$


Rearranging to solve for $V_{out}$:

$$[important]\frac{V_{out}}{R_f} = V_- \left( \frac{1}{R_1} + \frac{1}{R_f} \right) - \frac{V_{in1}}{R_1}[/important]$$

$$[important]V_{out} = V_- \left( 1 + \frac{R_f}{R_1} \right) - V_{in1} \left( \frac{R_f}{R_1} \right)[/important]$$

### Step 3: Final Expression
Substitute the expression for $V_+$ (since $V_- = V_+$) into the equation above:

$$[important]V_{out} = \left[ V_{in2} \cdot \left( \frac{R_g}{R_2 + R_g} \right) \right] \cdot \left( 1 + \frac{R_f}{R_1} \right) - V_{in1} \left( \frac{R_f}{R_1} \right)[/important]$$

Which simplifies to:

$$[/important]V_{out} = V_{in2} \left( \frac{R_g}{R_2 + R_g} \right) \left( \frac{R_1 + R_f}{R_1} \right) - V_{in1} \left( \frac{R_f}{R_1} \right)[/important]$$

---

### Special Case: Balanced Bridge
In most practical applications, the resistors are chosen such that the ratios are balanced (i.e., $\frac{R_f}{R_1} = \frac{R_g}{R_2}$). If this condition is met, the formula simplifies beautifully to a pure differential gain:

$$[important]V_{out} = \frac{R_f}{R_1} (V_{in2} - V_{in1})[/important]$$

This allows the circuit to reject "common-mode" noise (voltage present on both inputs) and only amplify the signal difference.
