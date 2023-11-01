# Amazon_FIne_Food_Review_Analysis

Sentiment analysis of Amazon Fine Food reviews involves classifying the sentiment (positive, negative) expressed in the reviews.Sentiment analysis helps organizations understand how customers feel about their products, services, or brands based on customer reviews, surveys, and social media comments. It allows companies to gauge customer satisfaction and make data-driven improvements.
Steps of Projects
1.Dataset : I downloaded Dataset from Kagggle. Here are the Link of Datasets 
https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
2.Data Preprocssing :
.Tokenization: Split the text into individual words or tokens.
.Stopword Removal: Remove common words (e.g., "the," "and") that don't carry much sentiment.
.Removing URL,Html tags and Punctuation words 
.Lemmatization or Stemming: Reduce words to their base or root form.
.Lowercasing: Convert all text to lowercase for consistent analysis.
3. WHY CONVERT TEXT TO A VECTOR?(Interview Question)
We convert Words Into Vector Because We can use  Easily Apply Math Concept Like Linear Algebra
and We convert into Vector Such That similar texts must be closer geometrically(Distance Between Vectors Should Be Less)
4.Feature Extraction:
TF-IDF Vectorization: Transform the text into numerical feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency) or Count Vectorization.
Word Embeddings: Use pre-trained word embeddings like Word2Vec, GloVe, or fastText for semantic understanding of words.
5.Model Selection:
I have used Random Forest But You can use Much more complex Neural Network Like LSTM , BERT
6.Checking Accuracy:
I got approx 90 percent accuracy .For More details about Precision and  Recall Please Check My python notebook.




## Data Set Expalaination:
# Amazon Fine Food Reviews Analysis


Data Source: https://www.kaggle.com/snap/amazon-fine-food-reviews <br>

(This is one of The Best EDA Techniques)
EDA: https://nycdatascience.com/blog/student-works/amazon-fine-foods-visualization/


The Amazon Fine Food Reviews dataset consists of reviews of fine foods from Amazon.<br>

Number of reviews: 568,454<br>
Number of users: 256,059<br>
Number of products: 74,258<br>
Timespan: Oct 1999 - Oct 2012<br>
Number of Attributes/Columns in data: 10 

Attribute Information:

1. Id
2. ProductId - unique identifier for the product
3. UserId - unqiue identifier for the user
4. ProfileName
5. HelpfulnessNumerator - number of users who found the review helpful
6. HelpfulnessDenominator - number of users who indicated whether they found the review helpful or not
7. Score - rating between 1 and 5
8. Time - timestamp for the review
9. Summary - brief summary of the review
10. Text - text of the review


#### Objective:
Given a review, determine whether the review is positive (rating of 4 or 5) or negative (rating of 1 or 2).


[Q] How to determine if a review is positive or negative?<br>

[Ans] We could use Score/Rating. A rating of 3 or 4 or 5 can be cosnidered as a positive review. A rating of 1 or 2 can be considered as negative one. This is an approximate and proxy way of determining the polarity (positivity/negativity) of a review.






