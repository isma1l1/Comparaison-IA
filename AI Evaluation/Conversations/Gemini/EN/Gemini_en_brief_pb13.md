## Utilisateur
Respond concisely, omitting any unnecessary information. 
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.
*(image of an electronic circuit diagram featuring two operational amplifiers, resistors labeled alpha R and (1-alpha)R, and a capacitor C0)*

## IA
To determine the equivalent capacitance $C = \frac{i}{s u}$, we analyze the circuit assuming ideal operational amplifiers (ALIs) in linear mode ($V_+ = V_-$).

### 1. Analysis of the Circuit
* **ALI 1:** This is a voltage follower. Its output voltage is equal to the input voltage: $V_{out1} = u$.
* **ALI 2:** The non-inverting terminal is grounded ($0\text{V}$), so the inverting terminal is also at $0\text{V}$ (virtual ground).
* **Resistor Network:** A current flows from the output of ALI 1 through the resistors. Since the inverting input of ALI 2 is at $0\text{V}$, the current through $\alpha R$ is:
$$i_R = \frac{u - 0}{\alpha R} = \frac{u}{\alpha R}$$
* **ALI 2 Output:** This current $i_R$ must flow through $(1-\alpha)R$ because no current enters the ALI inverting input. The output voltage of ALI 2 ($V_{out2}$) is:
$$V_{out2} = 0 - i_R \cdot (1-\alpha)R = -\frac{u}{\alpha R} \cdot (1-\alpha)R = -u \frac{1-\alpha}{\alpha}$$
* **Capacitor Current:** The current $i$ entering the circuit flows through $C_0$. The voltage across $C_0$ is $V_{C0} = u - V_{out2}$.
$$i = C_0 \frac{d(u - V_{out2})}{dt} \implies I(s) = C_0 s (U(s) - V_{out2}(s))$$

### 2. Equivalent Capacitance
Substitute $V_{out2}$ into the current equation:
$$I = C_0 s \left( u - \left( -u \frac{1-\alpha}{\alpha} \right) \right) = C_0 s u \left( 1 + \frac{1-\alpha}{\alpha} \right)$$
$$I = C_0 s u \left( \frac{\alpha + 1 - \alpha}{\alpha} \right) = \frac{C_0}{\alpha} s u$$
The equivalent admittance is $Y = \frac{I}{u} = s \frac{C_0}{\alpha}$. Comparing this to $Y = sC$:
**$$C = \frac{C_0}{\alpha}$$**

---

### 3. Purpose of the Circuit
This is a **capacitance multiplier** (specifically a Miller effect emulator).
* **Function:** It allows for a very large equivalent capacitance using a physically small, high-quality capacitor ($C_0$).
* **Adjustment:** By varying $\alpha$ (e.g., using a potentiometer), the capacitance can be tuned electronically without changing physical components.
