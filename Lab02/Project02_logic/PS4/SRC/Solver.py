
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

        thisValue = self.value().replace('-', '')
        thatValue = other.value().replace('-', '')

        return thisValue < thatValue

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

    def __eq__(self, other: 'Clause'):
        return self.__literals == other.literals()

    def __str__(self) -> str:
        
        if (self.isEmpty()):
            return "{}"

        needle = ' OR '
        orderedSet = sorted(self.__literals)
        buffer = needle.join(literal.value() for literal in orderedSet)
        
        return buffer


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
    __kb: set
    __stepResult: list

    def __init__(self) -> None:
        self.__stepResult = []

    def setAlpha(self, alpha: Clause) -> None:
        self.__alpha = alpha
    
    def setKB(self, kb: set) -> None:
        self.__kb = kb

    def stepResult(self) -> list:
        return self.__stepResult

    def kb(self) -> set:
        return self.__kb

    def addNotAlphaIntoKB(self) -> None:

        #Add the literal from alpha to kb
        for literal in self.__alpha.literals():
            self.__kb.add(Clause({literal.inverse()}, True))
    
    def pl_resolution(self) -> str:
        self.__stepResult = []

        self.addNotAlphaIntoKB()

        resolvent: Clause
        new = set()

        while True:
            resolvents = set()
            for clauseA in self.__kb:
                for clauseB in self.__kb:
                    if clauseA.isAbleToResolve(clauseB):
                        
                        resolvent = clauseA.resolve(clauseB)

                        #Check if the resolvent is not the True clause
                        #   => add to KB
                        if resolvent.isAppliable():
                            if resolvent not in self.__kb:
                                resolvents.add(resolvent)
                                new.add(resolvent)

            self.__stepResult.append(resolvents)

            if new.issubset(self.__kb):
                return "NO"

            for resolv in resolvents:
                self.__kb.add(resolv)

            for resolv in resolvents:
                if resolv.isEmpty():
                    return "YES"



                        
        