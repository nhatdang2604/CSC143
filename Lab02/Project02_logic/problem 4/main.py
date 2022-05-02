from source.FileReader import FileReader
from source.Solver import Literal, Clause, Solver

def main() -> None:

    #TODO:
    # reader = FileReader('/input', '/output')
    # reader.inputFiles()
    # reader.outputFiles()

    literals = {Literal('A'), Literal('-A'), Literal('-B'), Literal('-C'), Literal('----B'), Literal('--B')}
    clause = Clause(literals, True)
    ls = []

    solver = Solver(clause, ls)
    solver.addNotAlphaIntoKB()
    #print(clause)

if __name__ == '__main__':
    main()