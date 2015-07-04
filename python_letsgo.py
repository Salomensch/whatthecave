
# print('Genug gespielt!')

# print('Jetzt geht\'s los...')



def login():
    print('Enter your name:')
    name = input()
    print('Aha! Your name is ' + name + '!')
    return name

def lang(name):
    print('Länge: '+ str(len(name)))


name = login()
lang(name)


