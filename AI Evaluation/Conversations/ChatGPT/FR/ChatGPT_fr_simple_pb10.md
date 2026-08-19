## Utilisateur
On étudie un montage sommateur non-inverseur classique dans lequel les quatre résistances ont la même valeur R. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA
Considérons un AOP idéal en montage non-inverseur. Les quatre résistances sont égales à R.

1) Tension à l’entrée non-inverseuse (+)  
Cette entrée est reliée à V1 et V2 via deux résistances égales R. Comme l’entrée de l’AOP ne consomme pas de courant, le nœud est simplement un point milieu entre V1 et V2. Par superposition (ou diviseur symétrique), on obtient :
  
[[important]V+ = (V1 + V2) / 2  [\important]]

2) Relation entre V+ et V−  
Avec un AOP idéal en [[important]régime linéaire (contre-réaction)[\important]], on a :
  
[[important]V− = V+ [\important]]

Donc :
  
V− = (V1 + V2) / 2  

3) Réseau de contre-réaction (entrée inverseuse)  
L’entrée inverseuse est reliée à Vs et à la masse via deux résistances égales R. C’est donc un pont diviseur classique :

[[important]V− = Vs × (R / (R + R)) = Vs / 2  [\important]]

4) Égalisation des deux expressions de V−  

[[important]Vs / 2 = (V1 + V2) / 2  [\important]]

Donc :

[[important]Vs = V1 + V2  [\important]]

Conclusion : la sortie est la somme des deux entrées.
