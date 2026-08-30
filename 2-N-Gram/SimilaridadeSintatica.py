# Pedro Bastos Leite
# Felipe Augusto
# Giuseppe Bruno
# Isabelle Lopes

# Indicar a palavra mais próxima N-GRAM
# digramas carro
# ca ar rr ro - 4 digramas e 4 únicos
lex = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 'ananas', 'maca', 'mamao', 'manga', 'melancia', 'melao', 'mexerica', 'morango']

print(f"Léxico: ", lex)

lexDigrams = {}

for word in lex:
    digramas = []

    for i in range(len(word) - 1):
        digramas.append(word[i:i+2])

    lexDigrams[word] = digramas

print(lexDigrams)

userWord = input("Digite a palavra para analisar a proximidade: ")

userDigrams = []

for i in range(len(userWord) - 1):
    userDigrams.append(userWord[i:i+2])

print(userDigrams)

# Comparação: S = 2C / (A + B)
userDigramsUniques = set(userDigrams)
B = len(userDigramsUniques)

bestWord = None
bestSimilarity = -1

for word, digrams in lexDigrams.items():
    digramsUniques = set(digrams)      # únicos da palavra do léxico
    A = len(digramsUniques)
    C = len(digramsUniques & userDigramsUniques)  # interseção (compartilhados)

    S = (2 * C) / (A + B) if (A + B) > 0 else 0
    print(f"{word}: A={A} B={B} C={C} S={S:.2f}")

    if S > bestSimilarity:
        bestSimilarity = S
        bestWord = word

print(f"\nPalavra mais próxima de '{userWord}': {bestWord} (S = {bestSimilarity:.2f})")
