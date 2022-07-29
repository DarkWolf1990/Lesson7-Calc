def Variable():
    return input('Введите номер выбранного пункта : ')

def Reader(i:str):
    match i:
        case "Ir":
            return [input('Введите математическое выражение: ')]
        case "Comp":
            x = complex(input('Введите первое значение: '))
            y = complex(input('Введите второе значение: '))
            z = input('Введите знак операции: ')
            match z:
                case "+": return [x,'+',y]
                case "-": return [x,'-',y]
                case "*": return [x,'*',y]
                case "/": return [x,'/',y]
                case "^": return [x,'**',y]