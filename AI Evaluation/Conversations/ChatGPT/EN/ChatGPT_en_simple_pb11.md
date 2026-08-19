## Utilisateur

We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA

Assume an ideal op-amp (infinite gain, infinite input impedance, zero input current) and that the circuit is perfectly symmetric: each input is processed by an identical RC network (same R, same C), one feeding the inverting side and the other the non-inverting side in a matched way.

A clean way to analyze a “differential integrator” is in the Laplace domain, because each RC section becomes a simple transfer function.

For a single RC integrator (output taken across the capacitor), the transfer function is:
H(s) = 1/(RC s)
Because the two branches are identical, both inputs are subjected to the same dynamic operation:
V1 → (1/(RC s)) · V1
V2 → (1/(RC s)) · V2

The op-amp then forms a difference between the two processed signals (set by the symmetric feedback network). Therefore the output is proportional to the difference of the two integrated inputs:

[[important]Vs(s) = (1/(RC s)) (V2(s) − V1(s))[\important]] 

(The sign depends on which input is connected to the inverting terminal; with the usual convention V1 at inverting and V2 at non-inverting, V2 appears positive and V1 negative.)

Transforming back to the time domain gives:

[[important]Vs(t) = (1/RC) ∫ (V2(t) − V1(t)) dt + Vs(0)[\important]]

If we assume zero initial condition (capacitor initially uncharged or steady-state reference chosen), then:

Vs(t) = (1/RC) ∫ (V2(t) − V1(t)) dt

So the circuit produces the time integral of the voltage difference between the two inputs, scaled by 1/RC.
