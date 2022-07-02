
secret = str.lower("I hear the gooseberries are doing well this year, and so are the mangoes.")
cipher = 1


other = [" ",".",","]
alphabet = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = ""

print(len(alphabet))

for letter in secret:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + cipher
            if new_position > 25:
                new_position = new_position - 26

            word += alphabet[new_position]

        elif letter in other:
            word += letter   


        

print(word)