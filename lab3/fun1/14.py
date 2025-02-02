from function import grams_to_ounces, reverse_words

grams = float(input("salmaq gramda: "))
print(grams, "gr =", round(grams_to_ounces(grams), 2), "ounces")

sentence = input("soilem engiz: ")
print("kersinshe:", reverse_words(sentence))