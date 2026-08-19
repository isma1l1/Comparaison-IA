## Utilisateur

Voici un montage d"électronique analogique.
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.
*(image d'un schéma de circuit électronique comprenant un amplificateur opérationnel, deux résistances R et R', et un condensateur C montés en filtre actif inverseur)*

---

## IA

Ce montage est un **filtre actif inverseur**. Voici l'analyse détaillée de son fonctionnement et de ses caractéristiques.

### 1. Identification de la nature du filtre (sans calcul)

Pour identifier le filtre, on observe le comportement des composants réactifs (le condensateur $C$) aux fréquences limites :

* **À basse fréquence ($\omega \to 0$) :** Le condensateur se comporte comme un **circuit ouvert**. Le courant ne peut pas circuler de l'entrée vers l'amplificateur opérationnel. La tension de sortie $s$ est donc nulle.
* **À haute fréquence ($\omega \to \infty$) :** Le condensateur se comporte comme un **court-circuit** (fil de résistance nulle). Le montage devient alors un amplificateur inverseur classique de gain $-\frac{R'}{R}$.

Le signal passe aux hautes fréquences et est bloqué aux basses fréquences : il s'agit d'un **filtre passe-haut du premier ordre**.

### 2. Établissement de la fonction de transfert

On utilise la notation complexe et on considère l'amplificateur opérationnel comme idéal en régime linéaire ($V_+ = V_- = 0$ par masse virtuelle).

L'impédance d'entrée $Z_e$ est la mise en série de $R$ et $C$ :
$$Z_e = R + \frac{1}{jC\omega} = \frac{1 + jRC\omega}{jC\omega}$$

L'impédance de rétroaction est simplement $Z_s = R'$. La fonction de transfert $H(j\omega)$ pour un montage inverseur est donnée par $H(j\omega) = -\frac{Z_s}{Z_e}$ :

$$H(j\omega) = -\frac{R'}{\frac{1 + jRC\omega}{jC\omega}} = -\frac{jR'C\omega}{1 + jRC\omega}$$

En divisant le numérateur et le dénominateur par $jRC\omega$, on obtient la **forme canonique** d'un passe-haut :

$$H(j\omega) = \frac{H_0}{1 - j\frac{\omega_0}{\omega}} \quad \text{ou} \quad H(j\omega) = -A \frac{j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$$

Ici, on identifie :
* Le gain maximal (en haute fréquence) : $A = \frac{R'}{R}$
* La pulsation de coupure : $\omega_0 = \frac{1}{RC}$

### 3. Détermination des valeurs de $R'$ et $C$

On nous donne les contraintes suivantes :
* $R = 1 \text{ k}\Omega = 10^3 \Omega$
* $\omega_0 = 10^4 \text{ rad.s}^{-1}$
* $G_{dB} = 20 \text{ dB}$ (Gain en haute fréquence)

#### Calcul de $C$ :
À partir de la formule de la pulsation de coupure :
$$C = \frac{1}{R \cdot \omega_0} = \frac{1}{10^3 \cdot 10^4} = 10^{-7} \text{ F}$$
Soit **$C = 100 \text{ nF}$**.

#### Calcul de $R'$ :
Le gain en décibels est donné par $G_{dB} = 20 \log(|H_{max}|)$.
$$20 = 20 \log\left(\frac{R'}{R}\right) \implies \log\left(\frac{R'}{R}\right) = 1 \implies \frac{R'}{R} = 10^1 = 10$$
D'où :
$$R' = 10 \cdot R = 10 \cdot 10^3 = 10^4 \Omega$$
Soit **$R' = 10 \text{ k}\Omega$**.

### Résumé des caractéristiques
| Paramètre | Valeur |
| :--- | :--- |
| **Type de filtre** | Passe-haut (1er ordre) |
| **Condensateur $C$** | $100 \text{ nF}$ |
| **Résistance $R'$** | $10 \text{ k}\Omega$ |
