def createScanner(characters, keywords, tokens, nameATG):
    filename = open((nameATG+'Scanner.py'), 'w+')
    filename.write('#Scanner created with %s.ATG data'%nameATG)