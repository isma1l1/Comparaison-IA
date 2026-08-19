This is a **single, pastable Markdown block** for Obsidian, representing a **dedicated antenna analogical diagram**. It is separate from "Antenna Basics" and focuses purely on the electrical circuit aspect of the antenna stage.  
  
---  
  
## Antenna Analogical Circuit Diagram

    ~~~~~~ Antenna Wire ~~~~~~
    --------------------------
              |
              |
             --- C1
             ---  Variable Capacitor (Tuning)
              |
              L1
              |
              +------------------> [[02_RF_FrontEnd/RF Front-End Design]]
              |
             GND


---

## Explanation

- `~~~~~~ Antenna Wire ~~~~~~` – captures AM electromagnetic waves.  
- `C1` (Variable Capacitor) and `L1` (Inductor) form a **resonant LC circuit** for tuning the desired frequency.  
- Output node (`+`) feeds the **RF Front-End** for amplification.  
- `GND` represents the common circuit ground.  

---

## Notes

- This diagram shows the **electrical behavior** of the antenna stage, separate from the general explanation in "Antenna Basics".  
- Adjusting `C1` tunes the radio to different stations; adjusting `L1` changes resonance and sensitivity.  
- This is the standard starting circuit for a **crystal or beginner AM radio**.

---

## Links

- Next stage in the signal flow: [02_RF_FrontEnd/RF Front-End Design]  
- Global system view: [[AM Radio Architecture]] 
- The build and desi: [[Antenna Build and Design]]