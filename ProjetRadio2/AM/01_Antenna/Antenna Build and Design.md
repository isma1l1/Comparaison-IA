## 1. Target AM Frequency Range  
  
- Standard AM broadcast band: **530–1600 kHz**.  
- Center frequency for calculations: **~1000 kHz** (1 MHz).  
  
---  
  
## 2. Long Wire Antenna  
  
- Wavelength formula:

$$  
\lambda = \frac{c}{f}  
$$  
where $c = 3 \times 10^8$ m/s.  
  
- Example at 1 MHz:  
$$  
\lambda = \frac{3 \times 10^8}{1 \times 10^6} = 300 \text{ m}  
$$  
  
- Practical wire length: **1/4 wavelength → 75 m**, but for a small setup you can use **5–15 m** of insulated wire; it will still work, but efficiency is lower.  
  
---  
  
## 3. LC Resonant Circuit  
  
The antenna works with a **tuning capacitor C1** and **coil L1** to form an LC circuit resonant at the desired frequency:  
  
$$ 
f = \frac{1}{2\pi \sqrt{L C}}  
$$
  
- $f$ = desired frequency (Hz)  
- $L$ = inductance of coil (H)  
- $C$ = capacitance of variable capacitor (F)  
  
---  
  
### 3.1. Choosing the Capacitor (C1)  
  
- Use a **variable capacitor** for tuning.  
- Typical values for AM radio: **10–365 pF** (picofarads).  
- This range allows you to tune across the entire AM broadcast band when combined with a suitable coil.  
  
---  
  
### 3.2. Choosing the Coil (L1)  
  
- Coil specifications depend on wire gauge and number of turns.  
- Typical ferrite rod antenna coil for AM:  
- **Diameter of rod:** ~1–2 cm  
- **Length of rod:** ~5–10 cm  
- **Wire:** 28–32 AWG enamel-coated  
- **Turns:** 80–120 turns (single layer if possible)  
  
- You can adjust the number of turns slightly to match the full AM band with your chosen variable capacitor.  
  
---  
  
## 4. Practical Shopping List for Beginner AM Radio Antenna  
  
1. **Wire Antenna:** 5–15 m insulated copper wire  
2. **Ferrite Rod:** 1–2 cm diameter, 5–10 cm length (for compact inductor)  
3. **Enamel-Coated Wire:** 28–32 AWG for coil winding  
4. **Variable Capacitor:** 10–365 pF (tuning)  
5. **Basic Soldering Supplies:** optional for connecting wires to circuit  
6. **Breadboard / small perfboard:** optional for easy prototyping  
  
---  
  
## 5. Tuning Instructions  
  
1. Wind coil L1 around the ferrite rod.  
2. Connect variable capacitor C1 in parallel with L1.  
3. Connect antenna wire to one end of the LC circuit, other side to ground.  
4. Adjust C1 while listening for stations to find the resonance for the desired frequency.  
5. Test different coil turns or wire lengths if needed to optimize tuning range and reception.  
  
---  
  
## 6. Notes  
  
- Shorter wire lengths and fewer coil turns reduce efficiency but are fine for indoor, beginner setups.  
- The combination of L1 and C1 allows **full-band tuning**, so a single variable capacitor is sufficient.  
- After completing the antenna LC circuit, feed the signal into the RF Front-End stage for amplification (see RF Front-End Design).  
- The global system context is available in the combined Main Question + Global Diagram file.


[[Antenna Components]]
[[Antenna What to buy]]