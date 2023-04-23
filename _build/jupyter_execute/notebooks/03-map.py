#!/usr/bin/env python
# coding: utf-8

# # Python Map Function Tutorial: Working with Strings
# 
# This tutorial will introduce you to the map() function in Python, with a focus on working with strings. We'll use examples from Edgar Allan Poe's works to demonstrate the concepts in a manner that is relevant to humanists.
# 
# ## Example of a Problem
# 
# Imagine we wanted to count the length of every line in Edgar Allan Poe's famous poem, "The Raven." Let's try and solve this problem. First, let's create a list containing a few lines from the poem:

# In[5]:


lines = [
    "Once upon a midnight dreary, while I pondered, weak and weary,",
    "Over many a quaint and curious volume of forgotten lore—",
    "While I nodded, nearly napping, suddenly there came a tapping,",
    "As of some one gently rapping, rapping at my chamber door.",
]


# Now that we have our data, let's count each line with a `for` loop.

# In[6]:


line_lengths_list = []

for line in lines:
    line_length = len(line)
    line_lengths_list.append(line_length)

print(line_lengths_list)


# By using a for loop, we iterate through each line in the `lines` list, calculate the length of each line with `len(line)`, and append the result to the `line_lengths_list`. In this tutorial, we will learn about how the `map()` function can make this problem far simpler to solve with far less code.

# ## What is the `map()` function?
# 
# The `map()` function is a built-in Python function that allows you to apply a function to every item in an iterable (such as a list or tuple) and returns an iterable `map` object, which can be converted into a list or other iterable data structure.
# 
# 
# The `map()` function has the following syntax:
# 
# ```python
# map(function, iterable)
# ```
# 
# ## Basic usage of the map() function with strings
# 
# Let's start with a simple example. Suppose we have a list of strings containing lines from the same poem. We want to find the length of each line in the poem.
# 
# Let's use the same data.

# In[1]:


lines = [
    "Once upon a midnight dreary, while I pondered, weak and weary,",
    "Over many a quaint and curious volume of forgotten lore—",
    "While I nodded, nearly napping, suddenly there came a tapping,",
    "As of some one gently rapping, rapping at my chamber door.",
]


# Now, let's use the `map()` function to find the length of each line. We'll use the built-in `len()` function as the function to apply to each line:

# In[2]:


line_lengths = map(len, lines)

# Convert the map object to a list
line_lengths_list = list(line_lengths)

# Print the result
print(line_lengths_list)


# The `map()` function has applied the len() function to each line in the list, and the results have been returned in a new list.
# 
# ## Using custom functions with map()
# 
# Now let's create a custom function to count number of words in each line with split. We'll use this function with the `map()` function.
# 
# First, let's create the custom function:

# In[14]:


def count_words(line):
    return len(line.split())


# Now, let's use the `map()` function with our custom function to count the number of words in each line.

# In[15]:


word_counts = list(map(count_words, lines))
print(word_counts)


# The `map()` function has applied our custom `count_words()` function to each line in the list, and the results have been returned in a new list.
# 
# Often, when we use `map()`, we use it alongside `lambda` functions. We will meet those in the next tutorial.

# In[ ]:




