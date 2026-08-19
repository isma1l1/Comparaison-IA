## Utilisateur

Answer questions A.1.1, A.1.2, and A.1.3 shown in these images, explaining your reasoning in detail.

*(image of an electronics exam sheet about a Wheatstone bridge measuring water level in a tank using a potentiometer and resistive divider, including questions A.1.1, A.1.2, and A.1.3)*

## IA

For the Wheatstone bridge in Figure 2, the source (V_1) is applied between the top and bottom rails.
(V_2) is the voltage difference between the midpoint of the left divider ((R_2,R_1)) and the midpoint of the right divider ((R_3,R_4)).

---

# A.1.1 — Expression of (V_2)

Each side of the bridge is a voltage divider.

### Left branch

The midpoint voltage on the left side is:

[
V_L = V_1 \frac{R_1}{R_1+R_2}
]

because (R_1) is connected to the lower rail.

### Right branch

Similarly, the midpoint voltage on the right side is:

[
V_R = V_1 \frac{R_4}{R_3+R_4}
]

### Output voltage

From the diagram, (V_2) is the voltage from the right midpoint toward the left midpoint:

[
V_2 = V_L - V_R
]

Therefore,

[
\boxed{
V_2
===

V_1\left(
\frac{R_1}{R_1+R_2}
-------------------

\frac{R_4}{R_3+R_4}
\right)
}
]

---

# A.1.2 — Relation between (V_2) and (x)

We are given:

[
R_1 = kR,
\qquad
R_2 = (1-k)R,
\qquad
k=\frac{x}{h}
]

Since

[
R_1+R_2 = kR+(1-k)R = R
]

we get

[
\frac{R_1}{R_1+R_2}
===================

# \frac{kR}{R}

k
]

Thus:

[
V_2
===

V_1\left(
k-\frac{R_4}{R_3+R_4}
\right)
]

and since (k=x/h),

[
\boxed{
V_2
===

V_1\left(
\frac{x}{h}
-----------

\frac{R_4}{R_3+R_4}
\right)
}
]

This is the required relation between (V_2) and the water level (x).

---

# A.1.3 — Condition for (V_2=0) at half-full tank

We want:

[
V_2=0
\quad \text{when} \quad x=\frac{h}{2}
]

Using the previous result:

[
0
=

V_1\left(
\frac{1}{2}
-----------

\frac{R_4}{R_3+R_4}
\right)
]

Since (V_1\neq 0),

[
\frac{R_4}{R_3+R_4}=\frac12
]

Multiply both sides:

[
2R_4 = R_3+R_4
]

Hence

[
\boxed{R_3 = R_4}
]

---

## Minimum value of (V_2)

Minimum occurs for empty tank:

[
x=0
]

thus

[
V_{2,\min}
==========

V_1\left(
0-\frac12
\right)
]

So:

[
\boxed{
V_{2,\min}=-\frac{V_1}{2}
}
]

---

## Maximum value of (V_2)

Maximum occurs for full tank:

[
x=h
]

thus

[
V_{2,\max}
==========

V_1\left(
1-\frac12
\right)
]

Therefore:

[
\boxed{
V_{2,\max}=+\frac{V_1}{2}
}
]

---

# Final Answers

## A.1.1

[
\boxed{
V_2
===

V_1\left(
\frac{R_1}{R_1+R_2}
-------------------

\frac{R_4}{R_3+R_4}
\right)
}
]

## A.1.2

[
\boxed{
V_2
===

V_1\left(
\frac{x}{h}
-----------

\frac{R_4}{R_3+R_4}
\right)
}
]

## A.1.3

Condition:

[
\boxed{R_3=R_4}
]

Minimum:

[
\boxed{
V_{2,\min}=-\frac{V_1}{2}
}
]

Maximum:

[
\boxed{
V_{2,\max}=+\frac{V_1}{2}
}
]
