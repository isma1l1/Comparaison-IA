## Utilisateur
We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA
### Input-Output Relationship of a Differentiator Amplifier

**Result:**
The output voltage is the **negative derivative of the input voltage**, scaled by the time constant *RC*:

> **Vₒᵤₜ(t) = −R·C · (dVᵢₙ/dt)**

---

---

### 🔍 **Reasoning (Step-by-Step Derivation)**

#### 1. **Circuit Configuration**
The classic **op-amp differentiator** uses:
- An **ideal operational amplifier** (infinite input impedance, zero output impedance, infinite gain).
- A **capacitor C** in series with the input signal (connected to the inverting terminal).
- A **resistor R** in the feedback loop (from output to inverting terminal).
- The **non-inverting terminal is grounded**.

```
       Vᵢₙ ────┬───────
                C
                │
                ▼
   ┌───────────┴───────────┐
   │                       │
  ┌┴┐                     ┌┴┐
  │ │  Ideal Op-Amp       │ │
  │ └───────────┬─────────┘ │
  └─────────────┤           └───────────► Vₒᵤₜ
                R
                │
               GND
```

---

#### 2. **Ideal Op-Amp Properties**
- **Virtual short:** The voltage at the inverting terminal (*V⁻*) equals the non-inverting terminal (*V⁺*), which is **grounded (0V)**.
  → **V⁻ = 0V** (Virtual ground).

- **No input current:** The current into the op-amp’s input terminals is **zero** (infinite input impedance).
  → All current through *C* must flow through *R*.

---

#### 3. **Current Through the Capacitor**
The current through the capacitor is given by:
> **I_C = C · (d/dt)(Vᵢₙ − V⁻) = C · (dVᵢₙ/dt)**
*(since V⁻ = 0V)*

---

#### 4. **Current Through the Feedback Resistor**
The same current *I_C* flows through the feedback resistor *R* (from *V⁻* to *Vₒᵤₜ*):
> **I_R = (V⁻ − Vₒᵤₜ) / R = −Vₒᵤₜ / R**
*(since V⁻ = 0V)*

---
---
#### 5. **Equating Currents (KCL at V⁻)**
Since *I_C = I_R* (no current enters the op-amp):
> **C · (dVᵢₙ/dt) = −Vₒᵤₜ / R**

---
#### 6. **Solving for Vₒᵤₜ**
Rearranging:
> **Vₒᵤₜ(t) = −R·C · (dVᵢₙ/dt)**

---
---
### ✅ **Key Observations**
1. **Differentiation:** The output is proportional to the **time derivative** of the input.
2. **Inversion:** The negative sign indicates a **180° phase shift**.
3. **Scaling Factor:** The **time constant τ = R·C** determines the gain.
4. **Frequency Domain:** The transfer function is **H(jω) = −jωRC**, confirming differentiation (multiplication by *jω* in the frequency domain).

---
### ⚠️ **Limitations (Non-Ideal Behavior)**
- **High-frequency noise amplification:** Differentiators amplify high-frequency noise (since gain ∝ ω).
- **Saturation:** For sudden input changes (e.g., step inputs), the output can saturate due to finite op-amp slew rate.
- **Stability:** Often requires a **small feedback capacitor** in parallel with *R* to limit high-frequency gain.

---
### 📌 **Summary**
For an **ideal op-amp differentiator** with **one resistor (R)** and **one capacitor (C)**:
> **Vₒᵤₜ(t) = −RC · (dVᵢₙ/dt)**
