story = ""
last_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == last_word:
        print(story)
        break
    else:
        story += word + " "
        last_word = word