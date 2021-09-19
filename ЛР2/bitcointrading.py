import random

print("Яка ціна біткойна зараз?")
userinput = input()

responcelist = ("ЗАКУПАЄМОСЯ НА ПОВНУ КАТЛЕТУ", "ТУ ЗЕ МУН", "ВІДКУПАЄМО ДНО", "ЧАС ДОКУПАТЬ", "ЗАХОДИМ В ЛОНГ", "ПОРА ЗАКУПИТИСЬ НА ВСЮ ПЕНСІЮ БАБКИ")
print(random.choice(responcelist))