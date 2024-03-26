import pandas as pd
import spacy
from textblob import TextBlob

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Function for sentiment analysis
def predict_sentiment_spacy(review):
    doc = nlp(review)
    sentiment_score = 0
    for token in doc:
        sentiment_score += token.sentiment
    sentiment_label = 'Positive' if sentiment_score >= 0 else 'Negative'
    return sentiment_label

# Function for sentiment analysis 
def predict_polarity_textblob(review):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    return polarity

# Function to calculate similarity between two reviews
def calculate_similarity(review1, review2):
    doc1 = nlp(review1.lower().strip())
    doc2 = nlp(review2.lower().strip())
    similarity_score = doc1.similarity(doc2)
    return similarity_score

data = pd.read_csv(r"task21_capstone_project.py\amazon_product_reviews.csv")

clean_data = data.dropna(subset=['reviews.text'])

clean_data['sentiment_spacy'] = clean_data['reviews.text'].apply(predict_sentiment_spacy)

clean_data['polarity_textblob'] = clean_data['reviews.text'].apply(predict_polarity_textblob)


review1 = clean_data['reviews.text'].iloc[45]  
review2 = clean_data['reviews.text'].iloc[321]  

# Calculate similarity between the chosen reviews
similarity_score = calculate_similarity(review1, review2)

print("Review 1:", review1)
print("Review 2:", review2)
print("Similarity Score:", similarity_score)
