#Функции
def add_to_shopping_cart_beef():
    if beef >0:
        shoppingcart.append('beef')
    else:
        print('Продукта нет в наличии')

def add_to_shopping_cart_chiken():
    if chiken >0:
        shoppingcart.append('chiken')
    else:
        print('Продукта нет в наличии')

def add_to_shopping_cart_dobrycola():
    if dobrycola >0:
        shoppingcart.append('dobrycola')
    else:
        print('Продукта нет в наличии')


#Корзина
shoppingcart = []

#База продуктов
beef = 1
chiken = 1
dobrycola = 1

#Цены
beefcost = 250
chikencost = 180
dobrycolacost = 50


#Основной код
print('Каталог: beef,chiken,dobrycola.')

while True:
    print('Введите ваш выбор, либо введите buy для подведения итога')
    flag = True
    answer = input()

    if answer == 'beef':
        if beef >0:
            add_to_shopping_cart_beef()
            beef -=1
        else:
            add_to_shopping_cart_beef()


    elif answer == 'chiken':
        if chiken >0:
            add_to_shopping_cart_chiken()
            chiken -=1
        else:
            add_to_shopping_cart_chiken()

    elif answer == 'dobrycola':
        if dobrycola >0:
            add_to_shopping_cart_dobrycola()
            dobrycola -=1
        else:
            add_to_shopping_cart_dobrycola()

    if answer == 'buy':
        flag = False
        break

#Вычисление цены
totalcost = 0

beefcart = shoppingcart.count('beef')
chikencart = shoppingcart.count('chiken')
dobrycolacart = shoppingcart.count('dobrycola')

totalcost += beefcost * beefcart
totalcost += chikencost * chikencart
totalcost += dobrycolacost * dobrycolacart

#Вывод корзины
print('Ваша корзина:', *shoppingcart)

#Вывод цены
print('Итоговая цена:',totalcost,'рублей')