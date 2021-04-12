import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from textblob import TextBlob
import spacy
import re
# from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk
nltk.download('wordnet')

def polarity(s):  
	if s>0:
		return "Positive"
	if s<0:
		return "Negative"
	else:
		return "Neutral" 

def preprocess(text):
	result = []
	for token in gensim.utils.simple_preprocess(text):
		if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
			result.append(token)
	return result

def model_call(t):
	T=t
	sp = spacy.load('en_core_web_sm')
	sen = sp(t)
	names=[str(x) for x in sen.ents]
	for x in names:
		t=t.replace(x,"/NAMED/",1)
	sentences=t.split('.')

	l=[]
	l.append(sentences[0])
	for i in range(1,len(sentences)-1):
		words=sentences[i].split(" ")
		prev_word=sentences[i-1].split(" ")[-1]
		if prev_word[0].isupper() and len(prev_word)<=3:
			l[len(l)-1]=l[len(l)-1]+"."+sentences[i]
		else:
			l.append(sentences[i])

	count=0

	for i in range(len(l)):
		if count<len(names) and re.search("/NAMED/",l[i]):
			C=len(re.findall("/NAMED/",l[i]))
			for e in range(C):
				l[i]=l[i].replace("/NAMED/",names[count],1)
				count+=1
		
	F=[]

	for i in range(len(l)):
		if "!" in l[i]:
			w=l[i].split("!")
			F.append(w[0]+"!")
			F.append(w[1]+".")  
		if "?" in l[i]:
			w=l[i].split("?")
			F.append(w[0]+"?")
			F.append(w[1])  
		else:
			F.append(l[i]+".")      


	scores=[TextBlob(sentence).sentiment.polarity for sentence in F]
	sentiment=[]
	for s in scores:
		if s>0:
			sentiment.append("Positive")
		if s<0:
			sentiment.append("Negative")
		else:
			sentiment.append("Neutral")  
			  
	S=polarity(TextBlob(t).sentiment.polarity)    

	pre=preprocess(T)
	dictionary = gensim.corpora.Dictionary([pre])
	bow_corpus = [dictionary.doc2bow(doc) for doc in [pre]]
	lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=3, id2word=dictionary, passes=2, workers=2)
	E=lda_model.show_topics(formatted=False, num_words= 10)
	topics=[]

	for x in E[0][1]:
		topics.append(x[0])
	string=topics[0]+", "+topics[1]+" and "+topics[2] 

	return sentiment,F,S,string