## Utilisateur
Voici un montage d'électronique analogique. 
On étudie Uc(t) en fonction de E(t). Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

## IA
On reconnaît un circuit **R–L–C en série** avec la sortie prise aux bornes du condensateur \(C\). On cherche donc \(H(j\omega)=\dfrac{U_C}{E}\).

---

## 1) Nature du filtre

- À basse fréquence (\(\omega \to 0\)) :  
  \(Z_C \to \infty\) ⇒ toute la tension est sur \(C\) ⇒ \(U_C \approx E\)

- À haute fréquence (\(\omega \to \infty\)) :  
  \(Z_C \to 0\) ⇒ \(U_C \approx 0\)

Le circuit laisse passer les basses fréquences et atténue les hautes :

**[important] Filtre passe-bas du 2ᵉ ordre[/important]**

---

## 2) Fonction de transfert

Impédances :
\[
[important]Z_R = R,\quad Z_L = j\omega L,\quad Z_C = \frac{1}{j\omega C}[/important]
\]

Circuit série ⇒
\[
Z_{\text{total}} = R + j\omega L + \frac{1}{j\omega C}
\]

Diviseur de tension :
\[
[important](j\omega)=\frac{Z_C}{Z_{\text{total}}}[/important]
\]

On obtient après simplification :

\[
H(j\omega)=[important]\frac{1}{1 - \omega^2 LC + j\omega RC}[/important]
\]

---

## 3) Mise sous forme canonique

On pose :
\[
[important]\omega_0 = \frac{1}{\sqrt{LC}}, \quad Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]
\]

Alors :
\[
H(j\omega)=[important]\frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j\frac{\omega}{\omega_0 Q}}[/important]
\]

---

## 4) Bande passante

Pour un filtre du 2ᵉ ordre :

\[
[Important]\Delta \omega = \omega_2 - \omega_1 = \frac{\omega_0}{Q}[/important]
\]

Donc :

\[
\Delta \omega = [important]\frac{R}{L}[/important]
\]

**Largeur de bande :**
\[
\boxed{\Delta \omega = \frac{R}{L}}
\]

---

## 5) Diagramme de Bode (gain)

Module :
\[
|H(j\omega)| = \frac{1}{\sqrt{(1-\omega^2LC)^2 + (\omega RC)^2}}
\]

### Comportement :

- **[Important]Basses fréquences** :  
  \(|H| \approx 1\) ⇒ 0 dB[/important]

- **[important]Autour de \(\omega_0\)** :  
  Pic possible si \(Q > \frac{1}{\sqrt{2}}\)[/important]

- **[important]Hautes fréquences** :  
  \(|H| \sim \frac{1}{\omega^2}\) ⇒ pente = **–40 dB/décade[/important]**

---

## 6) Diagramme de phase

\[
\varphi(\omega) = -\arctan\left(\frac{\omega RC}{1 - \omega^2 LC}\right)
\]

### Évolution :
[important]
- \(\omega \to 0\) : \(0^\circ\)
- \(\omega = \omega_0\) : \(-90^\circ\)
- \(\omega \to \infty\) : \(-180^\circ\)
[/important]
---

## 7) Résumé

- **Type** : filtre passe-bas du 2ᵉ ordre  
- **Fréquence propre** : \(\omega_0 = \frac{1}{\sqrt{LC}}\)  
- **Facteur de qualité** : \(Q = \frac{1}{R}\sqrt{\frac{L}{C}}\)  
- **Bande passante** : \(\Delta \omega = \frac{R}{L}\)  
- **Pente HF** : –40 dB/décade  

---

Si tu veux, je peux te tracer les Bode (gain + phase) avec des valeurs numériques pour mieux visualiser 