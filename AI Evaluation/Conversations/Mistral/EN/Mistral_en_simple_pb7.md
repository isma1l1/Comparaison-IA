## Utilisateur
We study a standard difference amplifier with matched resistor pairs. Determine the input-output relationship of this system. Explain your reasoning.

## IA
### **Input-Output Relationship of a Standard Difference Amplifier**

For a **difference amplifier with matched resistor pairs** (R₁ and R₂), the output voltage is:

**\[
V_{\text{out}} = \frac{R_2}{R_1} (V_1 - V_2)
\]**

---

---

### **🔍 Derivation & Reasoning**

#### **1. Circuit Configuration**
A standard difference amplifier uses an ideal op-amp with:
- **Non-inverting input (+):** Connected to \( V_1 \) via \( R_1 \), and to ground via \( R_2 \).
- **Inverting input (−):** Connected to \( V_2 \) via \( R_1 \), and to \( V_{\text{out}} \) via \( R_2 \) (feedback).

#### **2. Ideal Op-Amp Constraints**
- **Virtual short:** \( V_+ = V_- \)
- **No input current:** \( I_+ = I_- = 0 \)

#### **3. Voltage at Non-Inverting Input (\( V_+ \))**
Using the voltage divider rule:
\[
V_+ = V_1 \cdot \frac{R_2}{R_1 + R_2}
\]

#### **4. Voltage at Inverting Input (\( V_- \))**
Using superposition (since \( I_- = 0 \)):
\[
V_- = V_2 \cdot \frac{R_2}{R_1 + R_2} + V_{\text{out}} \cdot \frac{R_1}{R_1 + R_2}
\]

#### **5. Equate \( V_+ \) and \( V_- \)**
\[
V_1 \cdot \frac{R_2}{R_1 + R_2} = V_2 \cdot \frac{R_2}{R_1 + R_2} + V_{\text{out}} \cdot \frac{R_1}{R_1 + R_2}
\]

#### **6. Solve for \( V_{\text{out}} \)**
Multiply both sides by \( (R_1 + R_2) \):
\[
V_1 R_2 = V_2 R_2 + V_{\text{out}} R_1
\]
\[
V_{\text{out}} R_1 = R_2 (V_1 - V_2)
\]
\[
V_{\text{out}} = \frac{R_2}{R_1} (V_1 - V_2)
\]

---
---
### **📌 Key Observations**
- **Differential gain:** The output is proportional to the **difference** between \( V_1 \) and \( V_2 \).
- **Matched resistors:** Ensures **common-mode rejection** (suppresses signals common to both inputs).
- **Special case:** If \( R_1 = R_2 \), then \( V_{\text{out}} = V_1 - V_2 \) (unity gain difference amplifier).
