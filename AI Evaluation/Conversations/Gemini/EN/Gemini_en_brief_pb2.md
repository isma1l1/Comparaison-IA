## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. Give me the formula for the gain of a non-inverter setup based on the values of the resistances R1 and R2. Explain your reasoning.

---

## IA
The gain of a non-inverting operational amplifier circuit is defined by the following formula:

$$[important]A_v = 1 + \frac{R_2}{R_1}[/important]$$

---

### Reasoning

To derive this, we apply two fundamental "ideal op-amp" assumptions:
1.  **Infinite Input Impedance:** No current flows into the op-amp input terminals.
2.  **Virtual Short:** The op-amp drives its output to make the voltage at the inverting input ($V_-$) equal to the voltage at the non-inverting input ($V_{in}$).

**Step-by-Step Derivation:**

* **Voltage at the nodes:** Since $[important]V_- = V_+[/important]$, we know $V_- = V_{in}$.
* **Voltage Divider:** The resistors $R_1$ and $R_2$ form a [important]voltage divider[/important] from the output ($V_{out}$) to ground. The voltage at the inverting terminal is:
    $$V_- = V_{out} \left( \frac{R_1}{R_1 + R_2} \right)$$
* **Substitution:** Replace $V_-$ with $V_{in}$:
    $$[important]V_{in} = V_{out} \left( \frac{R_1}{R_1 + R_2} \right)[/important]$$
* **Solve for Gain ($V_{out} / V_{in}$):** $$[important]\frac{V_{out}}{V_{in}} = \frac{R_1 + R_2}{R_1}[/important] = \frac{R_1}{R_1} + \frac{R_2}{R_1} = [important]1 + \frac{R_2}{R_1}[/important]$$

---

## Utilisateur
Convertis toute la conversation précédente en un texte markdown que je peux copier coller. 
Garde tous les détails, ne résume rien.
Les changements d'interlocuteur (et seulement eux) seront indiqués par ##, suivi du nom (Utilisateur ou IA) de la personne qui parle.