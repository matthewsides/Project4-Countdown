import random
import time
import winsound
import string

# Imports external libaries with pre-built functions for importation.

winsound.PlaySound('F:\countdown\countdowntheme.wav',winsound.SND_ASYNC)
# CountDown Theme Remix by Spiritman
#Finds and plays the defined wav file in conjunction with the rest of the code (plays in background) due to the addition of SND_ASYNC (asynchronous).
print ("Count Down V.01")
print ("Menu Choices:")
print("Start")
print("Instructions")
print("Exit")

instructions = ('instructions')
start = ('start')
exit = ('exit')

# menuinput = input ().lower()
# while len(menuinput) < 1 or (not menuinput.isalpha()):
    #menuinput = input ().lower()
    
# while menuinput is not start and instructions:
while True:
    menuinput = input().lower()
    if menuinput == instructions:
        print("Instructions")
        print("The contestant must choose 9 letters by selecting either a vowel or a consonant until there is a total of 9 letters.")
        print(" Players can choose the letters in any order, but the selection must include at least 4 consonants and 3 vowels, hence there are only three valid choices in modern Countdown: 3 vowels, 6 consonants; 4 vowels, 5 consonants; and 5 vowels, 4 consonants.")
        print ("A player scores points on a letters game by writing down a valid word within the 30 seconds. This word must be in the current New Oxford English Dictionary, but not a proper noun, nor an abbreviation.")
        print ("Players can use each letter only as many times as it appears in the selection.")
        print ("Words score 1 point per letter, except for nine-letter words which are worth 18.")
    
    if menuinput == exit:
     raise SystemExit
    if menuinput == start:
        time.sleep(4)
        print(" Beginning Game...")
        winsound.PlaySound(None, winsound.SND_PURGE)
# stops the sound or wavfile from playing setting the value to none.
        time.sleep(4)
        break
   # elif menuinput is not instructions or start:
       # print("no option known as",menuinput)


    
vowels_pile = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'i','i','i','i','i','i','i','i','i','i','i','i','i', 'o','o','o','o','o','o','o','o','o','o','o','o','o','u','u','u','u','u']

consonants_pile = ['b', 'b', 'c', 'c','c' , 'd','d','d', 'd','d','d', 'f','f','g','g','g','h','h','j','k','l','l','l','l','l','m','m','m','m','n','n','n','n','n','n','n','n','p','p','p','p','q','r','r','r','r','r','r','r','r','r','s','s','s','s','s','s','s','s','s','t','t','t','t','t','t','t','t','t','v','w','x','y','z']

chosen_letters = []

playerone_pile = []

playertwo_pile = []

inputerror_text = ['please type in one character that is either a vowel or constanent','I would prefer only letters and one character','Dont you understand the concept of either a vowel or constanent','I think you know what the problem is  just as well as I do','Im sorry Dave im afraid I cant do that']

playerone_score = 0

playertwo_score = 0
#rounds = int (0)

# The operator * doesnt seem to function properly with the .remove function since the remove function is only compatiable and looks for strings not integers or numerical values.    
# The * operator also appears to not work with append since it is a numerical value (int)
# The operator * was originally meant to be used for the duplication of the alpha letters or chars as a letter is equal to 1 multiplied by the amount set after the operator will equal to that amount.
# Thus making the code more structured, less cluttered and efficent, though it appears the other functions in use seem to clash with the operator and therefore each letter had to be typed seperately to eqaul the amount of chars there are of that letter.

#while rounds < 10:

#for i in range  (10):
while len (chosen_letters) < 9:
#loops until chosen_letters array or list amounts or equals nine, so nine letters chosen by the user.

# The lower function used below converts the string typed in caps to lower case, ensuring no errors appear when caps is used and making it so the program may accept capslock input.
    letter = input("please select either a vowel or constanent").lower()

# The code below tests whether the input length is equal to 1 and is alphabetical, if neither it loops asking for input again using the while loop.
# while len (chosen_letters) < 9:

    while len(letter) != 1 or (not letter.isalpha()):
        letter = input(random.choice(inputerror_text)).lower()
    
#make it give random response back
#letter = input("please type in one character that is either a vowel or constanent")
       
    if letter not in vowels_pile and letter not in consonants_pile:
        print("Out of avaliable letter")
            
    if  len(vowels_pile) < 63:
        vowels_pile *= 0
            
#print ("You have reached the limit of vowels allowed to be taken")
#print ("would you like to autocomplete the rest of the letters?")

# The above and below conditional statements exist to limit the amount of vowels and constenants being taken as 4 consonants and at least three vowels must be used.
# This leaves 3 possibilities or combinations; 3 vowels and six consonants, four vowels and five consonants or five vowels and four consonants.        
# The solution to the problem of how to implement this rule or system being to check whether the highest amount of vowels or consonants allowed to be taken out have been used and then limiting or stoping the user from taking any more out forcing them to take from the other remaining pile as the maxed out pile is cleared and discarded.

    if  len(consonants_pile) < 62:
        consonants_pile *= 0
        #print ("You have reached the limit of consonants allowed to be taken")
        
