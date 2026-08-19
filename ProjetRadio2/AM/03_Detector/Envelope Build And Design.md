
---

## 1. Overview

The envelope detector takes the **AM RF signal** from the RF Front-End and outputs a **low-frequency audio signal** for the amplifier.

Key requirements:

- Simple, **passive** circuit (no power needed)  
- Components must allow proper smoothing of the RF carrier to extract audio  
- Works well for the **AM band (~530–1600 kHz)**

---

## 2. Building Step by Step

### Step 1 – Prepare Components
- Diode, capacitor, resistor  
- Breadboard for testing (optional: perfboard for permanent assembly)  

### Step 2 – Connect RF Input
- RF signal comes from **collector of RF Front-End transistor** or antenna LC output  
- Connect to **anode of diode**  

### Step 3 – Connect Capacitor and Resistor
- Both **one leg of C and R** connect to **diode cathode**  
- Other leg of C → **ground**  
- Other leg of R → **ground**  

### Step 4 – Take Audio Output
- From **junction of diode cathode, C, and R**  
- Connect to **audio amplifier input**  

### Step 5 – Ground Connection
- Connect all grounds together (RF stage, detector, amplifier)

---

## 3. Layout Tips

- Keep **wires short** → reduces parasitic capacitance and noise  
- Use a **compact layout** → better high-frequency performance  
- Avoid placing near **noisy electronics** (LEDs, computers, power adapters)  

---

## 4. Testing and Adjustment

- Connect **RF Front-End**, then detector  
- Use a small speaker or headphones to check audio  
- Adjust **C or R** if:
  - Audio sounds too “hissy” → increase RC time constant  
  - Audio sounds “sluggish” → decrease RC time constant  

**Tip:** The goal is to smooth the RF carrier while keeping the audio intact.

---

## 5. Summary

- Components: **1 diode, 1 capacitor, 1 resistor**  
- Connect as shown in the **Envelope Detector Basics scheme**  
- Passive, simple, and suitable for beginners  
- Output is **ready for the Audio Amplifier stage**

---

## 6. Next Step

- Feed the output into the **Audio Amplifier** to drive a speaker or headphones

[[Envelope What to buy]]
