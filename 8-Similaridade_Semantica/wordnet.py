import nltk

nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def similaridade_entre_palavras(p1, p2):
    sentidos1 = wn.synsets(p1)
    sentidos2 = wn.synsets(p2)
    if not sentidos1 or not sentidos2:
        return 0
    return sentidos1[0].wup_similarity(sentidos2[0]) or 0

texto1 = ['cat', 'sleeping', 'sofa']
texto2 = ['feline', 'resting', 'room']

# Calcular a similaridade média
similaridades = [similaridade_entre_palavras(p1, p2) for p1, p2 in zip(texto1, texto2)]
media = sum(similaridades) / len(similaridades)
print(f"Similaridade semântica aproximada: {media:.2f}")