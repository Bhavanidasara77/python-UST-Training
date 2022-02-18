#!/usr/bin/env python
# coding: utf-8

# In[10]:


word = input('Enter a word to check wether the word is palindrome or not: ')
if str(word) == str(word)[::-1]:
    print(word,': is palindrome')
else:
    print(word,': is not a palindrome')

