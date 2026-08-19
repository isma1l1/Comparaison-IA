## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks.
We consider a differential assembly in electronics. Establish the expression of Vout based on the input voltages and resistors. Explain your reasoning.

## IA
For a differential amplifier assembly with input voltages \( V_1 \) and \( V_2 \), and resistors \( R_1, R_2, R_f, R_g \), the output voltage \( V_{out} \) is:

\[
V_{out} = \left(1 + \frac{R_f}{R_1}\right) \cdot \frac{R_2}{R_1 + R_2} \cdot (V_2 - V_1)
\]

**Reasoning:**
1. The differential input \( (V_2 - V_1) \) is applied to the non-inverting and inverting terminals.
2. The gain is set by \( \left(1 + \frac{R_f}{R_1}\right) \) for the non-inverting configuration.
3. The voltage divider \( \frac{R_2}{R_1 + R_2} \) scales the differential input.
