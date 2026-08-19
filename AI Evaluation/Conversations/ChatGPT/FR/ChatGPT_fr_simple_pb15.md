## Utilisateur
On étudie un montage filtre actif amplificateur classique (la borne + de l'ALI est reliée à la terre et la borne - est reliée à la sortie de l'ALI par une résistance R' et à l'entrée par un condensateur C et une résistance R).
Identifie sans calcul la nature de ce filtre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

## IA
Le montage décrit est un amplificateur inverseur dont l’impédance d’entrée est constituée de R en série avec C, et la contre-réaction est purement résistive (R′).  

À basse fréquence, le condensateur se comporte comme un circuit ouvert ⇒ aucun signal n’entre dans l’amplificateur ⇒ sortie nulle.  
À haute fréquence, le condensateur se comporte comme un court-circuit ⇒ on retrouve un amplificateur inverseur classique de gain −R′/R.  

Donc, sans calcul, il s’agit d’un **filtre passe-haut du premier ordre**.

---

Établissons la fonction de transfert.

L’impédance d’entrée vaut :  
Zₑ = R + 1/(jωC)

Le montage étant inverseur :  
H(jω) = Vₛ / Vₑ = − R′ / Zₑ

Donc :  
H(jω) = − R′ / (R + 1/(jωC))  

On met sous forme canonique :

H(jω) = − (R′/R) · (jωRC) / (1 + jωRC)

En posant ω₀ = 1/(RC), on obtient :

H(jω) = − (R′/R) · (jω/ω₀) / (1 + jω/ω₀)

---

Identification :

- Pulsation de coupure : ω₀ = 1/(RC)  
- Gain en haute fréquence : |H(∞)| = R′/R

---

On impose :

ω₀ = 10⁴ rad·s⁻¹  
R = 1 kΩ = 10³ Ω  

Donc :  
RC = 1/ω₀ = 10⁻⁴  

⇒ C = 10⁻⁴ / 10³ = 10⁻⁷ F = 100 nF  

---

Gain en haute fréquence : 20 dB  

20 dB ⇒ gain en module = 10  

Donc :  
R′ / R = 10  

⇒ R′ = 10 × 1 kΩ = 10 kΩ  

---

Résultats :

- Nature : filtre passe-haut du 1er ordre inverseur  
- Fonction de transfert :  
  H(jω) = − (R′/R) · (jω/ω₀) / (1 + jω/ω₀)  
- Valeurs :  
  C = 100 nF  
  R′ = 10 kΩ
