fisherman1 = int(input('Введите количество пойманных рыб первым рыбаком: '))
fisherman2 = int(input('Введите количество пойманных рыб вторым рыбаком: '))
if fisherman1 < fisherman2:
    print('Улов рыбака, которому повезло меньше:', fisherman1)
elif fisherman2 < fisherman1:
    print('Улов рыбака, которому повезло меньше:', fisherman2)
else:
    print('Оба рыбака поймали одинаковое количество рыб.')
