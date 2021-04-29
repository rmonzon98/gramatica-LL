#Scanner created with Aritmetica.ATG data
from converter import *

characters = []
characters.append('letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".')
characters.append('digit = "0123456789".')
characters.append('tab = CHR(9).')
characters.append('eol = CHR(10).')

keywords = []
keywords.append('while = "while".')
keywords.append('do = "do".')
keywords.append('if = "if".')
keywords.append('switch = "switch"')

tokens = []
tokens.append('ident = letter{letter|digit} EXCEPT KEYWORDS.')
tokens.append('number = digit{digit}.')

nameATG = "Aritmetica"
specialCharacters = {}
special = {}
specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "'" : set([39])})
special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "'" :'h'})
charactersDict = createCharactersDict(characters)
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