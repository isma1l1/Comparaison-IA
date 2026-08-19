# Prompt: now id like a diagram of all the different parts together
# Complete AM Receiver Circuit Overview

This diagram shows how the main stages of a simple analog AM receiver connect together:

1. Antenna
2. LC Tuning Circuit
3. RF Amplifier
4. Envelope Detector
5. Audio Amplifier
6. Speaker / Headphones

---

## Full System Diagram

```
        ANTENNA
           |
           |
           +------ L1 ------+
           |                |
           |                C1
           |                |
          GND              GND
           |
           |      (LC Tuning Circuit)
           |
           +---- C2 ----> RF Amplifier

                           +Vcc
                            |
                           Rc
                            |
                            +-------- C3 --------+
                            |                    |
                           Q1                    |
                        (RF Amp)                 |
                            |                    |
                           Re                    |
                            |                    |
                           GND                   |
                                                 |
                                          D1 (Diode Detector)
                                           |>
                                            |
                                            +------ Audio Signal
                                            |
                                           R3
                                            |
                                            +---- C4
                                            |      |
                                           GND    GND
                                            |
                                            |
                                        C5 (Coupling)
                                            |
                                            |
                                          Q2 (Audio Amp)
                                            |
                                           Rc2
                                            |
                                            +------ Speaker / Headphones
                                            |
                                           Re2
                                            |
                                           GND
```

---

## Stage Overview

| Stage | Function |
|------|---------|
| Antenna | Receives radio frequency signals |
| LC Tuning | Selects desired station frequency |
| RF Amplifier | Boosts weak RF signal |
| Detector | Extracts audio envelope from AM signal |
| Audio Amplifier | Amplifies recovered audio |
| Speaker | Converts signal into sound |

---

## Typical Signal Flow

```
Antenna
   ↓
LC Tuning Circuit
   ↓
RF Amplifier
   ↓
Envelope Detector
   ↓
Audio Amplifier
   ↓
Speaker
```

---

## Design Notes

- Keep RF wiring short to reduce noise and parasitic capacitance.
- Ferrite rods can improve antenna performance.
- High input impedance between stages helps prevent detuning.
- Additional filtering may be added for better audio quality.
