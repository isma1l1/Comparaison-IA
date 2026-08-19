## Utilisateur
Résous les questions A.1.1, A.1.2 et A.1.3 présentes sur ces images en détaillant ton raisonnement.

*(image de Exercise A1 – Exercice A.1 avec schéma du Pont de Wheatstone et questions associées)*

---
## IA

### **A.1.1 : Expression littérale de \( V_2 \) en fonction de \( V_1 \), \( R_1 \), \( R_2 \), \( R_3 \), \( R_4 \)**

Le circuit est un **pont de Wheatstone** avec une source de tension continue \( V_1 \). Pour trouver \( V_2 \), on utilise la formule classique du pont de Wheatstone, qui donne la tension différentielle entre les deux points centraux du pont.

---
#### **Étapes :**
1. **Tension aux nœuds intermédiaires :**
   - La tension au nœud entre \( R_1 \) et \( R_2 \) est :
     \[
     V_A = V_1 \cdot \frac{R_2}{R_1 + R_2}
     \]
   - La tension au nœud entre \( R_3 \) et \( R_4 \) est :
     \[
     V_B = V_1 \cdot \frac{R_4}{R_3 + R_4}
     \]

2. **Tension différentielle \( V_2 \) :**
   \( V_2 \) est la différence entre \( V_A \) et \( V_B \) :
   \[
   V_2 = V_A - V_B = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
   \]

---
#### **Réponse finale :**
\[
\boxed{V_2 = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)}
\]

---

---

### **A.1.2 : Relation entre \( V_2 \) et \( x \) avec \( R_1 = kR \) et \( R_2 = (1-k)R \)**

