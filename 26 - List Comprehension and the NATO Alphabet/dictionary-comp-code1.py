sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_sentence = sentence.split()

result = {split_sentence.index(word): word for word in split_sentence}

print(result)
