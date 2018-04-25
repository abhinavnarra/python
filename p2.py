#Demonstrate python program to form a frequency table of words in a given text.


text = input('enter a string:  ')#we have to enter a string  it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness

wordlist = text.split()#split method will split the given text into words

wordfreq = []#take an empty list for wordfrequency
for w in wordlist:#use for loop for iterating through the words
    wordfreq.append(wordlist.count(w))#count method will count the number of occurances of each word from wordlist and it will append to the wordfreq list
print("String\n" + text +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(dict(zip(wordlist,wordfreq))))#it will display the number of occurances of each word in text













#The above same thing can be acheived in a single line using list comprehension


#text = input('enter a string:  ')#we have to enter a string

#wordlist = text.split()

#wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension
#print("Frequencies\n" + str(wordfreq) )
