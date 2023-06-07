def get_pseudonym(name_surname):
    FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy', 'F': 'Function', 'G': 'Gloom', 'H': 'Holo', 'I': 'Inovation', 'J': 'Jealous', 'K': 'Katana', 'L': 'Logic', 'M': 'Malware', 'N': 'Negative', 'O': 'Operative', 'P': 'Paragon', 'Q': 'Quant', 'R': 'Recursive', 'S': 'Seismic', 'T': 'Triangle', 'U': 'Ultra', 'V': 'Violent', 'W': 'WiFi', 'X': 'X-ray', 'Y': 'Yell', 'Z': 'Zephyr'}
    SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'E': 'Enormous', 'F': 'Field', 'G': 'Garbage', 'H': 'Half-life', 'I': 'Intranet', 'J': 'Jack', 'K': 'Killer', 'L': 'Lava', 'M': 'Madness', 'N': 'Nickname', 'O': 'Ops', 'P': 'Payload', 'Q': 'Qubit', 'R': 'Radiant', 'S': 'Sygnus', 'T': 'T-Rex', 'U': 'Unity', 'V': 'Vox','W': 'Worm','X': 'Xeon','Y': 'Yawn','Z': 'Zeppelin'}
    name = name_surname.split(' ')[0]
    surname = name_surname.split(' ')[1]
    name = name.upper()
    surname = surname.upper()
    
    if (name[0] in FIRST_NAME) and (surname[0] in SURNAME):
        psev_name = FIRST_NAME[name[0]]
        psev_surname = SURNAME[surname[0]]
        return psev_surname + ' ' + psev_name
    else:
        return "Ваше имя должно начинаться с буквы от A до Z"
        
print(get_pseudonym(name_surname))
    
    
# У меня на экране при запуске этой задачи нет никакого вывода.
# Почему?
