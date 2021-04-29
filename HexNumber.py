#Scanner created with HexNumber.ATG data
from converter import *

characters = []
characters.append('upletter = "A".."Z".')
characters.append('downletter = "a".."z".')
characters.append('letter = "abcdefghijklmnopqrstuvwxyz"+upletter+downletter.')
characters.append('digit = "0123456789".')
characters.append('hexdigit = digit+"ABCDEF".')
characters.append('hexterm = "H".')
characters.append('tab = CHR(9).')
characters.append('eol = CHR(10).')
characters.append('whitespace = CHR(13)+eol+tab+CHR(13).')
characters.append('sign = "+"+"-".')

keywords = []
keywords.append('while = "while".')
keywords.append('do = "do".')

tokens = []
tokens.append('ident = letter{letter|digit} EXCEPT KEYWORDS.')
tokens.append('hexnumber = hexdigit{hexdigit}hexterm EXCEPT KEYWORDS.')
tokens.append('number = digit{digit}.')
tokens.append('signnumber = [sign]digit{digit}.')
tokens.append('whitetoken = whitespace{whitespace}.')

nameATG = "HexNumber"
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