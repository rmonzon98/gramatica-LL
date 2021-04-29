class AFD:

    def __init__(self, states, acceptance, name):
        self.name = name
        self.listStates = states
        self.afdAcceptanceDict = acceptance
        self.states = []
        self.nodes = []
        for i in self.listStates:  
            if i[0] not in self.states:
                temp = Node(self.afdAcceptanceDict.get(i[0]))
                self.states.append(i[0])
                temp.setInitial(i[0])
                self.nodes.append(temp)
            if i[2] not in self.states:
                temp = Node(self.afdAcceptanceDict.get(i[2]))
                self.states.append(i[2])
                temp.setInitial(i[2])
                self.nodes.append(temp)
            for j in self.nodes:
                if j.getInitial() == i[0]:
                    j.setNewTransition(i[2],i[1])
        self.transitions = self.setInitialTransitions()

    def getName(self):
        return self.name
        
    def correctTransitions(self, charactersDict, specialCharacters, special):
        keys = list(charactersDict.keys())
        values = list(charactersDict.values())
        for i in self.nodes:
            i.correctTransitions(keys,values,specialCharacters, special)
        self.transitions = self.getNewTransitions()

    def getNewTransitions(self):
        a = {}
        for i in self.nodes:
            a.update({i.getInitial():i.getTransitions()})
        return a
    
    def simulation(self, initialNode,expresion):
        for i in self.nodes:
            if i.getInitial() == initialNode:
                temp = i

    def getDict(self):
        return self.afdAcceptanceDict
    
    
    def getTransitions(self):
        return self.transitions

    def setInitialTransitions(self):
        a = {}
        for i in self.nodes:
            a.update({i.getInitial():i.getTransitions()})
        return a

class Node:

    def __init__(self, acceptance):
        self.acceptance = acceptance
        self.transitions = {}
    
    def correctTransitions(self, keys, values, specialCharacters, special):
        try:
            key = list(self.transitions.keys())
            specialValues = list(special.values())
            specialKeysAscci = list(specialCharacters.values())
            if len(key) == 1:
                key = key[0]
                temp = []
                valuesSub = list(self.transitions.values())[0]
                valuesSub = valuesSub[0]
                if valuesSub in ["a","b","c","d","e","f","g","h"]:
                    index = specialValues.index(valuesSub)
                    temp = specialKeysAscci[index]
                else:
                    valuesSub = int(valuesSub)
                    if type(key) == int:
                        for i in list(self.transitions.values()):
                            for j in i:
                                index = int(j)
                                temp.append(values[index])
                    
                    else:
                        index = specialValues.index(flag)
                        temp = specialKeysAscci[index]
                
                self.transitions.update({key:temp})
            else:
                for i in key:
                    flag = list(self.transitions.get(i))
                    flag = flag[0]
                    if flag.isnumeric():
                        temp = values[int(flag)]
                        self.transitions.update({i:temp})
                    else:
                        index = specialValues.index(flag)
                        temp = specialKeysAscci[index]
                        self.transitions.update({i:temp})
        except:
            pass

    def setNewTransition(self, nextNode, label):
        if nextNode in self.transitions:
            #Si la llave existe
            temp = list(self.transitions.get(nextNode))
            temp.append(label)
            self.transitions.update({nextNode:temp})
        else:
            #Si la llave no existe
            self.transitions.update({nextNode:[label]})
    
    def toString(self):
        s = "" 
        for key in self.transitions:
            t = ""
            for j in list(self.transitions.get(key)):
                t = t + j
            s = s + t + "\n"
        return ('node ' + str(self.initial) + ' has this labels: ' + s)

    def setInitial(self, initial):
        self.initial = initial

    def getInitial(self):
        return self.initial
    
    def getTransitions(self):
        return self.transitions