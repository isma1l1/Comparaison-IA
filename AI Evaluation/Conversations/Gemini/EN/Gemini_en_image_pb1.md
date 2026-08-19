## Utilisateur

Voici un montage d'électronique analogique. 
Donne-moi la formule du gain de ce circuit en fonction de la valeur des résistances R1 et R2. Explique ton raisonnement.

## IA

Le circuit présenté sur l'image est une configuration classique d'**Amplificateur Inverseur** utilisant un amplificateur opérationnel (AOP).

### La Formule
Le gain en tension en boucle fermée ($A_v$) de ce circuit est défini par le rapport entre la résistance de rétroaction ($R_1$) et la résistance d'entrée ($R_2$) :

$$[important]A_v = \frac{V_{out}}{V_{in}} = -\frac{R_1}{R_2}[/important]$$

---

### Raisonnement et Démonstration
Pour comprendre comment cette formule est établie, nous considérons que l'AOP est **idéal**. Cela implique deux règles fondamentales :
1.  **[important]Masse Virtuelle[/important] :** L'AOP agit de manière à maintenir la différence de potentiel entre ses deux bornes d'entrée à zéro. Comme la borne non-inverseuse ($+$) est reliée à la masse (0V), la borne inverseuse ($-$) est également à **0V**. Ce point est appelé "masse virtuelle".
2.  **Impédance d'entrée infinie :** Aucun courant ne pénètre dans les bornes d'entrée de l'AOP ($I_{in} \approx 0$).

#### Analyse étape par étape

* **Courant traversant $R_2$ :**
    Puisque le côté gauche de $R_2$ est à $V_{in}$ et le côté droit est à 0V (la masse virtuelle), le courant qui la traverse est :
    $$[important]I_{in}[/important] = \frac{V_{in} - 0}{R_2} = [important]\frac{V_{in}}{R_2}[/important]$$

* **Courant traversant $R_1$ :**
    Comme aucun courant ne peut entrer dans la borne de l'AOP, la totalité de $I_{in}$ doit circuler à travers la résistance de rétroaction $R_1$ vers la sortie.
    $$[important]I_{feedback[/important]} = \frac{0 - V_{out}}{R_1} = [important]-\frac{V_{out}}{R_1}[/important]$$

* **Égalité des courants :**
    Selon la loi des nœuds appliquée au nœud inverseur :
    $$\frac{V_{in}}{R_2} = -\frac{V_{out}}{R_1}$$

* **Calcul du gain :**
    En réorganisant les termes pour trouver le rapport entre la sortie et l'entrée, on obtient :
    $$\frac{V_{out}}{V_{in}} = [important]-\frac{R_1}{R_2}[/important]$$

---

### Points clés à retenir
* **Le signe moins :** Il indique une **inversion de phase**. Si l'entrée augmente, la sortie diminue.
* **Contrôle :** Vous pouvez régler le gain pour qu'il soit inférieur, égal ou très supérieur à 1 simplement en choisissant les valeurs de résistance appropriées.
* **Impédance d'entrée :** L'impédance d'entrée de ce montage spécifique est exactement égale à **$R_2$**.