## Utilisateur
Answer questions A.1.1, A.1.2, and A.1.3 shown in these images, explaining your reasoning in detail.
*(Image from Exercise A1 – Exercise A.1 with a diagram of the Wheatstone bridge and related questions)*

---
## IA
Let's tackle each part of **Exercise A1** step by step, using the Wheatstone bridge circuit and the given relationships.

---
---
## **A.1.1: Literal Expression of \( V_2 \) as a Function of \( V_1, R_1, R_2, R_3, R_4 \)**

### **Circuit Analysis**
The Wheatstone bridge circuit (Figure 2) consists of:
- A DC voltage source \( V_1 \).
- Four resistors: \( R_1, R_2, R_3, R_4 \).
- The output voltage \( V_2 \) is measured between the midpoints of the two voltage dividers formed by \( (R_1, R_2) \) and \( (R_3, R_4) \).

### **Voltage Divider Rule**
The voltage at the midpoint of a voltage divider with resistors \( R_a \) and \( R_b \) and input voltage \( V_{in} \) is:
\[
V_{mid} = V_{in} \cdot \frac{R_b}{R_a + R_b}
\]

### **Applying to the Wheatstone Bridge**
- The voltage at the midpoint of \( (R_1, R_2) \):
  \[
  V_{mid1} = V_1 \cdot \frac{R_2}{R_1 + R_2}
  \]
- The voltage at the midpoint of \( (R_3, R_4) \):
  \[
  V_{mid2} = V_1 \cdot \frac{R_4}{R_3 + R_4}
  \]
- The output voltage \( V_2 \) is the difference between \( V_{mid1} \) and \( V_{mid2} \):
  \[
  V_2 = V_{mid1} - V_{mid2} = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
  \]

### **Final Expression for \( V_2 \)**
\[
\boxed{V_2 = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)}
\]

---
---
## **A.1.2: Relation Between \( V_2 \) and \( x \) Given \( R_1 = kR \) and \( R_2 = (1-k)R \)**

### **Substitute \( R_1 \) and \( R_2 \)**
From the problem, \( k = \frac{x}{h} \), so:
\[
R_1 = kR = \frac{x}{h} R, \quad R_2 = (1-k)R = \left(1 - \frac{x}{h}\right) R
\]

### **Assume \( R_3 = R_4 = R \)**
The problem does not specify \( R_3 \) and \( R_4 \), but for a balanced Wheatstone bridge (as implied by the context), we can assume \( R_3 = R_4 = R \). This is a common setup for such problems.

### **Substitute into \( V_2 \) Expression**
\[
V_2 = V_1 \left( \frac{(1-k)R}{kR + (1-k)R} - \frac{R}{R + R} \right)
\]
Simplify the denominators:
\[
kR + (1-k)R = R, \quad R + R = 2R
\]
So:
\[
V_2 = V_1 \left( \frac{(1-k)R}{R} - \frac{R}{2R} \right) = V_1 \left( (1-k) - \frac{1}{2} \right)
\]
\[
V_2 = V_1 \left( \frac{1}{2} - k \right)
\]

### **Substitute \( k = \frac{x}{h} \)**
\[
V_2 = V_1 \left( \frac{1}{2} - \frac{x}{h} \right)
\]

### **Final Relation Between \( V_2 \) and \( x \)**
\[
\boxed{V_2 = V_1 \left( \frac{1}{2} - \frac{x}{h} \right)}
\]

---
---
## **A.1.3: Relation Between \( R_1 \) and \( R_4 \) for \( V_2 = 0 \) at Half-Full Tank (\( x = \frac{h}{2} \))**

### **Condition for \( V_2 = 0 \)**
From the expression for \( V_2 \):
\[
V_2 = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right) = 0
\]
This implies:
\[
\frac{R_2}{R_1 + R_2} = \frac{R_4}{R_3 + R_4}
\]

### **Substitute \( R_1 = kR \) and \( R_2 = (1-k)R \)**
\[
\frac{(1-k)R}{kR + (1-k)R} = \frac{R_4}{R_3 + R_4}
\]
Simplify the left side:
\[
\frac{1-k}{1} = \frac{R_4}{R_3 + R_4}
\]

### **Assume \( R_3 = R \)**
For simplicity, let \( R_3 = R \). Then:
\[
1 - k = \frac{R_4}{R + R_4}
\]
Solve for \( R_4 \):
\[
(1 - k)(R + R_4) = R_4
\]
\[
(1 - k)R + (1 - k)R_4 = R_4
\]
\[
(1 - k)R = R_4 - (1 - k)R_4
\]
\[
(1 - k)R = R_4 (1 - (1 - k)) = R_4 k
\]
\[
R_4 = \frac{(1 - k)R}{k}
\]

### **At Half-Full Tank (\( x = \frac{h}{2} \))**
\[
k = \frac{x}{h} = \frac{1}{2}
\]
So:
\[
R_4 = \frac{(1 - \frac{1}{2})R}{\frac{1}{2}} = \frac{\frac{1}{2}R}{\frac{1}{2}} = R
\]

### **Minimum and Maximum \( V_2 \)**
- **When \( x = 0 \) (empty tank, \( k = 0 \)):**
  \[
  V_2 = V_1 \left( \frac{1}{2} - 0 \right) = \frac{V_1}{2}
  \]
  So, \( V_{2min} = \frac{V_1}{2} \).

- **When \( x = h \) (full tank, \( k = 1 \)):**
  \[
  V_2 = V_1 \left( \frac{1}{2} - 1 \right) = -\frac{V_1}{2}
  \]
  So, \( V_{2max} = -\frac{V_1}{2} \).

### **Final Answer for A.1.3**
- **Relation between \( R_1 \) and \( R_4 \):**
  \[
  \boxed{R_4 = \frac{(1 - k)R}{k}}
  \]
  At \( x = \frac{h}{2} \), \( R_4 = R \).

- **Minimum and Maximum \( V_2 \):**
  \[
  \boxed{V_{2min} = \frac{V_1}{2}, \quad V_{2max} = -\frac{V_1}{2}}
  \]
