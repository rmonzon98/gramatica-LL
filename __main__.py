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
    line1 = "specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "+chr(34)+"'"+chr(34)+" : set([39])})"
    line2 = "special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "+chr(34)+"'"+chr(34)+" :'h'})"
    
    scanner = fileWritter(nameATG)
    scanner.writeImport('from converter import *')
    scanner.addArray("characters",characters)
    scanner.addArray("keywords",keywords)
    scanner.addArray("tokens",tokens)
    scanner.addVariable("nameATG",nameATG)
    scanner.writeSentence('specialCharacters = {}')
    scanner.writeSentence('special = {}')
    scanner.writeSentence(line1)
    scanner.writeSentence(line2)
    scanner.writeSentence('charactersDict = createCharactersDict(characters)')
    scanner.writeSentence('charactersDict = createCharactersDict(characters)')
    scanner.writeSentence('KeywordsDict = createKeywordsDict(charactersDict,keywords)')
    scanner.writeSentence('tokensDict, exceptions = createTokensDict(charactersDict, tokens, specialCharacters, special)')
    scanner.writeSentence('tokensArray = functionsCreator(tokensDict, charactersDict)')
    scanner.writeSentence('keysCharacters = list(charactersDict.keys())')
    scanner.writeFor('for i in tokensArray:')
    scanner.writeSentence('i.correctTransitions(charactersDict, specialCharacters, special)')
    scanner.substractTab()
    scanner.writeSentence('print("-"*45+"ADF de los tokens"+"-"*45)')
    scanner.writeFor('for i in tokensArray:')
    scanner.writeSentence('print(i.getTransitions())')
    print(".py escrito con exito")
