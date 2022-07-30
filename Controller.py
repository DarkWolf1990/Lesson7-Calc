import Interface as Iface
import Inpt as inp
import Calculator as cl
Iface.Intface("Welcome")
while(True):
    Iface.Intface("Menu")
    i = int(inp.Variable())
    match i:
        case 1: 
            print("Ответ: " + cl.Calc(inp.Reader("Ir")))
            Iface.Intface("End")
            if(int(inp.Variable()) == 2): break
        case 2: 
            print(f'Ответ: {cl.Calc(inp.Reader("Comp"))}')
            Iface.Intface("End")
            if(int(inp.Variable()) == 2): break
        case 3: print('Будет разработано когда-нибудь')
        case 4: 
            print('Запущен выход из программы')
            break
        case _: print("Нет данных")