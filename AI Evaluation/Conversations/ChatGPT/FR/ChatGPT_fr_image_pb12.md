## Utilisateur

Voici un montage d'électronique analogique. Simplifie ce circuit entre les points A et B pour le réduire à un circuit avec un générateur de tension et une résistance. Donne leurs valeurs en fonction des données.
*(image de schéma électrique comportant plusieurs résistances, trois sources de tension et deux bornes A et B avec une charge RL)*

## IA

On cherche l’équivalent de Thévenin vu entre A et B.

Tension de Thévenin
En circuit ouvert (sans (R_L)), la tension (V_{th}=V_A - V_B) vaut
[
V_{th}=\frac{15,V_{src1}+14,V_{src2}+23,V_{src3}}{23}.
]

Résistance de Thévenin
On annule les sources de tension (elles deviennent des courts-circuits) et on calcule la résistance équivalente vue entre A et B. On obtient
[
R_{th}=\frac{430}{23}\ \Omega.
]

Le circuit équivalent entre A et B est donc un générateur de tension (V_{th}) en série avec une résistance (R_{th}).
