import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2021/07/06/19/26/drops-6392473__340.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()

filename = 'fake_classifier.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
tfid_transformer = pickle.load(open('transformer.pkl','rb'))

st.title("Fake News Classifier")

sentence = st.text_area('Input your sentence here:')
port_stem = PorterStemmer()
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
sentence = stemming(sentence)

sentence = tfid_transformer.transform([sentence])

if st.button('Predict'):
    try:
        output = loaded_model.predict(sentence)
        if output ==  0:
            def header(text):
                st.markdown('<p style="background-color:powderblue;color:black;font-size:24px;border-radius:2%;">{}</p>'.format(text),
                            unsafe_allow_html=True)
            header(' It\'s not a fake News')
        else:
            def header(text):
                st.markdown('<p style="background-color:Tomato;color:black;font-size:24px;border-radius:2%;">{}</p>'.format(text),
                            unsafe_allow_html=True)
            header('It is Fake news')
    except:
        print('Exception has occured')