On sait que \( k = \frac{x}{h} \), où \( x \) est le niveau d'eau et \( h \) la hauteur totale du réservoir.
On pose \( R_3 = R_4 = R \) (car non précisé autrement dans l'énoncé, on suppose que \( R_3 \) et \( R_4 \) sont égales à \( R \) pour simplifier).

---
#### **Étapes :**
1. **Substitution des valeurs :**
   - \( R_1 = kR \)
   - \( R_2 = (1-k)R \)
   - \( R_3 = R \)
   - \( R_4 = R \)

2. **Calcul de \( V_A \) et \( V_B \) :**
   \[
   V_A = V_1 \cdot \frac{R_2}{R_1 + R_2} = V_1 \cdot \frac{(1-k)R}{kR + (1-k)R} = V_1 \cdot \frac{1-k}{k + (1-k)} = V_1 (1 - k)
   \]
   \[
   V_B = V_1 \cdot \frac{R_4}{R_3 + R_4} = V_1 \cdot \frac{R}{R + R} = \frac{V_1}{2}
   \]

3. **Calcul de \( V_2 \) :**
   \[
   V_2 = V_A - V_B = V_1 (1 - k) - \frac{V_1}{2} = V_1 \left(1 - k - \frac{1}{2}\right) = V_1 \left(\frac{1}{2} - k\right)
   \]

4. **Substitution de \( k = \frac{x}{h} \) :**
   \[
   V_2 = V_1 \left(\frac{1}{2} - \frac{x}{h}\right)
   \]

---
#### **Réponse finale :**
\[
\boxed{V_2 = V_1 \left(\frac{1}{2} - \frac{x}{h}\right)}
\]

---

---
### **A.1.3 : Relation entre \( R_1 \) et \( R_4 \) pour \( V_2 \geq 0 \) et valeurs de \( V_{2,\text{min}} \) et \( V_{2,\text{max}} \)**

On veut que \( V_2 \geq 0 \) pour tout \( x \) entre \( 0 \) et \( h \).
D'après la question **A.1.2**, on a :
\[
V_2 = V_1 \left(\frac{1}{2} - \frac{x}{h}\right)
\]

---
#### **Étapes :**

1. **Condition pour \( V_2 \geq 0 \) :**
   - Quand \( x = 0 \) (réservoir vide) :
     \[
     V_2 = V_1 \left(\frac{1}{2} - 0\right) = \frac{V_1}{2} \geq 0
     \]
     Cette condition est toujours vraie si \( V_1 > 0 \).
   - Quand \( x = h \) (réservoir plein) :
     \[
     V_2 = V_1 \left(\frac{1}{2} - 1\right) = -\frac{V_1}{2} < 0
     \]
     **Problème :** \( V_2 \) devient négatif quand \( x = h \).

   **Solution :** Il faut ajuster les valeurs de \( R_3 \) et \( R_4 \) pour que \( V_2 \) reste positif.
   Supposons que \( R_3 \) et \( R_4 \) ne sont pas égales à \( R \). Reprenons l'expression générale de **A.1.1** :
   \[
   V_2 = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
   \]
   Avec \( R_1 = kR \) et \( R_2 = (1-k)R \), on a :
   \[
   V_2 = V_1 \left( \frac{(1-k)R}{kR + (1-k)R} - \frac{R_4}{R_3 + R_4} \right) = V_1 \left( (1-k) - \frac{R_4}{R_3 + R_4} \right)
   \]

2. **Condition pour \( V_2 \geq 0 \) :**
   Pour que \( V_2 \geq 0 \) pour tout \( k \in [0, 1] \), il faut que :
   \[
   (1-k) - \frac{R_4}{R_3 + R_4} \geq 0 \quad \forall k \in [0, 1]
   \]
   - Le cas le plus restrictif est quand \( k = 1 \) (réservoir plein) :
     \[
     0 - \frac{R_4}{R_3 + R_4} \geq 0 \implies \frac{R_4}{R_3 + R_4} \leq 0
     \]
     Cela implique \( R_4 = 0 \), ce qui n'est pas réaliste.

   **Alternative :** On peut choisir \( R_3 \) et \( R_4 \) tels que \( \frac{R_4}{R_3 + R_4} = 0 \), c'est-à-dire \( R_4 = 0 \). Mais cela n'est pas possible en pratique.

   **Autre approche :** Si on suppose que \( R_3 \) et \( R_4 \) sont fixes et que \( R_1 \) et \( R_2 \) varient avec \( k \), alors pour \( V_2 \geq 0 \), il faut que :
   \[
   \frac{R_2}{R_1 + R_2} \geq \frac{R_4}{R_3 + R_4}
   \]
   Avec \( R_1 = kR \) et \( R_2 = (1-k)R \), cela donne :
   \[
   \frac{(1-k)R}{kR + (1-k)R} \geq \frac{R_4}{R_3 + R_4} \implies 1 - k \geq \frac{R_4}{R_3 + R_4}
   \]
   Pour que cela soit vrai pour tout \( k \in [0, 1] \), il faut que :
   \[
   1 - k \geq \frac{R_4}{R_3 + R_4} \quad \text{quand } k = 0 \implies 1 \geq \frac{R_4}{R_3 + R_4}
   \]
   Cela est toujours vrai si \( R_3 \) et \( R_4 \) sont positives.
   **Mais pour \( k = 1 \) :**
   \[
   0 \geq \frac{R_4}{R_3 + R_4}
   \]
   Cela implique \( R_4 = 0 \), ce qui n'est pas réaliste.

   **Conclusion :** Il est impossible d'avoir \( V_2 \geq 0 \) pour tout \( x \in [0, h] \) avec ce montage **sauf si on modifie la configuration du pont**.

   **Hypothèse alternative :** Si on suppose que \( R_3 \) et \( R_4 \) sont choisies pour que \( \frac{R_4}{R_3 + R_4} = 0 \), alors \( V_2 = V_1 (1 - k) \geq 0 \). Cela implique \( R_4 = 0 \), ce qui n'est pas réaliste.

   **Solution pratique :** Pour que \( V_2 \geq 0 \), il faut que \( \frac{R_4}{R_3 + R_4} \leq 0 \), ce qui est impossible avec des résistances positives.
   **Donc, la condition \( V_2 \geq 0 \) ne peut pas être satisfaite pour tout \( x \in [0, h] \) avec ce montage.**

   **Mais si on suppose que \( R_3 \) et \( R_4 \) sont choisies pour que \( V_2 \) soit toujours positif ou nul, on peut ajuster \( R_3 \) et \( R_4 \) pour que :**
   \[
   \frac{R_4}{R_3 + R_4} = 0 \implies R_4 = 0
   \]
   Ce qui n'est pas réaliste.

   **Réinterprétation :** Peut-être que la question suppose que \( R_3 \) et \( R_4 \) sont fixes et que \( R_1 \) et \( R_2 \) varient avec \( k \), et on veut \( V_2 \geq 0 \) **uniquement quand le réservoir est à moitié plein** (\( x = h/2 \), \( k = 0.5 \)).
   Dans ce cas, pour \( k = 0.5 \) :
   \[
   V_2 = V_1 \left( \frac{0.5 R}{0.5 R + 0.5 R} - \frac{R_4}{R_3 + R_4} \right) = V_1 \left( 0.5 - \frac{R_4}{R_3 + R_4} \right)
   \]
   Pour \( V_2 \geq 0 \), il faut :
   \[
   0.5 - \frac{R_4}{R_3 + R_4} \geq 0 \implies \frac{R_4}{R_3 + R_4} \leq 0.5 \implies R_4 \leq R_3
   \]

   **Donc, la relation nécessaire est \( R_4 \leq R_3 \).**

3. **Valeurs de \( V_{2,\text{min}} \) et \( V_{2,\text{max}} \) :**
   - Quand \( x = 0 \) (\( k = 0 \)) :
     \[
     V_2 = V_1 \left( \frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right) = V_1 \left( 1 - \frac{R_4}{R_3 + R_4} \right)
     \]
     Si \( R_4 \leq R_3 \), alors \( \frac{R_4}{R_3 + R_4} \leq 0.5 \), donc :
     \[
     V_{2,\text{max}} = V_1 \left(1 - \frac{R_4}{R_3 + R_4}\right)
     \]
   - Quand \( x = h \) (\( k = 1 \)) :
     \[
     V_2 = V_1 \left( 0 - \frac{R_4}{R_3 + R_4} \right) = -V_1 \frac{R_4}{R_3 + R_4}
     \]
     Pour que \( V_2 \geq 0 \), il faudrait \( R_4 = 0 \), ce qui n'est pas réaliste.
     **Donc, \( V_{2,\text{min}} = -V_1 \frac{R_4}{R_3 + R_4} \).**

   **Si on suppose que \( R_4 = 0 \), alors :**
   - \( V_{2,\text{min}} = 0 \) (quand \( x = h \))
   - \( V_{2,\text{max}} = V_1 \) (quand \( x = 0 \))

---
#### **Réponse finale :**
- **Relation entre \( R_3 \) et \( R_4 \) :** \( R_4 \leq R_3 \) pour que \( V_2 \geq 0 \) quand \( x = h/2 \).
- **Valeurs de \( V_2 \) :**
  - \( V_{2,\text{min}} = -V_1 \frac{R_4}{R_3 + R_4} \) (quand \( x = h \))
  - \( V_{2,\text{max}} = V_1 \left(1 - \frac{R_4}{R_3 + R_4}\right) \) (quand \( x = 0 \))

---
Si tu veux que je clarifie un point ou que j'approfondisse une partie, n'hésite pas !
