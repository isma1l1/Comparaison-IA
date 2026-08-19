

This file gives **simple, concrete recommendations** for buying a ready-made antenna for an AM radio project. The goal is: **cheap, simple, effective, and easy to integrate**.

---

## 🎯 Recommended Choice (Best for Beginner)

### 👉 Tunable AM Loop Antenna

**Example:**  
- https://www.tecsunradios.com.au/store/product/tecsun-an100-am-loop-antenna/

### Specs:
- Frequency range: **~500–1700 kHz (full AM band)**  
- Type: **Passive loop antenna (no power required)**  
- Built-in components:
  - Coil (inductor)
  - Variable capacitor (tuning knob)

### Why this is the best choice:
- Already includes **LC tuning** → no need to build C1 + L1  
- Very good **signal strength and selectivity**  
- Easy to use: just turn the knob to tune stations  
- Works directly with your RF front-end  

---

## 💸 Cheaper Alternative

### 👉 Basic AM Loop Antenna (2-wire)

**Example:**  
- https://www.amazon.fr/dp/B07F2Y6QK1

### Specs:
- Frequency: **~500–1600 kHz**  
- Output: **2-wire connection**  
- No tuning (or very limited)

### Pros:
- Very cheap (~10€)  
- Plug-and-play  

### Cons:
- Less selective (you rely more on your RF front-end)

---

## 📦 Compact Alternative

### 👉 Mini Loop Antenna (Portable)

**Example:**  
- https://www.banggood.com/Mini-Loop-Antenna-MW-SW-p-XXXXX.html

### Specs:
- Frequency: **AM/MW band**  
- Size: small (~10–15 cm loop)  
- Passive  

### Pros:
- Compact  
- Works indoors  

### Cons:
- Lower performance than larger loops  

---

## 🔌 How to Connect It

- The antenna output connects to your circuit **exactly where the antenna LC output was**  
- If the antenna has **2 wires**:
  - One → RF front-end input (C_in)  
  - One → Ground  

---

## 🧠 Important Insight

- AM antennas are **resonant systems (L + C)**  
- A **tunable loop antenna already includes this**, so:
  - You **do NOT need to build your own LC circuit**
  - Your RF front-end simply **amplifies the selected signal**

---

## 🎯 Final Recommendation

- If you want **simple and reliable** → buy a **tunable loop antenna**  
- If you want **very cheap** → buy a **basic loop antenna**  

Avoid:
- Telescopic antennas (bad for AM)
- FM antennas (wrong frequency range)

---

## 🔄 Integration in Your Project

- Replaces: your DIY antenna + LC tuning  
- Keeps: your RF Front-End unchanged  
- Next step: connect to RF amplifier, then detector  

---