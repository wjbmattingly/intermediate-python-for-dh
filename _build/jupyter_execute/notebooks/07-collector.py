#!/usr/bin/env python
# coding: utf-8

# # Collector from Collections
# 
# The Python `collections` library is a powerful module that extends the built-in collection types such as lists, dictionaries, and tuples. In this tutorial, we will explore some important classes in the collections module, like `Counter`, `deque`, `namedtuple`, `OrderedDict`, and `defaultdict`.
# 
# In this tutorial, we'll explore the `Counter()` class from the collections module in Python. This is a beginner-friendly tutorial, so don't worry if you're new to Python programming. We'll guide you through the basics step by step.
# 
# ## What is a Counter?
# 
# A `Counter` is a Python class that allows you to count the occurrences of elements in a collection, such as a list, tuple, or string. It is a subclass of the built-in dict class, so you can use it just like a regular dictionary.
# 
# ## Why use a Counter?
# 
# `Counter` can be incredibly useful when you need to count elements in a collection and store the results in a dictionary-like format. It simplifies the process by handling all the counting logic for you.
# 
# ## Importing Counter
# 
# Before we can use the `Counter()` class, we need to import it from the `collections` module. Here's how to do that:

# In[3]:


from collections import Counter


# ## Creating a Counter
# 
# To create a new Counter object, simply pass a collection (like a list, tuple, or string) as an argument to the `Counter()` function. Let's see an example:

# In[4]:


words = ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']
word_counter = Counter(words)

print(word_counter)


# As you can see, the Counter object counts the occurrences of each word in the words list and stores the result as a dictionary.
# 
# ## Accessing Counts
# 
# You can access the count of an element using the square bracket notation, just like you would do with a regular dictionary:

# In[5]:


to_count = word_counter['to']
print(to_count)


# In some instances, we may write code where we try count words that do not appear in the `Counter`. Rather than throwing an error, `Counter` will simply return a 0.

# In[6]:


print(word_counter["and"])


# ## Updating Counts
# 
# To update the counts in a `Counter`, you can use the `update()` method. This method takes an iterable as an argument and updates the counts accordingly:

# In[6]:


more_words = ['to', 'be', 'or', 'not', 'to', 'be']
word_counter.update(more_words)

print(word_counter)


# ## Finding Most Common Elements
# 
# Use the `most_common()` method to get a list of the n most common elements and their counts:

# In[7]:


top_three_words = word_counter.most_common(3)
print(top_three_words) 


# In[ ]:


word_counter.clear()
print(word_counter)


# ## Real Example for Finding Frequency in text.
# 
# Now that you have a basic understanding of how to use the `Counter()` class, let's see a practical example in the context of humanities research. In this example, we will count the frequencies of words in a given text. There are better ways to split a text (such as via spaCy), but for this example, the simple `split()` function will suffice.

# In[7]:


text = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them."""

# Convert the text to lowercase and split it into a list of words
words = text.lower().split()

# Create a Counter object to count the word occurrences
word_counter = Counter(words)

# Print the word frequencies
print(word_counter)


# Wth the word frequencies calculated, you can perform various analyses, such as finding the most common words, identifying themes, or comparing the usage of words across different texts. The Counter class is a powerful tool for humanities research, offering an easy and efficient way to count and analyze elements in a collection.

# In[ ]:




