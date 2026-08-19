## Utilisateur

We are studying a classic non-inverting summing circuit in which the four resistors have the same value R. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA

Assume an ideal op-amp with negative feedback, so ([[important]V_- = V_+[\important]]) and no input current flows into either input.

In this “non-inverting summing” configuration with all four resistors equal to (R), the non-inverting input node (V_+) is connected through three identical resistors to (V_1), (V_2), and the output (V_s). Since the op-amp input draws no current, that node is simply a resistive junction of three equal resistances, so it takes the average of the three connected voltages:

[
V_+ = \frac{V_1 + V_2 + V_s}{3}.
]

The op-amp is used with negative feedback in a unity-feedback (voltage follower) configuration, so:

[
V_s = V_+.
]

Substituting gives:

[
V_s = \frac{V_1 + V_2 + V_s}{3}.
]

Solving:

[
3V_s = V_1 + V_2 + V_s \quad \Rightarrow \quad 2V_s = V_1 + V_2 \quad \Rightarrow \quad V_s = \frac{V_1 + V_2}{2}.
]

So the circuit produces the arithmetic mean of the two input voltages.
