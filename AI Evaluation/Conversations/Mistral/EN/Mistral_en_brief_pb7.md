## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA
The input-output relationship is:

**Vₒᵤₜ = (R₂/R₁)(V₁ − V₂)**

### Reasoning:
1. **Op-amp rules**: V₊ = V₋ and no input current.
2. **KCL at V₊**: V₊ = V₁·R₂/(R₁ + R₂).
3. **KCL at V₋**: V₋ = (V₂/R₁ + Vₒᵤₜ/R₂)·R₁R₂/(R₁ + R₂).
4. **Equate V₊ and V₋**, solve for Vₒᵤₜ. Matched resistors cancel common-mode signals, yielding the difference scaled by R₂/R₁.
