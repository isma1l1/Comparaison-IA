## Utilisateur
Here is an analog electronics circuit.
Determine the input-output relationship of the filter shown (the four resistors have the same value). Explain your reasoning.

*(image of an analog electronics circuit with an operational amplifier, four resistors, and two capacitors)*

---
## IA
This circuit is a **Sallen-Key active filter**, specifically a **second-order low-pass filter** (since the output is taken from the op-amp, and the configuration suggests a low-pass response). The four resistors are equal in value, which simplifies the analysis.

---
### **Step 1: Identify the Circuit Topology**
- The circuit consists of:
  - Two resistors in series at the input (\(v_1\)).
  - Two resistors forming a feedback network around the op-amp.
  - Two capacitors: one in the feedback loop and one in the input path.
- The op-amp is in a non-inverting configuration.

---
### **Step 2: Assign Component Values**
Let the four resistors have the same value: \( R \).
Let the two capacitors have the same value: \( C \).

---
### **Step 3: Derive the Transfer Function**
For a Sallen-Key low-pass filter, the transfer function is:

\[
\frac{V_s}{V_1} = \frac{A}{1 + sRC(3 - A) + (sRC)^2}
\]

where:
- \( A = 1 + \frac{R_2}{R_1} \) is the gain of the non-inverting amplifier.
- Here, \( R_1 = R \) and \( R_2 = R \), so [[important]\( A = 2 \)[\important]].

Substituting \( A = 2 \):

\[
\frac{V_s}{V_1} = \frac{2}{1 + sRC(3 - 2) + (sRC)^2} = \frac{2}{1 + sRC + (sRC)^2}
\]

---
### **Step 4: Simplify the Transfer Function**
The transfer function can be rewritten as:

\[
\frac{V_s}{V_1} = \frac{2}{1 + sRC + s^2R^2C^2}
\]

This is a **second-order low-pass filter** with:
- **DC gain**: 2 (since at \( s = 0 \), \( \frac{V_s}{V_1} = 2 \)).
- **Cutoff frequency**: \( \omega_0 = \frac{1}{RC} \).
- **Damping ratio**: \( \zeta = \frac{1}{2} \) (critically damped).

---
### **Step 5: Final Input-Output Relationship**
The input-output relationship is:

\[
\boxed{
\frac{V_s}{V_1} = \frac{2}{1 + sRC + s^2R^2C^2}
}
\]

This is a **second-order Butterworth low-pass filter** with a gain of 2 and a cutoff frequency at \( \omega_0 = \frac{1}{RC} \).

---
### **Key Observations**
- The filter attenuates high-frequency signals.
- The gain at DC (0 Hz) is 2.
- The cutoff frequency is determined by \( R \) and \( C \).
