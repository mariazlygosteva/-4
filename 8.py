print('Здравствуйте! Как Вас зовут?')
name = input()
print(f'Очень приятно, {name}! Меня зовут Марк.')
print('Сколько Вам лет?')
age = int(input())
my_age = 78
age_difference = abs(my_age - age)
print(f'Да, {name}, я старше Вас на {age_difference} лет.')
print('Вам нравится программировать?')
programming_interest = input()
if programming_interest.lower() == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных'
          ' и хороших программ.')
elif programming_interest.lower() == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')