import re
from traitement_texte import balise_remover

# ------------------------
#         MESURES
# ------------------------
def length_anwser(discussion):
    """
    Description : 
    Calcule la somme des longueurs des réponses de l'IA dans la conversation discussion
    
    Entrées : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    
    Sorties : 
    - sum : int
    """
    discussion = balise_remover(discussion)
    sum = 0
    
    for texte in discussion:
        if texte["Interlocuteur"] == "IA":
            sum += len(texte["Message"])

    return sum
    

def av_nb_words(discussion):
    """
    Description : 
    Calcule le nombre de mots dans les réponses de l'IA durant la conversation discussion
    
    Entrées : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    
    Sorties : 
    - sum : int
    """
    discussion = balise_remover(discussion)
    sum = 0
    
    for texte in discussion:
        if texte["Interlocuteur"] == "IA":
            sum += len(texte["Message"].split())

    return sum


def interest_density(discussion):
    """
    Description : 
    Calcule la somme des longueurs des zones d'intérêt dans les réponses de l'IA durant la conversation discussion, 
    divisée par la longueur totale de ses prises de paroles
    Les "zones d'intérêt" sont indiquées dans le texte par les bornes [important] [/important]
    
    Entrées : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    
    Sorties : 
    - sum_tot : int
    """
    sum_tot = 0
    sum_interest = 0

    for prise_parole in discussion:
        if prise_parole["Interlocuteur"] == "IA":
            sum_tot += len(prise_parole["Message"])
            # Les "zones d'intérêt" sont indiquées dans le texte par les bornes [important] [/important]
            # Cette ligne nous permet de les isoler 
            sum_interest += len(' '.join(re.findall(r"\[important\](.*?)\[/important\]", prise_parole["Message with balise"], re.DOTALL)))
    if sum_tot > 0:
        return sum_interest/sum_tot
    else:
        return None



def pas_de_fonction_associee(*args, **kwargs):
    return None