#!/usr/bin/env python
# coding: utf-8

# # Lambda Functions for Humanists: A Beginner's Tutorial
# 
# Lambda functions are a powerful yet simple feature in many programming languages that can help you write concise and elegant code. This tutorial is designed for humanists with little to no programming experience, and we will use examples from literature to demonstrate the usefulness of lambda functions.
# 
# ## What are lambda functions?
# 
# Lambda functions are small, anonymous functions that can be created and used on-the-fly without needing a formal function definition. In simpler terms, they are one-liner functions that don't need a name.
# Why are lambda functions useful?
# 
# - They allow for more concise and readable code.
# - They can be used as arguments to higher-order functions (functions that take other functions as inputs).
# - They are excellent for simple operations that don't require a full function definition.
# 
# ## Basic syntax
# 
# In Python, the syntax for creating a lambda function is:
# 
# ```python
# lambda arguments: expression
# ```
# 
# The `lambda` keyword is followed by a list of arguments, a colon, and a single expression that the function will return.
# 
# For example, let's say we have a simple function that adds two numbers:

# In[1]:


def add(x, y):
    return x + y


# We can rewrite this function as a lambda function like this:

# In[2]:


add = lambda x, y: x + y


# ## Using lambda functions with our example lines
# 
# Let's say we have the following list of lines from a poem:

# In[4]:


lines = [
    "Once upon a midnight dreary, while I pondered, weak and weary,",
    "Over many a quaint and curious volume of forgotten lore—",
    "While I nodded, nearly napping, suddenly there came a tapping,",
    "As of some one gently rapping, rapping at my chamber door.",
]


# ### Example 1: Counting words in each line
# 
# Let's use a `lambda` function to count the number of words in each line. We can achieve this using the `map()` function, which applies a given function to each item in an iterable (like a list).

# In[5]:


word_count = map(lambda line: len(line.split()), lines)

# Convert the result to a list and print it
print(list(word_count))


# ### Example 2: Sorting lines by length
# 
# We can use a `lambda` function to sort the lines based on their length. The `sorted()` function can take a key argument, which is a function that defines how to sort the items.

# In[6]:


sorted_lines = sorted(lines, key=lambda line: len(line))

# Print the sorted lines
for line in sorted_lines:
    print(line)


# Here, `lambda line: len(line)` is a lambda function that takes a single argument line and returns its length.
# 
# While not essential in code, `lambda` functions can reduce the need to have functions for functional code that may only have a single use in your code. Lambda functions are a powerful tool for writing concise and elegant code. They can be especially useful for humanists working with text data, as they allow for quick and simple manipulation of strings and lists.

# In[ ]:




