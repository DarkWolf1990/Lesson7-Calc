import re

def Calc (ls):
    if(len(ls) == 1):
        return round(eval(ls[0]),3)
    else:
        match ls[0][1]:
            case "+": return ls[0][0]+ls[0][2]
            case "-": return ls[0][0]-ls[0][2]
            case "*": return ls[0][0]*ls[0][2]
            case "/": return ls[0][0]/ls[0][2]
            case "^": return ls[0][0]**ls[0][2]