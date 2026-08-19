## Utilisateur
Respond in a concise manner by suppressing any unnecessary remarks. Give me the expression of the intensity in the resistance R in a Zener diode setup. Explain your reasoning.

## IA
In a standard Zener diode regulator (series resistor \(R\), Zener in parallel with the load), when the Zener is in breakdown, it clamps the voltage across itself to \(V_Z\).

The voltage across the resistor is therefore:
\[
V_R = V_{\text{in}} - V_Z
\]

Using Ohm’s law, the current through the resistor is:
\[
I_R = \frac{V_{in} - V_Z}{R}
\]

**Reasoning:**  
- The Zener fixes the output node at \(V_Z\) (in regulation).  
- The resistor drops the remaining voltage from the supply.  
- Current through \(R\) depends only on that voltage drop and \(R\).  
- This current then splits between the Zener and the load:
  \[
  I_R = I_Z + I_L
  \]

This expression holds as long as the Zener diode remains in its breakdown (regulation) region.