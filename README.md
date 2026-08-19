## Partie II : Evaluation de modèles d'IA
Tous les fichiers et dossiers de cette partie se trouvent dans le dossier _AI Evaluation_

### 1) Objectifs
Dans cette partie, nous cherchons à évaluer la capacité de différents modèles d'IA à répondre efficacement à des problèmes classiques d'électronique analogique, avec des paramètres différents. 
Nous avons établi une liste d'indicateurs à mesurer dans les réponses des modèles, afin de caractériser la justesse de leurs réponses et l'efficacité avec laquelle ils la délivrent.
1. Longueur de la réponse (en nombre de caractères)
2. Nombre de mots
3. Densité d'informations pertinentes
4. Note (cf Critères de justesse)
5. Similarité Syntaxique


Ces différents critères pourront ultérieurement être combinés dans un score global attribué à l'IA et ses paramètres, permettant une lecture plus rapide des résultats.

---
### 2) Banque de problèmes
#### Choix des problèmes
Les problèmes sélectionnés sont des problèmes classiques d'électronique analogique. La liste des 15 problèmes peut être retrouvée dans le fichier _Liste\_Problèmes.pdf_ .
Nous les avons choisis parmi ceux proposés en TD de l'électif Systèmes Electroniques, et au sein de différentes banques de problèmes de prépa ou de sujets de TD trouvés en ligne.


#### Critères de justesse
Pour chaque problème une grille de notation a été définie. Elle rassemble tous les éléments de réponses attendus pour un problème, ainsi que le nombre de points associés, donnant finalement lieu à une note sur 10.
Toutes les grilles de notations peuvent être retrouvées dans _Liste\_Problèmes.pdf_, à la page du problème associé.

---
### 3) Modèles d'IA et paramètres évalués
Différents modèles et différents paramètres sont utilisés dans ce projet, afin d'établir une comparaison pertinente des différentes utilisations possible de l'IA.

**Modèles d'IA**
- ChatGPT
- Gemini
- Mistral

**Langues**
- Français
- Anglais

**3 Différents modes d'utilisation**
- Requête "simple" : Texte décrivant le circuit considéré (le plus souvent par son nom classique), et les objectifs à atteindre dans le problème considéré
- Requête "brief" : Une instruction est ajoutée à la requête précédente, demandant au modèle de répondre concise, en supprimant les éléments superflus de sa réponse.
- Requête "image" : La requête est accompagnée d'une image représentant le circuit considéré. On ne mentionne plus le nom ou l'architecture du circuit dans la requête.


/!\ Les problèmes 12, 13 et 14 constituent une exception à cette division. En effet, ces problèmes étaient trop compliqués à décrire par une phrase. Nous avons donc décidé de ne les étudier qu'avec des requêtes accompagnées d'image. Pour ces problèmes, on ne retrouve donc que 2 modes d'utilisation : "image" et "brief" (ce dernier est donc exceptionnellement accompagné d'une image pour ces problèmes)


En combinant tous ces paramètres, on obtient 18 configurations à tester pour chaque problème. Nous aurions voulus tester davantage de configurations, mais avons dû nous restreindre car chaque nouveau modèle d'IA ou chaque nouveau paramètre ajoutait une grande quantité de prompts à faire, à annoter et à évaluer.

---
### 4) Indicateurs de performance des réponses
#### Longueur de la réponse
On mesure tout d'abord la longueur en nombre de caractères de la réponse de l'IA à chaque prompt. Cette mesure permet de caractériser l'efficacité de sa réponse au problème donné. En effet les IA ont tendance à faire de longues réponses à des problèmes relativement simples. Ce critère, négatif donc, pourra permettre de distinguer les modèles répondant certes de manière juste aux problèmes, mais prenant beaucoup de détours pour y parvenir.

#### Nombre de mots
Nous mesurons également le nombre de mots utilisés par le modèle dans sa réponse. Cet indicateur peut être redondant avec le précédent, mais est facilement calculable et plus parlant pour les lecteurs.

#### Densité d'informations pertinentes
Pour chacune des réponses obtenues, nous indiquons à notre programme quelles parties du texte sont réellement importantes à la résolution du problème, et lesquelles sont superflues. 
Il peut s'agir par exemple de mots clés ("diviseur de tension", "filtre passe bas du second ordre"...), d'expressions mathématiques ou bien de détail d'un calcul.
On calcule ensuite la longueur totale de ces zones d'intérêt et on la divise par la longueur totale du message, pour obtenir la densité d'informations pertinentes dans la réponse.

/!\ Nous n'avons pas eu le temps de baliser tous les problèmes. Pour éviter de biaiser notre programme, nous ne le faisons donc tourner que sur les problèmes 1 à 11

#### Note de réussite
Il s'agit simplement d'une note attribuée manuellement suite à l'évaluation des critères de justesse définis plus haut.

/!\ Nous n'avons pas eu le temps de noter tous les problèmes. Pour éviter de biaiser notre programme, nous ne le faisons donc tourner que sur les problèmes 1 à 11


#### Similarité syntaxique
La similarité syntaxique est calculée à partir du modèle développé dans le dossier _Evaluation\_automatisée_. Il s'agit d'un indice calculé par une IA entraînée sur une grande base de données de textes d'électronique. Elle mesure la proximité entre la réponse de l'IA et les formules des critères de justesse. 
Tous les résultats de ces calculs ont été rassemblés dans le tableau _Resultats\_Benchmark.xlsx_, qui est ensuite lu par notre programme.


#### Score
Le score est un indice que nous avons défini par la formule suivante : 
$$Score = \frac{D^\alpha * N^\beta * S^\gamma}{exp(\delta * max(\frac{L}{\eta}-1,0))}$$

