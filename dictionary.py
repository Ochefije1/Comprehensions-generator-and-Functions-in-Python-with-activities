'''

    CREATE A DICTIONARY TO CHECK THE MEANING OF A GIVEN WORD
    - YOU MAY USE A FUNCTION FOR THIS.

'''

# dictionary ={
#     'come': 'to move towards a place or thing',
#     'extend': ' to make something longer or wider',
#     'cook': 'to prepare food by heating'
# }

# def get_meaning(word):
#     match word:
#         case 'come':
#             print(dictionary.get(word))



words = {
    'lagos': "The busiest city in Nigeria",
    'ghaya': 'The most beautifl in Bullseye',
    'school': 'A place of learning',
    'house': ' A building'
}

def checkMeaning(word):
    match word:
        case word if word in words.keys():
            return words[word]
        
print(checkMeaning('house'))





