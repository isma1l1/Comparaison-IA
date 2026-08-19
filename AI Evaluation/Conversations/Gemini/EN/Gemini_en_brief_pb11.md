## Utilisateur
Answer concisely, omitting any unnecessary information. 
We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA
To determine the output voltage $V_s$ for a differential integrator, we analyze the circuit based on the ideal op-amp assumptions: the voltages at the inverting ($V_-$) and non-inverting ($V_+$) inputs are equal, and no current enters the input terminals.

### 1. Analysis of the Non-Inverting Input ($V_+$)
The network at the non-inverting input is a low-pass RC filter. Using the voltage divider rule in the s-domain (where the impedance of the capacitor is $Z_C = \frac{1}{sC}$):

[[important]$$V_+ = V_2 \left( \frac{\frac{1}{sC}}{R + \frac{1}{sC}} \right) = V_2 \left( \frac{1}{R s C + 1} \right)$$[\important]]

---

### 2. Analysis of the Inverting Input ($V_-$)
Applying Kirchhoff’s Current Law (KCL) at the inverting node, the current through the resistor $R$ must equal the current through the feedback capacitor $C$:

[[important]$$\frac{V_1 - V_-}{R} = \frac{V_- - V_s}{\frac{1}{sC}}$$[\important]]
$$\frac{V_1 - V_-}{R} = sC(V_- - V_s)$$

### 3. Solving for $V_s$
Since [[important]$V_- = V_+$[\important]], we substitute the expression for $V_+$ into the KCL equation:

$$\frac{V_1}{R} - \frac{V_+}{R} = sC V_+ - sC V_s$$
$$sC V_s = V_+ \left( sC + \frac{1}{R} \right) - \frac{V_1}{R}$$
$$sC V_s = V_+ \left( \frac{RsC + 1}{R} \right) - \frac{V_1}{R}$$

Substitute $V_+ = \frac{V_2}{RsC + 1}$:

$$sC V_s = \left( \frac{V_2}{RsC + 1} \right) \left( \frac{RsC + 1}{R} \right) - \frac{V_1}{R}$$
$$sC V_s = \frac{V_2}{R} - \frac{V_1}{R}$$
[[important]$$V_s = \frac{1}{RCs} (V_2 - V_1)$$[\important]]

---

### Final Result
In the time domain, the output voltage is the integral of the differential input:

$$V_s(t) = \frac{1}{RC} \int (V_2 - V_1) \, dt$$

**Reasoning:** The circuit combines a passive RC integrator at the non-inverting input with an active inverting integrator. Because the components are matched ($R$ and $C$), the common-mode signals cancel out, leaving the integral of the difference between the two input voltages.
