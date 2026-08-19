## Utilisateur
Give me the formula for the gain of a non-inverter setup based on the values of the resistances R1 and R2. Explain your reasoning.

## IA
The gain \( A_v \) of a **non-inverting operational amplifier (op-amp) setup** is given by the following formula:

\[
[important]A_v = 1 + \frac{R_2}{R_1}[/important]
\]

### Explanation and Reasoning

#### Circuit Setup
In a non-inverting op-amp configuration:
- The input signal is applied directly to the non-inverting terminal (\( V_{in} \)).
- A feedback network consisting of resistors \( R_1 \) and \( R_2 \) is connected between the output and the inverting terminal.

#### Key Points
1. **Non-inverting Terminal:**
   The voltage at the non-inverting terminal is equal to the input voltage (\( V_{in} \)).

2. **Inverting Terminal:**
   The inverting terminal is at the same potential as the non-inverting terminal due to the **virtual short** principle of an ideal op-amp (i.e., \( [important]V_- = V_{in}[/important] \)).

3. **Feedback Network:**
   The feedback network divides the output voltage (\( V_{out} \)) and feeds a fraction back to the inverting terminal. The voltage at the inverting terminal is given by the voltage divider rule:
   \[
  [important] V_- = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]
   \]

4. **Equating Voltages:**
   Since \( [important]V_- = V_{in}[/important] \), we have:
   \[
   V_{in} = V_{out} \cdot \frac{R_1}{R_1 + R_2}
   \]

5. **Solving for Gain:**
   Rearranging the equation to solve for the gain (\( A_v = \frac{V_{out}}{V_{in}} \)):
   \[
   [important]\frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}[/important]
   \]

#### Conclusion
The gain of the non-inverting op-amp is always **greater than or equal to 1** and depends only on the ratio of the feedback resistors \( R_2 \) and \( R_1 \). This configuration is widely used for buffering and amplification without phase inversion.