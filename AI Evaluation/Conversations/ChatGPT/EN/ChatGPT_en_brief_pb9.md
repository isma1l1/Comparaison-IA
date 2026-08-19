## Utilisateur

Answer concisely, omitting any unnecessary information.  We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA

For the **classic op-amp differentiator**:

* capacitor (C) at the input,
* resistor (R) in feedback,
* non-inverting input grounded,

the ideal op-amp assumptions give:

* (v_- \approx 0) (virtual ground),
* no current enters the op-amp input.

The capacitor current is

[
i_C = C\frac{d(v_{in}-v_-)}{dt}
]

Since (v_- \approx 0),

[
i_C = C\frac{dv_{in}}{dt}
]

The same current flows through the feedback resistor:

[
i_R = \frac{v_- - v_{out}}{R}
]

Again using (v_- \approx 0),

[
i_R = -\frac{v_{out}}{R}
]

Equating currents:

[
C\frac{dv_{in}}{dt} = -\frac{v_{out}}{R}
]

Therefore the input-output relationship is

[
\boxed{v_{out}(t) = -RC,\frac{dv_{in}(t)}{dt}}
]

So the circuit outputs a voltage proportional to the **time derivative** of the input, with gain factor (-RC).
