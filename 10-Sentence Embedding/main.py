# pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Textos em inglês
model = SentenceTransformer('all-MiniLM-L6-v2')

# Textos em 15 línguas diferentes, incluindo PT-BR
model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

sentencas1 = ['Shipment of gold damaged in a fire',
'Delivery of silver arrived in a silver truck',
'Shipment of gold arrived in a truck']

sentencas2 = ['gold silver truck',
'gold silver truck',
'gold silver truck']

embeddings1 = model.encode(sentencas1, convert_to_tensor=True)
embeddings2 = model.encode(sentencas2, convert_to_tensor=True)
cosine_scores = util.cos_sim(embeddings1, embeddings2)
for i in range(len(sentencas1)):
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentencas1[i], sentencas2[i], cosine_scores[i][i]))