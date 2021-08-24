import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print('Did you mean %s instead'%get_close_matches(word,data.keys())[0])
        decide=input("Yes(Press y) or No(Press n)")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            print('Meaning of given word unavailable')
        else:
            print("Invalid input")

    else:
        print("Meaning of given word unavailable")

word=input('Enter a word')

output=translate(word)
if output==list:
    for i in output:
        print(i+'\n')
else:
    print(output)
