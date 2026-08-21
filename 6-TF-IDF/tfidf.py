"""
Giuseppe Filippin
Isabelle Lopes
Pedro Leite
Felipe Augusto
"""
import re
import math
from collections import Counter

STOPWORDS = {
    "o", "a", "os", "as", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "um", "uma", "uns", "umas",
    "e", "ou", "que", "com", "sem", "por", "para", "se"
}


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text, flags=re.UNICODE)
    tokens = text.split()
    return [t for t in tokens if t not in STOPWORDS]


def build_vocabulary(docs_tokens):
    vocab = set()
    for tokens in docs_tokens:
        vocab.update(tokens)
    return sorted(vocab)


def compute_tf(tokens, vocab):
    counts = Counter(tokens)
    total = sum(counts.values())
    return {term: (counts.get(term, 0) / total if total > 0 else 0.0) for term in vocab}


def compute_idf(docs_tokens, vocab):
    N = len(docs_tokens)
    idf = {}
    for term in vocab:
        df = sum(1 for tokens in docs_tokens if term in tokens)
        idf[term] = math.log(N / df) if df > 0 else 0.0
    return idf


def compute_tfidf(tf, idf, vocab):
    return {term: tf[term] * idf[term] for term in vocab}


def similarity(vec_q, vec_d, vocab):
    return sum(vec_q[term] * vec_d[term] for term in vocab)


def print_matrix(title, vocab, rows):
    print(f"\n{title}")
    header = " " * 10 + "".join(f"{t[:9]:>11}" for t in vocab)
    print(header)
    for name, vec in rows:
        line = f"{name:<10}" + "".join(f"{vec[t]:>11.4f}" for t in vocab)
        print(line)


def main():
    corpus = [
        "O rato roeu a roupa do rei de Roma.",
        "Nenhum rato roi a roupa do rei de Roma sem punicao.",
        "A rota de fuga do rato foi rapida."
    ]

    print("TF-IDF:\n")
    for i, d in enumerate(corpus, 1):
        print(f'  d{i}: "{d}"')

    docs_tokens = [tokenize(d) for d in corpus]
    vocab = build_vocabulary(docs_tokens)

    print(f"\ntermos do vocab:")
    print("  " + ", ".join(vocab))

    # IDF calculado sobre o corpus de documentos
    idf = compute_idf(docs_tokens, vocab)

    for term in vocab:
        print(f'  idf("{term}") = {idf[term]:.4f}')

    # TF-IDF de cada documento
    tfidf_docs = []
    for i, tokens in enumerate(docs_tokens, 1):
        tf = compute_tf(tokens, vocab)
        tfidf = compute_tfidf(tf, idf, vocab)
        tfidf_docs.append((f"d{i}", tfidf))

    print_matrix("matriz TF-IDF:", vocab, tfidf_docs)

    # Query digitada pelo usuario
    query = input("\ndigite uma query:\n> ").strip()
    if not query:
            exit()
    q_tokens = tokenize(query)
    q_tokens_in_vocab = [t for t in q_tokens if t in vocab]

    if not q_tokens_in_vocab:
        print("\nNenhum termo dessa query aparece no vocabulario dos documentos.")
        return

    tf_q = compute_tf(q_tokens_in_vocab, vocab)
    tfidf_q = compute_tfidf(tf_q, idf, vocab)

    print_matrix("vetor TF-IDF:", vocab, [("q", tfidf_q)])

    print("\n coeficiente de similaridade SC:")
    results = []
    for name, vec_d in tfidf_docs:
        sc = similarity(tfidf_q, vec_d, vocab)
        results.append((name, sc))
        print(f"  SC(q, {name}) = {sc:.6f}")

    results.sort(key=lambda x: x[1], reverse=True)
    mais_proximo, valor = results[0]
    print(f"\nO documento mais parecido com a sua query e o {mais_proximo}.")
    print("Ranking completo, do mais ao menos parecido:")
    for rank, (name, sc) in enumerate(results, 1):
        print(f"  {rank}o lugar: {name}  (SC = {sc:.6f})")


if __name__ == "__main__":
    main()
