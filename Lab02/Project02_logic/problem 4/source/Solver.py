
#Literal from the clause
class Literal:
    __value: str

    def __init__(self, value: str) -> None:
        self.__value = value
        self.reduce()

    def __hash__(self):
        return hash(self.__value)
    
    def __str__(self) -> str:
        return self.__value

    def __eq__(self, other: 'Literal'):
        return self.__value == other.value()

    def __lt__(self, other: 'Literal'):
        return self.value() < other.value()

    def value(self) -> str:
        return self.__value

    #Check if the literal is positive
    def isPositive(self) -> bool:
        numberOfMinus = self.__value.count('-')
        
        #If the number of minus is odd => not positive
        if 1 == numberOfMinus & 1:
            return False
        return True

    #Reduce literal to atom form
    #   Example:    ----A = A
    #               ---A = -A
    def reduce(self) -> None:

        if not self.isPositive():
            self.__value = self.__value.replace('-', '')
            self.__value = '-' + self.__value
        else:
            self.__value = self.__value.replace('-', '')

        
    def inverse(self) -> 'Literal':
        return Literal('-' + self.__value)

    #return true if (literal Or Not(literal))
    #   else: false
    def Or(self, literal: 'Literal') -> bool:

        inverseForm = self.inverse()
        if inverseForm == literal:
            return True

        return False

class Clause:
    __literals: set
    __isAppliable: bool

    def __init__(self, literals: set, isAppliable: bool) -> None:
        self.__literals = literals
        self.__isAppliable = isAppliable

    def __hash__(self):
        hashableSet = frozenset(self.__literals)
        return hash(hashableSet)

    def __str__(self) -> str:
        needle = ' OR '

        return needle.join(literal.value() for literal in self.__literals)


    def literals(self) -> set:
        return self.__literals

    def isAppliable(self) -> bool:
        return self. __isAppliable

    def isEmpty(self) -> bool:
        return 0 == len(self.__literals)

    def resolve(self, other: 'Clause') -> 'Clause':

        newClauseLiteral = self.literals().union(other.literals())
        
        #delete the 1st counter literals
        for literal in newClauseLiteral:
            inverse = literal.inverse()
            if inverse in newClauseLiteral:
                newClauseLiteral.remove(literal)
                newClauseLiteral.remove(inverse)
                break
        
        for literal in newClauseLiteral:
            inverse = literal.inverse()
            if inverse in newClauseLiteral:
                return Clause(newClauseLiteral, False)
        
        return Clause(newClauseLiteral, True)

        
    def isAbleToResolve(self, other: 'Clause') -> bool:

        for literal in self.__literals:
            if literal.inverse() in other.literals():
                return True

        return False


class Solver:
    __alpha: Clause
    __kb: list
    __stepResult: list

    def __init__(self, alpha: Clause, kb: list) -> None:
        self.__alpha = alpha
        self.__kb = kb

    def setAlpha(self, alpha: Clause) -> None:
        self.__alpha = alpha
    
    def setKB(self, kb: list) -> None:
        self.__kb = kb

    def addNotAlphaIntoKB(self) -> None:

        #split literal from literals,add to list, then sort it (because set is not ordered)
        literals = [literal.inverse() for literal in self.__alpha.literals()]
        literals.sort()
        
        #Add the literal from alpha to kb
        for literal in literals:
            self.__kb.append(literal)
    
    def pl_resolution(self) -> str:
        self.addNotAlphaIntoKB()

        resolvent: Clause
        

        while True:
            resolvents = []
            for i in range(0, len(kb) - 1):
                for j in range(i + 1, len(kb)):
                    if kb[i].isAbleToResolve(kb[j]):
                        
                        resolvent = kb[i].resolve(kb[j])

                        #Check if the resolvent is not the True clause
                        #   => add to KB
                        if resolvent.isAppliable():
                            resolvents.append(resolvent)

            
            self.__stepResult.append(resolvents)
            for resolv in resolvents:
                if resolv.isEmpty():
                    return "YES"



                        
        