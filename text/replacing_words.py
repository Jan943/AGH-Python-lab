file = open("example_file.txt", "r", encoding='utf8')
text = file.read()
file.close()

print("Before replacing words: ")
print(text, end="")

words_to_swap = {
		 "nigdy" 	: "prawie nigdy",
		"oraz" : "i",
		 "dlaczego"	: "czemu",
		"i": "oraz",
}

new_text_words = []
for word in text.split():
    if word in words_to_swap.keys():
        new_text_words.append(words_to_swap[word])
    else:
        new_text_words.append(word)

result = " ".join(new_text_words)
print("\nAfter removing words: ")
print(result)