## Utilisateur

Respond in a concise manner by deleting any unnecessary remarks.
We consider a differential assembly in electronics. Establish the expression of Vout based on the input voltages and resistors. Explain your reasoning.

## IA

Assume an [important]ideal[/important] op-amp (input currents ≈ 0 and [important]V+ = V−[/important]).

Non-inverting input is set by a [important]divider[/important]:
[
[important]V_+ = \frac{R_4}{R_3 + R_4} V_2[/important]
]

Thus:
[
[important]V_- = V_+[/important] = \frac{R_4}{R_3 + R_4} V_2
]

Apply [important]KCL[/important] at the inverting node:
[
[important]\frac{V_1 - V_-}{R_1} + \frac{V_{out} - V_-}{R_2} = 0[/important]
]

Solve for (V_{out}):
[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right)V_- - \frac{R_2}{R_1}V_1[/important]
]

Substitute (V_-):
[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right)\frac{R_4}{R_3 + R_4}V_2 - \frac{R_2}{R_1}V_1[/important]
]

If the resistor ratios are matched:
[
\frac{R_2}{R_1} = \frac{R_4}{R_3}
]

then the expression simplifies to:
[
[important]V_{out} = \frac{R_2}{R_1}(V_2 - V_1)[/important]
]
