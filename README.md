# am-fm-radio
AI prompts to learn what is an am/fm radio and how to build it
## Partie I : Résolution d'un problème assistée par l'IA  

### 1) Organisation

Cette partie du projet est dédiée à la compréhension, au dimensionnement et à l'implémentation d'un **récepteur radio AM**:
* d'abord de manière théorique,
* puis via le logiciel LTspice.

L'objectif est de documenter notre démarche technique et notre utilisation de l'IA au fil du projet.

#### Dossier : `ProjetRadio2`

Dans cette section du dossier ProjetRadio2, nous analysons le fonctionnement global d'une radio AM, son architecture  et le rôle précis de chaque étage.
Chaque bloc fonctionnel est isolé dans un sous-dossier numéroté pour une étude détaillée, de `\01_Antenna` à `\06_Optional_Parts`.

Pour chaque partie de la radio, nous avons documenté les points suivants grâce à des échanges avec l'IA :
* Objectif : Quel est le but de l'étage dans la chaîne de réception ?
* Design & Schématique : Étude du circuit analogique correspondant.
* Composants & Dimensionnement : Choix des valeurs ($R$, $L$, $C$) avec les justifications théoriques et calculs associés.
* Liste de matériel : Identification des composants réels à acquérir pour une construction physique.

#### Dossier : `RadioAMLtSpice`

Ce dossier regroupe nos différentes itérations de conception basées sur un schéma structurel commun. Nous avons exploré deux méthodologies d'implémentation distinctes assistées par IA :

##### 1. Approche par Netlist (`/Netlist`)

Dans cette section, nous avons testé une méthode de conception textuelle (fichiers '.cir'):

* **Méthode :** Génération initiale d'une *netlist* par l'IA à partir de notre schéma.
* **Optimisation :** Ajustements itératifs des paramètres par "prompt engineering" en fonction des résultats obtenus lors des simulations successives.

##### 2. Approche Graphique (`/LtSpiceV1` à `/LtSpiceV4`)

Cette partie contient l'implémentation visuelle classique (des fichiers '.asc') sur LTspice, réalisée de manière incrémentale :

* **Méthode :** Utilisation de l'IA comme tuteur pour un guidage étape par étape lors de la saisie du schéma.
* **Analyse :** Envoi de captures d'écran des diagrammes, des courbes de simulation ou des fichiers sources `.asc` à l'IA pour obtenir un diagnostic technique et corriger les erreurs de conception.
* **Évolution :** Les versions sont classées par ordre de maturité, de la **V1** à la **V4**.

Dans la pluspart des fichiers vous retrouverez un titre "#Prompt" suivie d'un titre "#Answer" pour mieux permettre la lecture des conversations avec l'IA.

### 2) Observations, Remarques et Conclusions

#### Demandes de Schémas Textuels - Problèmes relevés

Lors de la génération de schémas textuels (ASCII), nous avons observé une certaine variabilité entre les réponses produites par l'IA, même lorsque la demande portait sur exactement le même bloc fonctionnel.

L'exemple du **RF Front End** (qui est retrouvé à `"/ProjetRadio2/AM/Rf Front End Multiple Starting Diagrams.pdf"`) est représentatif de ce phénomène :

- changement du nom des composants (`CANT`, `CCOUP`, `Cc`, `C1`, etc.) ;
- changement des noms de signaux (`RF OUT`, `RF`, `Output`) ;
- modification des symboles de masse (`GND`, `0V`, `⏚`) ;
- déplacement apparent des points de sortie ;
- alternance entre schémas détaillés et représentations fonctionnelles ;
- apparition de topologies qui semblent différentes visuellement alors qu'elles sont censées décrire le même étage. On peut observer des parties qui sont en séries dans un schéma, et en parallèle dans l'autre.

Cette observation est particulièrement importante pour l'utilisateur/l'étudiant, qui peut avoir des difficultés à appréhender le schéma à cause de toutes les différences majeures qu'il peut y avoir pour un seul prompt demandant un schéma textuel.

#### Utilisation de l'IA pour la construction de circuits analogiques sur LTspice

##### Méthode 1:
*Avantages* :
* Rapidité
* Facilité à générer
  
*Désavantages* :
* Sensibilité aux erreurs : une erreur de syntaxe peut empêcher la compilation
* Difficulté à débugger : message d'erreurs pas clairs & si l'on est pas déjà familier avec le langage mauvaise lisibilité

##### Méthode 2:
*Avantages* :
* Support visuel
* Possibilité de tester en cours de construction
  
*Désavantages* :
* Demande du temps : IA ne génère rien sur LTspice, c'est à l'utilisateur de construire et suivre les directives données
* Pour le débuggage, on envoie soit une photo du résultat d'une simulation soit un photo du circuit construit, ce qui veut dire que l'IA doit savoir bien analyser une entrée image, au lieu de code 
* Utilisation de versions gratuites d'outils d'IA impose un quota quotidien strict de traitement d'images -> rhythme de travail ralenti.


#### Le fond du problème : Inconsistance de l'IA 

L'un des principaux freins rencontrés lors du développement de ce projet réside dans le manque de consistance des modèles d'IA. Pourtant nous avons essayé d'être rigoureux sur nos prompt et les informations que l'on lui a données. 
Par sa nature même, à partir d'un ensemble de données initiales strictement identiques, l'IA a généré des réponses d'une grande variabilité.

Cette instabilité s'est particulièrement manifestée lors des phases de correction ou d'amélioration.
Par exemple, après avoir suivi le mode d'emploi généré, nous avions obtenu une première version fonctionnelle de notre circuit sur LTSpice ('RadioAMLtSpice/Schematics/LtSpiceV1'). 
Cependant, lorsque le circuit n'a pas fonctionné comme attendu, nous avons tenté de le corriger en ouvrant deux discussions (*chats*) distinctes. Bien que la demande de correction ait été identique, l'IA a généré deux "versions 2" totalement disparates ('RadioAMLtSpice/Schematics/LtSpiceV2-1' et 'RadioAMLtSpice/Schematics/LtSpiceV2-2').

De plus,dans plusieurs cas, les corrections proposées par l'IA ne résolvaient pas le problème qu'elle avait elle-même identifié ou que nous lui avions soumis.

Cette inconsistance structurelle démontre pourquoi il nous semble impossible de mener à bien un projet complexe en totale autonomie avec l'IA, d'autant plus sur un sujet que l'on ne maîtrise pas pleinement : le processus manque cruellement de validation définitive. 
En effet, nous étions contraints de passer à l'étape suivante dès que le résultat nous *semblait* cohérent, sans jamais pouvoir obtenir du modèle une confirmation rigoureuse de la conformité du circuit.

#### Conclusion
Ainsi, si l'IA, lorsqu'elle est correctement exploitée, s'avère être un excellent outil pour dégager et assimiler les aspects théoriques de l'électronique, notre difficulté à obtenir un résultat concret et une version finale en laquelle nous pouvions avoir 100 % confiance met en lumière les limites de cette démarche en autonomie.

---
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
* **Subjectivité de l'annotation :** Malgré l'usage de grilles de correction, le balisage manuel des zones d'intérêt (calcul de densité $D$) et la notation académique comportent une part d'arbitraire inter-évaluateur.
