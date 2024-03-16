from pyfiglet import Figlet
import fade
import random
from listfonts import Best, allfonts, Anxer, Curios, xFonts

print (fade.fire('''
    ***************************************************   
    *    _   ___  ___ ___ ___   _____ _____  _______  *
    *   /_\\ / __|/ __|_ _|_ _| |_   _| __\\ \\/ /_   _| *
    *  / _ \\__ \\ (__ | | | |    | | | _|  >  <  | |   *
    * /_/ \\_\\___/\\___|___|___|   |_| |___/_/\\_\\ |_|   *
    *                                                 *
    *   ___ ___ _  _ ___ ___    _ _____ ___  ___      *
    *  / __| __| \\| | __| _ \\  /_\\_   _/ _ \\| _ \\     *
    * | (_ | _|| .` | _||   / / _ \\| || (_) |   /     *
    *  \\___|___|_|\\_|___|_|_\\/_/ \\_\\_| \\___/|_|_\\     *
    *                                                 *
    *              coded by ZLostTK                   *
    *                                                 *
    ***************************************************   
    *   popular ascii text are shown below :          *
    *                                                 *
    * [1] View best fonts   [2]View all fonts         *
    *                                                 *
    *     😊 Choose Your Favourite Font 😊           *
    *                                                 *
    ***************************************************
    '''))

option = input('> ')
if option == '1':
    found = [f'{Best[x]}{x}' for x in Best if x in Best]
    if found:
        for i in found:
            print(f'      {i}      ')
if option == '2':
    found = [f'{allfonts[x]}{x}' for x in allfonts if x in allfonts]
    if found:
        for i in found:
            print(f'      {i}      ')
if option == '3':
    found = [f'{Curios[x]}{x}' for x in Curios if x in Curios]
    if found:
        for i in found:
            print(f'      {i}      ')
if option == '4':
    found = [f'{Anxer[x]}{x}' for x in Anxer if x in Anxer]
    if found:
        for i in found:
            print(f'      {i}      ')
if option == '5':
    found = [f'{xFonts[x]}{x}' for x in xFonts if x in xFonts]
    if found:
        for i in found:
            print(f'      {i}      ')

custom_fig = Figlet(font=(input(" ==> Enter Your Choice 👉  ")))
text = input(" ==> Enter Your Text 👉  ")
print(fade.brazil(custom_fig.renderText(text)))
texto = custom_fig.renderText(text)
with open('ascii.txt', 'a') as file:
    file.write(f'{texto}\n')