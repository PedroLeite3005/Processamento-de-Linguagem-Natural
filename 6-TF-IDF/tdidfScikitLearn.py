from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

d1 = "O rato roeu a roupa do rei de Roma."
d2 = "Nenhum rato roi a roupa do rei de Roma sem punicao."
d3 = "A rota de fuga do rato foi rapida."

corpus = [d1,d2,d3]

vectorizer = TfidfVectorizer()
matriz_tfidf = vectorizer.fit_transform(corpus)

termos = vectorizer.get_feature_names_out()

for i, linha in enumerate(matriz_tfidf.toarray()):
    print(f"\nDocumento d{i + 1}: {corpus[i]}")
    for termo, peso in zip(termos, linha):
        if peso > 0:
            print(f"  {termo:10s} tf-idf={peso:.3f}")

query = input("\nDigite uma query: ")
vetor_query = vectorizer.transform([query])

similaridades = cosine_similarity(vetor_query, matriz_tfidf)[0]

print(f"\nQuery: {query}")
for i, similaridade in enumerate(similaridades):
    print(f"  d{i + 1} ({corpus[i]}) -> similaridade={similaridade:.3f}")
