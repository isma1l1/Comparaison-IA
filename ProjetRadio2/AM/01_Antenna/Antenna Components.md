
This file gives **practical buying guidance** for building or using antennas for a beginner AM radio. It covers both DIY parts and ready-made antenna options suitable for the standard AM broadcast band (530–1600 kHz).

---

## 1. DIY Antenna Components

### 1.1. Wire Antenna
- **Type:** Insulated copper wire  
- **Length:** 5–15 meters (longer if space allows; 1/4 wavelength ~75 m ideal)  
- **Purpose:** Captures the AM signal efficiently. Longer wire → stronger signal.

### 1.2. Coil (Inductor L1)
- **Core:** Ferrite rod  
  - Diameter: 1–2 cm  
  - Length: 5–10 cm  
- **Wire:** Enamel-coated copper, 28–32 AWG  
- **Turns:** ~80–120 (single-layer preferred)  
- **Purpose:** Forms the LC circuit for tuning AM frequencies.

### 1.3. Variable Capacitor (C1)
- **Type:** Variable capacitor  
- **Range:** 10–365 pF  
- **Purpose:** Tunes the LC circuit to resonate across AM band.

### 1.4. Extras
- Connector wires, breadboard/perfboard, soldering supplies for permanent assembly.

---

## 2. Ready-Made Antenna Options

If you want to **skip DIY winding**, you can use prebuilt antennas:

1. **AM Loop Antennas (Ferrite Rod Type)**
   - Compact, directional, with built-in coil.  
   - Typically tuned by an external variable capacitor in your circuit.  
   - Example: Standard hobby ferrite rod antenna ~1–2 cm diameter, 7–10 cm long.

2. **Commercial Long Wire Kits**
   - Pre-cut insulated copper wire for AM reception.  
   - Often includes connectors for easy attachment to breadboard or RF input.  

3. **AM/MW Portable Radio Antennas**
   - Salvage antennas from old portable radios (ferrite rod or telescopic).  
   - Can be connected directly to your LC tuning circuit.  

4. **Pre-Wound Coil Kits**
   - Coil wound on a ferrite rod with specified number of turns.  
   - Matches well with a 10–365 pF variable capacitor for full AM coverage.

---

## 3. Shopping Guidelines

- **Electronics hobby stores** or online marketplaces carry ferrite rods, variable capacitors, enamel wire, and pre-wound antenna kits.  
- For beginners, ready-made ferrite rod antennas or pre-cut long wire kits save time and reduce construction errors.  
- Ensure the coil’s inductance and capacitor range match the target AM band.

---

## 4. Notes

- DIY antennas give more learning experience but require experimentation with wire length, coil turns, and tuning.  
- Ready-made antennas provide convenience and consistent results; ideal if your goal is **to quickly receive AM stations**.  
- Connect your chosen antenna (DIY or pre-built) to the RF Front-End (see RF Front-End Design) to continue the AM radio project.  
- Global system overview and signal flow are in the Main Question + Global Diagram file.