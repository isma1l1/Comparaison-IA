## Utilisateur
Determine the output voltage v(t) for a sinusoidal input e(t) = E0sin(wt) in a Graetz Bridge setup. Explain your reasoning.

---

## IA
To determine the output voltage \( v(t) \) for a sinusoidal input \( e(t) = E_0 \sin(\omega t) \) in a **Graetz Bridge** (also known as a full-wave bridge rectifier), let's break down the process step by step.

---

## **1. Graetz Bridge Operation**
A Graetz Bridge consists of four diodes arranged in a bridge configuration. The input is an AC voltage, and the output is a pulsating DC voltage.

### **Key Points:**
- The bridge rectifier allows current to flow during [important]both the positive and negative half-cycles[/important] of the input AC voltage.
- The output voltage \( v(t) \) is the absolute value of the input voltage, minus the voltage drops across the diodes.

---

## **2. Input Voltage**
The input voltage is given by:
\[
e(t) = E_0 \sin(\omega t)
\]
where:
- \( E_0 \) is the peak amplitude of the input voltage,
- \( \omega \) is the angular frequency.

---

## **3. Output Voltage**
### **Ideal Case (No Diode Drops)**
In an ideal scenario (assuming ideal diodes with no forward voltage drop), the output voltage \( v(t) \) is simply the absolute value of the input voltage:
\[
[important]v(t) =  e(t)| = |E_0 \sin(\omega t)|[/important]
\]

### **Real Case (With Diode Drops)**
In practice, diodes have a forward voltage drop \( V_d \) (typically 0.7 V for silicon diodes). Therefore, the output voltage is:
\[
v(t) = |E_0 \sin(\omega t)| - 2V_d
\]
The factor of 2 accounts for the two diodes conducting in series during each half-cycle.

---

## **4. Waveform Description**
- For \( 0 \leq \omega t \leq \pi \): \( e(t) \) is positive, so \( v(t) = E_0 \sin(\omega t) - 2V_d \).
- For \( \pi \leq \omega t \leq 2\pi \): \( e(t) \) is negative, so \( v(t) = -E_0 \sin(\omega t) - 2V_d \).

The output waveform is a full-wave rectified sine wave, with a peak value of \( E_0 - 2V_d \).

---

## **5. Average Output Voltage**
The average (DC) value of the output voltage \( V_{dc} \) is given by:
\[
V_{dc} = \frac{2E_0}{\pi} - 2V_d
\]

---

## **6. Summary Table**
 | Parameter         | Ideal Case               | Real Case (with diode drops) |
 |-------------------|--------------------------|------------------------------|
 | Output Voltage    | \( |E_0 \sin(\omega t)| \)   | \( |E_0 \sin(\omega t)| - 2V_d \) |
 | Peak Output       | \( E_0 \)               | \( E_0 - 2V_d \)            |
 | Average (DC) Value| \( \frac{2E_0}{\pi} \)  | \( \frac{2E_0}{\pi} - 2V_d \) |

---

## **7. Visualization**
The output voltage \( v(t) \) looks like this:

- **Input (e(t))**: A pure sine wave.
- **Output (v(t))**: A full-wave rectified sine wave, shifted down by \( 2V_d \).

---

## **8. Practical Example**
If \( E_0 = 10 \) V and \( V_d = 0.7 \) V:
- Peak output: \( 10 - 1.4 = 8.6 \) V
- Average output: \( \frac{20}{\pi} - 1.4 \approx 6.366 - 1.4 = 4.966 \) V

---

Would you like a plot of the input and output waveforms, or further clarification on any step?