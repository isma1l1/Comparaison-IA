## Utilisateur
Answer concisely, omitting any unnecessary information. 
We are studying a classic non-inverting summing circuit in which the four resistors have the same value R. Determine Vs as a function of V1 and V2. Explain your reasoning.

## IA
For a classic non-inverting summing circuit with two inputs ($V_1$ and $V_2$) and four identical resistors ($R$), the output voltage is:

[[important]$$V_s = V_1 + V_2$$[\important]]

---

### Reasoning

1.  **Input Network (Voltage Divider):**
    The two input resistors form a passive summer at the non-inverting terminal ($V_+$). Using Superposition or Nodal Analysis:
    [[important]$$V_+ = \frac{V_1 + V_2}{2}$$[\important]]
    This occurs because the two resistors $R$ at the input create a voltage divider that averages the input signals.

2.  **Amplifier Gain:**
    The feedback network consists of two resistors of value $R$ (the feedback resistor and the resistor to ground). The gain ($A_v$) of a non-inverting amplifier is:
    [[important]$$A_v = 1 + \frac{R_{f}}{R_{g}} = 1 + \frac{R}{R} = 2$$[\important]]

3.  **Final Output:**
    The output $V_s$ is the product of the non-inverting terminal voltage and the gain:
   [[important] $$V_s = V_+ \cdot A_v $$[\important]]
    $$= \left( \frac{V_1 + V_2}{2} \right) \cdot 2 = V_1 + V_2$$
