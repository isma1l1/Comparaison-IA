
---

## 1. Overview

The audio amplifier:

- Receives audio from the **envelope detector**  
- Amplifies it to **drive headphones or a small speaker**  

Requirements for a beginner AM radio:

- Simple circuit (single transistor stage is enough)  
- Works with **low-voltage signals** (~1–2 V peak from detector)  
- Compatible with **8–32 Ω headphones or 8–16 Ω speaker**

---

## 2. Components Needed

- **Transistor (NPN)** → e.g., BC547, 2N3904  
- **Resistors** → for biasing and gain  
- **Capacitors** → for coupling (passing audio) and bypassing  
- **Speaker or headphones** → load for the amplifier  
- **Power supply** → 3–9 V battery is sufficient  

*(Exact values will depend on chosen transistor and desired gain — see component selection file for shopping list)*

---

## 3. Building Step by Step

### Step 1 – Prepare Components
- Transistor, resistors, capacitors, breadboard  
- Optional: perfboard for permanent assembly  

### Step 2 – Bias the Transistor
- Connect **resistors** to set the transistor’s **operating point**  
- Ensure transistor works in **active region** for linear amplification  

### Step 3 – Connect Coupling Capacitors
- Place **capacitors at input and output** to block DC  
- Input capacitor: between **detector output** and transistor base  
- Output capacitor: between **collector** and speaker/headphones  

### Step 4 – Connect Load
- Speaker or headphones connected to the **collector (or emitter depending on configuration)**  
- Other side connected to **ground**  

### Step 5 – Power the Circuit
- Connect **battery or regulated supply**  
- Ensure **correct polarity** for transistor operation  

---

## 4. Layout Tips

- Keep **signal wires short** to reduce noise  
- Avoid running near **power lines or noisy electronics**  
- Place **capacitors close** to transistor pins for stability  

---

## 5. Testing and Adjustment

- Connect the **detector output**  
- Power on and listen through headphones or small speaker  
- If audio is too low, check resistor values (adjust gain)  
- If distorted, check transistor biasing and capacitor orientation  

---

## 6. Summary

- Single-stage transistor amplifier is sufficient for **beginner AM radios**  
- Works with **headphones or small speaker**  
- Connect directly **after the envelope detector output**  

---

## 7. Next Step

- Select and buy components for your amplifier  
- After building, connect to **AM detector** and test overall radio circuit

[[Audio Amplifier What to buy]]