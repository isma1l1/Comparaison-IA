## Utilisateur
Voici un montage d'électronique analogique.
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.



---
## IA
Pour déterminer la relation entrée-sortie de ce filtre, analysons d'abord le schéma. Il s'agit d'un **filtre actif à rétroaction multiple (ou filtre de Sallen-Key)**. Voici les étapes pour établir la relation entrée-sortie :

---

## **1. Identification des composants et de la topologie**
- **Entrées** : \( e_1 \) et \( e_2 \) (sources de tension).
- **Sortie** : \( s \) (tension de sortie).
- **Composants passifs** : Résistances \( R \) et \( R' \).
- **Composant actif** : Amplificateur opérationnel (AO) en configuration non-inverseuse.
- **Topologie** : Le montage semble être une combinaison de **filtre passe-bas** et **filtre passe-haut** en raison de la rétroaction multiple.

---

## **2. Hypothèses de travail**
- L'AO est [important]idéal[/important] :
  - Impédance d'entrée infinie.
  - Gain en boucle ouverte infini.
  - Courant d'entrée nul (\( i^- = i^+ = 0 \)).
- Les tensions d'entrée \( e_1 \) et \( e_2 \) sont appliquées via des résistances \( R \) et \( R' \).
- La [important]rétroaction est appliquée via \( R \) et \( R' \) vers l'entrée inverseuse[/important] (\( - \)) de l'AO.

---

## **3. Équations des nœuds**

### **Nœud de l'entrée non-inverseuse (\( + \)) de l'AO**
La tension à l'entrée non-inverseuse est notée \( v^+ \). Elle est connectée à :
- \( e_1 \) via une résistance \( R \).
- \( e_2 \) via une résistance \( R \).
- La masse via une résistance \( R' \).

En utilisant le **théorème de Millman** pour calculer \( v^+ \) :
\[
[important]v^+ = \frac{\frac{e_1}{R} + \frac{e_2}{R} + \frac{0}{R'}}{\frac{1}{R} + \frac{1}{R} + \frac{1}{R'}} = \frac{\frac{e_1 + e_2}{R}}{\frac{2}{R} + \frac{1}{R'}} = \frac{(e_1 + e_2) R'}{2R' + R}[/important]
\]

---

### **Nœud de l'entrée inverseuse (\( - \)) de l'AO**
La tension à l'entrée inverseuse est notée \( v^- \). Elle est connectée à :
- La sortie \( s \) via une résistance \( R' \).
- La masse via une résistance \( R \).

En utilisant à nouveau le théorème de Millman :
\[
[important]v^- = \frac{\frac{s}{R'} + \frac{0}{R}}{\frac{1}{R'} + \frac{1}{R}} = \frac{\frac{s}{R'}}{\frac{R + R'}{R R'}} = \frac{s R}{R + R'}[/important]
\]

---
## **4. Condition de l'AO idéal**
Pour un AO idéal en régime linéaire :
\[
[important]v^+ = v^-[/important]
\]
Donc :
\[
\frac{(e_1 + e_2) R'}{2R' + R} = \frac{s R}{R + R'}
\]

---
## **5. Résolution pour \( s \)**
Isolons \( s \) :
\[
s = \frac{(e_1 + e_2) R' (R + R')}{R (2R' + R)}
\]

Simplifions l'expression :
\[
s = (e_1 + e_2) \cdot \frac{R' (R + R')}{R (2R' + R)}
\]

---
## **6. Relation entrée-sortie finale**
La relation entrée-sortie du filtre est donc :
\[
\boxed{[important]s = (e_1 + e_2) \cdot \frac{R' (R + R')}{R (2R' + R)}[/important]}
\]

---
## **7. Interprétation**
- **Comportement** : Ce montage combine les entrées \( e_1 \) et \( e_2 \) avec un gain dépendant des valeurs de \( R \) et \( R' \).
- **Cas particuliers** :
  - Si \( R = R' \), alors :
    \[
    s = (e_1 + e_2) \cdot \frac{R (R + R)}{R (2R + R)} = (e_1 + e_2) \cdot \frac{2R^2}{3R^2} = \frac{2}{3} (e_1 + e_2)
    \]
    Le gain est donc \( \frac{2}{3} \) pour chaque entrée.
  - Si \( R' \gg R \), alors \( s \approx e_1 + e_2 \) (suiveur de tension).

---
## **8. Remarque sur la fonction de transfert**
Si l'on considère que \( e_2 = 0 \) (seule \( e_1 \) est active), la relation devient :
\[
s = e_1 \cdot \frac{R' (R + R')}{R (2R' + R)}
\]
Ceci correspond à un **filtre passe-bas** du premier ordre si \( R' \) et \( R \) sont choisis pour former un réseau RC équivalent.

---
### **Conclusion**
La relation entrée-sortie est linéaire et dépend des valeurs des résistances \( R \) et \( R' \). Ce montage peut être utilisé comme **sommeur pondéré** ou comme **filtre actif** selon les valeurs des composants.

---
Si tu veux approfondir l'analyse en fréquence ou simuler ce filtre, je peux t'aider à le faire ! Veux-tu explorer un cas particulier ou une application spécifique ?
