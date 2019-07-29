number = int(raw_input("Enter Number:"))
word = str(raw_input("Enter Word:"))


def pluralize(word):
    if word[-3:] == "ife":
        return word[:-3] + "ives"
    if word[-2:] == "ch" or word[-2:] =="sh":
        return word + "es"
    if word[-2:] == "us":
        return word[-2:] + "i"
    if word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
        return word + "s"
    if word[-1:] == "y":
        return word[:-1] + "ies"
    else:
        return word+'s'

print( str(number) + " " + pluralize(word))
