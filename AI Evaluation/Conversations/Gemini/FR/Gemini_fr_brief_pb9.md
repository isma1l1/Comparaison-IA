## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
Voici l'étude du montage dérivateur idéal à base d'amplificateur opérationnel (AO).

### Schéma et Hypothèses
* **Composants :** Un condensateur $C$ en entrée et une résistance $R$ en contre-réaction.
* **AO idéal :** Courants d'entrée nuls ($i_+ = i_- = 0$) et [important]régime linéaire[/important] ($[important]V_+ = V_-[/important]$).
* **Masses :** La borne non-inverseuse est à la masse ($[important]V_+ = 0[/important]$), d'où $V_- = 0$ (masse virtuelle).

---

### Raisonnement
1.  **Loi des nœuds en $V_-$ :** Le courant traversant le condensateur ($i_C$) est égal à celui traversant la résistance ($i_R$).
    $$[important]i_C + i_R = 0 \implies i_C = -i_R[/important]$$

2.  **Caractéristique du condensateur :** Le courant est proportionnel à la dérivée de la tension à ses bornes ($e - V_-$).
    $$[important]i_C = C \frac{d(e - V_-)}{dt} = C \frac{de}{dt}[/important]$$

3.  **Loi d'Ohm pour la résistance :**
    $$[important]i_R = \frac{s - V_-}{R} = \frac{s}{R}[/important]$$

4.  **Égalité des courants :**
    $$[important]C \frac{de}{dt} = -\frac{s}{R}[/important]$$

---

### Relation Entrée-Sortie
La tension de sortie $s(t)$ est proportionnelle à la dérivée de la tension d'entrée $e(t)$ :

$$[important]s(t) = -RC \frac{de(t)}{dt}[/important]$$

Le signe négatif indique que le montage est également **inverseur**.
