## Utilisateur
Voici un montage d'électronique analogique.
Les deux résistances R et les deux condensateurs C sont identiques. Exprime dans le domaine fréquentiel puis temporel la relation entre la tension de sortie et les deux tensions d’entrée du montage. Explique ton raisonnement.

---

## IA
Pour analyser ce montage, identifions d'abord sa structure. Il s'agit d'un **filtre actif à rétroaction multiple (ou "Multiple Feedback Bandpass Filter")**, souvent utilisé pour réaliser des fonctions de transfert spécifiques, comme un filtre passe-bande.

---
## 1. Analyse dans le domaine fréquentiel

### Hypothèses et notations
- Les deux résistances sont identiques : \( R_1 = R_2 = R \).
- Les deux condensateurs sont identiques : \( C_1 = C_2 = C \).
- L'amplificateur opérationnel est idéal (impédance d'entrée infinie, gain infini, bande passante infinie).
- Les tensions d'entrée sont \( e_1(t) \) et \( e_2(t) \), et la tension de sortie est \( s(t) \).

---
### Équations du montage
Le montage peut être décomposé en deux parties :
1. **Entrée[[important] non-inverseuse[\important]]** : \( e_1 \) est appliquée directement à l'entrée non-inverseuse de l'AO.
2. **Entrée inverseuse** : \( e_2 \) est appliquée à l'entrée inverseuse via une résistance \( R \), et il y a une rétroaction complexe impliquant \( R \) et \( C \).

#### Nœud inverseur (nœud -)
Soit \( v^- \) la tension au nœud inverseur. Comme l'AO est idéal, \( [[important]v^- = v^+ [\important]]= e_1 \).

Le courant traversant la résistance connectée à \( e_2 \) est :
\[
i_{e2} = \frac{e_2 - v^-}{R} = \frac{e_2 - e_1}{R}
\]

Le courant traversant le condensateur \( C \) connecté à la sortie \( s \) est :
\[
i_{C1} = C \frac{d(s - v^-)}{dt} = C \frac{d(s - e_1)}{dt}
\]

Le courant traversant la résistance \( R \) connectée à la masse est :
\[
i_{R1} = \frac{v^-}{R} = \frac{e_1}{R}
\]

#### Conservation des courants au nœud inverseur
Au nœud inverseur, la somme des courants entrants est nulle (car l'impédance d'entrée de l'AO est infinie) :
\[
i_{e2} + i_{C1} + i_{R1} = 0
\]
\[
\frac{e_2 - e_1}{R} + C \frac{d(s - e_1)}{dt} + \frac{e_1}{R} = 0
\]

Simplifions :
\[
\frac{e_2 - e_1 + e_1}{R} + C \frac{ds}{dt} - C \frac{de_1}{dt} = 0
\]
\[
\frac{e_2}{R} + C \frac{ds}{dt} - C \frac{de_1}{dt} = 0
\]

#### Transformée de Laplace
En appliquant la transformée de Laplace (avec \( s \) comme variable complexe) :
\[
\frac{E_2(s)}{R} + C s S(s) - C s E_1(s) = 0
\]
\[
C s S(s) = C s E_1(s) - \frac{E_2(s)}{R}
\]
\[
S(s) = E_1(s) - \frac{E_2(s)}{R C s}
\]

---
### Fonction de transfert
La relation entre \( S(s) \), \( E_1(s) \), et \( E_2(s) \) est donc :
\[
\boxed{S(s) = E_1(s) - \frac{1}{R C s} E_2(s)}
\]

---
## 2. Passage dans le domaine temporel

En appliquant la transformée de Laplace inverse, on obtient :
\[
s(t) = e_1(t) - \frac{1}{R C} \int e_2(t) \, dt
\]

**Explication** :
- Le terme \( E_1(s) \) se traduit directement par \( e_1(t) \) dans le domaine temporel.
- Le terme \( \frac{1}{s} E_2(s) \) correspond à l'intégrale de \( e_2(t) \) dans le domaine temporel.

---
## 3. Interprétation physique
- **\( e_1(t) \)** : Contribution directe de l'entrée non-inverseuse.
- **\( \int e_2(t) \, dt \)** : L'entrée \( e_2(t) \) est intégrée (effet passe-bas) et soustraite à \( e_1(t) \), avec un facteur \( \frac{1}{R C} \).

---
## 4. Remarque sur la stabilité
Ce montage peut devenir instable si les pôles de la fonction de transfert ne sont pas correctement placés. En pratique, il est souvent utilisé comme **filtre passe-bande** ou **intégrateur** selon les valeurs de \( R \) et \( C \).

---
### Résumé final
- **Domaine fréquentiel** :
  \[
  S(s) = E_1(s) - \frac{1}{R C s} E_2(s)
  \]
- **Domaine temporel** :
  \[
  s(t) = e_1(t) - \frac{1}{R C} \int e_2(t) \, dt
  \]

---
Si tu veux approfondir un point particulier (par exemple, la réponse en fréquence ou la stabilité), n'hésite pas à demander !