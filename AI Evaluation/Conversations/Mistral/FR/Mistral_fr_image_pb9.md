## Utilisateur
Voici un montage d'électronique analogique.
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.

---

## IA
Ce schéma représente un **filtre passe-bas actif du premier ordre**, basé sur un amplificateur opérationnel (AO) monté en suiveur (ou buffer). Voici comment analyser sa relation entrée-sortie :

---

### **1. Identification des composants**
- **Entrée (e)** : Signal d'entrée appliqué au circuit.
- **Résistance (R)** et **Condensateur (C)** : Formant un réseau RC, qui détermine la fréquence de coupure du filtre.
- **Amplificateur opérationnel (AO)** : Monté en suiveur (sortie directement reliée à l'entrée inverseuse). Cela signifie que la tension de sortie \( s \) est égale à la tension sur l'entrée inverseuse, et que l'impédance d'entrée est très élevée (pas de charge sur le réseau RC).

---

### **2. Fonction de transfert du réseau RC**
Le réseau RC est un **filtre passe-bas passif** du premier ordre. Sa fonction de transfert en régime harmonique (domaine de Laplace ou fréquence complexe) est donnée par :

\[
H(j\omega) = \frac{V_{C}}{e} = \frac{1}{1 + jRC\omega}
\]

où :
- \( V_C \) est la tension aux bornes du condensateur (qui est aussi la tension sur l'entrée inverseuse de l'AO).
- \( \omega = 2\pi f \) est la pulsation (en rad/s).

---

### **3. Rôle de l'amplificateur opérationnel**
L'AO est monté en **suiveur** :
- \( s = V_C \) (car \( V_+ = V_- \) et \( V_+ \) est relié à la masse via une résistance de polarisation, souvent implicite).
- L'AO ne modifie pas le signal, mais il **isole** le réseau RC de la charge en aval (impédance de sortie très faible).

---
### **4. Fonction de transfert globale**
La fonction de transfert du filtre complet (réseau RC + AO) est donc identique à celle du réseau RC seul, car l'AO ne fait que reproduire \( V_C \) en sortie :

\[
H(j\omega) = \frac{s}{e} = \frac{1}{1 + jRC\omega}
\]

---
### **5. Expression temporelle (domaine temporel)**
En régime transitoire ou pour une entrée \( e(t) \), la relation différentielle est :

\[
RC \frac{ds(t)}{dt} + s(t) = e(t)
\]

C'est l'équation différentielle d'un **filtre passe-bas du premier ordre**.

---
### **6. Fréquence de coupure**
La fréquence de coupure \( f_c \) est définie par :

\[
f_c = \frac{1}{2\pi RC}
\]

À cette fréquence, le gain est atténué de **3 dB** (soit \( \frac{1}{\sqrt{2}} \) en amplitude).

---
### **7. Comportement asymptotique**
- **Basses fréquences** (\( \omega \to 0 \)) : \( H(j\omega) \approx 1 \) → \( s \approx e \) (le signal passe sans atténuation).
- **Hautes fréquences** (\( \omega \to \infty \)) : \( H(j\omega) \approx \frac{1}{jRC\omega} \) → \(  H| \approx \frac{1}{RC\omega} \) (atténuation de 20 dB/décade).

---
### **8. Diagramme de Bode**
- **Gain** : \( 20 \log_{10}|H(j\omega)| = -10 \log_{10}(1 + (RC\omega)^2) \).
- **Phase** : \( \phi = -\arctan(RC\omega) \).

---
### **Résumé de la relation entrée-sortie**
\[
\boxed{
s(t) = e(t) - RC \frac{ds(t)}{dt}
}
\]
ou, en régime harmonique :
\[
\boxed{
\frac{s}{e} = \frac{1}{1 + jRC\omega}
}
\]

---
### **Remarque**
Si le schéma avait inclus une résistance de rétroaction (par exemple, un montage non-inverseur), la fonction de transfert aurait été différente. Ici, l'AO sert uniquement à isoler le filtre RC, sans gain supplémentaire.

---
**Question pour toi** : Souhaites-tu que je détaille un point spécifique, comme la réponse impulsionnelle ou le tracé du diagramme de Bode ?