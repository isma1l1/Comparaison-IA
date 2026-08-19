## Utilisateur
Here is an analog electronics circuit.  
Determine the input-output relationship of the filter shown (the four resistors have the same value). Explain your reasoning.

*(image of an op-amp circuit with two input voltages v1 and v2 feeding the non-inverting input through equal resistors, and a feedback network with two equal resistors forming a non-inverting amplifier, output labeled vs)*

## IA
This is a nice example of how an op-amp can combine signals.

### Step 1: Look at the non-inverting (+) input
The + input is fed by **two resistors (equal value)** coming from \(v_1\) and \(v_2\).

Since the op-amp input draws ~0 current, that node is just a simple resistive averaging node. With equal resistors:
[[important]
\[
v_+ = \frac{v_1 + v_2}{2}
\][\important]]

---

### Step 2: Look at the inverting (–) input
The − input is connected to a standard **feedback divider**:
- One resistor from output \(v_s\) to the − input
- One resistor from − input to ground  
- Both resistors have the same value

This is a classic **non-inverting amplifier** configuration with gain:
[[important]
\[
A_v = 1 + \frac{R_f}{R_g} = 1 + \frac{R}{R} = 2
\][\important]]

---

### Step 3: Apply op-amp rule
For an ideal op-amp with negative feedback:
[[important]
\[
v_- = v_+
\][\important]]

So the output is:
[[important]
\[
v_s = 2 \cdot v_+
\][\important]]

---

### Step 4: Substitute \(v_+\)

\[
v_s = 2 \cdot \frac{v_1 + v_2}{2}
\]
[[important]
\[
v_s = v_1 + v_2
\][\important]]

---

### Final Answer
\[
\boxed{v_s = v_1 + v_2}
\]

---

### Interpretation
This circuit acts as a **summing amplifier**:
- It **adds the two input signals**
- No scaling (unity gain for each input)
- Uses a non-inverting topology with passive averaging + gain

---

If you want, I can also show how this changes if the resistor values are different (you get weighted sums).
```
