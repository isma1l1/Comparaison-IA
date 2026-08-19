## Utilisateur
Give me the formula for the gain of an inverter setup based on the values of resistances R1 and R2. Explain your reasoning.

## IA
The gain $ A $ of a **non-inverting operational amplifier (op-amp) inverter** (also called a **voltage inverter**) is determined by the feedback network formed by resistors $ R_1 $ and $ R_2 $. The standard configuration for an inverter uses an op-amp with $ R_1 $ connected to the input and $ R_2 $ as the feedback resistor.

---

### **Inverter Gain Formula**
For an **inverting op-amp configuration**, the gain $ A $ is given by:

$$
[important]A = -\frac{R_2}{R_1}[/important]
$$

---

### **Reasoning**
1. **Inverting Configuration**:
   - The input signal is applied to the **inverting terminal** of the op-amp.
   - The non-inverting terminal is grounded.
   - The feedback resistor $ R_2 $ connects the output to the inverting terminal.

2. **Virtual Ground Principle**:
   - The op-amp forces the inverting terminal to the same potential as the non-inverting terminal (which is grounded).
   - This means the [important]voltage at the inverting terminal is **0V** (virtual ground)[/important].

3. **Current Flow**:
   - The current through $ R_1 $ is $ [important]I_{in} = \frac{V_{in}}{R_1[/important]} $.
   - The same current flows through $ R_2 $ (since no current enters the op-amp input).
   - The voltage drop across $ R_2 $ is $ [important]V_{out} = -I_{in} \cdot R_2[/important] $.

4. **Gain Calculation**:
   - Substituting $ I_{in} $:
     $$
     [important]V_{out} = -\left(\frac{V_{in}}{R_1}\right) \cdot R_2
     [/important]$$
   - The gain $ A $ is the ratio of $ V_{out} $ to $ V_{in} $:
     $$
     [important]A = \frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}[/important]
     $$

---
### **Key Takeaways**
- The **negative sign** indicates that the output is **180° out of phase** with the input (inversion).
- The gain magnitude is purely determined by the ratio $ \frac{R_2}{R_1} $.
- If $ R_1 = R_2 $, the gain is **-1** (unity inversion).

Would you like a practical example or clarification on any part?
