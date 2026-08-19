---  
  
## AM Radio General Architecture  
  
An AM (Amplitude Modulation) radio receives amplitude-modulated signals, extracts the audio, and plays it through a speaker or headphones. The system is divided into clear functional blocks:  
  
1. **Antenna** – Captures electromagnetic waves from the air and converts them to a small AC voltage.  
2. **RF Front-End (Tuning & Amplification)** – Selects the desired frequency and amplifies the weak RF signal.  
3. **AM Detector / Demodulator** – Extracts audio from the modulated carrier (usually an envelope detector).  
4. **Audio Amplifier** – Boosts the demodulated audio to drive speakers or headphones.  
5. **Output (Speaker / Headphones)** – Converts electrical signals into sound.  
6. **Optional Blocks** – AGC (Automatic Gain Control) and Filters improve volume stability and reduce noise.  
  
---  
  
## Clickable AM Radio System Diagram


	  
	  +----------------------+
      | [01_Antenna/Antenna Basics.md] |
      |      Antenna         |
      +----------------------+
                 |
                 v
      +----------------------------+
      | [02_RF_FrontEnd/RF Front-End Design.md] |
      |       RF Front-End          |
      +----------------------------+
                 |
                 v
      +----------------------------+
      | Optional: [06_Optional_Parts/AGC.md] |
      |        AGC (Gain Control)          |
      +----------------------------+
                 |
                 v
      +----------------------------+
      | [03_Detector/Envelope Detector Design.md] |
      |        Detector             |
      +----------------------------+
                 |
                 v
      +----------------------------+
      | Optional: [06_Optional_Parts/Filters.md] |
      |          Filters           |
      +----------------------------+
                 |
                 v
      +-------------------------------+
      | [04_Audio_Amplifier/Simple Audio Amplifier Circuits.md] |
      |       Audio Amplifier         |
      +-------------------------------+
                 |
                 v
      +---------------------------+
      | [05_Output/Speakers and Headphones.md] |
      |          Output           |
      +---------------------------+

---


## Diagram Explanation

- Main signal path: **Antenna → RF Front-End → Detector → Audio Amplifier → Output**.  
- Optional blocks:  
  - **AGC** after RF Front-End, before Detector.  
  - **Filters** after Detector, before Audio Amplifier.  
- Each box corresponds to a **folder/file** in Obsidian. Clicking a link opens that file.  

## Flow Summary (with clickable links)

1. **Signal Reception:** [[Antenna Basics]]  
2. **Frequency Selection & Amplification:** [[RF Front-End Basics]]  
3. **Optional Gain Control:** [[AGC]]  
4. **Demodulation:** [[Envelope Detector Basics]]  
5. **Optional Filtering:** [[Filters]]  
6. **Audio Amplification:** [[Audio Amplifier Basics]]  
7. **Sound Output:** [[Speakers and Headphones]]  

## Notes for Obsidian

- Paste this Markdown directly into `AM Radio Global Diagram.md`.  
- Clickable links open the corresponding file in your vault.  
- Each functional block file should link back to this diagram for context.  
- Optional blocks (AGC, Filters) can be included or skipped; the diagram remains valid.