# Prompt : in full markdown, id like a graph of the RF amplifier part and any constraints on values that may be

# AM Receiver RF Amplifier Stage

## 1. Introduction

The **RF amplifier** in an AM receiver serves to:

1. Boost the weak RF signal received from the antenna/tuning circuit.
2. Improve **sensitivity** and **signal-to-noise ratio**.
3. Provide isolation between the antenna and the detector stage.

A typical analog RF amplifier uses a **single transistor** (BJT or FET) in a **common-emitter/common-source configuration** with an **LC tank for tuning**.

---

## 2. RF Amplifier Schematic (ASCII Graph)
               +Vcc
                |
                Rc
                |
                +----+--------> Output to Detector
                |    |
                |    L2
                |    |
           C1   |    C2
     Antenna---||---Q1 (BJT/FET)---GND
                |
               GND
**Legend:**

- **BJT/FET** – Active transistor for amplification  
- **Rc** – Collector (or drain) load resistor  
- **L2/C2** – LC tank or bypass capacitor for tuning/stability  
- **C1** – Coupling capacitor from antenna/tuning circuit  
- **C2** – Bypass capacitor (often to stabilize bias)  

---

## 3. Typical Component Values / Constraints

| Component | Typical Values / Range | Notes |
|-----------|----------------------|-------|
| **Transistor (Q1)** | 2N3904 (BJT) / J310 (FET) | Small-signal RF transistor |
| **Rc** | 1–10 kΩ | Load resistor; determines gain |
| **C1** | 100–1000 pF | Coupling capacitor; blocks DC, passes RF |
| **C2** | 10–100 nF | Bypass capacitor; stabilizes supply/ground |
| **L2** | 20–100 µH | Part of tuned LC; selects frequency band |

**Notes:**

1. **Biasing:** Proper DC bias must be set to operate transistor in linear region.  
2. **Gain vs Bandwidth:** Larger Rc → higher gain but narrower bandwidth.  
3. **LC Tank:** Optional for **selective amplification** at desired AM frequency.  
4. **Coupling:** C1 must be small enough to pass RF but block DC.  
5. **Noise Consideration:** Use low-noise transistor and minimize parasitic capacitance.

---

## 4. Design Tips

- For lab-scale AM receivers, a **single-stage BJT amplifier** is sufficient.  
- Ferrite-core coils can increase Q and selectivity in L2.  
- Adjust C1/C2 values depending on the next stage input and operating frequency.  
- Keep leads short to minimize parasitic inductance and capacitance at kHz–MHz range.  
