## Utilisateur

We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA

Consider the classic op-amp **difference amplifier** (also called a subtractor) with:

- \(R_1\) from \(V_1\) to the inverting input
- \(R_2\) feedback from output to the inverting input
- \(R_3\) from \(V_2\) to the non-inverting input
- \(R_4\) from the non-inverting input to ground

and the resistor ratios are matched:

\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}
\]

A common special case is:

\[
R_1 = R_3,\qquad R_2 = R_4
\]

---

# Step 1: Voltage at the non-inverting input

Because the op-amp input current is ideally zero, the \(+\) input sees a simple voltage divider:

\[
V_+ = \frac{R_4}{R_3+R_4}V_2
\]

With negative feedback and an ideal op-amp,

\[
V_- = V_+
\]

---

# Step 2: Apply KCL at the inverting node

At the inverting input:

\[
\frac{V_1 - V_-}{R_1}
=
\frac{V_- - V_o}{R_2}
\]

Substitute \(V_- = V_+\):

\[
\frac{V_1 - V_+}{R_1}
=
\frac{V_+ - V_o}{R_2}
\]

Solve for \(V_o\):

\[
R_2(V_1 - V_+) = R_1(V_+ - V_o)
\]

\[
R_2V_1 - R_2V_+
=
R_1V_+ - R_1V_o
\]

\[
R_1V_o
=
(R_1+R_2)V_+ - R_2V_1
\]

\[
V_o
=
\left(1+\frac{R_2}{R_1}\right)V_+
-\frac{R_2}{R_1}V_1
\]

Now substitute

\[
V_+ = \frac{R_4}{R_3+R_4}V_2
\]

giving

\[
V_o
=
\left(1+\frac{R_2}{R_1}\right)
\frac{R_4}{R_3+R_4}V_2
-\frac{R_2}{R_1}V_1
\]

---

# Step 3: Use the matched-ratio condition

If

\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}=k
\]

then

\[
\frac{R_4}{R_3+R_4}
=
\frac{k}{1+k}
\]

Therefore,

\[
\left(1+k\right)\frac{k}{1+k}=k
\]

and the expression simplifies to

\[
V_o = kV_2 - kV_1
\]

so the input-output relationship is

\[
\boxed{V_o = \frac{R_2}{R_1}(V_2 - V_1)}
\]

---

# Interpretation

The circuit amplifies the **difference** between the two inputs while rejecting any common signal present on both inputs.

- Differential gain:

\[
A_d = \frac{R_2}{R_1}
\]

- Ideal common-mode gain:

\[
A_{cm}=0
\]

For the unity-gain case \(R_1=R_2=R_3=R_4\),

\[
\boxed{V_o = V_2 - V_1}
\]

which is the standard subtractor behavior.

## Utilisateur

Convertis toute la conversation précédente en un texte markdown que je peux copier coller. Garde tous les détails, ne résume rien. Les changements d'interlocuteur (et seulement eux) seront indiqués par ##, suivi du nom ("Utilisateur" ou "IA") de la personne qui parle. reste en anglais
