
---

## 🧾 1. Diode (Rectifier)

The diode is essential to **extract the positive half of the AM signal**.

✔ Recommended options:
- **1N4148** – very common, cheap, fast switching  
- **1N914** – similar to 1N4148  
- **1N34A (germanium diode)** – lower voltage drop → better sensitivity (especially with weak signals)

👉 For a beginner project, the **1N4148** is fine.  
👉 If you want slightly better performance with weak signals, get a **1N34A**.

---

## 🧲 2. Capacitor (Peak Detector / Smoothing)

This capacitor needs to store peaks and release them slowly to follow the audio envelope.

✔ Recommended range:
- **100 nF – 470 nF** (0.1 µF – 0.47 µF)

✔ Type:
- **Ceramic capacitor** or **film capacitor**  
- Choose a value in the middle of the range (e.g., **220 nF**) for general use.

---

## 🧮 3. Resistor (Discharge Path)

The resistor is used to control how fast the capacitor discharges.

✔ Recommended range:
- **10 kΩ – 100 kΩ**

👉 Example good starter value: **47 kΩ**

- Lower value → capacitor discharges faster → can distort low-frequency audio  
- Higher value → capacitor discharges slower → can smear fast audio changes

---

## 🧫 4. Passive Breadboard Supplies (Optional but Useful)

- **Breadboard (small)** – for prototyping  
- **Jumper wires** – to make connections  
- **Perfboard (optional)** – for a permanent build

---

## 🔌 5. Connections

You don’t need any power supply for the detector itself — it is **passive**.

All grounds must be shared with the RF Front-End and the Audio Amplifier.

---

## 📦 Summary Shopping List

- 1× **Diode**: 1N4148 or 1N34A  
- 1× **Capacitor**: 100 nF – 470 nF (e.g., 220 nF)  
- 1× **Resistor**: 10 kΩ – 100 kΩ (e.g., 47 kΩ)  
- Optional prototyping items: breadboard, perfboard, jumper wires

---

## 🛒 Notes

- These are **standard, inexpensive components** available from hobby stores or online.  
- Tolerances don’t need to be precise — typical ±5% ceramic capacitors and resistors are fine.  
- This set is enough to build a basic envelope detector that works well for the AM broadcast band.