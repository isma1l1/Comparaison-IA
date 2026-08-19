## Utilisateur
Here is an assembly of analog electronics.
Determine the input-output relationship of the presented filter. Explain your reasoning.
*(image of a differential amplifier circuit with resistors R, R', and input voltages e1, e2, and output voltage s)*

---
## IA
This circuit is a **differential amplifier** using operational amplifiers (op-amps) and resistors. It is a classic configuration for subtracting two input voltages, \( e_1 \) and \( e_2 \), and producing an output voltage \( s \).

---

## Input-Output Relationship

The input-output relationship for this circuit is:

\[
s = \frac{R'}{R} (e_1 - e_2)
\]

---

### Reasoning

1. **Circuit Configuration**:
   - The circuit uses an op-amp with resistors \( R \) and \( R' \).
   - \( e_1 \) is applied to the non-inverting terminal (+) through a resistor \( R \).
   - \( e_2 \) is applied to the inverting terminal (-) through a resistor \( R \).
   - Feedback is provided via resistor \( R' \) from the output to the inverting terminal.

2. **Ideal Op-Amp Assumptions**:
   - The op-amp is ideal, so the input currents to the op-amp terminals are zero.
   - The voltage at the inverting and non-inverting terminals are equal (virtual short).

3. **Applying Kirchhoff's Current Law (KCL)**:
   - At the inverting terminal (-):
     The current through \( R \) (from \( e_2 \)) and the current through \( R' \) (feedback) must sum to zero.
     \[
     \frac{e_2 - v_-}{R} + \frac{s - v_-}{R'} = 0
     \]
     Since \( v_- = v_+ \) (virtual short), and \( v_+ = e_1 \) (from the non-inverting terminal):
     \[
     \frac{e_2 - e_1}{R} + \frac{s - e_1}{R'} = 0
     \]

4. **Solving for \( s \)**:
   - Rearrange the equation:
     \[
     \frac{e_2 - e_1}{R} = -\frac{s - e_1}{R'}
     \]
     \[
     (e_2 - e_1) R' = - (s - e_1) R
     \]
     \[
     s R = (e_1 - e_2) R'
     \]
     \[
     s = \frac{R'}{R} (e_1 - e_2)
     \]

---
### Conclusion
The output voltage \( s \) is proportional to the difference between the input voltages \( e_1 \) and \( e_2 \), scaled by the ratio \( \frac{R'}{R} \). This is the defining behavior of a **differential amplifier**.
