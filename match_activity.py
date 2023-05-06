word = 'one'

def checkWork(word):
    match word:
        case 'one':
            print('This is the first number')
        case 'two':
            print('This is the second number')
        case 'three':
            print('This is the third number')


checkWork('three')