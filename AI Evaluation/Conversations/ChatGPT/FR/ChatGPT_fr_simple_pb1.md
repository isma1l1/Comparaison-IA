## Utilisateur

Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA

Dans un **montage amplificateur inverseur** (avec un amplificateur opérationnel idéal), on cherche le gain en tension ( [important]A_v = \dfrac{V_{\text{out}}}{V_{\text{in}}}[/important] ).

### Raisonnement

1. **Hypothèses d’un AOP idéal** :

   * Courant d’entrée nul → aucun courant ne rentre dans les bornes de l’AOP.
   * Tension entre les entrées (+) et (−) nulle → ( [important]V^- = V^+[/important] )

2. **Montage** :
   
   * L’entrée (+) est reliée à la masse →  ( [important]V^+ = 0 [/important]) 
   * Donc [important] ( V^- = 0 ) (masse virtuelle)
   [/important]
3. **Courants dans le circuit** :

   * Courant dans ( R_1 ) :
     [
     [important]I_1 = \frac{V_{\text{in}} - 0}{R_1} = \frac{V_{\text{in}}}{R_1}[/important]
     ]
     
   * Courant dans ( R_2 ) :
   
     [
     [important]I_2 = \frac{0 - V_{\text{out}}}{R_2} = -\frac{V_{\text{out}}}{R_2}[/important]
     ]

4. **Loi des nœuds** :

   * Comme aucun courant ne rentre dans l’AOP :
   
     [
     [important]I_1 = I_2[/important]
     ]
     

5. **Égalité et simplification** :

   [
   [important]\frac{V_{\text{in}}}{R_1} = -\frac{V_{\text{out}}}{R_2}[/important]
   ]

---

### Formule du gain

[
[important]A_v = \frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}[/important]
]

---

### Interprétation

* Le **signe négatif** → le signal de sortie est **inversé** (déphasage de 180°).
* Le **rapport ( R_2 / R_1 )** → fixe l’amplification :

  * Si ( R_2 > R_1 ) → amplification
  * Si ( R_2 < R_1 ) → atténuation

---

Si tu veux, je peux te faire un schéma du montage ou te donner un exemple numérique
