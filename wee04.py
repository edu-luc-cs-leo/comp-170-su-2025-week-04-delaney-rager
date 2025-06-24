#finding the longest word

def longest_word(words: list[str])-> str:  #function that inputs list of strings and returns a string   
  if not words:                             #if the string is None
    longest_word_is = None
  else:  
    longest_word_is = words[0]
    for i in words:                         #for loop that retreives each string in the list
      length = len(i)
      if length > len(longest_word_is):     #evaluates length of strings and compares
        longest_word_is = i
  return longest_word_is    
    
#finding the shortest word

def shortest_word(words: list[str]) -> str:  #function that takes a list of strings and outputs a string
  if not words:                               #if the list is none
    shortest_word_is = None
  else:
    shortest_word_is = words[0]   
    for i in words:                         # for loop that compares the length of each word to the previous longest word
      length = len(i)
      if length < len(shortest_word_is):
        shortest_word_is = i
  return shortest_word_is


# find odd words

def odd_words(words: list[str]) -> list[str]:  #function that inputes a list of strings and outputs a list of strings
  if not words:     # if the list is None, it returns None
    new_list = None
  else:   
    new_list = []         #starting with an empty list
    for word in words:
      if len(word) % 2 == 1:      #checking length of each index and then appending the list
        new_list.append(word)
  return new_list    


# find average words
#that returns a list with all the strings in words whose length is ±1 from the average length of all strings in words.
def average_words(words: list[str]) -> list[str]:
  if not words:       #if list is None return None
    new_list = None
  else:
    new_list = []       #empty list used to append to later on
    length = 0
    for word in words:      #for loop that sums the length of the words together
      length = length + len(word)
    average = length // len(words)      #taking the average using // so the answer is an integer
    for word in words:
      if average -1 <= len(word)<= average +1: #seeing if each word is +/- within the length of the average then appending the list
        new_list.append(word)
  return new_list      



# find an intersection
# that returns True if lists foo and bar have at least one element in common, anf False otherwise.
def intersect(foo: list[str], bar: list[str]) -> bool:
  if not foo: #if foo is None return False
    value = False
  else:   # if bar is none return false
    if not bar:
      value = False  
    else:
      value = False #preset value to false
      for word in foo:    #two for loops to check if they have a word in common
        for word2 in bar:
          if word == word2:
            value = True
  return value          


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
