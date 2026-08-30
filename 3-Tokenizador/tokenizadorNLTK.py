# Contar Palavras
from collections import Counter
texto = "Este texto está sendo utilizado para demonstrar o funcionamento de diferentes formas tokenização. O processo de tokenização pode ser realizado com objetivos distintos."
palavras = texto.replace('\n',' ').replace('\t','').replace(',', '').replace('.', ' ').split(' ')
contador = Counter(palavras)
for cont in contador.items():
    print(cont)

# Contar Tokens
from collections import Counter
import nltk
nltk.download('punkt_tab')
from nltk import tokenize
texto = "Este texto está sendo utilizado para demonstrar o funcionamento de diferentes formas tokenização. O processo de tokenização pode ser realizado com objetivos distintos."
palavras_tokenize = tokenize.word_tokenize(texto)
print(palavras_tokenize)
contador = Counter(palavras_tokenize)
for cont in contador.items():
    print(cont)

#Stemmer
nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()
print(stemmer.stem("abóbora"))
print(stemmer.stem("maça"))
print(stemmer.stem("Curitiba"))

# Exercícios
# • Avaliar o algoritmo de Tokenização para os seguintes textos:
# • "São Paulo, SP, S.P., S. Paulo“
# • nome@pucpr.br
# • "CPF: 001.002.003-04“
