#Scanner created with Double.ATG data
from converter import *

characters = []
characters.append('digit = "0123456789".')
characters.append('tab = CHR(9).')
characters.append('eol = CHR(10).')
characters.append('blanco = eol+CHR(13)+tab+" ".')

keywords = []
keywords.append('while = "while".')
keywords.append('do = "do".')

tokens = []
tokens.append('number = digit{digit}.')
tokens.append('decnumber = digit{digit}"."digit{digit}.')
tokens.append('white = blanco{blanco}.')

nameATG = "Double"
specialCharacters = {}
special = {}
specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "'" : set([39])})
special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "'" :'h'})
charactersDict = createCharactersDict(characters)
KeywordsDict = createKeywordsDict(charactersDict,keywords)
tokensDict, exceptions = createTokensDict(charactersDict, tokens, specialCharacters, special)
tokensArray = functionsCreator(tokensDict, charactersDict)
keysCharacters = list(charactersDict.keys())
for i in tokensArray:
    i.correctTransitions(charactersDict, specialCharacters, special)
print("-"*45+"ADF de los tokens"+"-"*45)
for i in tokensArray:
    print(i.getTransitions())
#for i in tokensArray:
    #print(i.getName(),": ",i.getTransitions())
    #print("")
#tokensArray[0].simulation(0,'asdava')