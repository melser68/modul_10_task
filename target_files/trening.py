import keyboard

key = 'a'

while True:
    if keyboard.is_pressed(key):
        print('Нажата клавиша: ' + key)
        False
