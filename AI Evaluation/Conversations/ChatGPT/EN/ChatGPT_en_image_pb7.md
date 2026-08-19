## Utilisateur

Here is an assembly of analog electronics.
Determine the input-output relationship of the presented filter. Explain your reasoning.

*(image of a circuit diagram showing an op-amp with four resistors arranged as a differential amplifier, with inputs labeled e1 and e2, resistors R and R', and output labeled s)*

## IA

This isn’t actually a frequency-selective filter (no capacitors/inductors), it’s a **differential (subtractor) amplifier** built with an [important]ideal[/important] op-amp and matched resistor pairs.

### Step 1: Identify the structure

* The **top branch** (with (e_1)) goes into the **inverting input** through (R), with feedback (R') from output.
* The **bottom branch** (with (e_2)) feeds the **non-inverting input** through (R), with a divider (R') to ground.

This is the classic 4-resistor difference amplifier configuration.

---

### Step 2: Voltage at the non-inverting input

The non-inverting input sees a voltage divider:

[
[important]V_+ = e_2 \cdot \frac{R'}{R + R'}[/important]
]

---

### Step 3: Use ideal op-amp property

For an ideal op-amp with [important]negative feedback[/important]:

[
[important]V_- = V_+[/important]
]

Let (V = V_+ = V_-).

---

### Step 4: Apply KCL at the inverting node

[
\frac{e_1 - V}{R} + \frac{s - V}{R'} = 0
]

Solve for (s):

[
\frac{s - V}{R'} = -\frac{e_1 - V}{R}
]

[
s = V - \frac{R'}{R}(e_1 - V)
]

[
[important]s = V\left(1 + \frac{R'}{R}\right) - \frac{R'}{R} e_1[/important]
]

---

### Step 5: Substitute (V)

[
[important]V\left(1 + \frac{R'}{R}\right)
= e_2 \cdot \frac{R'}{R + R'} \cdot \frac{R + R'}{R}
= \frac{R'}{R} e_2[/important]
]

---

### Final result

[
\boxed{
[important]s = \frac{R'}{R},(e_2 - e_1)[/important]
}
]

---

### Interpretation

* The circuit outputs a **scaled difference** between the two inputs.
* Gain = ( \frac{R'}{R} )
* It rejects common-mode signals (if resistors are well matched).

So despite being labeled a “filter,” it’s actually a **linear differential amplifier (subtractor)**.
