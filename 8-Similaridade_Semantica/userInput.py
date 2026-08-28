# Peça ao usuário para digitar duas frases em inglês.
# Extraia as palavras principais (retirar stopwords, como "the", "is", etc).
# Calcule a similaridade semântica média entre as palavras das duas
# frases usando wup_similarity.
# Mostre a similaridade final e destaque os pares de palavras mais semelhantes.
# Use nltk.word_tokenize para separar as palavras.
# Filtre palavras usando a lista stopwords do NLTK.
# Use o código já visto para calcular similaridades com WordNet.
# Mostre também os pares de palavras com a maior similaridade
import nltk
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

firstPhrase = input("Write the first phrase: ")
secondPhrase = input("Write the second phrase: ")

firstPhrase = [p for p in word_tokenize(firstPhrase.lower()) if p.isalpha() and p not in stop_words]
secondPhrase = [p for p in word_tokenize(secondPhrase.lower()) if p.isalpha() and p not in stop_words]

def similaridade_entre_palavras(p1, p2):
    sentidos1 = wn.synsets(p1)
    sentidos2 = wn.synsets(p2)
    if not sentidos1 or not sentidos2:
        return 0
    return sentidos1[0].wup_similarity(sentidos2[0]) or 0

if not firstPhrase or not secondPhrase:
    print("Nenhuma palavra relevante restou após remover as stopwords.")
else:
    # para cada palavra da primeira frase, encontra a mais parecida na segunda
    melhores_pares = []
    for p1 in firstPhrase:
        p2, sim = max(
            ((p2, similaridade_entre_palavras(p1, p2)) for p2 in secondPhrase),
            key=lambda par: par[1],
        )
        melhores_pares.append((p1, p2, sim))

    media = sum(sim for _, _, sim in melhores_pares) / len(melhores_pares)
    print(f"\nSimilaridade semântica aproximada: {media:.2f}")

    melhores_pares.sort(key=lambda par: par[2], reverse=True)
    print("\nPares de palavras mais semelhantes:")
    for p1, p2, sim in melhores_pares:
        print(f"  {p1} - {p2}: {sim:.2f}")
