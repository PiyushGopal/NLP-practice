#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk')


# In[2]:


paragraph = """
Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] (listen); born 17 September 1950)[b] is an Indian politician who has served as the 14th Prime Minister of India since May 2014. Modi was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister from outside the Indian National Congress.

Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at age eight. His account of helping his father sell tea at the Vadnagar railway station has not been reliably corroborated. At age 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. After the state of emergency was declared by Prime Minister Indira Gandhi in 1975, he went into hiding. The RSS assigned him to the BJP in 1985 and he held several positions within the party hierarchy until 2001, rising to the rank of general secretary.[c]
"""


# In[3]:


paragraph


# In[4]:


import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


# In[5]:


##tokenization-- converts paragraph-sentences-words
nltk.download('punkt')
sentences = nltk.sent_tokenize(paragraph)
sentences


# In[6]:


#stemming finds base of words
stemmer = PorterStemmer()
stemmer.stem('history')


# In[7]:


stemmer.stem('going')


# In[12]:





# In[15]:


nltk.download('wordnet', quiet=True)


# In[16]:


#lemmatizer doesnt changes the meaning of the words
from nltk.stem import WordNetLemmatizer


# In[17]:


lemmatizer = WordNetLemmatizer()


# In[11]:


lemmatizer.lemmatize('drinking')


# In[ ]:




