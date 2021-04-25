from DirectAFD.builder import buildAFD
from PostfixGen.infixtopostfix import *

def addOr(expresion):
    newExpresion = ""
    newExpresion = expresion[0]
    i=1
    while i<len(expresion):
        newExpresion = newExpresion +"|"+expresion[i]
        i = i + 1
    return newExpresion
    print(newExpresion)

def extractExp(expresion):
    newExpresion = ""
    for i in expresion:
        newExpresion = newExpresion + i
    return newExpresion

def createCharactersDict(characters):
    charactersDict = {}
    for i in characters:
        index = i.index("=") + 2
        name = i[:index-3]  #Se toma el nombre del character
        info = i[index:] + chr(3)   #Se toma toda la informacion del character
        j = 0
        output = []
        exp = []
        count = 0
        par = False
        while j < len(info)-1:  #Se analiza todo la informacion
            if info[j] == '"':
                if count == 0:
                    count = 1
                else:
                    output.append(addOr(exp))
                    exp = []
                    count = 0
            elif info[j] == '(':
                temp = extractExp(exp)
                exp = []
            elif info[j] ==')':
                if temp == "CHR":
                    output.append(chr(int(extractExp(exp))))
            elif ((info[j] == "." and info[j+1] == chr(3)) or info[j] == chr(3)):
                pass
            else:
                exp.append(info[j])
            j = j + 1
        charactersDict.update({name:output[0]})
    return charactersDict

def createKeywordsDict(charactersDict, keywords):
    keywordsDict = {}
    for i in keywords:
        index = i.index("=") + 2
        name = i[:index-3]  #Se toma el nombre del character
        info = i[index:].replace('"', '') + chr(3)
        info = info.replace('.', '')
        keywordsDict.update({name:info})
    return keywordsDict

def createTokensDict(charactersDict, tokens):
    keys = list(charactersDict.keys())
    tokensDict = {}
    exceptions = []
    for i in tokens:
        
        index = i.index("=") + 2
        name = i[:index-3]  #Se toma el nombre del character
        info = i[index:].replace('{', '(').replace('}', ')*') + chr(3)
        if "EXCEPT " in info:
            index = info.index("EXCEPT ") + 7
            tempExc = info[index:len(info)-2]
            exceptions.append(tempExc)
            info = info.replace((' EXCEPT '+ tempExc), '')
        else:
            exceptions.append(None)
        for j in keys:
            if j in info:
                info = info.replace(j, ('('+charactersDict.get(j)+')'))
        j = 0
        while j<len(info):
            if info[j] == chr(3):
                info = info.replace(('.'+chr(3)), '')
            j=j+1
        tokensDict.update({name:info})
    return tokensDict,exceptions
        