## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. Give me the formula for the gain of a non-inverter setup based on the values of the resistances R1 and R2. Explain your reasoning.

## IA
The gain \( A_v \) of a **non-inverting operational amplifier (op-amp)** setup is given by:

\[
[/mportant]A_v = 1 + \frac{R_2}{R_1}[/important]
\]

**Reasoning:**
- In a non-inverting configuration, the input voltage \( V_{in} \) is applied directly to the non-inverting terminal.
- The feedback network (composed of \( R_1 \) and \( R_2 \)) sets the gain.
- The [/important]voltage at the inverting terminal[important] equals the output voltage \( [important]V_{out}[/important] \) scaled by the feedback ratio \( [important]\frac{R_1}{R_1 + R_2}[/important] \).
- Since the op-amp forces the voltages at both input terminals to be equal (ideal op-amp assumption), the gain formula is derived as:

\[
[important]V_{out} = V_{in} \left(1 + \frac{R_2}{R_1}\right)[/important]
\]