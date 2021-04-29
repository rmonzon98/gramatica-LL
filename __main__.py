from EscrituraPy.fileWritter import *
from LecturaATG.fileReader import read_file
from converter import *

if __name__ == "__main__":
    
    archivo = input('Ingrese el nombre del archivo: ')
    characters, keywords, tokens, nameATG = read_file(archivo)
    print("-"*40,nameATG,"-"*40)
    print("Characters:")
    for i in characters:
        print(chr(9)+i)
    print("Keywords:")
    for i in keywords:
        print(chr(9)+i)
    print("Tokens:")
    for i in tokens:
        print(chr(9)+i)
    
    specialCharacters = {}
    special = {}
    specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "'" : set([39])})
    special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "'" :'h'})

    charactersDict = createCharactersDict(characters)
    KeywordsDict = createKeywordsDict(charactersDict,keywords)
    tokensDict, exceptions = createTokensDict(charactersDict, tokens, specialCharacters, special)

    tokensArray = functionsCreator(tokensDict, charactersDict)
    for i in tokensArray:
        i.correctTransitions(charactersDict, specialCharacters, special)

    #print("-"*45+"ADF de los tokens"+"-"*45)
    #for i in tokensArray:
        #print(i.getTransitions())
    """
    line1 = "specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "+chr(34)+"'"+chr(34)+" : set([39])})"
    line2 = "special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "+chr(34)+"'"+chr(34)+" :'h'})"
    scanner = fileWritter(nameATG)
    scanner.writeImport('from converter import *')
    scanner.addVariable("nameATG",nameATG)
    scanner.writeSentence('specialCharacters = {}')
    scanner.writeSentence('special = {}')
    scanner.writeSentence(line1)
    scanner.writeSentence(line2)
    scanner.addDict('charactersDict', charactersDict)
    scanner.addDict('KeywordsDict', KeywordsDict)
    scanner.addDict('tokensDict', tokensDict)   
    scanner.writeFor('for i in tokensArray:')
    scanner.writeSentence('i.correctTransitions(charactersDict, specialCharacters, special)')
    scanner.substractTab()
    scanner.writeSentence('print("-"*45+"ADF de los tokens"+"-"*45)')
    scanner.writeFor('for i in tokensArray:')
    scanner.writeSentence('print(i.getTransitions())')
    """
    print(".py escrito con exito")