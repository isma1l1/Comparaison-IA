## Utilisateur
Respond in a concise manner by deleting any unnecessary remarks. Determine the output voltage v(t) for a sinusoidal input e(t) = E0sin(wt) in a Graetz Bridge setup. Explain your reasoning.

## IA
### Graetz Bridge (Full-Wave Rectifier) Output Voltage

**Input:**
\( e(t) = E_0 \sin(\omega t) \)

**Output Voltage \( v(t) \):**
For a Graetz Bridge (full-wave rectifier with 4 diodes), the output voltage is the absolute value of the input voltage:

\[
[important]v(t) =  E_0 \sin(\omega t)|[/important]
\]

---

#### **Reasoning:**
1. **Diode Behavior:**
   - The Graetz Bridge uses 4 diodes arranged so that both halves of the input sinusoid are rectified.
   - During the [important]positive half-cycle[/important] of \( e(t) \), two diodes conduct, and [important]the output follows \( e(t)[/important] \).
   - During the negative half-cycle, the other two diodes conduct, [important]inverting the negative half-cycle[/important] to positive.

2. **Result:**
   - The output \( v(t) \) is always non-negative, mirroring the absolute value of the input sinusoid.
   - The [important]frequency of \( v(t) \) is twice that of \( e(t) \)[/important]due to full-wave rectification.