#!/usr/bin/env python
# coding: utf-8

# # Generators

# Generators are a powerful concept in Python that can help us work with large amounts of text-based data more efficiently. In this tutorial, we will introduce generators, explain why they are important for memory management, and provide examples tailored to humanists.
# 
# ## Introduction to Iterators and Generators
# 
# Before diving into generators, let's briefly introduce the concept of iterators. An iterator is an object that allows us to loop over a collection of items, such as a list or a string, one item at a time. Python has built-in iterator objects for many data structures like lists, tuples, and strings. 
# 
# A generator is a special type of iterator that allows us to generate a sequence of values on-the-fly, without having to store all the values in memory. Generators are created using a special type of function called a generator function. Instead of using the return keyword, generator functions use the `yield` keyword to `return` values one at a time.
# 
# ## Memory Management and the Importance of Generators
# 
# As humanists, we work primarily with texts. Often, our texts are quite short, but when we want to work with large collections of documents, it can be challenging to hold all the data in your computer's memory.
# 
# Memory, in the context of computers, refers to the temporary storage used by a computer to hold data that it is currently processing or has recently processed. Think of it like the desk space you use when working on a project. You can only have a limited number of items on the desk at once, and the more items you have, the harder it is to find and work with the ones you need.
# 
# Computer memory, often called RAM (Random Access Memory), works in a similar way. It holds data and instructions that the computer needs to access quickly while performing tasks. The more data and instructions you try to store in memory, the more resources the computer needs to manage them, which can slow down the system.
# 
# When working with large text-based data, memory management becomes crucial. Storing large amounts of data in memory can be inefficient and slow down your program. This is where generators come in handy.
# 
# Generators allow you to process large datasets one item at a time, without loading the entire dataset into memory. This means that you can work with data that is too large to fit in memory, or process data more efficiently by only loading the necessary items.
# 
# ## Creating and Using Generators
# 
# To create a generator function, use the `def` keyword to define a function, just like a regular function, but use the `yield` keyword instead of return to return values. Here's a simple example:

# In[1]:


def word_generator(text):
    for word in text.split():
        yield word


# This generator function takes a text string as input and yields words one at a time. To use the generator, you need to create a generator object by calling the generator function:

# In[2]:


text = "To be, or not to be, that is the question"
word_gen = word_generator(text)

for word in word_gen:
    print(word)


# ##  Example: Analyzing Literary Works
# 
# Let's say you want to analyze the frequency of words in a large literary work, like "War and Peace" by Leo Tolstoy. With a generator, you can efficiently process the text without loading the entire book into memory.
# 
# First, create a generator function to read the book line by line:

# In[3]:


def read_book_line_by_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


# In[20]:


shakespeare = read_book_line_by_line("../data/shakespeare.txt")


# ## Accessing the Generator Data with `next()`
# 
# The `next()` function is a built-in Python function that allows you to manually retrieve the next item from a generator. When you call `next()` with a generator as its argument, the generator function runs until it encounters the yield keyword, at which point it returns the value specified after the `yield`. The next time you call next() on the same generator, it continues executing from where it left off, retaining its previous state and any local variables.

# In[21]:


print(next(shakespeare))
print(next(shakespeare))
print(next(shakespeare))


# Here, we are not loading the entire book into memory, rather we are loading merely a single line at a time. This means that if we are using a computer with low amounts of memory, we can work with larger amounts of data without overloading the system hardware.

# 
