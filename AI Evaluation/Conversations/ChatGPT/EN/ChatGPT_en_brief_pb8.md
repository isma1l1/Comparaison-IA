## Utilisateur

Respond in a concise manner by deleting any unnecessary remarks.
We are studying an inverting hysteresis comparator circuit in which the resistance between ground and the non-inverting input is denoted R1 and the resistance between the non-inverting input and the ALI output is denoted R2. Identify the operating regime of the ALI, express the potential v+ as a function of s, deduce the switching voltages, represent the hysteresis cycle of the circuit in the case where R2 = 2·R1, and represent the output signal for a sinusoidal input with an amplitude of 10V. Explain your reasoning.

---

## IA

ALI operates in [important]open-loop saturated regime[/important] (comparator mode): output is driven to +V_sat or −V_sat depending on the sign of v− − v+.

Non-inverting node is a [important]divider[/important] between output and ground, so:
[important]v+ = (R1 / (R1 + R2)) · v_out.[/important]

With two stable output states:
if v_out = +V_sat ⇒ v+ = (R1/(R1+R2)) V_sat
if v_out = −V_sat ⇒ v+ = −(R1/(R1+R2)) V_sat

Switching occurs when v− = v+ (inverting input equals reference), hence switching thresholds are:
[important]V_T+ = (R1/(R1+R2)) V_sat[/important] (for rising input)
[important]V_T− = −(R1/(R1+R2)) V_sat[/important] (for falling input)

For [important]R2 = 2R1[/important]:
v+ = v_out / 3
thus:
[important]V_T+ = +V_sat/3, V_T− = −V_sat/3[/important]

Hysteresis cycle:
[important]the input must exceed +V_sat/3 to force output to −V_sat (since inverting configuration), and drop below −V_sat/3 to switch back to +V_sat[/important]. This produces a [important]rectangular loop[/important] with symmetric thresholds ±V_sat/3.

For a sinusoidal input v_in(t) = 10 sin(ωt):

* when v_in > +V_sat/3 → output switches to −V_sat
* when v_in < −V_sat/3 → output switches to +V_sat
* between thresholds, output state is retained

Thus the output is a [important]saturated square wave[/important] at the same frequency as the sine but with duty cycle determined by how long 10 sin(ωt) stays above +V_sat/3 and below −V_sat/3. Since 10 ≫ V_sat typically, [important]switching occurs near the sine’s crossings of ±V_sat/3[/important], yielding a nearly 50% duty cycle square wave if V_sat ≪ 10 V.
