#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
msexcount = agecount = wcount = 0
while True:
    age = int(input('Age: '))
    sex = str(input('Sex[M/F]: '))[0].upper()
    while sex not in 'MF':
        sex = str(input('Sex[M/F]'))[0].upper()
    k = str(input('Do you want to continue[Y/N]:'))[0].upper()
    while k not in 'YN':
        k = str(input('Do you want to continue[Y/N]'))[0].upper()
    if sex == 'F' and age < 20:
        wcount += 1
    if sex == 'M':
        msexcount += 1
    if age > 18:
        agecount += 1
    if k == 'N':
        break
print(f'There are {agecount} persons with more than 18 years old')
print(f'There are {msexcount} mans registered')
print(f'There are {wcount} womans with less than 20 years old')