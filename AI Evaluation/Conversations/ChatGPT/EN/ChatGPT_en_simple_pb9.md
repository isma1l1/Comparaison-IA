## Utilisateur

We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA

A classic RC differentiator amplifier is usually built with:

- a **capacitor \(C\)** in series with the input,
- a **resistor \(R\)** to ground,
- and the output taken across the resistor.

It behaves approximately like a differentiator because the output voltage is proportional to the **time derivative** of the input voltage.

## Circuit reasoning

Let:

- \(v_{in}(t)\) = input voltage
- \(v_{out}(t)\) = output voltage across the resistor

Since the capacitor and resistor are in series, the same current \(i(t)\) flows through both components.

### Step 1: Current through the capacitor

For a capacitor:

\[
i(t)=C\frac{d}{dt}\big(v_C(t)\big)
\]

In the differentiator configuration, when the time constant is small enough, the voltage across the capacitor is approximately the input voltage:

\[
v_C(t)\approx v_{in}(t)
\]

So:

\[
i(t)\approx C\frac{dv_{in}(t)}{dt}
\]

### Step 2: Output voltage across the resistor

Using Ohm’s law:

\[
v_{out}(t)=Ri(t)
\]

Substitute the capacitor current:

\[
v_{out}(t)=RC\frac{dv_{in}(t)}{dt}
\]

# Input-output relationship

Therefore, the differentiator relationship is:

\[
\boxed{v_{out}(t)=RC\frac{dv_{in}(t)}{dt}}
\]

This shows that:

- the output is proportional to the **rate of change** of the input,
- rapid changes in the input produce larger outputs,
- constant inputs produce zero output.

## Frequency-domain form

Using Laplace transforms:

\[
H(s)=\frac{V_{out}(s)}{V_{in}(s)}
\]

For the RC differentiator:

\[
\boxed{H(s)=sRC}
\]

which is the transfer function of an ideal differentiator (within the frequency range where the approximation is valid).
