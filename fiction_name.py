def get_pseudonym(name_surname):
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