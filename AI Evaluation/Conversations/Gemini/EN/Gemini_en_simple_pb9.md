## Utilisateur

We are studying a classic differentiator amplifier (one resistance and one capacitor). Determine the input-output relationship of this system. Explain your reasoning.

## IA

To find the input-output relationship of a classic differentiating amplifier, we analyze an ideal operational amplifier (op-amp) configured with a capacitor at the input and a resistor in the feedback loop.

Here is the step-by-step derivation based on fundamental circuit laws.

---

### The Circuit Setup

In a standard inverting differentiator configuration:

* The capacitor $C$ is connected between the input voltage $v_{in}(t)$ and the inverting input ($-$) of the op-amp.
* The resistor $R$ is connected in the feedback path between the inverting input ($-$) and the output $v_{out}(t)$.
* The non-inverting input ($+$) is connected directly to the ground ($0\text{ V}$).

---

### Step-by-Step Derivation

#### 1. Ideal Op-Amp Properties

To analyze the circuit, we apply two key rules of ideal op-amps:

* **Virtual Ground:** Because the non-inverting terminal is grounded and the op-amp maintains negative feedback, the voltage at the inverting terminal ($v_-$) is forced to $0\text{ V}$.

$$v_- = v_+ = 0\text{ V}$$


* **Zero Input Current:** No current enters the op-amp's inverting input terminal ($i_- = 0$). Therefore, all the current flowing through the capacitor ($i_C$) must flow directly through the resistor ($i_R$).

$$i_C(t) = i_R(t)$$



#### 2. Current Through the Capacitor

The current flowing through a capacitor is proportional to the time rate of change of the voltage across it. The voltage across $C$ is $v_{in}(t) - v_-$. Since $v_- = 0\text{ V}$:


$$i_C(t) = C \frac{d(v_{in}(t) - 0)}{dt} = C \frac{dv_{in}(t)}{dt}$$

#### 3. Current Through the Resistor

Using Ohm's Law, the current flowing through the feedback resistor from the inverting node to the output node is:


$$i_R(t) = \frac{v_- - v_{out}(t)}{R} = \frac{0 - v_{out}(t)}{R} = -\frac{v_{out}(t)}{R}$$

#### 4. Equating the Currents

Since $i_C(t) = i_R(t)$, we can substitute our expressions from steps 2 and 3:


$$C \frac{dv_{in}(t)}{dt} = -\frac{v_{out}(t)}{R}$$

---

### The Input-Output Relationship

Solving for the output voltage $v_{out}(t)$ gives the final governing equation for the system:

$$v_{out}(t) = -RC \frac{dv_{in}(t)}{dt}$$

### Explanation of the Result

* **Differentiation:** The output voltage is directly proportional to the **time derivative** (the rate of change) of the input voltage. If the input is constant, the output is zero. If the input changes rapidly (like a steep ramp or a square wave edge), the output spikes.
* **Scaling Factor ($RC$):** The product of the resistance and capacitance acts as a gain constant.
* **Inversion (The Negative Sign):** The negative sign indicates a $180^\circ$ phase shift, which is a hallmark of the inverting op-amp configuration.

### Frequency Domain (Alternative Perspective)

If you look at this system in the Laplace domain (assuming zero initial conditions), the transfer function $H(s)$ is:


$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} = -sRC$$


Substituting $s = j\omega$ shows that the gain increases linearly with frequency, which explains why ideal differentiators are highly susceptible to high-frequency noise.
