## Utilisateur
Answer concisely, omitting any unnecessary information.
We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA
For a classic differential integrator circuit with two resistors \( R \) and two capacitors \( C \), the output voltage \( V_s \) as a function of the input voltages \( V_1 \) and \( V_2 \) is:
[[important]
\[
V_s = \frac{1}{RC} \int (V_2 - V_1) \, dt + V_s(0)
\][\important]]

**Reasoning:**
The circuit subtracts \( V_1 \) from \( V_2 \) and integrates the result over time, scaled by \( \frac{1}{RC} \). \( V_s(0) \) is the initial condition of the integrator.
