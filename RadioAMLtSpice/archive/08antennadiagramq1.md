# Prompt: in the antenna diagram the output leave from the left ground, why is that ?
# Correcting the LC Antenna Diagram

You are correct to question the diagram. In the original version, the **output appeared to come from the ground node**, which would not provide a usable RF signal. The **correct output node is the junction between the inductor (L) and the capacitor (C)**.

Ground is only used as the reference node for the LC tank, not as the signal output.

---

## Correct LC Antenna / Tuning Circuit

```
        AM Antenna
             |
             |
             +---- L ----+------> Output to RF Amplifier / Detector
             |           |
             |           C
             |           |
            GND         GND
```

---

## Explanation

- **Antenna** receives the incoming radio signal.
- **L (Inductor)** and **C (Capacitor)** form the resonant LC tuning circuit.
- The **output is taken from the junction of L and C**, where the tuned RF voltage appears.
- Both L and C connect to **ground as a reference**, but the output signal is not taken from ground.

At the resonant frequency, the voltage at the LC junction becomes large, allowing the receiver to pass the desired station to the next stage (RF amplifier or detector).

---

## Optional Improved Version (With Antenna Coupling Capacitor)

In practice, a small **coupling capacitor** is often used so the antenna does not detune the LC circuit.

```
        Antenna
           |
           |
          Cc
           |
           +---- L ----+------> Output to RF Amplifier
           |           |
           |           C
           |           |
          GND         GND
```

Typical value:

| Component | Typical Value |
|-----------|---------------|
| Cc (coupling capacitor) | 10 pF – 100 pF |

This allows the antenna to **inject RF energy into the tank circuit without heavily loading it**, improving tuning selectivity.
