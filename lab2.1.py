#!/usr/local/bin/python3
# Name: August Brenner
# File name: lab2.1.py
# Date: July 3rd, 2013

from urllib.request import urlopen
import lab2modules

print("Content-type: text/html\n")
lab2modules.HTML_START("Lab 2 Exercise 2.1")

# open file from URL
file = urlopen('http://server.csmcis.net/~putnamd/oliver.txt')
oliver_text = file.read().decode('utf-8').replace('--', ' ').replace('.', '').replace(',', '').lower()

print(oliver_text)


# Break file into words and print first 100 in a table
oliver_words = oliver_text.split()
lab2modules.table(oliver_words[0:100], 6)


# function for printing unique words of a set
def unique_words(word_array, set_description):
    unique_words = set(word_array)
    lab2modules.table(unique_words, 6)
    print('<pre> There are ' + str(len(unique_words)) + ' unique words in ' + set_description + '</pre>')


# table of all unique words in the first 100 words
unique_words(oliver_words[0:100], "the first 100 words")

# table of all unique words in the first 100 words
unique_words(oliver_words[-100:], "the last 100 words")

# table of all unique words in the first and last 100 words
unique_words_union = set(oliver_words[0:100]).union(set(oliver_words[-100:]))
lab2modules.table(unique_words_union, 6)
print('<pre> There are ' + str(len(unique_words_union)) + ' unique words in the first and last 100 words</pre>')

# table of all unique words in the first 100 and last 100 words that are in one set or another, but not in both
unique_words_symmetric_difference = set(oliver_words[0:100]).symmetric_difference(set(oliver_words[-100:]))
lab2modules.table(unique_words_symmetric_difference, 6)
print('<pre> There are ' + str(len(unique_words_symmetric_difference)) +
      ' unique words in the first and last 100 that are in one set or another, but not in both</pre>')


# function to remove members of the second list from the first list
def exclude(base_list, removal_list):
    base_list = list(set(base_list))
    for word in removal_list:
        if word in base_list:
            base_list.remove(word)
    return sorted(base_list)


# table of all unique words in the first 100 words that are not in the last 100 words
unique_words(exclude(oliver_words[0:100], oliver_words[-100:]), "the first 100 words not in the last 100 words")

# table of all unique words in the first 100 words that are not in the last 100 words
unique_words(exclude(oliver_words[-100:], oliver_words[0:100]), "the last 100 words not in the first 100 words")


lab2modules.HTML_End
