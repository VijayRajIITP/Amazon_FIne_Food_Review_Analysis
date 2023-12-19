# Amazon Fine Food Review Analysis
<img width="771" alt="food_review_outout_png" src="https://github.com/VijayRajIITP/Amazon_FIne_Food_Review_Analysis/assets/149241319/12dc18bd-3a7a-495f-896a-5be999936454">

**Introduction:**

Sentiment analysis of Amazon Fine Food reviews involves classifying the sentiment (positive, negative) expressed in the reviews. It helps organizations understand customer sentiment and make data-driven improvements.

**Life Cycle Of Projects:**

1. **Dataset:** I downloaded the dataset from Kaggle. You can find it [here](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews).

2. **Data Preprocessing:**
   - Tokenization: Split the text into individual words or tokens.
   - Stopword Removal: Remove common words (e.g., "the," "and") that don't carry much sentiment.
   - Removing URL, HTML tags, and punctuation.
   - Lemmatization or stemming: Reduce words to their base or root form.
   - Lowercasing: Convert all text to lowercase for consistent analysis.

3. **Why Convert Text to a Vector?**
   - We convert words into vectors to apply mathematical concepts like linear algebra.
   - It ensures that similar texts are closer geometrically (distance between vectors should be less).

4. **Feature Extraction:**
   - TF-IDF Vectorization: Transform text into numerical feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency) or Count Vectorization.
   - Word Embeddings: Use pre-trained word embeddings like Word2Vec, GloVe, or fastText for semantic understanding of words.

5. **Model Selection:** Use machine learning models like Random Forest, or more complex models like LSTM or BERT.

6. **Checking Accuracy:** Assess model performance, including precision and recall.

7. **Deployemnet:** Leveraging Streamlit, I effectively deployed my model and conducted comprehensive testing on Amazon reviews sourced directly from the website

**Dataset Explanation:**

**Amazon Fine Food Reviews Analysis**

- Data Source: [Kaggle Dataset](https://www.kaggle.com/snap/amazon-fine-food-reviews)
- EDA: [EDA Techniques](https://nycdatascience.com/blog/student-works/amazon-fine-foods-visualization/)

**Dataset Details:**

- Number of reviews: 568,454
- Number of users: 256,059
- Number of products: 74,258
- Timespan: Oct 1999 - Oct 2012
- Number of Attributes/Columns in data: 10

**Attribute Information:**

1. Id
2. ProductId - unique identifier for the product
3. UserId - unique identifier for the user
4. ProfileName
5. HelpfulnessNumerator - number of users who found the review helpful
6. HelpfulnessDenominator - number of users who indicated whether they found the review helpful or not
7. Score - rating between 1 and 5
8. Time - timestamp for the review
9. Summary - brief summary of the review
10. Text - text of the review

**Objective:**

Given a review, determine whether the review is positive (rating of 4 or 5) or negative (rating of 1 or 2).

