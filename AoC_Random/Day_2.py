"""🐍 Daily Python Challenge – Day 2

Title: Word Frequency Counter

Task:
Write a function word_count(text) that takes a string and returns a dictionary where:

Keys are the unique words (case-insensitive).

Values are how many times each word appears.

Requirements:

Ignore punctuation (. , ! ? etc).

Treat uppercase/lowercase words as the same ("Hello" == "hello").

Example Input:

text = "Hello, hello! This is a test. A simple test."


Expected Output:

{
  "hello": 2,
  "this": 1,
  "is": 1,
  "a": 2,
  "test": 2,
  "simple": 1
}"""







def count_words(text):
    comp_list=[]
    comp_title = set()
    words = text.lower().split()

    for word in words:
        comp_word = []
        for char in word:
            if char.isalpha():
                comp_word.append(char)        
        x = "".join(comp_word)
        if x:
            comp_list.append(x)
            comp_title.add(x)
            comp_title_sorted=(sorted(comp_title))
    for word in comp_title_sorted:
        print(f'{word} : {comp_list.count(word)}')

   



text = "Hello, hello! This is a test. A simple test."
count_words(text)


