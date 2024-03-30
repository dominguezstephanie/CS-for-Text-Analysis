# -*- coding: utf-8 -*-
"""word_generation_1.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FPxsJ7tQD0J3dJ3Ij1EedWmBeS0O-X1m
"""

#TASK---- Word Generation: A word that is three letters long, always beginning with a vowel

#importing random seed
import random

#selecting a fun seed number
#random.seed(90222)

#establishing variables
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

#random vowel index is created by having a random.randint
randomVowelIndex = random.randint(0,len(vowels)-1)

randomVowel = vowels[randomVowelIndex]

#random consonant 0 is created

#randomConsonantIndex = random.randint(0,len(consonants)-1)
#randomConsonant = consonants[randomConsonantIndex]

#random consonant 1 is created

#randomConsonantIndex1 = random.randint(0,len(consonants)-1)
#randomConsonant1 = consonants[randomConsonantIndex1]

#new variable to not overwrite randomwVowel

threeLetterWord =  randomVowel

for i in range (0,2):
  randomConsonantIndex = random.randint(0,len(consonants)-1)
  randomConsonant = consonants[randomConsonantIndex]
  threeLetterWord =  threeLetterWord + randomConsonant


#let's try it out using print

print(threeLetterWord)

# TASK---- A word that is four letters long, with a vowel always in the second place

#importing random seed
import random

#selecting a fun seed number
#random.seed(90222)


#establishing variables
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"


#random vowel index is created by having a random.randint
randomVowelIndex = random.randint(0,len(vowels)-1)

randomVowel = vowels[randomVowelIndex]


#random vowel index 1 is created by having a random.randint
#randomVowelIndex1 = random.randint(0,len(vowels)-1)

#randomVowel1 = vowels[randomVowelIndex1]

#random consonant is created

randomConsonantIndex = random.randint(0,len(consonants)-1)
randomConsonant = consonants[randomConsonantIndex]

#random consonant 1 is created

#randomConsonantIndex1 = random.randint(0,len(consonants)-1)
#randomConsonant1 = consonants[randomConsonantIndex1]


#three letter word variable

#threeLetterWord =  randomConsonant + randomVowel + randomConsonant1

#creating for loop

#for i in range (1):
  #print(threeLetterWord + randomVowel1)


twoLetterVowel =  randomVowel

twoLetterConsonant = randomConsonant

fourLetterWord = randomConsonant + randomVowel

for i in range (2):
  randomConsonantIndex = random.randint(0,len(consonants)-1)
  randomConsonant = consonants[randomConsonantIndex]
  fourLetterWord = fourLetterWord + randomConsonant

print(fourLetterWord)

#TASK -----A word that is five letters long, with vowels always in the second and fourth places


#importing random seed
import random

#selecting a fun seed number
#random.seed(90222)


#establishing variables
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

fiveLetterWord = ""

for i in range (2):
  randomVowelIndex = random.randint(0,len(vowels)-1)
  randomVowel = vowels[randomVowelIndex]
  randomConsonantIndex = random.randint(0,len(consonants)-1)
  randomConsonant = consonants[randomConsonantIndex]
  fiveLetterWord = fiveLetterWord + randomConsonant + randomVowel

fiveLetterWord = fiveLetterWord + randomConsonant

print(fiveLetterWord)


#random vowel index 0 is created by having a random.randint
#randomVowelIndex = random.randint(0,len(vowels)-1)

#randomVowel = vowels[randomVowelIndex]



#random vowel index 1 is created by having a random.randint
#randomVowelIndex1 = random.randint(0,len(vowels)-1)

#randomVowel1 = vowels[randomVowelIndex1]

#random consonant 0 is created



#random consonant 1 is created

#randomConsonantIndex1 = random.randint(0,len(consonants)-1)
#randomConsonant1 = consonants[randomConsonantIndex1]


#three letter word variable

#threeLetterWord =  randomConsonant + randomVowel + randomConsonant1

#creating for loop

#for i in range (1):
  #print(threeLetterWord + randomVowel1 + randomConsonant1)