import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
clean_text = lower_case.translate(str.maketrans("", "", string.punctuation))
tokenised_words = word_tokenize(clean_text, "english")


final_words = []
for word in tokenised_words :
    if word not in stopwords.words("english"):
        final_words.append(word)
emotion_list = []        
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        
        
        if word in final_words:
            emotion_list.append(emotion)

w = Counter (emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    
    if neg > pos :
        print(" This text have a negative vibe")
    elif pos > neg :
        print("This text have a positive vibe")
    else:
        print("This text have a neutral vibe")

sentiment_analyse(clean_text )    

plt.bar(w.keys(), w.values())
plt.savefig('graph.png')
plt.show()