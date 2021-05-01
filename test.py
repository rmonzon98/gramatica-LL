#Scanner created with HexNumber.ATG data
from AFDFixed.AFD import *


adfArray = []
ident= 'ident'
temp = AFD(ident)
tempidentAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidentAcceptance)
tempidentTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 1: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}, {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempidentTransitions)
adfArray.append(temp)
hexnumber= 'hexnumber'
temp = AFD(hexnumber)
temphexnumberAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(temphexnumberAcceptance)
temphexnumberTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: {65, 66, 67, 68, 69, 70, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57}, 2: {72}}, 2: {}}

temp.setTransition(temphexnumberTransitions)
adfArray.append(temp)
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumberTransitions)
adfArray.append(temp)
signnumber= 'signnumber'
temp = AFD(signnumber)
tempsignnumberAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(tempsignnumberAcceptance)
tempsignnumberTransitions = {0: {1: {43, 45}, 2: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}}, 1: {2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 2: {2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempsignnumberTransitions)
adfArray.append(temp)
whitetoken= 'whitetoken'
temp = AFD(whitetoken)
tempwhitetokenAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempwhitetokenAcceptance)
tempwhitetokenTransitions = {0: {1: [{9, 10, 13}]}, 1: {1: [{9, 10, 13}]}}

temp.setTransition(tempwhitetokenTransitions)
adfArray.append(temp)
temp = ''
name = ""
previousName = ''
previousAcceptance = ''
found = False
tokensFound = []
text = '12H   -2 22 sdasd  22 22sa'
for i in text:
    temp = temp + i
    for j in range (0,len(adfArray)):
        found, acceptance, name= adfArray[j].simulation(temp)
        if found:
            previousName = name
            previousAcceptance = acceptance
            break
        else:
            if not(j == len(adfArray)-1):
                pass
            else: 
                temp = temp[:len(temp)-1]
                if not(previousName == '') and not(previousAcceptance == ''):
                    tokensFound.append((temp,previousName))
                previousName = ''
                temp = i
                for k in adfArray:
                    found, acceptance, name= k.simulation(temp)
                    if found:
                        previousName = name
                        previousAcceptance = acceptance
                        break
                if found:
                    break

print(temp)
print(previousAcceptance)
if acceptance:
    tokensFound.append((temp,name))
print(tokensFound)