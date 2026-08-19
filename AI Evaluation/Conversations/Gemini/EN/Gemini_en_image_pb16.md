## Utilisateur

Answer questions A.1.1, A.1.2, and A.1.3 shown in these images, explaining your reasoning in detail.
*(image of a linear potentiometer water tank system and a Wheatstone bridge circuit diagram with related physics problems)*

---

## IA

This exercise focuses on a **Wheatstone Bridge** circuit used to measure the water level in a tank. The level $x$ is converted into a resistance value via a linear potentiometer.

### A.1.1) Literal expression of $V_2$ as a function of $V_1, R_1...R_4$

To find $V_2$, we look at the potential difference between the two branches of the bridge. Assuming the voltmeter measuring $V_2$ has infinite impedance (standard for ideal analysis), we can treat each side as a **voltage divider**.

1.  **Potential at the left node ($V_L$):**
    Using the voltage divider formula across $R_1$ and $R_2$:
    $$V_L = V_1 \cdot \frac{R_1}{R_1 + R_2}$$

2.  **Potential at the right node ($V_R$):**
    Using the voltage divider formula across $R_3$ and $R_4$:
    $$V_R = V_1 \cdot \frac{R_4}{R_3 + R_4}$$

3.  **Expression for $V_2$:**
    The voltage $V_2$ is the difference between these two potentials:
    $$V_2 = V_L - V_R$$
    $$V_2 = V_1 \left( \frac{R_1}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)$$

---

### A.1.2) Relation between $V_2$ and $x$

We are given that $R_1 = kR$ and $R_2 = (1-k)R$, where $k = \frac{x}{h}$.

1.  **Simplify the left branch ratio:**
    $$\frac{R_1}{R_1 + R_2} = \frac{kR}{kR + (1-k)R} = \frac{kR}{R} = k$$
    Substituting $k = \frac{x}{h}$, the ratio is simply $\frac{x}{h}$.

2.  **Substitute into the $V_2$ equation:**
    $$V_2 = V_1 \left( \frac{x}{h} - \frac{R_4}{R_3 + R_4} \right)$$

This shows that $V_2$ is a **linear function** of the water level $x$.

---

### A.1.3) Condition for half-full tank and boundary values

**1. Relation between $R_3$ and $R_4$ for $V_2 = 0$ at $x = h/2$:**
If the tank is half full, then $x = h/2$, which means $k = 0.5$.
For $V_2$ to be zero, the two branches of the bridge must be balanced:
$$\frac{x}{h} = \frac{R_4}{R_3 + R_4} \implies 0.5 = \frac{R_4}{R_3 + R_4}$$
This implies that **$R_3 = R_4$**.

**2. Minimum value $V_{2min}$ (when $x = 0$):**
Using $R_3 = R_4$, the right-hand term $\frac{R_4}{R_3+R_4}$ becomes $0.5$.
At $x = 0$:
$$V_{2min} = V_1 (0 - 0.5) = - \frac{V_1}{2}$$

**3. Maximum value $V_{2max}$ (when $x = h$):**
At $x = h$, the ratio $\frac{x}{h} = 1$:
$$V_{2max} = V_1 (1 - 0.5) = + \frac{V_1}{2}$$

---
**Summary Table**

| Parameter | Value/Condition |
| :--- | :--- |
| **Balance Condition ($x=h/2$)** | $R_3 = R_4$ |
| **Minimum Voltage ($x=0$)** | $-V_1/2$ |
| **Maximum Voltage ($x=h$)** | $+V_1/2$ |
