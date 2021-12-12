file = open("example_file.txt", "r", encoding='utf8')
text = file.read()
file.close()

print("Before removing words: ")
print(text, end="")

words_to_delete = [" się ", " i ", " oraz ", " nigdy ", " dlaczego "]

for word_to_delete in words_to_delete:
	text = text.replace(word_to_delete, " ")
print("\nAfter removing words: ")
print(text, end="")