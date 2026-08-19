## Utilisateur
We are studying a classic active filter amplifier circuit (the + terminal of the ALI is connected to ground, and the - terminal is connected to the ALI output via a resistor R' and to the input via a capacitor C and a resistor R).
Identify the type of this filter without calculation, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, if a cutoff frequency of ω₀ = 10⁴ rad/s and a gain of 20 dB at high frequencies are desired.

## IA
### **1. Identifying the Filter Type**
The described circuit is a **non-inverting active filter** with the following configuration:
- The **+ terminal** of the operational amplifier (ALI) is **grounded**.
- The **- terminal** is connected to:
  - The **output** via a resistor **R'**.
  - The **input** via a **capacitor C** and a **resistor R** in series.

This configuration is characteristic of a **Sallen-Key topology**, but since the **+ terminal** is grounded, it is actually a **single-pole active low-pass filter** (also known as a **first-order active low-pass filter**).

**Conclusion:** This is a **first-order active low-pass filter**.

---

---
### **2. Transfer Function in Canonical Form**
For a first-order active low-pass filter, the transfer function \( H(s) \) in the Laplace domain is:

\[
H(s) = \frac{H_0 \cdot \omega_0}{s + \omega_0}
\]

Where:
- \( H_0 \) is the **DC gain** (gain at low frequencies).
- \( \omega_0 \) is the **cutoff frequency** (in rad/s).

However, for an **inverting configuration** (which this is, since the input is applied to the **- terminal**), the transfer function is:

\[
H(s) = -\frac{R'}{R} \cdot \frac{1}{1 + s R' C}
\]

But since the **+ terminal** is grounded, this is a **non-inverting configuration** with feedback. The correct transfer function for this **first-order low-pass filter** is:

\[
H(s) = \frac{R'}{R} \cdot \frac{1}{1 + s R' C}
\]

To express it in **canonical form**, we rewrite it as:

\[
H(s) = \frac{H_0}{1 + s / \omega_0}
\]

Where:
- \( H_0 = \frac{R'}{R} \) (gain at low frequencies).
- \( \omega_0 = \frac{1}{R' C} \) (cutoff frequency).

---
---
### **3. Determining R' and C**
Given:
- \( R = 1 \, \text{k}\Omega = 1000 \, \Omega \)
- \( \omega_0 = 10^4 \, \text{rad/s} \)
- **Gain at high frequencies = 20 dB**

#### **Step 1: Convert Gain from dB to Linear Scale**
The gain in dB is given by:
\[
20 \, \text{dB} = 20 \log_{10} ( H_0|)
\]
\[
 |H_0| = 10^{20/20} = 10
\]

So, the **low-frequency gain** \( H_0 = 10 \).

#### **Step 2: Relate \( H_0 \) to \( R' \) and \( R \)**
From the transfer function:
\[
H_0 = \frac{R'}{R}
\]
\[
10 = \frac{R'}{1000}
\]
\[
R' = 10 \times 1000 = 10 \, \text{k}\Omega
\]

#### **Step 3: Solve for C**
From the cutoff frequency:
\[
\omega_0 = \frac{1}{R' C}
\]
\[
10^4 = \frac{1}{10,000 \times C}
\]
\[
C = \frac{1}{10^4 \times 10,000} = \frac{1}{10^8} = 10 \, \text{nF}
\]

---
---
### **Final Answer**
- **Filter Type:** First-order active low-pass filter.
- **Transfer Function (Canonical Form):**
  \[
  H(s) = \frac{10}{1 + s / 10^4}
  \]
- **Component Values:**
  - \( R' = 10 \, \text{k}\Omega \)
  - \( C = 10 \, \text{nF} \)