# 67 chars in vowels_pile in total.
# The above code is a conditional statement essentially stating that if the letter inputted is not in any of the pile then inform the user and make them re-input.
#else if the condition is not met and the letter is avaliable in one of the piles then move onto the next statement.

    if letter in vowels_pile:
        chosen_letters.append (letter)
        vowels_pile.remove (letter)
        print (*chosen_letters)
            
    if letter in consonants_pile:
        chosen_letters.append (letter)
        consonants_pile.remove (letter)       
        print (*chosen_letters)
            
        

print ("Chosen letters:",*chosen_letters)
playerone_pile.append (chosen_letters)
# print ("players pile test",*playerone_pile)
winsound.PlaySound('F:\countdown\countdownclock.wav',winsound.SND_ASYNC)
start_time = time.clock()
wordone = input ("Player 1 you have 30 seconds to make and type the longest word you can think of out of the chosen letters").lower()
while len(wordone) > 9 or (not wordone.isalpha()):
        start_time = time.clock()
        wordone = input("please input correctly you have 30 seconds starting now").lower()

for i in range(0,len(wordone)):
  if wordone [i] in playerone_pile:
    print("true")
  else:
   break
            
            #playerone_pile.find ('wordone')
    #for var in input: #and object in playerone_pile
         #if var in playerone_pile:
          #   print("yes")
       #  if var not in playerone_pile:
        #     print ("no")
if start_time > 30:
     winsound.PlaySound(None, winsound.SND_PURGE)
     print (time.clock() - start_time, "seconds")
     print ("You took to long and therefore equit your points for this round") 
    #if wordone   
    # (forfiet points)
        
if start_time == 30 or start_time < 30:
    winsound.PlaySound(None, winsound.SND_PURGE)
    print (time.clock() - start_time, "seconds")
    print ("you were in time congratulations player")
    fobj = open("list.txt")
    text = fobj.read().strip().split()
    # fobj stands for file object
    
        
    if wordone not in text: #string is absent in the text file
        onevalid = False
    if wordone in text: #string in present in the text file
        onevalid = True
    fobj.close()

playertwo_pile.append (chosen_letters)
winsound.PlaySound('F:\countdown\countdownclock.wav',winsound.SND_ASYNC)
start_time = time.clock()
wordtwo = input ("Player 2 you have 30 seconds to make and type the longest word you can think of out of the chosen letters").lower()
while len(wordtwo) > 9 or (not wordone.isalpha()):
        start_time = time.clock()
        wordtwo = input("please input correctly you have 30 seconds starting now").lower()

for i in range(0,len(wordtwo)):
  if wordtwo [i] in playertwo_pile:
    print("true")
  else:
    break
          
if start_time > 30:
    winsound.PlaySound(None, winsound.SND_PURGE)
    print (time.clock() - start_time, "seconds")
    print ("You took to long and therefore equit your points for this round")
     
if start_time == 30 or start_time < 30:
    winsound.PlaySound(None, winsound.SND_PURGE)
    print (time.clock() - start_time, "seconds")
    print ("you were in time congratulations player")
    fobj = open("list.txt")
    text = fobj.read().strip().split()
    # fobj stands for file object

    if wordtwo not in text: #string is absent in the text file
            twovalid = False
    if wordtwo in text: #string in present in the text file
            twovalid = True 
       
    fobj.close()

if twovalid and onevalid == True:
    if len (wordtwo) > len (wordone):
      playertwo_score =  playertwo_score + len (wordtwo)
    if len (wordone) > len (wordtwo):
      playerone_score = playerone_score + len (wordone)
    if len (wordone) == len (wordtwo):
        print ("Draw both players distributed points")
        playertwo_score = playertwo_score + len (wordtwo)
        playerone_score = playerone_score + len (wordone)
if twovalid and onevalid == False:
    print ("neither words given by the players are valid, hence no one gets points") 
if twovalid == False and onevalid == True:
  playerone_score =  playerone_score + len(wordone)
if onevalid == False and twovalid == True:
  playertwo_score = playertwo_score + len (wordtwo)

if playerone_score > playertwo_score:
    print("Playerone Wins")
    print ("Final Scores:", playerone_score,playertwo_score)
   
if playertwo_score > playertwo_score:
    print("Playertwo Wins")
    print ("Final Scores:", playertwo_score,playerone_score)
if playerone_score == playertwo_score:
    print ("Draw")
    print ("Final Scores:", playerone_score,playertwo_score)
# rounds + 1
       
# The * operator or star unpacks the list and return every element in the list.
# Essentially removing the brackets, commas, etc.





