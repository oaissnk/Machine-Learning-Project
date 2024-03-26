import spacy
from textblob import TextBlob


nlp = spacy.load("en_core_web_sm")

#Function for sentiment analysis 
def predict_sentiment_spacy(review):
    doc = nlp(review)
    sentiment_score = 0
    for token in doc:
        sentiment_score += token.sentiment
    sentiment_label = 'Positive' if sentiment_score >= 0 else 'Negative'
    return sentiment_label

#Function for sentiment analysis 
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

# Examples
reviews = [
    "I order 3 of them and one of the item is bad quality. Is missing backup spring so I have to put a pcs of aluminum to make the battery work.",
    "Bulk is always the less expensive way to go for products like these.",
    "Well they are not Duracell but for the price i am happy.",
    "Seem to work as well as name brand batteries at a much better price.",
    "These batteries are very long lasting the price is great.",
    "Bought a lot of batteries for Christmas and the AmazonBasics Cell have been good. I haven't noticed a difference between the brand name batteries and the Amazon Basic brand. Just a lot easier to purchase and have arrive at the house and have on hand. Will buy again.",
    "I've not had any problem with these batteries have ordered them in the past been very pleased."
]

# Apply sentiment analysis using spaCy to examples
sentiments_spacy = [predict_sentiment_spacy(review) for review in reviews]

# Apply polarity calculation using TextBlob to examples
polarities_textblob = [predict_polarity_textblob(review) for review in reviews]


review1 = reviews[0]  
review2 = reviews[1]  

# Calculate similarity between the chosen reviews
similarity_score = calculate_similarity(review1, review2)

print("Sentiments (spaCy):", sentiments_spacy)
print("Polarities (TextBlob):", polarities_textblob)
print("Similarity Score between review 1 and review 2:", similarity_score)


