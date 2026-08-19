## Utilisateur
Answer concisely, omitting any unnecessary information. We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA
The input-output relationship for a **classic op-amp differentiator** (with one resistor \( R \) in feedback and one capacitor \( C \) at the input) is:

\[
V_{\text{out}} = -R C \frac{dV_{\text{in}}}{dt}
\]

**Reasoning:**
1. The capacitor current is \( I = C \frac{dV_{\text{in}}}{dt} \).
2. In an ideal op-amp (inverting configuration), this current flows through the feedback resistor \( R \), producing \( V_{\text{out}} = -I R \).
3. Substituting \( I \) gives \( V_{\text{out}} = -R C \frac{dV_{\text{in}}}{dt} \).
