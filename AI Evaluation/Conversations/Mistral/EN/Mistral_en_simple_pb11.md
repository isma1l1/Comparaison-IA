## Utilisateur
We are studying a classic differential integrator circuit in which the two resistors have the same value R and the two capacitors have the same value C. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA
To determine the output voltage \( V_s \) as a function of the input voltages \( V_1 \) and \( V_2 \) in a **classic differential integrator circuit** with two resistors \( R \) and two capacitors \( C \), we need to analyze the circuit step-by-step.

---
## **Circuit Description**
A classic differential integrator circuit typically consists of:
- Two input voltages: \( V_1 \) and \( V_2 \).
- Two resistors \( R \) (one for each input).
- Two capacitors \( C \) (one for each input).
- An operational amplifier (op-amp) in an integrator configuration.

The circuit is designed to **integrate the difference** between the two input voltages \( V_1 \) and \( V_2 \).

---
## **Assumptions**
1. The op-amp is **ideal** (infinite input impedance, zero output impedance, and infinite gain).
2. The circuit is in the [[important]**linear region**[\important]] of operation (no saturation).
3. The capacitors are initially **uncharged** (initial voltage across capacitors is zero).

---
## **Analysis**

### **Step 1: Apply[[important] Kirchhoff's Current Law[\important]] (KCL) at the Inverting Terminal**
The inverting terminal of the op-amp is a **virtual ground** (voltage = 0 V). The currents through the resistors and capacitors are:

- Current through \( R \) connected to \( V_1 \):
  \[
  I_1 = \frac{V_1 - 0}{R} = \frac{V_1}{R}
  \]

- Current through \( R \) connected to \( V_2 \):
  \[
  I_2 = \frac{V_2 - 0}{R} = \frac{V_2}{R}
  \]

- Current through the capacitor \( C \) connected to \( V_1 \):
  \[
  I_{C1} = C \frac{d(V_1 - 0)}{dt} = C \frac{dV_1}{dt}
  \]

- Current through the capacitor \( C \) connected to \( V_2 \):
  \[
  I_{C2} = C \frac{d(V_2 - 0)}{dt} = C \frac{dV_2}{dt}
  \]

However, in a **differential integrator**, the capacitors are typically connected in the feedback loop, not directly to the inputs. Let's correct the analysis for a **standard differential integrator configuration**:

---
### **Step 2: Correct Circuit Configuration**
A **differential integrator** is usually implemented as follows:
- \( V_1 \) is applied to the **non-inverting terminal** through a resistor \( R \).
- \( V_2 \) is applied to the **inverting terminal** through a resistor \( R \).
- A capacitor \( C \) is connected in the **feedback loop** (from output to inverting terminal).
- Another capacitor \( C \) is connected from the **non-inverting terminal to ground**.

But a more common configuration is:
- Both \( V_1 \) and \( V_2 \) are applied to the **inverting terminal** through resistors \( R \).
- A capacitor \( C \) is connected in the **feedback loop** (from output to inverting terminal).
- The non-inverting terminal is **grounded**.

In this case, the output voltage \( V_s \) is the **integral of the difference** between \( V_1 \) and \( V_2 \).

---
### **Step 3: Apply KCL at the Inverting Terminal**
The inverting terminal is a **virtual ground**, so the sum of currents entering it is zero:

\[
I_{R1} + I_{R2} + I_C = 0
\]

Where:
- \( I_{R1} = \frac{V_1 - 0}{R} = \frac{V_1}{R} \)
- \( I_{R2} = \frac{V_2 - 0}{R} = \frac{V_2}{R} \)
- \( I_C = C \frac{d(0 - V_s)}{dt} = -C \frac{dV_s}{dt} \)

Substituting:

\[
\frac{V_1}{R} + \frac{V_2}{R} - C \frac{dV_s}{dt} = 0
\]

\[
\frac{V_1 + V_2}{R} = C \frac{dV_s}{dt}
\]

\[
\frac{dV_s}{dt} = \frac{V_1 + V_2}{RC}
\]

But this is **not a differential integrator**. For a **differential integrator**, the inputs are applied **differentially**, meaning:

- \( V_1 \) is applied to the **non-inverting terminal** through \( R \).
- \( V_2 \) is applied to the **inverting terminal** through \( R \).
- A capacitor \( C \) is in the **feedback loop** (from output to inverting terminal).
- Another capacitor \( C \) is connected from the **non-inverting terminal to ground**.

In this case, the output voltage \( V_s \) is:

\[
V_s = -\frac{1}{RC} \int (V_2 - V_1) \, dt + V_s(0)
\]

Where \( V_s(0) \) is the initial voltage across the capacitor.

---
### **Step 4: Final Expression for \( V_s \)**
Assuming the capacitors are initially **uncharged** (\( V_s(0) = 0 \)):

\[
[[important]V_s = -\frac{1}{RC} \int (V_2 - V_1) \, dt[\important]] 
\]

This means the output voltage \( V_s \) is the **negative integral of the difference** between \( V_2 \) and \( V_1 \), scaled by \( \frac{1}{RC} \).

---
## **Summary**
The output voltage \( V_s \) of a **differential integrator circuit** with two resistors \( R \) and two capacitors \( C \) is:

\[
\boxed{V_s = -\frac{1}{RC} \int (V_2 - V_1) \, dt}
\]

This circuit **integrates the difference** between the two input voltages \( V_1 \) and \( V_2 \). The negative sign indicates that the output is **inverted** relative to the input difference.

---
Would you like to explore a specific example or clarify any part of the derivation?
