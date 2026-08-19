## Utilisateur

We are studying a classic active filter amplifier circuit (the + terminal of the ALI is connected to ground, and the - terminal is connected to the ALI output via a resistor R' and to the input via a capacitor C and a resistor R).
Identify the type of this filter without calculation, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, if a cutoff frequency of ω₀ = 10⁴ rad/s and a gain of 20 dB at high frequencies are desired.

## IA

From the topology: the non-inverting input is grounded and the signal is applied to the inverting node through a series network consisting of a capacitor C and a resistor R, with a feedback resistor R' from output to the inverting input. This is an inverting first-order active filter in which the input impedance is frequency-dependent.

At low frequency, the capacitor blocks the signal, so the gain tends to zero. At high frequency, the capacitor behaves like a short circuit, so the circuit reduces to a simple inverting amplifier with gain -R'/R. Therefore, the circuit is a first-order inverting high-pass filter.

Writing the input impedance as
Z_in = R + 1/(sC)
and Z_f = R'

the transfer function is
H(s) = -Z_f / Z_in
= -R' / (R + 1/(sC))
= -(R'sC) / (1 + sRC)

In canonical form:
H(s) = -(R'/R) · (s/ω₀) / (1 + s/ω₀),
with ω₀ = 1/(RC).

Now apply the specifications:

Cutoff pulsation:
ω₀ = 10⁴ ⇒ RC = 10⁻⁴.
With R = 1 kΩ:
C = (10⁻⁴) / (10³) = 10⁻⁷ F = 100 nF.

High-frequency gain:
|H(∞)| = R'/R = 10 (since 20 dB = 10).
Thus:
R' = 10R = 10 kΩ.

Final results: it is a first-order inverting high-pass filter, with R' = 10 kΩ and C = 100 nF.
