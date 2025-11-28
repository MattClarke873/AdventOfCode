"""🐍 Daily Python Challenge – Day 3

Title: Anagram Checker

Task:
Write a function are_anagrams(word1, word2) that checks if two words are anagrams.

An anagram means they use the same letters in a different order.

Ignore case and punctuation.

Examples:

are_anagrams("listen", "silent")     # True
are_anagrams("Triangle", "Integral") # True
are_anagrams("hello", "world")       # False

🔧 Extra Challenge (Optional)

Write a function find_anagrams(word, word_list) that returns all words from word_list that are anagrams of word.

Example:

find_anagrams("listen", ["enlist", "google", "inlets", "banana"])
# Output: ["enlist", "inlets"]


Save your results in a nice printed format like:

listen → enlist, inlets


This one will give you practice with:
✔️ String manipulation
✔️ Sorting / sets
✔️ Lists & loops"""



def are_anagrams(word1):

    words = ["listen", "silent", "enlist", "hello", "olleh", "world", "dworl", "python"]


    word1_letters = []
    word_letters = []
    # if len((word1)) != len(word2):
    #     return False
    # else:
    #     for char in word1:
    #         if char.isalpha():    
    #             word1_letters.append(char.lower())
    #     for char2 in word2:
    #         if char2.isalpha():
    #             word2_letters.append(char2.lower())

    # if sorted(word1_letters) == sorted(word2_letters):
    #     return True
    # else:
    #     return False
    


    for word in words:
        if len((word1)) != len(word):
            return False
        else:
            for char in word1:
                if char.isalpha():
                    word1_letters.append(char.lower())  
            for char2 in word:
                if char2.isalpha():
                    word_letters.append(char2.lower())

        if sorted(word1_letters) == sorted(word_letters):
            return True
        else:
            return False




print(are_anagrams("Word", "word"))

 
