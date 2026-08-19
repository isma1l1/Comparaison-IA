## Utilisateur
On étudie un montage filtre actif amplificateur classique (la borne + de l'ALI est reliée à la terre et la borne - est reliée à la sortie de l'ALI par une résistance R' et à l'entrée par un condensateur C et une résistance R).
Identifie sans calcul la nature de ce filtre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

---
## IA
### 1. **Identification de la nature du filtre**

Le montage décrit est un **filtre actif passe-bas du premier ordre**.
- **Explication** :
  - La borne **+** de l'ALI est reliée à la masse (0 V).
  - La borne **–** est reliée à la sortie par une résistance \( R' \) et à l'entrée par un condensateur \( C \) en série avec une résistance \( R \).
  - Ce montage correspond à un **amplificateur inverseur avec un filtre passe-bas RC** en entrée.
  - En haute fréquence, le condensateur \( C \) se comporte comme un court-circuit, et le gain est déterminé par le rapport des résistances \( R' \) et \( R \).
  - En basse fréquence, le condensateur se comporte comme un circuit ouvert, et le signal d'entrée est atténué.

---

### 2. **Fonction de transfert sous forme canonique**

La fonction de transfert \( H(j\omega) \) d'un filtre passe-bas du premier ordre est de la forme :
\[
H(j\omega) = \frac{H_0}{1 + j\frac{\omega}{\omega_0}}
\]
où :
- \( H_0 \) est le **gain statique** (gain en basse fréquence).
- \( \omega_0 = \frac{1}{RC} \) est la **pulsation de coupure**.

Dans ce montage, l'ALI est en configuration inverseuse, donc le gain en haute fréquence (quand \( \omega \to \infty \)) est donné par :
\[
H_{\infty} = -\frac{R'}{R}
\]
La fonction de transfert complète est donc :
\[
H(j\omega) = -\frac{R'}{R} \cdot \frac{1}{1 + jRC\omega}
\]
On peut la réécrire sous forme canonique en identifiant \( \omega_0 = \frac{1}{RC} \) :
\[
H(j\omega) = -\frac{R'}{R} \cdot \frac{1}{1 + j\frac{\omega}{\omega_0}}
\]

---

### 3. **Détermination de \( R' \) et \( C \)**

#### **Données :**
- \( R = 1\,\text{k}\Omega = 1000\,\Omega \)
- \( \omega_0 = 10^4\,\text{rad/s} \)
- Gain en haute fréquence : \( 20\,\text{dB} \)

#### **Étape 1 : Calcul du gain en haute fréquence**
Le gain en haute fréquence en décibels est donné par :
\[
20\,\text{dB} = 20 \log_{10} \left( \left  -\frac{R'}{R} \right| \right)
\]
\[
20 = 20 \log_{10} \left( \frac{R'}{R} \right)
\]
\[
1 = \log_{10} \left( \frac{R'}{R} \right)
\]
\[
\frac{R'}{R} = 10^1 = 10
\]
\[
R' = 10 \times R = 10 \times 1000 = 10\,000\,\Omega = 10\,\text{k}\Omega
\]

#### **Étape 2 : Calcul de \( C \)**
La pulsation de coupure est donnée par :
\[
\omega_0 = \frac{1}{RC}
\]
\[
10^4 = \frac{1}{1000 \times C}
\]
\[
C = \frac{1}{1000 \times 10^4} = \frac{1}{10^7} = 10^{-7}\,\text{F} = 0.1\,\mu\text{F}
\]

---
### **Résumé des résultats**
- **Nature du filtre** : Passe-bas du premier ordre.
- **Fonction de transfert** :
  \[
  H(j\omega) = -10 \cdot \frac{1}{1 + j\frac{\omega}{10^4}}
  \]
- **Valeurs des composants** :
  - \( R' = 10\,\text{k}\Omega \)
  - \( C = 0.1\,\mu\text{F} \)

---
Si tu veux approfondir un point ou vérifier un calcul, n'hésite pas à demander !