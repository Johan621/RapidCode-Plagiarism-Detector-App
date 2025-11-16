from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(code1, code2):
    docs = [code1, code2]
    tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    matrix = tfidf.fit_transform(docs)
    sim = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(sim * 100, 2)
