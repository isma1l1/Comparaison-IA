## Utilisateur
We are studying an inverting hysteresis comparator circuit in which the resistance between ground and the non-inverting input is denoted R1 and the resistance between the non-inverting input and the ALI output is denoted R2. Identify the operating regime of the ALI, express the potential v+ as a function of s, deduce the switching voltages, represent the hysteresis cycle of the circuit in the case where R2 = 2*R1, and represent the output signal for a sinusoidal input with an amplitude of 10V. Explain your reasoning.

## IA
We are dealing with an inverting comparator with positive feedback, i.e. a Schmitt trigger. The “ALI” (ideal operational amplifier) does not operate in its linear regime here but in [important]saturation[/important], because there is no negative feedback enforcing \(v_+ \approx v_-\). The slightest difference between the inputs drives the output to one of its saturation levels. So the operating regime is: saturated, with \(s = \pm V_{sat}\).

Let the output be \(s\), and denote the non-inverting input voltage by \(v_+\). The node \(v_+\) is connected to ground through \(R_1\) and to the output through \(R_2\). Since the op-amp input current is zero, we apply a simple [important]voltage divider[/important] between 0 and \(s\):

\[
[important]v_+ = \frac{R_1}{R_1 + R_2} \, s[/important]
\]

The inverting input receives the input signal \(v_e\). The switching occurs when \(v_- = v_+\), i.e.:

\[
[important]v_e = v_+[/important]
\]

Thus the switching thresholds are:

\[
[important]V_{th} = \pm \frac{R_1}{R_1 + R_2} \, V_{sat}[/important]
\]

More precisely:
- when the output is at \(+V_{sat}\), the threshold is \(+ \frac{R_1}{R_1+R_2} V_{sat}\),
- when the output is at \(-V_{sat}\), the threshold is \(- \frac{R_1}{R_1+R_2} V_{sat}\).

Now take the case \([important]R_2 = 2R_1[/important]\). Then:

\[
\frac{R_1}{R_1 + R_2} = \frac{R_1}{3R_1} = \frac{1}{3}
\]

So the thresholds are:

\[
[important]V_{th} = \pm \frac{V_{sat}}{3}[/important]
\]

The hysteresis cycle is therefore a [important]rectangular loop[/important]:
- [important]if the input \(v_e\) increases, the output switches from \(+V_{sat}\) to \(-V_{sat}\) when \(v_e = +V_{sat}/3\),[/important]
- [important]if the input decreases, the output switches from \(-V_{sat}\) to \(+V_{sat}\) when \(v_e = -V_{sat}/3\).[/important]

This produces a hysteresis loop centered at 0, with width \(2V_{sat}/3\).

For a sinusoidal input of amplitude 10 V:
\[
v_e(t) = 10 \sin(\omega t)
\]

As long as the amplitude exceeds the thresholds (which is the case if \(10 > V_{sat}/3\), typically true), the output will switch at each crossing of the thresholds:
- when the sine rises and crosses \(+V_{sat}/3\), the output flips to \(-V_{sat}\),
- when it falls and crosses \(-V_{sat}/3\), the output flips to \(+V_{sat}\).

Thus the output is a [important]square wave alternating between \(\pm V_{sat}\), with transitions occurring at the instants where the sine reaches the thresholds[/important]. The waveform is not exactly symmetric in phase with the input zero crossings, but [important]shifted according to the threshold values[/important].

Graphically:
- input: sinusoid of amplitude 10 V,
- output: rectangular signal at \(\pm V_{sat}\),
- switching points located at the intersections of the sinusoid with \(\pm V_{sat}/3\).

This is the characteristic behavior of an inverting Schmitt trigger: noise immunity and clean switching due to hysteresis.
