"""
GLAB 927.4.1: Hands-On Sentiment Analysis With Python
Student: Anthony Emmanuel

Sentiment analysis is a Natural Language Processing (NLP) technique that
figures out the emotional tone of a piece of text.

This program uses the TextBlob library to measure two things:
    - Polarity:     how negative or positive the text is
                    (-1.0 = very negative, 0 = neutral, 1.0 = very positive)
    - Subjectivity: how much the text is opinion instead of fact
                    (0.0 = pure fact, 1.0 = pure opinion)

How to run:
    uv run sentiment-analysis
"""

# Importing TextBlob library
from textblob import TextBlob


# ---------------------------------------------------------------
# Task 1: Importing Libraries
# ---------------------------------------------------------------
def task_1_check_installation():
    # Sample text for checking TextBlob installation
    sample_text = "TextBlob is successfully installed and ready to use!"

    # Print confirmation message
    print(f"TextBlob library successfully imported. Sample text: {sample_text}")
    print()


# ---------------------------------------------------------------
# Task 2: Implementing Sentiment Analysis
# ---------------------------------------------------------------
def task_2_single_text():
    # Sample text for sentiment analysis (feedback on a new product launch)
    sample_text = "I absolutely love this product! The quality is excellent and it arrived on time."

    # Create a TextBlob object so TextBlob can study the text
    blob = TextBlob(sample_text)

    # Perform sentiment analysis (gives us polarity and subjectivity)
    sentiment = blob.sentiment

    # Print the original text and sentiment analysis results
    print("=== Task 2: Sentiment Analysis ===")
    print("Original Text:", sample_text)
    print("Sentiment Analysis Result:")
    print("Polarity:", sentiment.polarity)  # Range from -1 (negative) to 1 (positive)
    print("Subjectivity:", sentiment.subjectivity)  # Range from 0 (objective) to 1 (subjective)
    print()


# ---------------------------------------------------------------
# Task 3: Analyzing Business Communication Data
# ---------------------------------------------------------------

# Function to analyze sentiment of each comment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


# Extra: turn a polarity number into a word a manager can understand
def label_sentiment(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def task_3_customer_feedback():
    # Sample customer feedback comments about recent service improvements
    feedback_comments = [
        "The service was fantastic and the staff was very helpful.",
        "I am unhappy with the product quality and delivery was delayed.",
        "The product is okay, but it could be improved.",
        "Amazing experience! I am very satisfied with my purchase.",
    ]

    # Analyze and print sentiment for each feedback comment
    print("=== Task 3: Customer Feedback Analysis ===")
    polarity_scores = []  # empty list to collect every score

    for comment in feedback_comments:
        sentiment = analyze_sentiment(comment)
        polarity_scores.append(sentiment)
        print(f"Feedback: {comment}")
        print(f"Sentiment Polarity: {sentiment}")
        print(f"Sentiment Label: {label_sentiment(sentiment)}")
        print("-----")

    # Extra: find the overall average to see the big-picture trend
    average_polarity = sum(polarity_scores) / len(polarity_scores)
    print(f"Average Polarity of All Feedback: {average_polarity:.2f}")
    print(f"Overall Customer Sentiment: {label_sentiment(average_polarity)}")


# ---------------------------------------------------------------
# main(): runs every task in order.
# This is the "front door" of the app. The command
# `uv run sentiment-analysis` calls this function.
# ---------------------------------------------------------------
def main():
    task_1_check_installation()
    task_2_single_text()
    task_3_customer_feedback()


# Lets the file also run directly with:
#   uv run python src/sentiment_analysis/sentiment_analysis.py
if __name__ == "__main__":
    main()