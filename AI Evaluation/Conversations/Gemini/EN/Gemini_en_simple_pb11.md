## Utilisateur

We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA

To determine the output voltage $V_s$ (often denoted as $V_{out}$) for a differential integrator, we look at a circuit that combines the properties of a differential amplifier and a standard integrator.

### The Circuit Configuration
In a classic differential integrator, the components are typically arranged as follows:
* **The Inverting Path:** Input $V_1$ is connected through a resistor $R$ to the inverting input $(-)$. A capacitor $C$ is placed in the feedback loop between the output and the inverting input.
* **The Non-Inverting Path:** Input $V_2$ is connected through a resistor $R$ to the non-inverting input $(+)$, which is then connected to ground via a capacitor $C$.

### Step-by-Step Derivation

To find the relationship, we apply the ideal op-amp assumptions: the currents into the input terminals are zero, and the voltages at the terminals are equal ([[important]$V_+ = V_-$[\important]]).

**1. Calculate the voltage at the non-inverting terminal ($V_+$)**
The non-inverting side acts as a low-pass $RC$ network. Using the voltage divider rule in the $s$-domain (where the impedance of a capacitor $Z_C = \frac{1}{sC}$):

[[important]$$V_+ = V_2 \left( \frac{\frac{1}{sC}}{R + \frac{1}{sC}} \right) = V_2 \left( \frac{1}{R s C + 1} \right)$$[\important]]

**2. Apply KCL at the inverting terminal ($V_-$)**
The sum of currents entering the inverting node must be zero:

[[important]$$\frac{V_1 - V_-}{R} + \frac{V_s - V_-}{\frac{1}{sC}} = 0$$[\important]]

Since $V_- = V_+$, we substitute the expression for $V_+$ into the equation and solve for $V_s$:

$$\frac{V_1}{R} - \frac{V_+}{R} + (V_s - V_+)sC = 0$$
$$\frac{V_1}{R} - \frac{V_+}{R} + V_s s C - V_+ s C = 0$$

Multiplying the entire equation by $R$:
$$V_1 - V_+ + V_s s R C - V_+ s R C = 0$$
$$V_s s R C = V_+(1 + s R C) - V_1$$

**3. Substitute $V_+$ back into the equation**
Using $V_+ = \frac{V_2}{1 + sRC}$:

$$V_s s R C = \left( \frac{V_2}{1 + sRC} \right)(1 + sRC) - V_1$$
$$V_s s R C = V_2 - V_1$$

**4. Final Expression in the Time Domain**
Rearranging for $V_s$ in the $s$-domain:
$$V_s = \frac{1}{sRC} (V_2 - V_1)$$

To return to the time domain, we perform the inverse Laplace transform (where $\frac{1}{s}$ represents integration):

$$V_s(t) = \frac{1}{RC} \int (V_2 - V_1) dt$$

---

### Summary of Reasoning
The circuit effectively subtracts $V_1$ from $V_2$ and then integrates the resulting difference. 
* The **non-inverting input** creates a filtered version of $V_2$.
* The **inverting input** works with the feedback capacitor to integrate the difference between the input and the reference voltage at $V_+$.
* Because the $RC$ constants are matched on both branches, the "proportional" terms cancel out perfectly, leaving only the **integral of the differential input**.
