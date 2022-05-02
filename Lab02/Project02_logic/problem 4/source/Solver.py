
#Literal from the clause
class Literal:
    __value: str

    def __init__(self, value: str) -> None:
        self.__value = value
        self.reduce()

    def __hash__(self):
        return hash(self.__value)
    
    def __str__(self):
        return self.__value

    def value(self) -> str:
        return self.__value

    #Check if the literal is positive
    def isPositive(self) -> bool:
        numberOfMinus = self__value.count('-')

        #If the number of minus is odd => not positive
        if 1 == numberOfMinus&1:
            return False
        return True

    #Reduce literal to atom form
    #   Example:    ----A = A
    #               ---A = -A
    def reduce(self) -> None:

        #Delete all minus in literal
        self.__value = self.__value.replace('-', '')

        if not self.isPositive():
            self.__value = '-'.join(self.__value)
        
    def inverse(self) -> Literal:
        return Literal('-'.join(self.__value ))

class Clause:
    __literals: set

    def __init__(self, literals: set) -> None:
        self.__literals = literals

    def literals(self) -> set:
        return self.__literals

    def Or(self, literal: Literal) -> None:

        #Check if there are an inverse of the given literal
        inverse = literal.inverse()

        #Add the literal if there is no inverse form in the clause, else remove the inverse form
        if inverse not in self.__literals:
            self.__literals.add(literal)
        else:
            self.__literals.remove(inverse)
    
    def Or(self, clause: Clause) -> None:
        literals = clause.literals()
        for literal in literals:
            self.Or(literal)
