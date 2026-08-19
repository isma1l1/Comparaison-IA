## Utilisateur

Here is an analog electronics circuit.
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.
*(image of an analog electronics circuit diagram featuring two operational amplifiers, a capacitor labeled C0, and resistors labeled alpha R and (1-alpha)R)*

---

## IA

Based on the circuit diagram provided, we can determine the equivalent capacitance by analyzing the relationship between the input voltage $u$ and the input current $i$.

### Circuit Analysis

1.  **Operational Amplifier ①:**
    This op-amp is configured as a **voltage follower** (buffer). Since it operates in linear mode, the voltage at the inverting input follows the non-inverting input. Thus, the output voltage of Op-amp ① is:
    $$V_{out1} = u$$

2.  **Operational Amplifier ②:**
    This op-amp is in an **inverting amplifier** configuration. The non-inverting input is grounded ($0\text{V}$), so the inverting input is a virtual ground ($V_- \approx 0\text{V}$). 
    The current flowing through the resistor $\alpha R$ comes from the output of Op-amp ①. This current is:
    $$i_R = \frac{V_{out1} - 0}{\alpha R} = \frac{u}{\alpha R}$$
    This same current must flow through the feedback resistor $(1-\alpha)R$ to the output of Op-amp ②. Therefore, the output voltage $V_{out2}$ is:
    $$V_{out2} = 0 - i_R \cdot (1-\alpha)R = -\frac{u}{\alpha R} \cdot (1-\alpha)R = -u \frac{1-\alpha}{\alpha}$$

3.  **The Input Current $i$:**
    The input current $i$ flows entirely through the capacitor $C_0$ because the input impedance of Op-amp ① is ideally infinite. The voltage across $C_0$ is the difference between $u$ and $V_{out2}$:
    $$v_{C_0} = u - V_{out2} = u - \left( -u \frac{1-\alpha}{\alpha} \right) = u \left( 1 + \frac{1-\alpha}{\alpha} \right) = u \left( \frac{\alpha + 1 - \alpha}{\alpha} \right) = \frac{u}{\alpha}$$

4.  **Equivalent Capacitance:**
    Using the complex impedance of a capacitor ($I = C \cdot \frac{dv}{dt}$ or $I = j\omega C U$), the current $i$ is:
    $$i = C_0 \frac{d}{dt}(v_{C_0}) = C_0 \frac{d}{dt}\left(\frac{u}{\alpha}\right) = \frac{C_0}{\alpha} \frac{du}{dt}$$
    By definition, the equivalent capacitance $C$ is defined by $i = C \frac{du}{dt}$. Comparing the terms, we get:
    $$C = \frac{C_0}{\alpha}$$

---

### Purpose of the Circuit

This circuit is a **Capacitance Multiplier** (specifically, a Miller-effect based synthetic capacitor). 

* **Capacitance Scaling:** By varying the parameter $\alpha$ (which is typically controlled by a potentiometer or a voltage divider where $0 < \alpha \leq 1$), you can make the circuit behave like a much larger capacitor than $C_0$. For example, if $\alpha = 0.01$, the equivalent capacitance is $100 \times C_0$.
* **Space Efficiency:** Large physical capacitors (like large electrolytics) are bulky and often have poor tolerances. This circuit allows an engineer to use a small, high-quality ceramic or film capacitor to simulate a very large capacitance.
* **Tunability:** It allows for a **variable capacitor** that can be adjusted electronically or via a simple knob, which is much easier than finding a variable capacitor with a high Farad rating.
