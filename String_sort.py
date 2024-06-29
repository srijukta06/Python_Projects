# Write a Python function to sort the words in a string

def sort_words(words):
  return ' '.join(sorted(words.split(), key=str.casefold))
