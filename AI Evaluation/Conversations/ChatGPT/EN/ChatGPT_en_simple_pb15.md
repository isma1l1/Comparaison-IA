## Utilisateur

We are studying a classic active filter amplifier circuit (the + terminal of the ALI is connected to ground, and the - terminal is connected to the ALI output via a resistor R' and to the input via a capacitor C and a resistor R).
Identify the type of this filter without calculation, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, if a cutoff frequency of ω₀ = 10⁴ rad/s and a gain of 20 dB at high frequencies are desired.

## IA

The topology is an inverting first-order active filter in which the input network is a series \(RC\) feeding the inverting node and the feedback is purely resistive. This is the standard configuration of a first-order active high-pass filter.

At low frequency, the capacitor behaves as an open circuit, so the output tends to zero. At high frequency, the capacitor behaves as a short circuit, leaving a simple inverting amplifier with gain \(-R'/R\). The circuit is therefore a high-pass filter.

The transfer function is obtained using the impedance of the input branch \(Z_{in} = R + \frac{1}{sC}\) and the feedback resistor \(R'\):
\[
H(s) = -\frac{R'}{R + \frac{1}{sC}} = -\frac{R'sC}{1 + sRC}
\]

In canonical first-order high-pass form:
\[
H(s) = K \frac{s/\omega_0}{1 + s/\omega_0}
\]

with:
\[
\omega_0 = \frac{1}{RC}, \quad K = -\frac{R'}{R}
\]

Now apply the design conditions.

Cutoff pulsation:
\[
\omega_0 = 10^4 \ \text{rad/s} = \frac{1}{RC}
\Rightarrow C = \frac{1}{R\omega_0}
\]

With \(R = 1\,\text{k}\Omega = 10^3\,\Omega\):
\[
C = \frac{1}{10^3 \cdot 10^4} = 10^{-7}\,\text{F} = 100\,\text{nF}
\]

High-frequency gain requirement: \(20\,\text{dB}\)

\[
20 \log_{10}|K| = 20 \Rightarrow |K| = 10
\]

Since \(K = -R'/R\):
\[
\frac{R'}{R} = 10 \Rightarrow R' = 10\,R = 10\,\text{k}\Omega
\]

Final results:

Type: first-order inverting active high-pass filter  
Transfer function:
\[
H(s) = -10 \frac{s/10^4}{1 + s/10^4}
\]

Component values:
\[
R' = 10\,\text{k}\Omega, \quad C = 100\,\text{nF}
\]
