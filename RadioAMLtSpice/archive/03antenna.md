# Prompt :
# AM Receiver Antenna Circuit

## 1. Introduction

The **antenna stage** of an AM receiver serves three main purposes:  

1. **Signal capture:** Picks up the radio waves from the air.  
2. **Frequency selection:** An LC resonant circuit selects the desired AM frequency.  
3. **Signal transfer:** Feeds the selected RF signal to the detector or amplifier stage.  

This section focuses on the antenna and LC tank portion of an analog AM receiver.

---

## 2. Schematic (Text Diagram)

        AM Antenna
             |
             +---- L ----+
             |           |
             |           C
             |           |
            GND         GND
             |
             +----> Output to RF stage / Detector


**Components:**

| Component       | Typical Value / Range | Notes |
|-----------------|--------------------|-------|
| **Antenna**     | 1–5 m wire          | Longer → better signal pickup |
| **L (Inductor)**| ~50 µH              | Depends on tuning; use ferrite core for higher Q |
| **C (Capacitor)**| 100–1000 pF         | Variable capacitor allows tuning across the AM band |

---

## 3. Resonant Frequency

The resonant frequency of the LC tank is:


f = 1/(2*pi*sqrt(LC))

**Example:** To tune to **1 MHz**, choosing (C = 500 pF):

L = 1/((2pif)^2 C) ~ 50muH


This ensures the circuit resonates at the desired AM broadcast frequency.

---

## 4. Design Notes / Constraints

1. **Antenna length:** 1–2 m wire is sufficient for lab projects; longer wires improve signal capture.  
2. **Coil Q-factor:** Higher Q gives sharper tuning and better selectivity. Ferrite cores can help increase Q without making coils huge.  
3. **Parasitic capacitance:** Real coils have some stray capacitance; fine-tune C accordingly.  
4. **Tuning:** A variable capacitor allows scanning the full AM band (530–1700 kHz).  
5. **Coupling:** Series or parallel connection to the next stage affects impedance matching and signal strength.
