## 1. Role Reminder

The RF Front-End:
- Receives a **small RF signal** from the antenna  
- **Amplifies** it without distorting the modulation  
- Prepares it for the **detector stage**

It must therefore be:
- **Stable**
- **Low-noise**
- **Linear (no distortion)**

---

## 2. Chosen Architecture (Beginner-Friendly)

We use a **common-emitter NPN amplifier**:

- Simple  
- Cheap  
- Works well for AM frequencies (~1 MHz)  

---

## 3. Circuit Design (Dimensioning)

We want the transistor to operate in its **linear region**.

### 3.1. Power Supply

- Use: **5V to 9V**
- Example: 9V battery (clean, low noise)

---

### 3.2. Transistor Choice

- Type: **NPN small-signal transistor**
- Examples:
  - BC547  
  - 2N2222  

These work well up to several MHz → suitable for AM.

---

### 3.3. Biasing the Transistor

We set a stable operating point.

#### Recommended values:

- **Rc (collector resistor):** 4.7 kΩ  
- **Re (emitter resistor):** 1 kΩ  
- **Rb (base bias):** 100 kΩ  

👉 This gives:
- Moderate gain  
- Good stability  
- Low distortion  

---

### 3.4. Coupling Capacitors

These pass AC (signal) and block DC.

- **C_in (input):** 10 nF – 100 nF  
- **C_out (output):** 10 nF – 100 nF  

👉 Why:
- At ~1 MHz, these values have low impedance → signal passes easily  

---

## 4. Step-by-Step Build

### Step 1 – Place Components
- Put transistor on breadboard  
- Keep layout **compact**  

---

### Step 2 – Build Bias Network
- Rc → Vcc  
- Re → GND  
- Rb → Vcc → Base  

---

### Step 3 – Connect Input
- Antenna → C_in → Base  

---

### Step 4 – Connect Output
- Collector → C_out → Detector stage  

---

### Step 5 – Power
- Vcc → 5–9V  
- GND → common ground  

---

## 5. Practical Design Rules

### Keep it RF-friendly:
- Short wires → reduce паразitic capacitance  
- Tight layout → better high-frequency behavior  
- Avoid breadboard if possible (but OK for first test)

---

### Noise Reduction:
- Use battery (not USB power)  
- Keep away from:
  - Computers  
  - Chargers  
  - LED lights  

---

## 6. Gain and Stability

### If signal is too weak:
- Increase Rc (e.g., 10 kΩ) → more gain  

### If signal is distorted:
- Increase Re → more stability  
- Reduce Rc → less gain  

---

## 7. Interaction with Antenna

### If using tunable loop antenna:
- Already tuned → perfect match  
- RF front-end only amplifies  

### If using simple wire:
- Less selective → RF stage becomes more important  

---

## 8. Expected Results

- Without RF stage → very weak or no signal  
- With RF stage → stronger, clearer reception  
- Still noisy → normal (detector + filters come next)

---

## 9. Summary

You are building:
- A **single-stage RF amplifier**
- With:
  - 1 transistor  
  - 3 resistors  
  - 2 capacitors  

👉 Simple, cheap, and sufficient for a working AM radio.

---

## 10. Next Step

After this stage:
- Build the **AM Detector (envelope detector)**  
- Then the **Audio Amplifier**

[[RF What to buy ]]
