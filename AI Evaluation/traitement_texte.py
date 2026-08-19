import re


# -------------------------
#    TRAITEMENT DU TEXTE
# -------------------------
def text_cleaner(text):
    """
    Description : 
    Enlève certains caractères d'un texte pour le nettoyer, ne garder que des mots.
    
    Entrées : 
    - text : str
    
    Sorties : 
    - text : str
    """
    motifs = [r"\n",r"!",r"\?",r"\.",r":"]
    for motif in motifs:
        text = re.sub(motif, '', text)
    return text


def discussion_cleaner(discussion):
    """
    Description : 
    Nettoie chaque prise de parole dans discussion avec text_cleaner
    
    Entrées : 
    - discussion : list of dict with three keys : "Interlocuteur", "Message" and "Message with balise"
     
    Sorties : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    """
    for item in discussion:
        item["Message with balise"] = text_cleaner(item["Message with balise"])
        
    return discussion

def balise_remover(discussion):
    """
    Description : 
    Retire les balises [important] et [/important] du texte discussion
    
    Entrées : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    
    Sorties : 
    - discussion : list of dict with two keys : "Interlocuteur" and "Message"
    """
    for item in discussion:
        item["Message"] = re.sub(r"\[/?important\]", "", item["Message with balise"])
        
    return discussion