## Utilisateur

Respond concisely, omitting any unnecessary information.
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.
*(image of an electronic circuit with two operational amplifiers, a capacitor labeled C0, and two resistors labeled αR and (1−α)R forming a network between input voltage u and current i)*

## IA

With both op-amps ideal and in linear operation, their inputs are at equal voltages (virtual short).

The resistor divider ( \alpha R ) and ( (1-\alpha)R ) fixes intermediate node voltages as fractions of the input (u). The feedback forces the voltage across (C_0) to be a scaled version of the input voltage, effectively increasing the charge variation seen at the input.

Carrying out the node analysis (using virtual short conditions and current through (C_0)) leads to an input current:
[
i = C_0 ,\frac{1}{\alpha(1-\alpha)} ,\frac{du}{dt}
]

So the equivalent capacitance is:
[
\boxed{C = \frac{C_0}{\alpha(1-\alpha)}}
]

**Purpose:**
This is a **capacitance multiplier (synthetic capacitor)**. It allows you to realize a much larger effective capacitance using a small physical capacitor (C_0), which is useful when large capacitors are impractical (size, cost, or precision).
