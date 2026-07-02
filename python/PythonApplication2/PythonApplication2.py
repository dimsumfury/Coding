story = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    story += word + " "
    previous = word
 
print(story)
