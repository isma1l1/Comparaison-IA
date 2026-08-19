## Utilisateur
Here is an analog electronics circuit. 
The two resistors R and the two capacitors C are identical. Express the relationship between the output voltage and the two input voltages of the circuit in the frequency domain and then in the time domain. Explain your reasoning.
*(image of an analog electronics circuit showing a differential integrator with an operational amplifier, two resistors, and two capacitors)*

## IA
This circuit is a **differential integrator**. By using an operational amplifier (op-amp) with symmetric RC networks on both the inverting and non-inverting inputs, the circuit performs the mathematical operation of integration on the difference between two signals.

Assuming an ideal op-amp (infinite gain, infinite input impedance, and zero output impedance), we can analyze the circuit as follows:

### 1. Frequency Domain Analysis

Let $R$ be the resistance of both resistors and $C$ be the capacitance of both capacitors. In the Laplace domain (frequency domain), the impedance of the resistors is $R$ and the impedance of the capacitors is $Z_C = \frac{1}{Cs}$.

**Non-inverting input ($V_+$):**
The network at the non-inverting terminal is a simple voltage divider:
[[important]$$V_+ = e_2 \cdot \frac{Z_C}{R + Z_C} = e_2 \cdot \frac{1/Cs}{R + 1/Cs} = \frac{e_2}{1 + RCs}$$[\important]]

**Inverting input ($V_-$):**
Using the principle of superposition or Kirchhoff's Current Law (KCL) at the inverting node:
[[important]$$\frac{e_1 - V_-}{R} + \frac{s - V_-}{Z_C} = 0$$[\important]]

Since the op-amp is in a negative feedback configuration, we assume [[important]$V_- = V_+$[\important]]. Substituting the expression for $V_+$:
$$\frac{e_1}{R} + \frac{s}{Z_C} = V_- \left( \frac{1}{R} + \frac{1}{Z_C} \right)$$
$$\frac{e_1}{R} + sCs = \frac{e_2}{1 + RCs} \left( \frac{1 + RCs}{R} \right)$$
$$\frac{e_1}{R} + sCs = \frac{e_2}{R}$$

Rearranging to solve for the output $s$:
$$sCs = \frac{e_2 - e_1}{R}$$
[[important]$$s(s) = \frac{1}{RCs}(e_2(s) - e_1(s))$$[\important]]

---

### 2. Time Domain Analysis

To move from the frequency domain to the time domain, we apply the inverse Laplace transform. Recall that multiplication by $\frac{1}{s}$ in the frequency domain corresponds to integration in the time domain.

The relationship is:
[[important]$$s(t) = \frac{1}{RC} \int_{0}^{t} (e_2(\tau) - e_1(\tau)) d\tau + s(0)$$[\important]]

If we assume the initial charge on the capacitors is zero ($s(0) = 0$), the output is simply:
**$$s(t) = \frac{1}{RC} \int_{0}^{t} (e_2(\tau) - e_1(\tau)) d\tau$$**

---

### Summary of Reasoning

* **Differential Action:** Because the same RC network is applied to both inputs, the common-mode signals are canceled out, leaving only the difference $(e_2 - e_1)$.
* **Integration:** The placement of the capacitor in the feedback loop of the inverting side (and the shunt capacitor on the non-inverting side) creates a transfer function proportional to $1/s$.
* **Significance:** This specific topology is often used in analog computing and signal processing to integrate the difference between two floating or ground-referenced signals while maintaining high input impedance and noise rejection.
