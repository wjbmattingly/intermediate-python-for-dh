#!/usr/bin/env python
# coding: utf-8

# # The Zip Function
# 
# In this tutorial, we'll explore the zip() function in Python, which is a useful tool for working with multiple sequences, a category of data structure that includes lists, tuples, or strings. This tutorial is designed for humanists and those new to Python, so we'll use simple examples to help you understand the concept.
# 
# Like `enumerate()`, there are other ways to produce the same results as `zip()`. Also like `enumerate()`, `zip()` significantly reduces the amount of code you need to write to perform those same actions. You will likely encounter `zip()` when reading code from colleagues or in online tutorials. Often, you will not see it explained or described. Because of this, it can be useful to learn about `zip()` early in your Python career.
# 
# <center><iframe width="560" height="315" src="https://www.youtube.com/embed/Ek49cGiAOwo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>
# 
# ## What is the `zip()` function?
# 
# The zip() function is a built-in Python function that allows you to combine two or more sequences (like lists, tuples, or strings) element-wise. It returns an iterator, which yields pairs (or tuples) of corresponding elements from the input sequences. The resulting iterator stops when the shortest input sequence is exhausted.
# 
# The basic syntax of the zip() function is:
# 
# ```python
# zip(sequence1, sequence2, ...)
# ```
# 
# - `sequence1`, `sequence2`, ...: Two or more sequences you want to combine (e.g., lists, tuples, or strings).
# 
# You can use the `zip()` function with a for loop or convert the iterator to a list or tuple for further processing.
# 
# 
# ## Using the `zip()` function with lists
# 
# Let's say you have two lists, one with authors and another with their corresponding book titles. You want to create pairs of authors and book titles. You can use the `zip()` function to achieve this.

# In[1]:


authors = ["Jane Austen", "George Orwell", "F. Scott Fitzgerald", "Harper Lee"]
books = ["Pride and Prejudice", "1984", "The Great Gatsby", "To Kill a Mockingbird"]

author_book_pairs = zip(authors, books)

for author, book in author_book_pairs:
    print(author, ":", book)


# As you can see, the zip() function combines the two lists element-wise, creating pairs of authors and book titles.
# 
# ## Using the `zip()` function with strings
# 
# You can also use the `zip()` function with strings. Let's say you have two strings, and you want to create pairs of corresponding characters.

# In[3]:


string1 = "abcde"
string2 = "12345"

char_pairs = zip(string1, string2)

for char1, char2 in char_pairs:
    print(char1, char2)


# In[ ]:




