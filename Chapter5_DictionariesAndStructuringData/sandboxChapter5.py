spam = {'name': 'Pooka', 'age':5}
if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white')
print(spam)