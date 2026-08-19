Utilisateur

Answer concisely, omitting any unnecessary information.
We are studying a classic non-inverting summing circuit in which the four resistors have the same value R. Determine Vs as a function of V1 and V2. Explain your reasoning.

IA

At the non-inverting input, no current enters the op-amp, so the node voltage is set only by the resistor network.

With two equal resistors R from V1 and V2 into the node, KCL gives:
[[important](V1 − V+) / R + (V2 − V+) / R = 0

V1 + V2 − 2V+ = 0 ⇒ V+ = (V1 + V2)/2[/important]]

The feedback network has two equal resistors R, so the non-inverting gain is:
Vs = (1 + R/R) V+ = 2V+

Substituting:
Vs = 2 · (V1 + V2)/2 = V1 + V2

So,
[[important] Vs = V1 + V2 [/important]]
