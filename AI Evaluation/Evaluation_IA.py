import enregistrement_excel as bilan_sheet
from traitement_texte import *
from analyse import *

import sys
from pathlib import Path


# ----------------------------
# VARIABLES GLOBALES
# ----------------------------
global Nb_crit
Nb_crit = 5
global Criteres
Criteres = [{"Nom" : "Longueur (en caractères)",
                  "Objectif" : "Minimiser",
                  "Fonction" : length_anwser},
                 {"Nom" : "Longueur (en mots)",
                  "Objectif" : "Minimiser",
                  "Fonction" : av_nb_words},
                 {"Nom" : "Densité d'information importante",
                  "Objectif" : "Maximiser",
                  "Fonction" : interest_density},
                 {"Nom" : "Note",
                  "Objectif" : "Maximiser",
                  "Fonction" : pas_de_fonction_associee},
                 {"Nom" : "Similarité syntaxique",
                  "Objectif" : "Maximiser",
                  "Fonction" : pas_de_fonction_associee},
                 {"Nom" : "Score global",
                  "Objectif" : "Maximiser",
                  "Fonction" : pas_de_fonction_associee}]

# ----------
# Données utilisées dans notre étude particulière
# ----------

# Nombres de sujets de problèmes considérés
global Nb_pb
Nb_pb = 11


# Liste des IA utilisées 
global Liste_IA
Liste_IA = ["ChatGPT","Gemini","Mistral"]

# Mode de fonctionnement des IA à évaluer
global categories_names
categories_names = ["Réponse détaillée, sans image","Réponse synthétique, sans image","Réponse avec image"]

# Langues testées
global langues
langues = ["FR","EN"]

# ----------
# Constantes du calcul du score
# ----------
global alpha, beta, gamma, delta, eta

alpha = 0.25 # Densité
beta = 1.5 # Note
gamma = 1 # Similarité
delta = 0.5 # Coef influence réponse

# Longueur des réponses attendue (en nombre de mots)
eta = 250


# ----------------------------
#  LECTURE DE LA CONVERSATION
# ----------------------------

def parse_markdown_chat(file_path):
    """
    Description : 
    Lit la discussion contenue dans le fichier markdown situé en file_path et sépare les prises de parole de l'IA et de l'utilisateur.
    Elle sera alors stockée comme une liste de prises de paroles, où chaque prise de parole est constituée d'un nom d'interlocuteur et d'un message
    
    Entrées : 
    - file_path : str

    
    Sorties : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    """
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    discussion = []
    current_message = None

    # Détection des changements de personne
    pattern = re.compile(r'^##\s+(Utilisateur|IA)', re.IGNORECASE)

    for line in lines:
        match = pattern.match(line)
        if match:
            # Fin de la prise de parole précédente
            if current_message:
                discussion.append(current_message)
            
            # Début d'une nouvelle prise de parole
            current_interlocuteur = match.group(1)
            current_message = {"Interlocuteur": current_interlocuteur, "Message": "", "Message with balise": ""}
        else:
            # Si on est au milieu d'une prise de parole, on ajout simplement la nouvelle ligne au reste du message
            if current_message is not None:
                current_message["Message with balise"] += line

    # Ajouter le dernier message après la boucle
    if current_message:
        discussion.append(current_message)

    # Nettoyage final : on retire les espaces et sauts de ligne superflus
    for msg in discussion:
        msg["Message with balise"] = msg["Message with balise"].strip()

    return discussion





# -------------------------
#        EXECUTION
# -------------------------

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        wb = bilan_sheet.initialisation_etude()
        cpt_file_not_found = 0
        
        Liste_prefixes = ["simple_pb","brief_pb","image_pb"]
        
        
        
        n = len(Liste_IA)
        for i in range(n):
            for l in range(len(langues)):
                for j in range(1,Nb_pb+1):
                    
                    for k in range(len(Liste_prefixes)):
                        file_path = f"Conversations/{Liste_IA[i]}/{langues[l]}/{Liste_IA[i]}_{str.lower(langues[l])}_{Liste_prefixes[k]}{j}.md"
                        try : 
                            discussion = parse_markdown_chat(file_path)
                            discussion = discussion_cleaner(discussion)
                            
                            liste_crit = [j]
                            for c in range(Nb_crit):
                                liste_crit.append(Criteres[c]["Fonction"](discussion))
                                
                            bilan_sheet.write_line(wb,Liste_IA[i],liste_crit,start_col=1+k*(Nb_crit+3),start_row=j+3+l*(Nb_pb+5))
                            
                        except FileNotFoundError:
                            print(f"Le fichier '{file_path}' est introuvable")
                            cpt_file_not_found+=1
                            bilan_sheet.write_line(wb,Liste_IA[i],[j,None,None,None,None],start_col=1+k*(Nb_crit+3),start_row=j+3+l*(Nb_pb+5))
        
        
        if cpt_file_not_found > 0:
            print("Il manque",str(cpt_file_not_found),"fichiers")
        
        
        # Copie des notes des pb dans le tableau depuis le fichier "Notes.xlsx"
        bilan_sheet.copie_notes(wb)
        bilan_sheet.copie_similarite(wb)
        
        bilan_sheet.save(wb,"Resultat_etude.xlsx")
        print("Traitement terminé")