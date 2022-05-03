from IO import FileReader, Parser
from Solver import Literal, Clause, Solver

def main() -> None:

    #TODO:
    reader = FileReader('input/', 'output/')
    infiles = reader.inputFiles()
    outfiles = reader.outputFiles()

    parser = Parser()
    solver = Solver()

    for i in range(len(infiles)):
        parser.read(infiles[i])
        solver.setAlpha(parser.alpha())
        solver.setKB(parser.kb())
        conclusion = solver.pl_resolution()
        parser.write(outfiles[i], solver.stepResult(), conclusion)

if __name__ == '__main__':
    main()