from FileReader import FileReader
from Solver import Literal, Clause, Solver

def main() -> None:

    #TODO:
    # reader = FileReader('/input', '/output')
    # reader.inputFiles()
    # reader.outputFiles()

    # literals = {Literal('A'), Literal('-A'), Literal('-B'), Literal('-C'), Literal('----B'), Literal('--B')}
    # clause = Clause(literals, True)
    # ls = []

    # solver = Solver(clause, ls)
    # solver.addNotAlphaIntoKB()

    alpha_literals = {Literal('-A')}

    literals0 = {
        Literal('-A'),
        Literal('B'),
    } 

    literals1 = {
        Literal('B'),
        Literal('-C'),
    }

    literals2 = {
        Literal('A'),
        Literal('-B'),
        Literal('C'),
    }

    literals3 = {
        Literal('-B'),
    }

    alpha = Clause(alpha_literals, True)
    kb = {
        Clause(literals0, True), 
        Clause(literals1, True), 
        Clause(literals2, True), 
        Clause(literals3, True), 
    }

    solver = Solver(alpha, kb)
    solver.pl_resolution()

    for resolvents in solver.stepResult():
        print(len(resolvents))
        for resolvent in resolvents:
            print(resolvent)


if __name__ == '__main__':
    main()