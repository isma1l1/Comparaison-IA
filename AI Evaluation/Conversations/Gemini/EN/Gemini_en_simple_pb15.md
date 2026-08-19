## Utilisateur
We are studying a classic active filter amplifier circuit (the + terminal of the ALI is connected to ground, and the - terminal is connected to the ALI output via a resistor R' and to the input via a capacitor C and a resistor R).
Identify the type of this filter without calculation, express its transfer function in canonical form, and determine the values of R' and C for R = 1 kΩ, if a cutoff frequency of ω₀ = 10⁴ rad/s and a gain of 20 dB at high frequencies are desired.

---

## IA
Based on your description, the circuit features a capacitor $C$ in series with a resistor $R$ at the input, and a feedback resistor $R'$ connecting the output to the inverting input. With the non-inverting terminal grounded, this is an **inverting active high-pass filter**.

---

### 1. Filter Identification (No Calculation)
In this configuration:
* **At low frequencies (DC):** The capacitor $C$ acts as an open circuit ($Z_C \to \infty$). No current flows from the source to the inverting terminal, resulting in zero output.
* **At high frequencies:** The capacitor $C$ acts as a short circuit ($Z_C \to 0$). The circuit behaves like a standard inverting amplifier with a gain determined by $-R'/R$.

Since it blocks low frequencies and passes high frequencies, it is a **1st-order High-Pass Filter**.

---

### 2. Canonical Transfer Function
The transfer function $H(j\omega)$ for a first-order active high-pass filter is expressed as:

$$H(j\omega) = \frac{A_v \cdot j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$$

Where:
* **$A_v$** is the passband gain (at high frequencies).
* **$\omega_0$** is the cutoff angular frequency.

For this specific circuit:
* $A_v = -\frac{R'}{R}$
* $\omega_0 = \frac{1}{RC}$

---

### 3. Determining Component Values
Given the requirements:
* $R = 1 \text{ k}\Omega$
* $\omega_0 = 10^4 \text{ rad/s}$
* High-frequency gain = $20 \text{ dB}$

#### Step A: Calculate $R'$
The gain in decibels is defined as $20 \log_{10}(|A_v|)$. 
$$20 \text{ dB} \implies |A_v| = 10^1 = 10$$
Since $|A_v| = \frac{R'}{R}$:
$$R' = |A_v| \cdot R = 10 \cdot 1000 \Omega = \mathbf{10 \text{ k}\Omega}$$

#### Step B: Calculate $C$
Using the cutoff frequency formula $\omega_0 = \frac{1}{RC}$:
$$C = \frac{1}{R \cdot \omega_0}$$
$$C = \frac{1}{1000 \cdot 10^4} = 10^{-7} \text{ F}$$
**$C = 100 \text{ nF}$**

---

### Summary Table
| Parameter | Value |
| :--- | :--- |
| **Filter Type** | Inverting High-Pass (1st Order) |
| **Feedback Resistor ($R'$)** | $10 \text{ k}\Omega$ |
| **Capacitor ($C$)** | $100 \text{ nF}$ |
| **Passband Gain ($A_v$)** | $-10$ (or $20 \text{ dB}$) |
