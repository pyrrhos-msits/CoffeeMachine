import math


# Bestand an Rohstoffen in der Kaffeemaschine
water = 1200
milk = 540
beans = 120
cups = 9
money = 550

# Funktion zum Ausdruck der Bestände - prt_Inv = print Inventar
def prt_Inv():
    print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of money\n'''.format(water, milk, beans, cups, money))



# Programmexecution startet hier
prt_Inv() # druckt das Inventar vor dem Start aus

action = input('Write action (buy, fill, take):\n>')




# # Precondition
# water_const = 200 #ml
# milk_const = 50 #ml
# beans_const = 15 #g
# #1. Abfragen der vorhandenen Mengen an Rohstoffen
# water_av = int(input('Write how many ml of water the coffee machine has: >'))
# milk_av = int(input('Write how many ml of milk the coffee machine has: >'))
# beans_av = int(input('Write how many grams of coffee beans the coffee machine has: >'))
# #2. Abfragen der gewünschten Kaffeemenge
# cups_count = int(input('Write how many cups of coffee you will need: >'))
# #3. Berechnen wieviel Tassen Kaffee geliefert werden können
# water_pos = math.floor(water_av / water_const)
# milk_pos = math.floor(milk_av / milk_const)
# beans_pos = math.floor(beans_av / beans_const)
# cups_pos = min(water_pos, milk_pos, beans_pos)
#
# if cups_pos <= 0:
#     print('No, I can make only 0 cups of coffee'.format(cups_pos))
# elif cups_pos > cups_count:
#     cups_more = cups_pos - cups_count
#     print('Yes, I can make that amount of coffee (and even {} more than that)'.format(cups_more))
# elif cups_pos > 0 and cups_pos < cups_count:
#     print('No, I can make only {} cups of coffee'.format(cups_pos))
# elif cups_pos == cups_count:
#     print('Yes I can make that amount of coffee')
#
