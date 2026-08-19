## Utilisateur
Here is an analog electronics circuit. 
Determine the input-output relationship of the filter shown. Explain your reasoning.

*(image of an analog circuit with an operational amplifier: the non-inverting input is grounded, the input signal passes through a capacitor into the inverting input, and a resistor provides feedback from the output to the inverting input)*

## IA
This is a classic **op-amp differentiator** configuration (an inverting high-pass filter). Let’s walk through it carefully.

---

### 1. Identify the structure
- The **non-inverting (+) input** is grounded → this is an **inverting configuration**.
- The input signal \( e(t) \) goes through a **capacitor \(C\)** into the inverting input.
- A **resistor \(R\)** provides feedback from output \( s(t) \) to the inverting input.

Because of the op-amp’s high gain and negative feedback:
- The inverting input is at **virtual ground** (≈ 0 V).
- No current enters the op-amp input → currents flow through \(C\) and \(R\).

---

### 2. Current through the capacitor
The input current is determined by the capacitor:

\[
i_C = C \frac{d}{dt} e(t)
\]

(since the inverting node is at ~0 V)

---

### 3. Current through the feedback resistor
That same current must flow through the resistor:

\[
i_R = \frac{0 - s(t)}{R} = -\frac{s(t)}{R}
\]

---

### 4. Equate currents
\[
C \frac{d e(t)}{dt} = -\frac{s(t)}{R}
\]

---

### 5. Solve for output
\[
s(t) = -RC \frac{d e(t)}{dt}
\]

---

### 6. Frequency-domain (transfer function)

\[
H(s)=\frac{S(s)}{E(s)}=-RC\,s
\]

---

### 7. Interpretation
- The circuit **differentiates the input signal**.
- It behaves as a **high-pass filter**:
  - Low frequencies → output ≈ 0  
  - High frequencies → amplified (proportional to frequency)

---

### Final Answer
\[
\boxed{s(t) = -RC \frac{d e(t)}{dt}}
\]

This is an **inverting differentiator**.
```
