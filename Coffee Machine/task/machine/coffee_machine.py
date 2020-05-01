
# Bestand an Rohstoffen in der Kaffeemaschine
water = 400
milk = 540
beans = 120
cups = 9
money = 550

# deklaration der Variable action
action = ''

# string wenn genug Ressourcen für die Zubereitung eines Kaffees vorhanden sind
enough = "I have enough resources, making you a coffee!\n"

#String für Nicht genug Wasser, bohnen tassen
new = 'Sorry, not enough water'
neb = 'Sorry, not enough beans'
nec = 'Sorry, not enough cups'
nem = 'Sorry not enough milk'

# err_count wird zur Steuerung der while Schleife benutzt
err_count = 0

# function für das Hauptmenü
def main():
    global action
    action = input('\nWrite action (buy, fill, take, remaining, exit):\n')

# Funktion zum Ausdruck der Bestände - prt_Inv = print Inventar
def prt_Inv():
    print('''\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money\n'''.format(water, milk, beans, cups, money))

# def der Funktion nach Auswahl der action 'fill'
def fill():
    global water, milk,beans,cups,money
    water = water + int(input('Write how many ml of water do you want to add:\n'))
    milk = milk + int(input('Write how many ml of milk do you want to add:\n'))
    beans = beans + int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups = cups + int(input('Write how many disposable cups of coffee do you want to add:\n'))

# def der Funktion nach Auswahl der Aktion take
def take():
    global money
    print('I gave you ${}\n'.format(money))
    money = 0

# def der Funktion nach Auswahl der action 'exit'
'''über builtIn exit()'''

# def function 'remaining'
def remaining():
    prt_Inv()
# zum Schluss wenn die Schleife fertig ist

# def der einzelnen Kaffeesorten
def espresso():
    global water, beans, cups, money
    if water >= 250 and beans >= 16 and cups >= 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
        print(enough)
    else:
        if water < 250:
            print(new)
        elif beans < 16:
            print(neb)
        elif cups < 1:
            print(nec)

def latte():
    global water, beans, cups, milk, money
    if water >= 350 and beans >= 20 and cups >= 1 and milk >= 75:
        water -= 350
        beans -= 20
        milk -= 75
        cups -= 1
        money += 7
        print(enough)
    else:
        if water < 350:
            print(new)
        elif beans < 20:
            print(neb)
        elif cups < 1:
            print(nec)
        elif milk < 75:
            print(nem)

def cappuccino():
    global water, beans, cups, milk, money
    if water >= 200 and beans >= 12 and cups >= 1 and milk >= 100:
        water -= 200
        beans -= 12
        milk -= 100
        cups -= 1
        money += 6
        print(enough)
    else:
        if water < 200:
            print(new)
        elif beans < 12:
            print(neb)
        elif cups < 1:
            print(nec)
        elif milk < 100:
            print(nem)

# def der Funktion buy
def buy():
    coffe_typ = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\nback - to main  menu:')
    if coffe_typ == '1':
        espresso()
    elif coffe_typ == '2':
        latte()
    elif coffe_typ == '3':
        cappuccino()




# def error wenn falsche Eingabe gemacht wird
def error():
    global err_count
    print('Only: "buy", "fill", "remaining","exit" are allowed to enter. Please try again')
    err_count += 1

# error count zurücksetzen wenn er 1 ist und die action ausgeführt wurde
def errct():
    global err_count
    if err_count == 1:
        err_count -= 1
# Programmexecution startet hier >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 1. Start
# druckt das Inventar vor dem Start aus
# prt_Inv()
# Fragt die gewünschte Aktion zum Start ab
main()
# 2. Schleife des eigentlichen Programms

while action != 'exit':
    # ruft die entsprechende Funktion auf
    if action == 'fill':
        fill()
        errct()
    elif action == 'take':
        take()
        errct()
    elif action == 'exit':
        errct()
        exit()
    elif action == 'remaining':
        remaining()
        errct()
    elif action == 'buy':
        buy()
        errct()
    elif action != 'buy' and action != 'fill' and action != 'take' and action != 'remaining' and action != 'back' and err_count == 0:
        errct()
        error()
    main()
