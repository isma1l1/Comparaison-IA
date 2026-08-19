## Utilisateur

Here is an assembly of analog electronics.
Establish the expression of Vout according to the input tensions. Explain your reasoning.
*(image of an operational amplifier circuit with two inputs Vin1 and Vin2, resistors R1, R2, Rf, and Rg forming a feedback and voltage divider network)*

## IA

Treat the op-amp as [important]ideal[/important] (very high gain, no input current), so:

* The inputs satisfy **virtual short**: ([important]V_- = V_+[/important])
* No current enters the op-amp inputs

---

### 1) Voltage at the non-inverting input (V_+)

The lower network is just a voltage divider from (V_{in2}) through (R_2) and (R_g) to ground:

[
[important]V_+ = \frac{R_g}{R_2 + R_g} , V_{in2}[/important]
]

---

### 2) Apply [important]KCL[/important] at the inverting node (V_-)

At node (V_-), currents through (R_1) and (R_f) sum to zero:

[
[important]\frac{V_{in1} - V_-}{R_1} + \frac{V_{out} - V_-}{R_f} = 0[/important]
]

Since (V_- = V_+), substitute:

[
\frac{V_{in1} - V_+}{R_1} + \frac{V_{out} - V_+}{R_f} = 0
]

Solve for (V_{out}):

[
[important]V_{out} = V_+ \left(1 + \frac{R_f}{R_1}\right) - \frac{R_f}{R_1} V_{in1}[/important]
]

---

### 3) Substitute (V_+)

[
[important]V_{out} = \left(1 + \frac{R_f}{R_1}\right)\frac{R_g}{R_2 + R_g} , V_{in2}
;-; \frac{R_f}{R_1} V_{in1}[/important]
]

---

### Final Expression

[
\boxed{
[important]V_{out} =
\left(1 + \frac{R_f}{R_1}\right)\frac{R_g}{R_2 + R_g} , V_{in2}

* \frac{R_f}{R_1} V_{in1}[/important]
  }
  ]

---

### Interpretation

* The circuit is a **weighted differential amplifier**
* (V_{in1}) contributes through an **inverting gain** (-R_f/R_1)
* (V_{in2}) is first attenuated by the divider, then amplified by a **non-inverting gain** (1 + R_f/R_1)

If you want, I can show how to choose resistors so it behaves like a pure difference amplifier (e.g., (V_{out} \propto V_{in2} - V_{in1})).
