from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font for the title
pdf.set_font("Arial", size=16)

# Title
pdf.cell(200, 10, txt="Sentiment Analysis Report", ln=True, align="C")

# Line break
pdf.ln(10)

# Set font for the sections
pdf.set_font("Arial", size=12)

# Section 5.1: Description of the Dataset Used
pdf.cell(200, 10, txt="5.1 Description of the Dataset Used:", ln=True)
pdf.multi_cell(0, 10, "The dataset used for sentiment analysis consists of 28,322 rows of Amazon customer reviews. Each row contains data regarding a single customer review, including the review text, product information, and other relevant details. The data is stored in a CSV file format, making it easy to access and analyze using Python libraries such as pandas.")
pdf.ln(5)

# Section 5.2: Details of the Processing Steps
pdf.cell(200, 10, txt="5.2 Details of the Processing Steps:", ln=True)
pdf.multi_cell(0, 10, "The processing steps for sentiment analysis involved several key components:\n\n- Data loading: The dataset was loaded into memory using the pandas library, allowing for easy manipulation and analysis.\n\n- Text preprocessing: Text preprocessing techniques, such as tokenization and stop-word removal, were applied to clean the review text and prepare it for analysis.\n\n- Sentiment analysis: Sentiment analysis was performed using two different approaches:\n  - TextBlob library: The TextBlob library was used to calculate the polarity of each review text, providing a measure of sentiment ranging from -1 (negative) to 1 (positive).\n  - spaCy library: The spaCy library was used to perform sentiment analysis based on pre-trained models, assigning each review a sentiment label (positive or negative) based on the sentiment score calculated for the text.")
pdf.ln(5)

# Section 5.3: Evaluation of Results
pdf.cell(200, 10, txt="5.3 Evaluation of Results:", ln=True)
pdf.multi_cell(0, 10, "The results obtained from the sentiment analysis were found to be accurate based on the evaluation conducted during the analysis process. The accuracy of the sentiment predictions was verified by comparing the predicted sentiment labels with the actual sentiments expressed in the customer reviews. Additionally, the results were validated using exploratory data analysis techniques to identify patterns and trends in the sentiment distributions across different product categories or time periods.")
pdf.ln(5)

# Section 5.4: Insights into the Model's Strengths and Limitations
pdf.cell(200, 10, txt="5.4 Insights into the Model's Strengths and Limitations:", ln=True)
pdf.multi_cell(0, 10, "The sentiment analysis model implemented using spaCy and TextBlob demonstrated several strengths, including:\n\n- Accuracy: The model achieved high accuracy in predicting sentiment labels for customer reviews.\n\n- Efficiency: The model's computational efficiency allowed for fast and scalable sentiment analysis of large datasets.\n\n- Flexibility: The model's flexibility enabled customization and fine-tuning to suit specific requirements or domains.\n\nHowever, the model also has some limitations, such as:\n\n- Dependency on pre-trained models: The accuracy of the sentiment analysis may be affected by the quality and relevance of the pre-trained models used by spaCy.\n\n- Sensitivity to context: The model's performance may vary depending on the context and language used in the customer reviews, leading to potential biases or inaccuracies in sentiment predictions.")
pdf.ln(5)

# Save the PDF
pdf.output("sentiment_analysis_report.pdf")
