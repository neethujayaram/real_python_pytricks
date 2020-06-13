firstname="Neethu"
lastname="Jayaram"

#first way
print(f'Hey {firstname} {lastname} !!!!')

#second way
print('Hey %s %s !!!!' %(firstname,lastname))

#third way
print('Hey {} {} !!!!'.format(firstname,lastname))