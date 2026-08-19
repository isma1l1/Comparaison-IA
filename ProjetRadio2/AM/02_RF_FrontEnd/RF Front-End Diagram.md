## 1. RF Front-End Analogical Circuit

      Antenna Input
      ----------------------
              |
              |   <-- Signal from antenna LC circuit
              |
             --- C_RF
             --- Variable Capacitor (tuning in RF front-end, optional)
              |
             L_RF
              |   <-- Inductor in RF front-end tuning
              |
              +-----> Base of Q1
              |
             R1
              |   <-- Bias resistor for transistor
              |
             GND
              
            [Q1] NPN Transistor RF Amplifier
              |
              C2
             --- Coupling capacitor to next stage
              |
              +-----> Output to Detector (AM Demodulator)
              |
             R2
              |
             GND


---

## 2. Circuit Explanation

- **Antenna Connection:**  
  The node labeled **Antenna Input** connects to the output of the antenna LC circuit. This is where the passive tuning stage feeds the first active stage.

- **RF Front-End Tuning (C_RF + L_RF):**  
  Optionally, a small LC resonant circuit can be included in the front-end to further refine frequency selectivity. These components are **separate from the antenna’s LC (C1/L1)**.

- **Transistor (Q1):**  
  Acts as the **RF amplifier**, boosting the small voltage signal from the antenna LC circuit.

- **Biasing Resistor (R1):**  
  Provides proper operating voltage/current for the transistor to function in its linear region.

- **Coupling Capacitor (C2):**  
  Passes the amplified AC signal to the detector stage while blocking DC from the transistor circuit.

- **Output Node:**  
  Feeds directly to the AM detector/demodulator for demodulation.

---

## 3. Notes

- For a **beginner AM radio**, a single NPN transistor is sufficient for the RF Front-End.  
- The antenna LC circuit is **physically connected to the input of this stage**, but the front-end components (C_RF, L_RF) are separate.  
- Optional additions include **AGC** or **band-pass filtering** to improve selectivity and stability.  
- After this stage, the signal flows to the **Detector stage** (see Detector Design) and eventually to the Audio Amplifier.


[[RF Front End Complete Diagram]]
