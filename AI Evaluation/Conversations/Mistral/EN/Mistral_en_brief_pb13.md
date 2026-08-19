## Utilisateur
Respond concisely, omitting any unnecessary information.
The two ALIs in the circuit operate in linear mode, show that this circuit is equivalent to a capacitor with capacitance C. Express C as a function of C0 and alpha, and explain the purpose of such a circuit.

*(image of a circuit diagram with two operational amplifiers, resistors labeled αR and (1-α)R, and a capacitor labeled C0)*

---
## IA
### Equivalence to a Capacitor
The circuit is equivalent to a **single capacitor** with capacitance:
**C = α C₀**

---

### Purpose
This circuit is a **floating capacitor multiplier**. It emulates a larger capacitance (by a factor of **1/α**) using a smaller physical capacitor **C₀**, which is useful in integrated circuits where large capacitance values are impractical to realize directly. The parameter **α** (0 < α < 1) controls the effective multiplication factor.
