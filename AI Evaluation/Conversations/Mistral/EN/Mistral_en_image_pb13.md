## Utilisateur
Here is an analog electronics circuit.
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.
*(image of analog electronics circuit with two operational amplifiers, a capacitor C0, resistors αR and (1-α)R, input current i, and input voltage u)*

---
## IA
Let's analyze the circuit step by step. This is a **floating capacitor multiplier** circuit, often used to simulate a capacitor with an effective capacitance larger than the physical capacitor \( C_0 \) used in the circuit.

---
## **1. Circuit Analysis**

### **Components and Connections**
- Two operational amplifiers (ALIs) in linear mode.
- A capacitor \( C_0 \) connected between the output of the first op-amp and the input of the second op-amp.
- Two resistors: \( \alpha R \) and \( (1-\alpha)R \), where \( \alpha \) is a scaling factor (\( 0 < \alpha < 1 \)).
- The input current is \( i \), and the input voltage is \( u \).

### **Assumptions**
- The op-amps are ideal: infinite input impedance, zero output impedance, and virtual short at their inputs.
- The circuit operates in linear mode, so the op-amps do not saturate.

---
## **2. Deriving the Equivalent Capacitance**

### **Step 1: Voltage at the Input of the First Op-Amp**
The first op-amp (labeled ①) is in a **voltage follower** configuration. Its output voltage \( v_1 \) is equal to the input voltage \( u \):
\[
v_1 = u
\]

### **Step 2: Current Through \( C_0 \)**
The capacitor \( C_0 \) is connected between \( v_1 \) and the input of the second op-amp (labeled ②). The current through \( C_0 \) is:
\[
i_{C_0} = C_0 \frac{d(v_1 - v_2)}{dt}
\]
where \( v_2 \) is the voltage at the input of the second op-amp.

### **Step 3: Voltage at the Input of the Second Op-Amp**
The second op-amp is also in a **voltage follower** configuration, so its output voltage \( v_2 \) is equal to the voltage at its non-inverting input. The non-inverting input is connected to a voltage divider formed by \( \alpha R \) and \( (1-\alpha)R \).

The voltage at the non-inverting input of the second op-amp is:
\[
v_2 = \frac{(1-\alpha)R \cdot v_1 + \alpha R \cdot 0}{(1-\alpha)R + \alpha R} = (1-\alpha) v_1
\]
Since \( v_1 = u \), we have:
\[
v_2 = (1-\alpha) u
\]

### **Step 4: Current Through \( C_0 \) in Terms of \( u \)**
Substitute \( v_1 = u \) and \( v_2 = (1-\alpha)u \) into the current equation:
\[
i_{C_0} = C_0 \frac{d(u - (1-\alpha)u)}{dt} = C_0 \frac{d(\alpha u)}{dt} = \alpha C_0 \frac{du}{dt}
\]

### **Step 5: Input Current \( i \)**
The input current \( i \) is equal to the current through \( C_0 \), because the op-amps draw no input current:
\[
i = i_{C_0} = \alpha C_0 \frac{du}{dt}
\]

### **Step 6: Equivalent Capacitance**
The input current \( i \) can also be expressed in terms of an equivalent capacitance \( C \):
\[
i = C \frac{du}{dt}
\]
Comparing the two expressions for \( i \):
\[
C \frac{du}{dt} = \alpha C_0 \frac{du}{dt}
\]
Thus, the equivalent capacitance is:
\[
C = \alpha C_0
\]

---
## **3. Purpose of the Circuit**
This circuit is a **capacitance multiplier**. It allows you to simulate a capacitor with an effective capacitance \( C = \alpha C_0 \) using a smaller physical capacitor \( C_0 \). This is useful in applications where:
- A large capacitance is needed, but physical space or cost constraints limit the use of large capacitors.
- You want to **emulate** a large capacitor using a smaller one and active components (op-amps).

For example, if \( C_0 = 1 \mu F \) and \( \alpha = 10 \), the circuit behaves like a \( 10 \mu F \) capacitor.

---
## **4. Summary**
- The circuit is equivalent to a capacitor with capacitance:
  \[
  \boxed{C = \alpha C_0}
  \]
- **Purpose**: To simulate a larger capacitance using a smaller physical capacitor and op-amps. This is useful in filter design, timing circuits, and other applications requiring large capacitances.
