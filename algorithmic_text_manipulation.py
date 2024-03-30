# -*- coding: utf-8 -*-
"""Algorithmic Text Manipulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NnjBZEUiZjXZZbCuLSTekwno4GN9nKcN
"""

#Stephanie Domínguez
#December 6, 2023

#Task:Algorithmic text manipulation
#Defines functions called toLower, removePunct, countWords and stringToList which convert a string to lowercase letters, remove punctuation from the string, count the number of words in that string and convert the string to a list.


#convers letters into lower case
#function signature with parameter
def toLower (lowerWord):
# have an empty string to fill later
  finalWord = ""
#going thru the full range of the word
  for i in range(0, len(lowerWord)):
#pulling from the first character in the string and getting the ascii value of it as well
    firstChar = ord(lowerWord[i])
#if the character is inbetween the uppercase range, we're going to add 32 to lowercase it
    if 90 >=firstChar >= 65:
      firstChar = firstChar + 32
# storing/updating the final word
      finalWord= finalWord + chr(firstChar)
#if not inbetween the uppercase range, were going to leave it alone
    else:
      finalWord= finalWord + chr(firstChar)
#making it fruitful
  return finalWord


#fucntion removed punctuation

#function signature with parameter
def removePunct (noPunct):
#have an empty string to fill for later
  finalWord= ""
#python goes thru th full range of characters in the word
  for i in range(0,len(noPunct)):
  #pulling from the first character in the string and getting the ascii value of it as well
    firstChar = ord(noPunct[i])
  #boolean statements for firstChar. the first one is for uppercase letter
  #the second one is for lowercase letters, and the last one is for the space
    if 65 <= firstChar <= 90 or 97<= firstChar <=122 or firstChar == 32:
    #tell python to keep the things we care about bc it's going to forget about the punctuation
      finalWord= finalWord + chr(firstChar)
  #making it fruitful
  return finalWord



#function makes into Lowercase
#function signature with parameter
def toLower (lowerWord):
# have an empty string to fill later
  finalWord = ""
#going thru the full range of the word
  for i in range(0, len(lowerWord)):
#pulling from the first character in the string and getting the ascii value of it as well
    firstChar = ord(lowerWord[i])
#if the character is inbetween the uppercase range, we're going to add 32 to lowercase it
    if 90 >=firstChar >= 65:
      firstChar = firstChar + 32
# storing/updating the final word
      finalWord= finalWord + chr(firstChar)
#if not inbetween the uppercase range, were going to leave it alone
    else:
      finalWord= finalWord + chr(firstChar)
#making it fruitful
  return finalWord


#function that converts words of a string into a list
def stringToList(parameter):
#establish list len by having a variable of num to hold the word count of the param
  num = countWords(parameter)
  #finalList is going to have an empty string and multiply it by the number of words in param
  finalList = [""] * num
  wordHolder = ""
  wordCounter = 0
 #setting counter variable i to 0
  i = 0
#creating a while loop to iterate through each character in the param length (0 index)
  while i <= len(parameter) - 1:
#if i does not hit a blank spot (aka just letter, it will hold the word, store it, and add the param index to wordHolder)
    if parameter[i] != " ": #if param index position does not equal to an empty space
      wordHolder = wordHolder + parameter[i]
#if our i does hit a blank spot, it will add the next number up to wordCounter and keep wordHolder empty
    else:
      finalList[wordCounter] = wordHolder
      wordCounter = wordCounter + 1
      wordHolder = ""
    i = i + 1
  finalList[wordCounter] = wordHolder

  return finalList

#signature line for function countWords and setting my parameter as a variable
def countWords(parameter):
  #set my index count to 1 because there is no need to start at 0
  finalCount = 1
  #making an empty string to store parameter, and if paramater is nothing, then it counts as 0
  if parameter == "":
    #if the string is empty that means there are zero words
    finalCount = 0
    #using a for loop used to iterate through spaces and the range is my param
  for i in range (len(parameter)):
    #using if statement to connect to the ascii value of space
    if ord(parameter[i]) == 32:
      #concatonating the spaces to calculate the number of words
      finalCount = finalCount + 1
      #return function to get a value back/ making it fruitful
  return finalCount

# testing my stuff out

def main():
  print(toLower("WHEN I WAS THIRTEEN")) # test 1 for toLower

  print(toLower("I HAD MY FIRST LOVE")) # test 2 for toLower

  print(toLower("thEre Was NoBoDY thAt CoulD ComPARE to My BABy and came between us nor could ever come above"))  # test 3 for toLower


  print(removePunct("myDog.is.mid")) # test 1 for removePunct

  print(removePunct("I-really-wanna-graduate")) # test 2 for removePunct

  print(removePunct("How many people do you think Drake has kissed?")) # test 3 for removePunct

  #test 1 for countWords
  print(countWords("the primary goal of digital and computational studies is to bridge the liberal arts education in the spirit of interdisciplinarity to computing and the digital world."))
  #test2
  print(countWords("digital and computational Studies Courses fall into a continuum of experiences that range from critical digital studies to programming, with an integrated core that embraces both"))
  #test3
  print(countWords("Historically speaking, data has been controlled by a very specific group of people. As a result, many people have been left out of the data creation process thus creating implicit bias within our data... by shifting the paradigm in which data exists to be more accessible and usable I think that we will see a more equitable e-universe."
))



  #test 1 for stringToList
  print(stringToList("the primary goal of digital and computational studies is to bridge the liberal arts education in the spirit of interdisciplinarity to computing and the digital world."))

  #test 2 for stringToList
  print(stringToList("Digital and Computational Studies Courses fall into a continuum of experiences that range from critical digital studies to programming, with an integrated core that embraces both"))

  #test 3 for stringToList
  print(stringToList("Historically speaking, data has been controlled by a very specific group of people. As a result, many people have been left out of the data creation process thus creating implicit bias within our data... by shifting the paradigm in which data exists to be more accessible and usable I think that we will see a more equitable e-universe."))
main()

