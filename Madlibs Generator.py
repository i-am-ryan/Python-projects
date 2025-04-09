# With ensures the file is automatically closed after the block ends, even if an error occurs.
#Prevents resource leaks (safer than manually calling f.close()).

with open("story.txt", "r") as f: #Opens the file story.txt in read mode ("r"),ssigns the opened file object to the variable f
    story = f.read() # gives you all the text in the file

print(story)
print("\n")

words = set() #set() makes sure that it only has unique values 
start_of_word = -1
target_start = "<"
target_end = ">"

#enumerate() function to loop over the characters in a string (or items in a list) while keeping track of both the index (i) and the character (char).

for i, char in enumerate(story): #i = Current index (0, 1, 2, ...).char = Current character ('H', 'e', ...).
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ") 
    answers [word] = answer  #stores their responses in a dictionary (answers) where the original words are the keys and the user's inputs are the values.


for word in words:
    story = story.replace(word, answers[word])

print(story)


