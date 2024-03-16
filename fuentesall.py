from pyfiglet import FontNotFound
import pyfiglet
import time
import fade
from listfonts import allfonts

print(fade.fire('''
    ***************************************************
    *    _   ___  ___ ___ ___   _____ _____  _______  *
    *   /_\\ / __|/ __|_ _|_ _| |_   _| __\\ \\/ /_   _| *
    *  / _ \\\\__ \\ (__ | | | |    | | | _| >  <  | |   *
    * /_/ \\_\\\\___/\\___|___|___|  |_| |___/_/\\_\\ |_|   *
    *                                                 *
    *   ___ ___ _  _ ___ ___    _ _____ ___  ___      *
    *  / __| __| \\| | __| _ \\  /_\\_   _/ _ \\| _ \\     *
    * | (_ | _|| .` | _||   / / _ \\| || (_) |   /     *
    *  \\___|___|_|\\_|___|_|_\\/_/ \\_\\_| \\___/|_|_\\     *
    *                                                 *
    *              coded by ZLostTK                   *
    *                                                 *
    ***************************************************
    *                                                 *
    *     😊 Choose Your Favourite Font 😊           *
    *                                                 *
    ***************************************************
    '''))
n = 100
def barra(a,b):
  frac = b/a
  falta = a - b
  icono = u'\u2588'
  print(f'\r |{icono*b}{'-'*falta}|{frac:.2%}', end='\r')

text = input(" ==> Enter Your Text 👉  ")
found = [x for x in allfonts if x in allfonts]
if found:
    for i in found:
        try:
            custom_fig = pyfiglet.Figlet(font=i)
            texto = custom_fig.renderText(text)
            with open('ascii.txt', 'a', encoding='utf-8') as file:
                file.write(f'{texto}\n')
        except FontNotFound:
            print('')
    for i in range(n+1):
        time.sleep(0.02)
        barra(n,i) 