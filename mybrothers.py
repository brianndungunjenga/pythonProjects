myBrothers = ['Ian', 'Ndung\'u','Ndungu', 'ndungu', 'Dennis', 'dennis', 'Iguku', 'iguku', 'ian', 'Jessee']
print('Enter a brother\'s name:')
name = input()
if name not in myBrothers:
    print(name+ ' is not my brother.')
else:
    print(name+ ' is my brother.')