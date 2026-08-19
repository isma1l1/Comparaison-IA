## Utilisateur

Respond in a concise manner by deleting any unnecessary remarks. We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA

For the standard difference amplifier (subtractor) with an ideal op-amp and matched resistor ratios,

\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}
\]

the circuit is:

- \(V_1\) applied to the inverting input through \(R_1\), with feedback \(R_2\)
- \(V_2\) applied to the non-inverting input through divider \(R_3,R_4\)

Using ideal op-amp assumptions:

- input currents are zero
- \(V_- = V_+\)

First compute the non-inverting node voltage:

\[
V_+ = \frac{R_4}{R_3+R_4}V_2
\]

Thus,

\[
V_- = \frac{R_4}{R_3+R_4}V_2
\]

Apply KCL at the inverting node:

\[
\frac{V_1 - V_-}{R_1} = \frac{V_- - V_o}{R_2}
\]

Solve for \(V_o\):

\[
V_o = \left(1+\frac{R_2}{R_1}\right)V_- - \frac{R_2}{R_1}V_1
\]

Substitute \(V_-\):

\[
V_o =
\left(1+\frac{R_2}{R_1}\right)
\frac{R_4}{R_3+R_4}V_2
-
\frac{R_2}{R_1}V_1
\]

With matched ratios,

\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}=k
\]

we get

\[
\frac{R_4}{R_3+R_4}=\frac{k}{1+k}
\]

hence

\[
V_o = (1+k)\frac{k}{1+k}V_2-kV_1
\]

so the input-output relation is

\[
\boxed{V_o = k(V_2 - V_1)}
\]

where

\[
k=\frac{R_2}{R_1}=\frac{R_4}{R_3}.
\]

Special case: if all resistor pairs are equal (\(R_1=R_3,\; R_2=R_4\)) and \(R_2=R_1\), then \(k=1\) and

\[
\boxed{V_o = V_2 - V_1}.
\]
