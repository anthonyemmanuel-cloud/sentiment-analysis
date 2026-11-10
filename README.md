# Sentiment Analysis with TextBlob

**GLAB 927.4.1: Hands-On Sentiment Analysis With Python**
Per Scholas AI Prompt Engineering (2026-CAX-255) · Anthony Emmanuel

## What this app does

This program uses Python's **TextBlob** library to read customer feedback and measure its emotional tone:

- **Polarity** tells how negative or positive the text is, from **-1.0** (very negative) to **1.0** (very positive).
- **Subjectivity** tells how much the text is opinion instead of fact, from **0.0** (fact) to **1.0** (opinion).

It also labels each comment **Positive**, **Negative** or **Neutral**, and calculates the **average** sentiment of all comments.

## What problem it solves

Businesses get more reviews, emails and social media comments than people can read. Sentiment analysis sorts them automatically, so a team can quickly find unhappy customers and see whether overall satisfaction is going up or down.

## Technologies used

-    - Python 3.13+
- uv for project and dependency management
- TextBlob for sentiment analysis

## How to install dependencies

```bash
uv sync
```

## How to run

```bash
   uv run sentiment-analysis
```

## Expected results

| Feedback | Polarity | Label |
|---|---|---|
| The service was fantastic and the staff was very helpful. | 0.30 | Positive |
| I am unhappy with the product quality and delivery was delayed. | -0.60 | Negative |
| The product is okay, but it could be improved. | 0.50 | Positive |
| Amazing experience! I am very satisfied with my purchase. | 0.70 | Positive |

**Average polarity:** 0.23 (Positive overall)

## What I learned

TextBlob scores words from a built-in list. It rated *"okay, but it could be improved"* as **positive (0.50)**, even though a person would read it as neutral or slightly negative. Sentiment tools are helpful for sorting large amounts of text, but people should still review the results before making business decisions.