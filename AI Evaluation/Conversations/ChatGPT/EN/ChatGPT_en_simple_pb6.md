```markdown
## Utilisateur
We consider a differential assembly in electronics. Establish the expression of Vout based on the input voltages and resistors. Explain your reasoning.

## IA
<<<<<<< HEAD
Consider the standard differential amplifier built with an ideal operational amplifier and four resistors:[important] \(R_1, R_2\) on the inverting side and \(R_3, R_4\) on the non-inverting side. Let \(V_1\) be the voltage applied to the inverting input through \(R_1\), and \(V_2\) the voltage applied to the non-inverting input through the divider \(R_3\)-\(R_4\).[/important]
=======
Consider the standard differential amplifier built with an [important]ideal[/important] operational amplifier and four resistors: \(R_1, R_2\) on the inverting side and \(R_3, R_4\) on the non-inverting side. Let \(V_1\) be the voltage applied to the inverting input through \(R_1\), and \(V_2\) the voltage applied to the non-inverting input through the divider \(R_3\)-\(R_4\).
>>>>>>> 0c129619b6887b70613a4270fb6c133f144a34bc

Assume an ideal op-amp: input currents are zero and the inputs are at the same potential (virtual short), so \([important]V^- = V^+[/important]\).

First determine \(V^+\). The non-inverting input sees a voltage divider:
\[
[important]V^+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important].
\]

By the virtual short:
\[
[important]V^- = V^+[/important] = V_2 \cdot \frac{R_4}{R_3 + R_4}.
\]

Now apply [important]Kirchhoff’s current law[/important] at the inverting node. Since no current enters the op-amp:
\[
<<<<<<< HEAD
[important]\frac{V_1 - V^-}{R_1} = \frac{V^- - V_{out}}{R_2}[/important]
=======
[important]\frac{V_1 - V^-}{R_1} = \frac{V^- - V_{out}}{R_2}[/important].
>>>>>>> 0c129619b6887b70613a4270fb6c133f144a34bc
\]

Substitute \(V^- = V^+\):
\[
\frac{V_1 - V^+}{R_1} = \frac{V^+ - V_{out}}{R_2}.
\]

Solve for \(V_{out}\):
\[
[important]R_2 (V_1 - V^+) = R_1 (V^+ - V_{out})[/important],
\]
\[
R_2 V_1 - R_2 V^+ = R_1 V^+ - R_1 V_{out},
\]
\[
R_1 V_{out} = R_1 V^+ - R_2 V_1 + R_2 V^+,
\]
\[
<<<<<<< HEAD
[important]V_{out} = V^+ \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1.[/important]
=======
[important]V_{out} = V^+ \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1[/important].
>>>>>>> 0c129619b6887b70613a4270fb6c133f144a34bc
\]

Now substitute \(V^+\):
\[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right) \cdot \frac{R_4}{R_3 + R_4} \cdot V_2 - \frac{R_2}{R_1} V_1[/important].
\]

This is the general expression.

A common special case is when the resistor ratios are matched:
\[
\frac{R_2}{R_1} = \frac{R_4}{R_3}.
\]

Under this condition, the expression simplifies to:
\[
[important]V_{out} = \frac{R_2}{R_1}(V_2 - V_1)[/important],
\]
which shows true differential amplification with gain \(R_2/R_1\).

The key reasoning steps are: use the ideal op-amp constraints, compute the non-inverting node voltage via a divider, enforce equality of input node voltages, and apply KCL at the inverting node to relate currents and solve for the output.
