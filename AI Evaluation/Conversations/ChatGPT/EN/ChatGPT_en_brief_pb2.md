## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. Give me the formula for the gain of a non-inverter setup based on the values of the resistances R1 and R2. Explain your reasoning.

## IA
For a non-inverting amplifier, the voltage gain comes from how the feedback network divides the output voltage and feeds it back to the inverting input.

\[
[important]A_v = 1 + \frac{R_2}{R_1}[/important]
\]

**Reasoning (brief):**
- The op-amp forces its inputs to the same voltage (virtual short), so \([important]V_- = V_+[/important]\).
- The inverting input sees a fraction of the output via the resistor divider \(R_1\) (to ground) and \(R_2\) (to output).
- That fraction is \([important]V_- = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]\).
- Setting \(V_- = V_{in}\) and solving for \([important]V_{out}/V_{in}[important]\) gives \([/important]1 + \frac{R_2}{R_1}[/important]\).

So the gain is always ≥ 1 and increases as \(R_2\) grows relative to \(R_1\).
