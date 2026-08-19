## Utilisateur

Answer concisely, omitting any unnecessary information.  We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA

In an ideal differentiator amplifier, the input-output relationship is given by the following equation:

$$[important]v_{out}(t) = -RC \frac{dv_{in}(t)}{dt}[/important]$$

---

### **The Reasoning**



1. **Virtual Ground:** In an ideal op-amp configuration with [important]negative feedback[/important], the inverting input ($V_-$) is held at a virtual ground ($0\text{ V}$) because the non-inverting input ($V_+$) is connected to ground.
2. **Input Current ($i_C$):** The current flowing through the input capacitor depends on the rate of change of the voltage across it:
   $$[important]i_C(t) = C \frac{d(v_{in}(t) - 0)}{dt} = C \frac{dv_{in}(t)}{dt}[/important]$$
3. **Feedback Current ($i_R$):** Because an ideal op-amp draws zero input current, [important]all of $i_C$ must flow through the feedback resistor $R$ toward the output[/important]. 
4. **Output Voltage ($v_{out}$):** Using Ohm's law across the resistor (from virtual ground to the output):
   $$[important]v_{out}(t) = 0 - i_R(t)R = -i_C(t)R[/important]$$

Substituting the capacitor current equation into the Ohm's law equation yields the final relationship:
$$[important]v_{out}(t) = -RC \frac{dv_{in}(t)}{dt}[/important]$$

Thus, the output voltage is directly proportional to the time derivative of the input voltage, with an inversion.
