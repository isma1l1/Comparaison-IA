## Utilisateur

Here is an analog electronics circuit.
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.
*(image of an analog circuit with two operational amplifiers, a capacitor labeled C0, and resistors split into αR and (1−α)R)*

## IA

What you have there is a classic **active capacitance multiplier / simulated capacitor** built with two ideal linear amplifiers (op-amps), a split resistor (R = \alpha R + (1-\alpha)R), and a physical capacitor (C_0).

### Key idea

Because both amplifiers operate in linear mode:

* Their inputs are at (virtually) the same voltage.
* They act to **force specific node voltages**, effectively scaling the voltage seen across (C_0).

This creates a situation where the current drawn at the input behaves like that of a much larger capacitor.

---

### Result: Equivalent capacitance

The circuit is equivalent to a single capacitor (C) seen at the input, with:

[
C = \frac{C_0}{\alpha(1 - \alpha)}
]

---

### Why this happens (intuition)

* The resistor divider defines a fraction (\alpha) and (1-\alpha).
* The op-amps buffer and enforce these ratios without loading.
* As a result, the voltage across (C_0) is only a **fraction** of the input voltage.
* Since capacitor current is (i = C_0 \frac{dv}{dt}), reducing the voltage swing across (C_0) makes the input current *look like* it's charging a larger capacitor.

So the circuit **multiplies the effective capacitance** by:

[
\frac{1}{\alpha(1-\alpha)}
]

---

### Purpose of the circuit

This is used as a:

#### 👉 **Capacitance multiplier / active capacitor**

**Why useful:**

* Real large capacitors are bulky, expensive, and non-ideal.
* This circuit allows you to **simulate a very large capacitance** using:

  * a small physical capacitor (C_0)
  * resistors
  * op-amps

**Typical applications:**

* Active filters (especially low-frequency)
* Integrators
* Analog signal processing
* Power supply smoothing (in some designs)

---

### Insight

The maximum multiplication occurs near:
[
\alpha = 0.5 \Rightarrow C = \frac{C_0}{0.25} = 4C_0
]

But if (\alpha) is very small or very close to 1, the denominator shrinks and the equivalent capacitance becomes **very large**—at the cost of sensitivity and practical limitations (noise, op-amp bandwidth, stability).

---

If you want, I can walk through the nodal analysis step-by-step to show exactly how the formula comes out.
