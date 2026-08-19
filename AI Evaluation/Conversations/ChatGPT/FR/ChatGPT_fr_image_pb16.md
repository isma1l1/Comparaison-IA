## Utilisateur

Résous les questions A.1.1, A.1.2 et A.1.3 présentes sur ces images en détaillant
ton raisonnement.

*(image de deux pages d’un sujet d’électronique analogique portant sur un réservoir d’eau avec flotteur, un potentiomètre linéaire et un pont de Wheatstone, contenant les questions A.1.1, A.1.2 et A.1.3 à résoudre)*

## IA

On étudie le pont de Wheatstone de la figure 2.

On note :

* (R_1=kR)
* (R_2=(1-k)R)
* (k=\dfrac{x}{h})
* (V_1) : source continue
* (V_2) : tension entre les points milieux des deux branches.

---

# A.1.1 — Expression littérale de (V_2)

Le montage est constitué de deux diviseurs de tension :

* à gauche : (R_2) en haut et (R_1) en bas,
* à droite : (R_3) en haut et (R_4) en bas.

On prend le bas du circuit comme référence (0 V).

## Tension au point milieu gauche

Le courant dans la branche gauche vaut :

[
I_g=\frac{V_1}{R_1+R_2}
]

La tension du point milieu gauche (entre (R_2) et (R_1)) vaut donc :

[
V_g=I_g R_1
]

d’où

[
V_g=\frac{V_1R_1}{R_1+R_2}
]

---

## Tension au point milieu droit

Même raisonnement :

[
I_d=\frac{V_1}{R_3+R_4}
]

et

[
V_d=I_dR_4
]

donc

[
V_d=\frac{V_1R_4}{R_3+R_4}
]

---

## Expression de (V_2)

D’après le schéma, (V_2) est orientée du point milieu droit vers le point milieu gauche :

[
V_2 = V_g - V_d
]

Ainsi :

[
\boxed{
V_2
===

V_1\left(
\frac{R_1}{R_1+R_2}
-------------------

\frac{R_4}{R_3+R_4}
\right)
}
]

---

# A.1.2 — Relation entre (V_2) et (x)

On utilise :

[
R_1=kR,\qquad R_2=(1-k)R
]

Alors :

[
R_1+R_2=kR+(1-k)R=R
]

Donc :

[
\frac{R_1}{R_1+R_2}
===================

# \frac{kR}{R}

k
]

Comme (k=\dfrac{x}{h}), on obtient :

[
\frac{R_1}{R_1+R_2}=\frac{x}{h}
]

En remplaçant dans l’expression précédente :

[
\boxed{
V_2
===

V_1\left(
\frac{x}{h}
-----------

\frac{R_4}{R_3+R_4}
\right)
}
]

C’est la relation demandée entre (V_2) et (x).

---

# A.1.3 — Condition pour avoir (V_2=0) à mi-hauteur

On veut :

[
V_2=0
\quad \text{quand} \quad x=\frac{h}{2}
]

Donc :

[
\frac{x}{h}=\frac12
]

On remplace dans l’expression de (V_2) :

[
0
=

V_1\left(
\frac12-\frac{R_4}{R_3+R_4}
\right)
]

Comme (V_1\neq 0),

[
\frac12=\frac{R_4}{R_3+R_4}
]

Résolution :

[
R_3+R_4=2R_4
]

[
R_3=R_4
]

Donc la condition recherchée est :

[
\boxed{R_3=R_4}
]

---

## Valeur minimale de (V_2)

Quand (x=0),

[
\frac{x}{h}=0
]

et avec (R_3=R_4),

[
\frac{R_4}{R_3+R_4}=\frac12
]

Ainsi :

[
V_{2\min}
=========

V_1\left(0-\frac12\right)
]

[
\boxed{
V_{2\min}=-\frac{V_1}{2}
}
]

---

## Valeur maximale de (V_2)

Quand (x=h),

[
\frac{x}{h}=1
]

Donc :

[
V_{2\max}
=========

V_1\left(1-\frac12\right)
]

[
\boxed{
V_{2\max}=+\frac{V_1}{2}
}
]

---

# Résultats finaux

## A.1.1

[
\boxed{
V_2
===

V_1\left(
\frac{R_1}{R_1+R_2}
-------------------

\frac{R_4}{R_3+R_4}
\right)
}
]

---

## A.1.2

[
\boxed{
V_2
===

V_1\left(
\frac{x}{h}
-----------

\frac{R_4}{R_3+R_4}
\right)
}
]

---

## A.1.3

Condition :

[
\boxed{R_3=R_4}
]

Valeurs extrêmes :

[
\boxed{
V_{2\min}=-\frac{V_1}{2}
}
\qquad
\boxed{
V_{2\max}=+\frac{V_1}{2}
}
]
