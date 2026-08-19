## Utilisateur

Respond in a concise manner by deleting any unnecessary remarks. Give me the formula for the gain of an inverter setup based on the values of resistances R1 and R2. Explain your reasoning.

## IA

For an ideal inverting op-amp:

[
[important]\frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}[/important]
]

**Reasoning:**

* The non-inverting input is grounded, so [important]the inverting node is at virtual ground (≈ 0 V)[/important].
* No current enters the op-amp input, so the [important]current through (R_1) equals the current through (R_2)[/important]:
  [
  [important]\frac{V_{in}}{R_1} = \frac{-V_{out}}{R_2}[/important]
  ]
* Rearranging gives:
  [
  [important]V_{out}/V_{in} = -R_2/R_1[/important]
  ]

Negative sign indicates 180° phase inversion.
