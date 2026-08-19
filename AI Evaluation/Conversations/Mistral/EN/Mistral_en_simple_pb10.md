## Utilisateur
We are studying a classic non-inverting summing circuit in which the four resistors have the same value R. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA
To determine the output voltage \( V_s \) of a **non-inverting summing circuit** with four resistors of equal value \( R \), let's analyze the circuit step-by-step.

---
## **Circuit Description**
A classic non-inverting summing circuit typically uses an operational amplifier (op-amp) with resistors connected to the non-inverting terminal. For this problem, we assume:
- Two input voltages: \( V_1 \) and \( V_2 \).
- Four resistors, all with resistance \( R \).
- The op-amp is ideal (infinite input impedance, zero output impedance, and virtual short at the input terminals).

---
## **Assumptions**
1. The op-amp is in **non-inverting configuration**.
2. The four resistors are arranged such that:
   - Two resistors are connected to \( V_1 \) and \( V_2 \) respectively, and their other ends are tied together and connected to the non-inverting terminal of the op-amp.
   - The other two resistors are part of the feedback network (one from the non-inverting terminal to ground, and one from the non-inverting terminal to the output \( V_s \)).

   This forms a **voltage divider** at the non-inverting terminal.

---
## **Analysis**

### Step 1: Voltage at the Non-Inverting Terminal
The non-inverting terminal sees a voltage \( V_+ \) that is the average of \( V_1 \) and \( V_2 \), because the two input resistors (each \( R \)) form a voltage divider:
[[important]
\[
V_+ = \frac{V_1 + V_2}{2}
\][\important]]

This is because the two resistors are equal, so the voltage at the junction is the average of \( V_1 \) and \( V_2 \).

---
### Step 2: Feedback Network
The feedback network consists of two resistors (each \( R \)):
- One resistor connects \( V_+ \) to ground.
- The other connects \( V_+ \) to \( V_s \).

The op-amp ensures that[[important] \( V_+ = V_- \)[\important]], but since the inverting terminal is grounded (or connected to a reference), we have:

\[
V_- = 0 \quad \text{(virtual ground)}
\]

However, in a **non-inverting summing configuration**, the feedback network does not invert the signal. Instead, the output voltage \( V_s \) is directly proportional to \( V_+ \).

---
### Step 3: Gain of the Non-Inverting Amplifier
The gain \( A \) of a non-inverting amplifier with feedback resistors \( R_f \) and \( R_g \) is:

\[
A = 1 + \frac{R_f}{R_g}
\]

In this case, since both feedback resistors are \( R \):
[[important]
\[
A = 1 + \frac{R}{R} = 2
\][\important]]

Thus, the output voltage \( V_s \) is:
[[important]
\[
V_s = A \cdot V_+ = 2 \cdot \frac{V_1 + V_2}{2} = V_1 + V_2
\][\important]]

---
## **Final Result**
The output voltage \( V_s \) is simply the **sum of the input voltages**:

\[
\boxed{V_s = V_1 + V_2}
\]

---
## **Explanation Summary**
- The non-inverting terminal voltage \( V_+ \) is the average of \( V_1 \) and \( V_2 \).
- The non-inverting amplifier configuration with equal feedback resistors (\( R \)) gives a gain of 2.
- Multiplying \( V_+ \) by the gain yields \( V_s = V_1 + V_2 \).
