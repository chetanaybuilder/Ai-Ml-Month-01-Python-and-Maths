#importing required libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path


#load dataset
file_path = Path("data/sentences.txt")

with open(file_path,"r") as file:
    sentences = [line.strip() for line in file if line.strip()]


# initialize TF-IDF
vectorizer = TfidfVectorizer()


#convert all sentences into numerical vectors
vectors = vectorizer.fit_transform(sentences)


#get user query
query = input("\nEnter your search query:")

#convert query into vector
query_vector = vectorizer.transform([query])


#calculating cosine similarity
scores = cosine_similarity(query_vector, vectors)


#rank sentences by similarity
ranked_indices = np.argsort(scores[0])[::-1]


#display top 5 match
print("\nTop 5 similar sentence:")

for rank , index in enumerate(ranked_indices[:5], start=1):

    sentence = sentences[index]
    score = scores[0][index]


print(f"\nRank: {rank}")
print(f"\nSentence: {sentence}")
print(f"\nSimilarity: {score:.4f}")