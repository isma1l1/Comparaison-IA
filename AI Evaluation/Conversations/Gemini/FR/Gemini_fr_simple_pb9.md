## Utilisateur

On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

---

## IA

Le montage **dérivateur** est un circuit fondamental de l'électronique analogique utilisant un amplificateur opérationnel (AO). Comme son nom l'indique, il permet d'obtenir une tension de sortie proportionnelle à la **dérivée par rapport au temps** de la tension d'entrée.

Voici l'analyse détaillée pour établir la relation entre l'entrée $v_e(t)$ et la sortie $v_s(t)$.

### 1. Schéma et Hypothèses
Dans un montage dérivateur idéal :
* Le condensateur $C$ est placé en série sur l'entrée.
* La résistance $R$ est placée dans la boucle de contre-réaction (entre la sortie et l'entrée inverseuse).
* L'amplificateur opérationnel est considéré comme **idéal** et fonctionne en **régime linéaire** (grâce à la boucle de rétroaction sur la borne $-$).

**Hypothèses de l'AO idéal :**
* Les courants d'entrée sont nuls : $i_+ = i_- = 0$.
* La tension différentielle d'entrée est nulle : $\epsilon = v_+ - v_- = 0$.
* Comme la borne non-inverseuse ($+$) est reliée à la masse, on a $v_+ = 0$, d'où **$v_- = 0$** (masse virtuelle).

### 2. Raisonnement et Calcul

Le raisonnement repose sur l'application de la loi des nœuds au point $v_-$ et sur les relations constitutives des composants.

**Étape A : Courant dans le condensateur ($i_C$)**
Le courant traversant le condensateur d'entrée est lié à la variation de la tension à ses bornes ($v_e - v_-$) :
$$i_C(t) = C \frac{d(v_e(t) - v_-(t))}{dt}$$
Comme $v_- = 0$, on obtient :
$$i_C(t) = C \frac{dv_e(t)}{dt}$$

**Étape B : Courant dans la résistance ($i_R$)**
D'après la loi d'Ohm, le courant traversant la résistance de rétroaction est :
$$i_R(t) = \frac{v_-(t) - v_s(t)}{R}$$
En remplaçant $v_-$ par 0 :
$$i_R(t) = -\frac{v_s(t)}{R}$$

**Étape C : Loi des nœuds**
Au nœud $v_-$, puisque $i_- = 0$, tout le courant arrivant du condensateur repart dans la résistance :
$$i_C(t) = i_R(t)$$

En remplaçant par les expressions précédentes :
$$C \frac{dv_e(t)}{dt} = -\frac{v_s(t)}{R}$$

### 3. Relation Entrée-Sortie

En isolant $v_s(t)$, on obtient la relation finale :

> $$v_s(t) = -RC \frac{dv_e(t)}{dt}$$

### 4. Interprétation
* **Opération mathématique :** La tension de sortie est bien l'image de la dérivée de l'entrée. Le terme $RC$ (en secondes) agit comme une constante de temps de gain.
* **Signe Moins :** Le montage est inverseur ; une rampe positive en entrée produira une tension constante négative en sortie.
* **Limites réelles :** En pratique, ce montage "pur" est instable et très sensible au bruit de haute fréquence (car la dérivée d'un bruit rapide donne de grandes pointes de tension). On ajoute souvent une petite résistance en série avec le condensateur pour limiter le gain en haute fréquence.
