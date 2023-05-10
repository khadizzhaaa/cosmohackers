# Каждому начинающему хакеру нужен псевдоним! 
# https://media.giphy.com/media/13AN8X7jBIm15m/giphy.gif
# Phantom Phreak, Acid Burn, Zero Cool и Crash Override - вот некоторые примечательные примеры из фильма "Хакеры".

# Ваша задача - написать скрипт, который превращает имя и фамилию в псевдоним.

# Примечания:
# 1.
# Скрипт должн превращать первую букву имени в значение из словаря FIRST_NAME
# Соответственно, первая буква фамилии должна превращаться в значение из словаря SURNAME
# Имя и фамилия должны быть записаны латиницей!
# Используйте следующие словари

FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy', 'F': 'Function', 'G': 'Gloom', 'H': 'Holo', 'I': 'Inovation', 'J': 'Jealous', 'K': 'Katana', 'L': 'Logic', 'M': 'Malware', 'N': 'Negative', 'O': 'Operative', 'P': 'Paragon', 'Q': 'Quant', 'R': 'Recursive', 'S': 'Seismic', 'T': 'Triangle', 'U': 'Ultra', 'V': 'Violent', 'W': 'WiFi', 'X': 'X-ray', 'Y': 'Yell', 'Z': 'Zephyr'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'E': 'Enormous', 'F': 'Field', 'G': 'Garbage', 'H': 'Half-life', 'I': 'Intranet', 'J': 'Jack', 'K': 'Killer', 'L': 'Lava', 'M': 'Madness', 'N': 'Nickname', 'O': 'Ops', 'P': 'Payload', 'Q': 'Qubit', 'R': 'Radiant', 'S': 'Sygnus', 'T': 'T-Rex', 'U': 'Unity', 'V': 'Vox','W': 'Worm','X': 'Xeon','Y': 'Yawn','Z': 'Zeppelin'}

# 2.
# Если первый символ любого из имен не является буквой от A до Z, вы должны вернуть 
# "Ваше имя должно начинаться с буквы от A до Z".

# 3.
# Иногда люди могут забыть написать первую букву своего имени с заглавной буквы, поэтому ваш скрипт должн учитывать эти грамматические ошибки.

name_surname = input()


name = name_surname.split(' ')[0]
surname = name_surname.split(' ')[1] 

name = name.upper()
surname = surname.upper()

if (name[0] in FIRST_NAME) and (surname[0] in SURNAME):
    psev_name = FIRST_NAME[name[0]]
    psev_surname = SURNAME[surname[0]]
    print(psev_surname, psev_name)
else:
    print("Ваше имя должно начинаться с буквы от A до Z")
    
# Хорошо! Теперь необходимо превратить это решение в функцию.
# Его также нужно передать на репозиторий с помощью git 
