import streamlit as st
import pickle
import string
import re
import sklearn
#from sklearn.exceptions import InconsistentVersionWarning
import warnings
import pickle
import numpy as np


bow1 = pickle.load(open('cv.pkl', 'rb'))
bow2=  pickle.load(open('cv2.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
st.title("Amazon Fine Food Review ")
input_sms1 = st.text_area("Enter the summary of Review")
input_sms2=st.text_area("Enter the Exact Reviews")
input_sms3=st.text_area("Enter Helpfullness Numerator")
input_sms4=st.text_area("Enter Helpfullness Denominator")
# preprocess
def remove_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    return re.sub(url_pattern, '', text)
# remove tags
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result

# remove punctuation
exclude=string.punctuation
def remove_punc(text):
    for char in exclude:
        text =text.replace(char,"")
    return text
## stopwords

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])
# convert lower
def lower1(text):
    return text.lower()
# remove stop word
def remove_stop(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)

if st.button('Predict'):

    input_sms1 = remove_urls(input_sms1)
    input_sms1 = remove_tags(input_sms1)
    input_sms1 = remove_punc(input_sms1)
    input_sms1 = remove_stop(input_sms1)
    input_sms1 = lower1(input_sms1)

    input_sms2 = remove_urls(input_sms2)
    input_sms2 = remove_tags(input_sms2)
    input_sms2 = remove_punc(input_sms2)
    input_sms2 = remove_stop(input_sms2)
    input_sms2 = lower1(input_sms2)
    vector_input1 = bow2.transform([input_sms1])
    vector_input2 = bow1.transform([input_sms2])


    # Assuming vector_input1 and vector_input2 are sparse matrices, and input_sms3 and input_sms4 are numbers
    # Convert vector_input1 and vector_input2 to dense arrays for stacking
    vector_input1_dense = vector_input1.toarray()[0]
    vector_input2_dense = vector_input2.toarray()[0]

    # Combine vector_input1_dense, vector_input2_dense, input_sms3, and input_sms4 into a single feature vector
    # Make sure to reshape input_sms3 and input_sms4 to have the same shape as vector_input1_dense
    feature_vector = np.hstack((vector_input1_dense, vector_input2_dense, int(input_sms3), int(input_sms4)))

    # Now, you can use feature_vector for prediction
    result = model.predict([feature_vector])[0]

    if result == 1:
        st.header("Positive")
    if result == 0:
        st.header("Negative")





