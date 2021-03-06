# Assignment 2
This repo has been updated to work with `Python v3.8` and up.

## About the project
In this project, we have been asked to use a paragraph of a minimum of 2000 words to work on. We have to segment the text into sentences and then have to calculate scores on them. At last, we had to generate a topic for the paragraph.

### model.py
This file contains three functions polarity, preprocess and model_call.

#### preprocess(text)
It uses the gensim library to clean text and remove stopwords from the text. We have to perform this preprocessing before generating the topic.

#### polarity(score)
It gives output as "positive", "negative" and "neutral" based on the polarity of the sentiment score.

#### model_call(text)
This is the function which is called from app.py. We think of splitting the text by ".". The problems which we will face by doing this are as follows-:
1. If any name (with ".") or designation is present in the text (eg. Mr./Dr./Er. K. Singh or C.Ronaldo Jr.)
2. If any decimal number is present in the text
3. If there are " ? " and " ! " are present in the text. (We could have included ":" and ";" in this but these punctuations are used to add sentences)

#### Our approach
Before splitting, we found the named entities in the text using Spacy module, and replaced them with "/NAMED/". Found entities will be saved as a list. Named entities include all the names of  people, places, brands, monetary values. This also includes the numbers which are present in the data. So, it helps us with the problems 1 and 2. <br /><br />
For eg., Er. K. Singh is an engineer.
It gets converted to Er. /NAMED/ is an engineer.<br /><br />
Still, it doesn't catch the Mr./Dr./Mrs. present before the name so we have to add this separately in our code. We know that any designation follows majorly these conditions i.e. maximum of 3 characters long and have a capital letter at the beginning. For this, after splitting the text by "." and saving the result into the list, we iterate and check if the last word of the list item follows the aforementioned conditions. If found we will add the list items.<br /><br />
Now, we will replace "/NAMED/" with entities from the list.
For the last problem, we will split once again the list items "?" and "!" if they are present in the text.

We perform these steps here-:
1.  Sentence segmentation approach using the above approach.
2.  Sentiment score calculation using Textblob.
3.  We will perform the topic modelling using the LDA model.

### app.py
Use this to run the server.

Note: I had developed an environment for that.

#### How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
![image](https://user-images.githubusercontent.com/65654054/114431595-4a350b00-9bdd-11eb-8de6-da211ac2ab0d.png)