Où : 
- D est la densité d'information moyenne sur toutes les réponses dans un contexte (IA, langue, mode d'utilisation)
- N la note moyenne (ramenée entre 0 et 1)
- S la similarité syntaxique moyenne (ramenée entre 0 et 1)
- L la longueur des réponses moyenne (en nombre de mots)


Les autres grandeurs sont des paramètres du modèle, dont la valeur peut être changée au début de _{Evaluation_IA.py}_.
On a pris pour l'étude : $\alpha = 0.25, \beta = 1.5, \gamma = 1, \delta = 0.5, \eta = 250$

Explication : 
D, N et S sont des grandeurs que l'on cherche à maximiser, d'où leur présence au numérateur. $\alpha, \beta, \gamma$ peuvent être interprétés comme le poids associé à chacune des grandeurs. 

$\eta$ correspond à la longueur de message recherchée. Les messages plus longs sont pénalisés de manière exponentielle, paramétrée par $\lambda$, et les messages plus courts ne sont pas avantagés.

##### Remarques : 
- Il est à noter que les valeurs ici sont arbitraires, mais ont été ajustées pour obtenir des résultats cohérents avec nos observations et notre ressenti à la lecture des prompts. Une telle formule peut donc être utilisée pour comparer à cette étude d'autres prompts, venant d'autres modèles.
- $\alpha$ est de valeur faible car la densité d'information est souvent très proche de 0 et a tendance à aplatir toutes les mesures. 
- Pour les réponses où l'on a spécifié aux IA de répondre de manière brève, leur longueur est souvent inférieure à la longueur visée. Elles ne sont donc pas comparées sur la base de leur longueur.

---
### 5) Code
#### Exportation et stockage des réponses des IA
Pour chaque requête envoyée à l'IA, une seconde requête nous permet de formater la réponse précédente en un texte markdown pour faciliter son export et son traitement.
Toutes les réponses des IA sont ensuite stockées dans l'arborescence du dossier _Conversations_, selon le modèle d'IA et la langue utilisés.

Ici leur nom suit un format spécifique : 

**NomIA_Langue_Mode_Numéro**

Avec :

* **NomIA** : ChatGPT, Gemini ou Mistral
* **Langue** : fr ou en
* **Mode** : simple, brief ou image
* **Numéro** : numéro du problème étudié

Exemples :

_ChatGPT_en_brief_pb1.md_

_Gemini_fr_simple_pb7.md_

_Mistral_en_image_pb12.md_



#### Traitement des réponses
Notre code est réuni dans 3 fichiers python : 
- _Evaluation_IA.py_ : Fichier principal à appeler pour l'exécution. Contient également les fonctions d'ouverture des fichiers contenant les réponses des IA et quelques fonctions de nettoyage et de mise en forme de ces fichiers.
- _analyse.py_ : Rassemble les fonctions de calcul des indicateurs de performance des réponses.
- _enregistrement_excel.py_ : Contient les fonctions relatives à la création, la mise en forme et l'écriture dans le tableau excel __ qui contient nos s.


#### Utilisation
Pour lancer le programme, exécuter la commande "py Evaluation_IA.py" (ou "python Evaluation_IA.py", ou autre selon la machine), ou bien le lancer depuis un éditeur de code (comme Visual Studio Code).

---
### 6) Résultats
Les résultats de nos mesures sont rassemblés dans le tableur excel _Resultat\_etude.xlsx_. Celui-ci est composé de plusieurs pages.
- Une page "**Comparatif**"
- Une page par modèle d'IA évalué

#### Pages spécifiques aux IA
On y retrouve le détail de toutes nos mesures, rassemblées en différents tableaux (un par combinaison de paramètres : langue et mode d'utilisation)

Lorsqu'une ligne est vide, c'est que le fichier correspondant n'existe pas. C'est le cas par exemple des problèmes 12, 13 et 14 pour lesquels il n'y a aucune réponse pour un requête "simple" (détaillée, sans image) (en effet, les problèmes concernés ne pouvaient être décrits facilement sans image). Comme la liste des problèmes traités ici s'arrête au problème 11, de tels cas ne devraient pas se produire

#### Page "Comparatif"
On y retrouve, pour chaque langue et chaque mode d'utilisation un tableau récapitulatif des performances de l'IA, permettant une comparaison plus simple. 
La meilleure performance dans chaque cas est surlignée en vert, et la moins bonne en rouge. 

---


### 7) Utilisation
Pour lancer le programme, il faut exécuter la commande "py Evaluation_IA.py" depuis le dossier AI Evaluation.
Le tableau récapitulatif est alors enregistré sous le nom _"Resultat_etude.xlsx"_
Vérifier que les tableurs Excel mentionnés par le README ne sont bien pas ouverts. Le cas échéant le programme peut planter.

### Conclusion 
Grâce à cette partie du projet, on voit qu'il est possible de mesurer les performances de modèles d'IA. Notre étude nous permet notamment de voir que Mistral est généralement le moins bon dans toutes les catégories. Pour ce qui est de la comparaison entre ChatGPT et Gemini, ce dernier est souvent plus bavard, même lorsqu'on lui demande d'être bref mais répond de manière plus juste et exhaustive.

---
### 8) Limites de l'approche

L'interprétation des performances globales reste conditionnée par trois verrous méthodologiques :

* **Complexité multimodale :** La retranscription et le traitement des schémas de circuits électroniques par les modèles introduisent une rupture de symétrie technique par rapport aux requêtes purement textuelles, compliquant leur évaluation standardisée.
* **Variabilité stochastique :** La nature non déterministe des LLM induit une fluctuation des réponses pour un prompt identique, ce qui limite la reproductibilité stricte des métriques de longueur et de similarité syntaxique.
