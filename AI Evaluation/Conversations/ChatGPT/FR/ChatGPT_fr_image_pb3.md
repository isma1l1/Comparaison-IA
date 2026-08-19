```markdown
## Utilisateur
Voici un montage d'électronique analogique.  
Donne moi de l'intensité dans la résistance R. Explique ton raisonnement.

## IA
On peut lire ton schéma comme un montage classique de régulation par diode Zener :

- À gauche : deux générateurs \(e_1\) et \(e_2\) avec résistances internes \(R_1\) et \(R_2\), reliés au même nœud.
- Au milieu : une diode Zener reliée entre le nœud et la masse.
- À droite : la résistance de charge \(R\), dans laquelle circule le courant \(I\) demandé.

---

## 1. Idée générale

Le comportement dépend de l’état de la Zener :

### 🔹 Cas 1 : Zener bloquée  
Si la tension au nœud est **inférieure à \(U_Z\)**, la Zener ne conduit pas.

→ Le circuit devient simplement deux générateurs en parallèle alimentant \(R\).

### 🔹 Cas 2 : Zener en conduction  
Si la tension atteint \(U_Z\), la Zener **fixe la tension du nœud à \(U_Z\)**.

→ Le courant en excès est absorbé par la Zener.

---

## 2. Cas 1 : Zener bloquée

On remplace les deux branches de gauche par leur équivalent de Thévenin :

### Tension équivalente :
\[
V_{th} = \frac{e_1/R_1 + e_2/R_2}{1/R_1 + 1/R_2}
\]

### Résistance équivalente :
\[
R_{th} = \frac{R_1 R_2}{R_1 + R_2}
\]

Le courant dans \(R\) vaut alors :
\[
I = \frac{V_{th}}{R_{th} + R}
\]

👉 Mais ce résultat n’est valable que si :
\[
V_{th} < U_Z
\]

---

## 3. Cas 2 : Zener en régime

Si la Zener conduit, elle impose :
\[
V = U_Z
\]

Donc directement :

\[
I = \frac{U_Z}{R}
\]

---

## 4. Condition de validité

Il faut vérifier que les sources peuvent fournir assez de courant :

Courant total fourni par les sources :
\[
I_{sources} = \frac{e_1 - U_Z}{R_1} + \frac{e_2 - U_Z}{R_2}
\]

Courant dans la charge :
\[
I_R = \frac{U_Z}{R}
\]

Courant dans la Zener :
\[
I_Z = I_{sources} - I_R
\]

👉 Pour que la Zener soit bien en conduction :
\[
I_Z > 0
\]

---

## 5. Résultat final (résumé)

- Si \(V_{th} < U_Z\) :
\[
I = \frac{V_{th}}{R_{th} + R}
\]

- Si \(V_{th} \ge U_Z\) :
\[
I = \frac{U_Z}{R}
\]

---

Si tu veux, je peux refaire le calcul avec des valeurs numériques ou te tracer les courbes pour bien visualiser le point de fonctionnement 👍
```
