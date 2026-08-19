## Utilisateur
On étudie un montage comparateur à hystérésis inverseur dans lequel la résistance entre la masse et l'entrée non-inverseuse est notée R1 et la résistance entre l'entrée non-inverseuse et la sortie de l'ALI est notée R2. Identifie le régime de fonctionnement de l'ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d'hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d'amplitude 10V. Explique ton raisonnement.

## IA
On a affaire à un comparateur à hystérésis (trigger de Schmitt) **[important]inverseur[/important]**, donc l’ALI ne fonctionne pas en régime linéaire mais en **[important]régime saturé[/important]**.

---

### 1) Régime de fonctionnement

L’ALI est utilisé en comparateur :  
- gain en boucle ouverte très grand  
- la sortie bascule entre deux saturations :  

\[
s = +V_{sat} \quad \text{ou} \quad s = -V_{sat}
\]

Il n’y a donc **pas de rétroaction négative stabilisante**, mais une **[important]rétroaction positive[/important]** via \(R_2\), ce qui crée l’hystérésis.

---

### 2) Expression de \(v_+\)

L’entrée non-inverseuse est reliée :
- à la masse via \(R_1\)
- à la sortie via \(R_2\)

C’est un **[important]pont diviseur[/important]** entre \(s\) et 0 V :

\[
[important]v_+ = \frac{R_1}{R_1 + R_2} \, s[/important]
\]

---

### 3) Condition de basculement

L’entrée inverseuse reçoit le signal d’entrée \(e(t)\).

Le basculement se produit quand :
\[
[important]v_- = v_+[/important]
\quad \Rightarrow \quad e(t) = v_+
\]

Donc les seuils sont :

\[
[important]V_{th} = \pm \frac{R_1}{R_1 + R_2} V_{sat}[/important]
\]

Plus précisément :
- si \(s = +V_{sat}\), alors \(v_+ = +\frac{R_1}{R_1+R_2}V_{sat}\)
- si \(s = -V_{sat}\), alors \(v_+ = -\frac{R_1}{R_1+R_2}V_{sat}\)

Donc :
\[
\boxed{V_{th+} = +\frac{R_1}{R_1 + R_2} V_{sat}}
\quad ; \quad
\boxed{V_{th-} = -\frac{R_1}{R_1 + R_2} V_{sat}}
\]

---

### 4) Cas \([important]R_2 = 2R_1[/important]\)

Alors :

\[
\frac{R_1}{R_1 + R_2} = \frac{R_1}{3R_1} = \frac{1}{3}
\]

Donc :

\[
[important]V_{th+} = +\frac{V_{sat}}{3}, \quad V_{th-} = -\frac{V_{sat}}{3}[/important]
\]

---

### 5) Cycle d’hystérésis

On représente \(s\) en fonction de \(e\) :

- [important]si \(e\) augmente :
  - \(s = +V_{sat}\) jusqu’à \(e = +V_{sat}/3\)
  - puis bascule à \(s = -V_{sat}[/important]\)

- [important]si \(e\) diminue :
  - \(s = -V_{sat}\) jusqu’à \(e = -V_{sat}/3\)
  - puis bascule à \(s = +V_{sat}[/important]\)

→ On obtient une **[important]boucle rectangulaire[/important]** (hystérésis) entre [important]\(-V_{sat}/3\) et \(+V_{sat}/3\)[/important].

---

### 6) Réponse à une entrée sinusoïdale \(e(t)\) d’amplitude 10 V

On suppose :
\[
e(t) = 10 \sin(\omega t)
\]

Comparaison avec les seuils :

- si \(10 > V_{sat}/3\), ce qui est presque toujours vrai en pratique  
→ le signal franchit les seuils

Donc :

- quand \(e(t) > +V_{sat}/3\) → \(s = -V_{sat}\)
- quand \(e(t) < -V_{sat}/3\) → \(s = +V_{sat}\)

Entre les deux → état dépend de l’historique (hystérésis)

---

### 7) Forme du signal de sortie

Le résultat est :

- un **[important]signal carré[/important]**
- [important]basculement aux instants où la sinusoïde franchit ±\(V_{sat}/3\)[/important]
- [important]déphasé (inverseur)[/important]

Donc :
- sortie = créneau ±\(V_{sat}\)
- fréquence identique à l’entrée
- rapport cyclique ≈ 50 % si sinusoïde centrée

---

### Conclusion

- ALI en régime saturé (comparateur)
- rétroaction positive → hystérésis
- seuils : ±\(V_{sat}/3\) pour \(R_2 = 2R_1\)
- sortie : signal carré issu de la sinusoïde, avec basculement aux seuils

---

Si tu veux, je peux te tracer proprement le cycle d’hystérésis et le signal temporel pour que tu voies exactement la forme attendue en TD.
