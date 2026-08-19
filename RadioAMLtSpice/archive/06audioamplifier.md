# Prompt: in full markdown, i'd like a graph of the audio amplifierpart and any constraints on values that may be
# AM Receiver Audio Amplifier

## 1. Introduction

The **audio amplifier** stage increases the amplitude of the recovered audio signal from the detector so it can drive a **speaker or headphones**.

The detector output signal is typically **very small (millivolts)** and must be amplified before it can be used by an output device.

A simple implementation uses a **single BJT transistor amplifier** in a **common-emitter configuration**.

---

## 2. Audio Amplifier Schematic

```
                +Vcc
                 |
                 |
                Rc
                 |
                 +--------- C2 ---------> Audio Output
                 |
                 |
                Q1
              (NPN)
                 |
                 |
                Re
                 |
                 |
                GND


Audio Input
(from Detector)
      |
      |
     C1
      |
      +---- Base (Q1)
      |
     R1
      |
     +Vcc
      |
     R2
      |
     GND
```

---

## 3. Component Legend

| Component | Description |
|-----------|-------------|
| Q1 | NPN transistor (e.g., 2N3904, BC547) |
| Rc | Collector resistor |
| Re | Emitter resistor |
| R1, R2 | Bias voltage divider |
| C1 | Input coupling capacitor |
| C2 | Output coupling capacitor |

---

## 4. Typical Component Values

| Component | Typical Range | Purpose |
|-----------|---------------|--------|
| Q1 | 2N3904 / BC547 | Small signal transistor |
| Rc | 1 kΩ – 10 kΩ | Controls gain |
| Re | 100 Ω – 1 kΩ | Stabilizes bias |
| R1 | 47 kΩ – 220 kΩ | Bias network |
| R2 | 10 kΩ – 47 kΩ | Bias network |
| C1 | 1 µF – 10 µF | Passes audio signal |
| C2 | 10 µF – 220 µF | Couples signal to output |

---

## 5. Design Constraints

### Bias Point

For proper amplification the transistor should operate in the **active region**.

Typical design condition:

Vcollector ≈ Vcc / 2

This allows the signal to swing both positive and negative without clipping.

---

### Frequency Response

Typical AM audio bandwidth:

20 Hz – 5 kHz

Coupling capacitors should be chosen so the cutoff frequency satisfies:

fc = 1 / (2πRC)

Design rule:

fc < 20 Hz

so that low-frequency audio is not attenuated.

---

### Load Impedance

Typical loads:

| Device | Impedance |
|--------|-----------|
| Headphones | 32 Ω – 300 Ω |
| Small speaker | 4 Ω – 8 Ω |

A single transistor stage works best with **high-impedance loads**.  
Driving a low-impedance speaker often requires an **additional power amplifier stage**.

---

## 6. Practical Notes

- Keep wiring short to reduce noise pickup.
- Use **electrolytic capacitors** for larger capacitance values.
- Additional amplifier stages may be added if higher output power is required.
