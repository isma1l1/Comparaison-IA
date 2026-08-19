## Utilisateur
Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt) dans un montage de Pont de Graetz. Explique ton raisonnement.

## IA
Pour déterminer la tension de sortie \( v(t) \) d’un **pont de Graetz** (ou pont de diodes) alimenté par une entrée sinusoïdale \( e(t) = E_0 \sin(\omega t) \), analysons le fonctionnement du montage étape par étape.

---

## 1. **Principe du Pont de Graetz**
Le pont de Graetz est un montage redresseur **double alternance** composé de 4 diodes. Il permet de redresser une tension alternative en une tension continue pulsée, en utilisant les deux alternances (positive et négative) du signal d’entrée.

---

## 2. **Fonctionnement pour une entrée sinusoïdale**
### **[important]Alternance positive[/important] (\( e(t) > 0 \))**
- Les diodes [important]\( D_1 \) et \( D_2 \)[/important] sont **passantes** (conduction directe).
- Les diodes [important]\( D_3 \) et \( D_4 \)[/important] sont **bloquées**.
- La tension de sortie \( v(t) \) est égale à la tension d’entrée : \( [important]v(t) = e(t)[/important] = E_0 \sin(\omega t) \).

### **[important]Alternance négative[/important] (\( e(t) < 0 \))**
- Les diodes [important]\( D_3 \) et \( D_4 \) sont **passantes[/important]**.
- Les diodes [important]\( D_1 \) et \( D_2 \) sont **bloquées[/important]**.
- La tension de sortie \( v(t) \) est égale à la valeur absolue de la tension d’entrée : \( [important]v(t) =  -e(t)[/important] = -E_0 \sin(\omega t) \).

---

## 3. **Expression de \( v(t) \)**
La tension de sortie est donc la **valeur absolue** de la tension d’entrée :

\[
[important]v(t) = |E_0 \sin(\omega t)|[/important]
\]

### **Visualisation**
- Pour \( 0 \leq \omega t \leq \pi \) : \( v(t) = E_0 \sin(\omega t) \)
- Pour \( \pi \leq \omega t \leq 2\pi \) : \( v(t) = -E_0 \sin(\omega t) \)

Cela donne un signal **périodique de période \( T = \frac{2\pi}{\omega} \)**, toujours positif, avec une [important]fréquence double de celle de l’entrée.[/important]

---

## 4. **Valeur moyenne de \( v(t) \)**
La valeur moyenne \( V_{\text{moy}} \) de la tension redressée est donnée par :
\[
V_{\text{moy}} = \frac{1}{\pi} \int_{0}^{\pi} E_0 \sin(\omega t) \, d(\omega t) = \frac{2E_0}{\pi} \approx 0.637 E_0
\]

---

## 5. **Conclusion**
- **Forme d’onde** : \( v(t) = |E_0 \sin(\omega t)| \)
- **Valeur moyenne** : \( V_{\text{moy}} = \frac{2E_0}{\pi} \)
- **Fréquence** : Double de celle de l’entrée.

---

### **Remarque**
Si une charge résistive \( R \) est connectée en sortie, le courant dans la charge suit la même forme que \( v(t) \).

---
**As-tu besoin d’une simulation ou d’un schéma pour illustrer ce fonctionnement ?**