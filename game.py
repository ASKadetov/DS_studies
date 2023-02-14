# Игра "Угадай число"

import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))
    
    if predict_number < number:
        print("Угадываемое число больше")
    elif predict_number > number:
        print("Угадываемое чило меньше")
    else:
        print(f"Вы угадали число за {count} попыток. Это число: {number}")
        break
    
