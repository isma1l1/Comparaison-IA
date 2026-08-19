## Utilisateur

Here is an analog electronics circuit.
The two resistors R and the two capacitors C are identical. Express the relationship between the output voltage and the two input voltages of the circuit in the frequency domain and then in the time domain. Explain your reasoning.

*(image of an op-amp circuit with two identical resistors and two identical capacitors: one RC network feeding the non-inverting input from input e2, another resistor from input e1 to the inverting input, and a capacitor providing feedback from the output to the inverting input)*

---

## IA

This is a nice symmetric op-amp network—once you notice that the non-inverting side is just an RC low-pass, everything falls into place.

---

## 1) Key observations

* The op-amp is ideal ⇒
  [
  [[important]v_- = v_+ = v[\important]]
  ]

* **Bottom branch (non-inverting input):**
  A simple RC low-pass from (e_2) to ground:

  * resistor (R) from (e_2) to node (v)
  * capacitor (C) from (v) to ground

* **Top branch (inverting input):**

  * resistor (R) from (e_1) to node (v)
  * capacitor (C) from output (s) back to node (v)

---

## 2) Frequency-domain analysis

### (a) Voltage at the non-inverting input

This is a standard RC low-pass:

[
[[important]V = \frac{E_2}{1 + j\omega RC}[\important]]
]

---

### (b) KCL at the inverting node

At node (v):

* Current through input resistor:
  [
  \frac{E_1 - V}{R}
  ]

* Current through feedback capacitor:
  [
  j\omega C (V - S)
  ]

KCL:
[
\frac{E_1 - V}{R} + j\omega C (V - S) = 0
]

Solve for (S):

[
j\omega C (V - S) = -\frac{E_1 - V}{R}
]

[
S = V + \frac{E_1 - V}{j\omega RC}
]

---

### (c) Substitute (V)

[
V = \frac{E_2}{1 + j\omega RC}
]

So:

[
S = \frac{E_2}{1 + j\omega RC}

* \frac{E_1 - \frac{E_2}{1 + j\omega RC}}{j\omega RC}
  ]

---

### Final frequency-domain relation:

[
\boxed{
S(\omega)
=========

\frac{E_2}{1 + j\omega RC}
+
\frac{E_1}{j\omega RC}
----------------------

\frac{E_2}{(1 + j\omega RC)(j\omega RC)}
}
]

---

## 3) Time-domain equation

Start from the KCL form:

[
\frac{e_1(t) - v(t)}{R} + C \frac{d}{dt}(v(t) - s(t)) = 0
]

Rewriting:

[
C\left(\frac{dv}{dt} - \frac{ds}{dt}\right) = -\frac{e_1 - v}{R}
]

[
\frac{ds}{dt}
=============

\frac{dv}{dt}
+
\frac{1}{RC}(e_1 - v)
]

---

### Also from the RC low-pass:

[
RC \frac{dv}{dt} + v = e_2
]

---

### Final time-domain system:

[
\boxed{
\begin{aligned}
RC \frac{dv}{dt} + v &= e_2 \
\frac{ds}{dt} &= \frac{dv}{dt} + \frac{1}{RC}(e_1 - v)
\end{aligned}
}
]

---

## 4) Interpretation

* (e_2) is **low-pass filtered**
* (e_1) is **integrated (via (1/j\omega))**
* The output combines:

  * a filtered version of (e_2)
  * an integrated difference between (e_1) and that filtered signal

So this circuit behaves like a **mixed integrator + low-pass differential processor**.

---

If you want, I can simplify the final expression into a single transfer function (S/E_1) and (S/E_2) or sketch the Bode behavior.
