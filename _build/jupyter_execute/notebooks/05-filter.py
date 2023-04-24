#!/usr/bin/env python
# coding: utf-8

# # The Filter Function
# 
# In this tutorial, we'll explore how to use the `filter()` function in Python, specifically for digital humanists. The `filter()` function is a built-in Python function. This means you do not need to install a library to use it. The function processes a sequence of data (such as lists, tuples, or any other iterable) and keeps only the elements that satisfy a specific condition. This condition is defined by a function or a lambda expression that returns a boolean value (True or False).
# 
# When the filter() function is called, it iterates through each element in the sequence, applies the condition, and retains only the elements for which the condition returns True. The result is a new iterable, usually a list or a tuple, containing the filtered elements. If you are familiar with filtering in databases or a Pandas `DataFrame` in Python, then you may already be familiar with this concept.
# 
# In simpler terms, the filter() function helps you selectively keep elements from a dataset based on a particular criterion or test. This is especially useful when working with large datasets or when you need to focus on specific aspects of the data.
# 
# This powerful tool is particularly useful in digital humanities projects, where you often need to extract relevant information from large datasets, such as texts, metadata, or collections of cultural artifacts.
# 
# For instance, digital humanists may want to identify specific words or phrases in a corpus of texts, filter out irrelevant data from a dataset of historical records, or analyze the occurrence of certain artistic features in a collection of paintings. The `filter()` function, when combined with appropriate conditions, can help streamline these tasks and provide valuable insights.
# 
# We will be working with the following data:

# In[3]:


lines = [
    "Once upon a midnight dreary, while I pondered, weak and weary,",
    "Over many a quaint and curious volume of forgotten lore—",
    "While I nodded, nearly napping, suddenly there came a tapping,",
    "As of some one gently rapping, rapping at my chamber door.",
]


# ## Using the `filter()` Function
# 
# The filter() function has the following syntax:
# 
# ```python
# filter(function, iterable)
# ```
# 
# 
# - `function`: A function that tests each item in the iterable and returns a boolean value (True or False).
# - `iterable`: An iterable (e.g., list, tuple, or string) whose elements will be tested by the function.
# 
# The `filter()` function returns an iterator containing the elements that satisfy the condition set by the function.
# 
# Let's start with a simple example. We will create a function that checks if a line starts with the word "While":

# In[4]:


def starts_with_while(line):
    return line.startswith("While")


# Now, let's use the filter() function to keep only the lines that start with "While":

# In[5]:


filtered_lines = filter(starts_with_while, lines)


# The filtered_lines variable is an iterator. To see the result, you can convert it to a list:

# In[6]:


print(list(filtered_lines))


# ## Using `filter()` with Lambda Functions
# 
# For simple filtering conditions, you can use lambda functions instead of defining a separate function. A lambda function is an anonymous, one-line function that you can define and use directly in the `filter()` function.
# 
# For example, let's filter the lines that contain the word "rapping" using a lambda function:

# In[7]:


filtered_lines = filter(lambda line: "rapping" in line, lines)
print(list(filtered_lines))

