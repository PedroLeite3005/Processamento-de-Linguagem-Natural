import matplotlib.pyplot as plt
import re
from collections import Counter

# Contar quantas ocorrências de cada palavra (Pontuação não entra)
# Plotar Histograma para ver se a Lei de Zipf está correta (cauda longa)
# Calcular TF-IDF de cada palavra - mostrar total de palavras e total de palavras com 0 no TF-IDF

caminho_arquivo = 'C:/Users/pedro/Documents/GitHub/Processamento-de-Linguagem-Natural/5-TF-IDF/2000_textos.txt'

with open(caminho_arquivo, encoding='utf-8') as arquivo:
    corpus = arquivo.readlines()

contagem_palavras = Counter()

for linha in corpus:
    linha = linha.strip()
    if not linha:
        continue

    # cada linha do arquivo é "sentimento;;texto"
    sentimento, texto = linha.split(';;', 1)

    texto = f"{sentimento} {texto}".lower()
    palavras = re.findall(r'\b[a-zà-ú]+\b', texto)  # só letras, pontuação fora

    contagem_palavras.update(palavras)

print(f"Total de palavras distintas: {len(contagem_palavras)}")
print(contagem_palavras.most_common(20))

frequencias = sorted(contagem_palavras.values(), reverse=True)

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(frequencias) + 1), frequencias)
plt.xlabel("Rank da palavra (mais frequente -> menos frequente)")
plt.ylabel("Frequência")
plt.title("Distribuição de frequência das palavras (Lei de Zipf)")
plt.ylim(0, 4000)
plt.show()