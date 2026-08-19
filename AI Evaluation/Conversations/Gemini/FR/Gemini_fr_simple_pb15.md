## Utilisateur
On étudie un montage filtre actif amplificateur classique (la borne + de l'ALI est reliée à la terre et la borne - est reliée à la sortie de l'ALI par une résistance R' et à l'entrée par un condensateur C et une résistance R).
Identifie sans calcul la nature de ce filtre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

## IA
C'est un grand classique de l'électronique analogique ! Ce montage correspond à un **amplificateur inverseur** où l'impédance d'entrée et l'impédance de rétroaction ont été modifiées pour filtrer le signal.

Voici l'analyse détaillée de ton circuit.

---

### 1. Identification de la nature du filtre (sans calcul)

Pour déterminer la nature du filtre, on observe le comportement des composants aux fréquences limites :

* **En basse fréquence ($\omega \to 0$) :** Le condensateur $C$ se comporte comme un **interrupteur ouvert**. Le courant ne peut plus circuler depuis l'entrée vers l'inverseuse. La tension de sortie est donc nulle.
* **En haute fréquence ($\omega \to \infty$) :** Le condensateur $C$ se comporte comme un **fil court-circuit**. Le montage devient alors un amplificateur inverseur classique de gain $G = -R'/R$. Le signal passe.

**Conclusion :** Puisque le signal est bloqué en basse fréquence et amplifié en haute fréquence, il s'agit d'un **filtre passe-haut du premier ordre**.

---

### 2. Établissement de la fonction de transfert

On utilise la formule du gain d'un amplificateur inverseur : $\underline{H} = -\frac{\underline{Z}_2}{\underline{Z}_1}$
* $\underline{Z}_2 = R'$ (impédance de la boucle de retour)
* $\underline{Z}_1 = R + \frac{1}{jC\omega}$ (impédance de la branche d'entrée)

En développant, on obtient :
$$\underline{H}(j\omega) = \frac{-R'}{R + \frac{1}{jC\omega}} = \frac{-jR'C\omega}{1 + jRC\omega}$$

Pour la mettre sous **forme canonique** d'un passe-haut ($H = \frac{H_\infty \cdot j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$), on factorise par $RC\omega$ au numérateur :
$$\underline{H}(j\omega) = -\frac{R'}{R} \cdot \frac{jRC\omega}{1 + jRC\omega}$$

D'où les paramètres caractéristiques :
* **Pulsation de coupure :** $\omega_0 = \frac{1}{RC}$
* **Gain asymptotique (HF) :** $H_\infty = -\frac{R'}{R}$

---

### 3. Détermination des valeurs de $R'$ et $C$

On nous donne $R = 1 \text{ k}\Omega$.

#### Calcul de $C$ (via la pulsation de coupure)
On utilise la relation $\omega_0 = \frac{1}{RC}$ :
$$C = \frac{1}{R \cdot \omega_0} = \frac{1}{10^3 \cdot 10^4} = 10^{-7} \text{ F}$$
Soit **$C = 100 \text{ nF}$**.

#### Calcul de $R'$ (via le gain en haute fréquence)
Le gain en décibels est donné par $G_{dB} = 20 \log |H_\infty|$. On veut $20 \text{ dB}$, ce qui correspond à un rapport de 10 en valeur absolue :
$$|H_\infty| = \frac{R'}{R} = 10$$
$$R' = 10 \cdot R = 10 \cdot 10^3 = 10^4 \Omega$$
Soit **$R' = 10 \text{ k}\Omega$**.

---

### Résumé des caractéristiques :
| Paramètre | Valeur |
| :--- | :--- |
| **Type** | Passe-haut 1er ordre |
| **Résistance $R'$** | $10 \text{ k}\Omega$ |
| **Condensateur $C$** | $100 \text{ nF}$ |
| **Gain HF** | $-10$ (soit $20 \text{ dB}$) |
