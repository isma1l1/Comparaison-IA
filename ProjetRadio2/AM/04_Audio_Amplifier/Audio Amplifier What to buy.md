# 04_AudioAmplifier/Audio Amplifier Components.md – What to Buy

This is a **single continuous Markdown block** for Obsidian. It gives a **clear shopping list** of components you need to build the audio amplifier stage for your AM radio.

---

## 🧾 1. Transistor (Amplifying Element)

You need a small-signal transistor to amplify the audio signal.

✔ Recommended options (all work well for beginner audio amps):

- **BC547** – common, cheap, easy to use  
- **2N3904** – equally good alternative  
- **BC337** – slightly higher current capability

👉 Any of these is fine; they are cheap and widely available.

---

## 🔊 2. Resistors (Bias & Gain)

These set the transistor’s operating point and gain.

Typical recommended values for a basic amplifier:

- **R1 (base bias):** 10 kΩ  
- **R2 (collector load):** 4.7 kΩ  
- **Re (emitter resistor):** 1 kΩ  
- **Optional bypass resistor:** 100 Ω – 1 kΩ (if using a bypass capacitor)

⚠ You don’t need exact values; tolerances of ±5% or ±10% are fine.

### What to buy:

- A **resistor assortment kit (E12 or similar)** → covers all values up to 100 kΩ

---

## 🧲 3. Capacitors (Coupling & Filtering)

Capacitors are used to pass the AC audio signal while blocking DC, and in some cases stabilizing bias.

Typical recommended values:

- **Input coupling capacitor:** 10 µF (electrolytic or film)  
- **Output coupling capacitor:** 10 µF (electrolytic or film)  
- **Optional emitter bypass capacitor:** 10 µF (if using an emitter resistor)

### What to buy:

- A **small electrolytic capacitor assortment** (e.g., 4.7 µF, 10 µF, 22 µF)  
- A few **film or ceramic capacitors** (e.g., 1 µF, 10 µF) if you prefer film parts

---

## 🔊 4. Speaker / Headphones

Depending on your intended output:

**Headphones (recommended for beginners):**
- **Impedance:** ~32 Ω  
- Simple earbuds or small headphones work fine.

**Small Speaker (optional):**
- **Size:** 3–5 inches  
- **Impedance:** 8–16 Ω  
- Requires more current → may need a stronger amplifier stage later

---

## 🔋 5. Power Supply

The audio amplifier needs a DC supply.

✔ Recommended:

- **9V battery + clip** → portable and low noise  
- OR **5V regulated supply** (e.g., from USB with proper filtering)

👉 Battery is easier and cleaner (less noise).

---

## 🧱 6. Prototyping Materials

- **Breadboard (medium size)**  
- **Jumper wires**  
- **Perfboard (optional)** for final assembly  
- **Soldering kit** (optional)

---

## 📦 Summary Shopping List

- **1× Transistor:** BC547 / 2N3904 / BC337  
- **Resistors:** assortment kit (10 Ω – 100 kΩ)  
- **Capacitors:**  
  - Electrolytic: 4.7–22 µF  
  - Film/ceramic: 1–10 µF  
- **Speaker or Headphones:**  
  - Headphones: ~32 Ω  
  - Or speaker: 8–16 Ω (optional)  
- **Power Source:** 9V battery + clip (recommended)  
- **Prototyping:** breadboard, jumper wires, perfboard, soldering kit

---

## 🛒 Notes

- Tolerance doesn’t need to be tight  
- Most parts are **very inexpensive**  
- Assortment kits are useful because they can be reused in later circuits