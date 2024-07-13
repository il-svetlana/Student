import random

password = ''

random_num = random.randrange(3, 21)
print('Число для подбора пароля: ', random_num)

for i in range(1, random_num):
    for j in range(i+1, random_num):
        if not random_num % (i + j):
            password = password + str(i) + str(j)

print('Подобранный пароль: ', password)

