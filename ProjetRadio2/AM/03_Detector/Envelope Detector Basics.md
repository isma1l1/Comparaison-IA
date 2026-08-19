# 03_Detector/Envelope Detector Basics.md – Purpose and Principle with Clear Wiring Scheme


---

## 1. Purpose of the Envelope Detector

After the RF Front-End, the signal is:

- A **high-frequency RF carrier** (~1 MHz)  
- Whose **amplitude varies slowly** (contains the audio)

👉 This is an **AM signal**, and the detector extracts the audio.

---

## 2. Clear Wiring Scheme (Text-Based)

 RF Input (from RF Front-End)
            │
            │
            ├─────────────┐
            │                       │
		    ┌─┐                   │
		    │D│ Diode       │
		    └─┘                  │
            │                     │
            │                    │
            └──────┐       │
                   │        │
                  ┌─┐    ┌─┐
                  │C│    │R│
                  └─┘    └─┘
                   │         │
                   │           │
               Audio Out    │
                   │           │
                   └──────┘
                   │
                  GND


**Connection Details:**

1. **RF Input:** Connects directly from the **output of the RF Front-End**  
2. **Diode (D):** Anode towards RF input, cathode to the junction of capacitor and resistor  
3. **Capacitor (C):** One leg connects to diode cathode, the other to **ground**  
4. **Resistor (R):** One leg connects to diode cathode, the other to **ground**  
5. **Audio Output:** Taken from the junction between **diode, capacitor, and resistor**  
6. **GND:** Connects to circuit ground (common with RF Front-End)

---

## 3. How it Works Step by Step

1. **Rectification:** The diode passes only positive half-cycles of the RF signal  
2. **Peak Detection:** The capacitor charges to the highest voltage of each cycle  
3. **Smoothing:** The resistor discharges the capacitor slowly → smooth envelope  
4. **Audio Output:** The junction of D-C-R gives the recovered audio

---

## 4. Input vs Output

| Signal      | Characteristics                       |
|------------|---------------------------------------|
| Input       | Fast RF (~1 MHz), amplitude modulated |
| Output      | Audio (~20 Hz – 20 kHz), smooth       |

---

## 5. Notes

- RC values control how fast the capacitor discharges → affects audio quality  
- Passive, requires **no external power**  
- Simple and effective for beginner AM radios  

---

## 6. Next Step

- The audio signal is weak → feed into the **Audio Amplifier** to drive a speaker or headphones

[[Envelope Build And Design]]
