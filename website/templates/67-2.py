d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word): #dict tells it that it is a dictionary. vocabulary looks at the word in the tuple
    try:
        return d[word] #returns the word from the relevant string
    except KeyError:
        return "That word doesn't exist!"
word = input("Enter word: ")
print(vocabulary(word))
