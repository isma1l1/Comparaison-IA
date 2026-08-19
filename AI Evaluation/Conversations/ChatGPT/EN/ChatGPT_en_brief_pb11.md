## Utilisateur

Answer concisely, omitting any unnecessary information.
We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA

Assume an ideal op-amp with negative feedback, so ([[important]v_- = v_+ = v_x[\important]]) and input currents are zero.

Because the two branches are perfectly symmetrical ((R) and (C) matched), the current injected from each input must flow through its respective capacitor:

[
i_1 = C,\frac{d}{dt}(V_1 - v_x), \quad i_2 = C,\frac{d}{dt}(V_2 - v_x)
]

These currents pass through equal resistors into the summing structure, and by symmetry the net current into the inverting and non-inverting nodes must balance, which forces the capacitor currents to oppose each other:

[
i_1 = - i_2
]

Hence:
[
C\frac{d}{dt}(V_1 - v_x) = -C\frac{d}{dt}(V_2 - v_x)
]

Cancel (C) and expand:
[
\frac{dV_1}{dt} - \frac{dv_x}{dt} = -\frac{dV_2}{dt} + \frac{dv_x}{dt}
]

So:
[
2\frac{dv_x}{dt} = \frac{dV_1}{dt} + \frac{dV_2}{dt}
\quad \Rightarrow \quad
\frac{dv_x}{dt} = \frac{1}{2}\left(\frac{dV_1}{dt} + \frac{dV_2}{dt}\right)
]

Integrating:
[
v_x = \frac{1}{2}(V_1 + V_2) + \text{const}
]

The output stage of a differential integrator subtracts the two capacitor voltages, giving:

[
[[important]V_s = \frac{1}{RC}\int (V_2 - V_1),dt + V_s(0)[\important]]
]

So, up to initial conditions:
[
\boxed{V_s(t) = \frac{1}{RC}\int_0^t \big(V_2(\tau) - V_1(\tau)\big),d\tau}
]
