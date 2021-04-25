class AFD:

    def __init__(self, states, acceptance):
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
        
    def getDict(self):
        return self.afdAcceptanceDict    
    
    def getTransitions(self):
        a = []
        for i in self.nodes:
            a.append(i.getTransitions())
        return a
    """
    def toString(self):
        a = []
        for i in self.nodes:
            a.append(i.getTransitions())
        return a
        s = []
        for i in self.nodes:
            s.append(i.toString())
        return s
    """


class Node:

    def __init__(self, acceptance):
        self.acceptance = acceptance
        self.transitions = {}

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
        return ('node ' + str(self.initial) + ' has this transitions: ' + s)

    def setInitial(self, initial):
        self.initial = initial

    def getInitial(self):
        return self.initial
    
    def getTransitions(self):
        return self.transitions

def concatAFD():
    print()