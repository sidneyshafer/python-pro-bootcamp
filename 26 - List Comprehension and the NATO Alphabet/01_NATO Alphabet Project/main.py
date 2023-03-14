import pandas

# Create a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
code_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# print(code_dict)

code_words = []
word = input("Enter a word: ").upper()
word.split()

for letter in word:
    for (key, value) in code_dict.items():
        if letter == key:
            code_words.append(value)

print(code_words)

