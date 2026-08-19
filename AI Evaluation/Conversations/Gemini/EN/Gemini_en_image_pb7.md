## Utilisateur
Here is an assembly of analog electronics. 
Determine the input-output relationship of the presented filter. Explain your reasoning.
*(image of a differential amplifier circuit diagram featuring an operational amplifier, four resistors labeled R and R', two input voltages e1 and e2, and an output voltage s)*

## IA
This circuit is a classic **differential amplifier** (also known as a subtractor). To find the input-output relationship, we assume an [important]ideal[/important] operational amplifier (Op-Amp) operating in its [important]linear regime[/important].

### 1. Key Assumptions
For an ideal Op-Amp:
* **Virtual Short Circuit:** The voltages at the inverting ($V_-$) and non-inverting ($V_+$) inputs are equal: $[important]V_+ = V_-[/important]$.
* **Infinite Input Impedance:** No current flows into the Op-Amp input terminals.

---

### 2. Analysis of the Non-Inverting Terminal ($V_+$)
The lower part of the circuit is a simple **voltage divider** formed by $R$ and $R'$ connected to the input $e_2$. Using the voltage divider formula:

$$[important]V_+ = e_2 \cdot \frac{R'}{R + R'}[/important]$$

### 3. Analysis of the Inverting Terminal ($V_-$)
The upper part of the circuit involves the input $e_1$, the output $s$, and the resistors $R$ and $R'$. We can apply **Millman's Theorem** (or Kirchhoff's Current Law) at the node $V_-$:

$$[important]\frac{e_1 - V_-}{R} + \frac{s - V_-}{R'} = 0[/important]$$

Rearranging this to solve for $V_-$:

$$\frac{e_1}{R} + \frac{s}{R'} = V_- \left( \frac{1}{R} + \frac{1}{R'} \right)$$
$$\frac{e_1 R' + s R}{R R'} = V_- \left( \frac{R' + R}{R R'} \right)$$
$$[important]V_- = \frac{e_1 R' + s R}{R + R'}[/important]$$

### 4. Combining the Equations
Since $V_+ = V_-$, we set the two expressions equal to each other:

$$\frac{e_2 R'}{R + R'} = \frac{e_1 R' + s R}{R + R'}$$

The denominators $(R + R')$ cancel out:

$$e_2 R' = e_1 R' + s R$$

Now, solve for the output $s$:

$$s R = R'(e_2 - e_1)$$
$$[important]s = \frac{R'}{R}(e_2 - e_1)[/important]$$

---

### 5. Conclusion
The input-output relationship is:

$$s = \frac{R'}{R}(e_2 - e_1)$$

**Reasoning Summary:**
* The circuit calculates the **difference** between the two input signals ($e_2 - e_1$).
* It then applies a **gain factor** determined by the ratio of the resistors $\frac{R'}{R}$. 
* If $R = R'$, the circuit acts as a pure subtractor where $s = e_2 - e_1$.
