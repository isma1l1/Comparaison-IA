## Utilisateur

Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA

C'est un classique de l'électronique ! Le montage non-inverseur est particulièrement apprécié car il présente une impédance d'entrée très élevée, ce qui évite de "charger" le signal source.

Voici la formule et le cheminement pour y arriver.

---

### La Formule du Gain

Pour un montage amplificateur non-inverseur, le gain en tension ($A_v$) est donné par :

$$[important]A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}[/important]$$

* **$V_{in}$** est appliqué sur l'entrée non-inverseuse (+).
* **$R_2$** est la résistance de contre-réaction (entre la sortie et l'entrée -).
* **$R_1$** est la résistance reliée à la masse.

---

### Le Raisonnement (Pas à pas)

Pour comprendre d'où vient cette formule, on s'appuie sur les deux hypothèses de l'**amplificateur opérationnel idéal** en [important]régime linéaire[/important] :

1. **L'équilibre des potentiels :** $[important]V_+ = V_-[/important]$(le gain infini tend à annuler la différence de tension entre les entrées).
2. **Courants d'entrée nuls :** Aucun courant ne rentre dans les bornes (+) ou (-).

#### 1. Analyse du potentiel en $V_+$

Le signal d'entrée est branché directement sur la borne (+), donc :


$$[important]V_+ = V_{in}[/important]$$

#### 2. Analyse du potentiel en $V_-$

Le réseau de résistances $R_1$ et $R_2$ forme un **pont diviseur de tension** entre la sortie ($V_{out}$) et la masse ($0V$). Puisque aucun courant n'entre dans la borne (-), on peut écrire :


$$[important]V_- = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]$$

#### 3. Égalité et simplification

En appliquant la règle $V_+ = V_-$, on obtient :


$$[important]V_{in} = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]$$

Pour isoler le gain ($\frac{V_{out}}{V_{in}}$), on inverse la fraction :


$$\frac{V_{out}}{V_{in}} = \frac{R_1 + R_2}{R_1}$$

Ce qui se simplifie mathématiquement par :


$$[important]\frac{V_{out}}{V_{in}}[/important] = \frac{R_1}{R_1} + \frac{R_2}{R_1} = [important]1 + \frac{R_2}{R_1}[/important]$$

---

> **Note rapide :** On remarque que le gain est toujours supérieur ou égal à 1. Si tu enlèves $R_1$ et que tu remplaces $R_2$ par un fil, tu obtiens un gain de 1, ce qu'on appelle un **suiveur de tension**.

Souhaites-tu que je calcule les valeurs de résistances nécessaires pour obtenir un gain spécifique (par exemple un gain de 10) ?