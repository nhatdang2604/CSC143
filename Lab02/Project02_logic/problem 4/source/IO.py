import os
from os import listdir, walk
from os.path import isfile, join
from Solver import Clause, Literal

class FileReader:

    __inputDir: str
    __outputDir: str

    __inputFiles: list
    __outputFiles: list 

    def __init__(self, inputDir: str, outputDir: str) -> None:
        self.__inputDir = inputDir
        self.__outputDir = outputDir

    
    def __createFileIfNotExists(self, filePath: str) -> None:
        if not os.path.exists(filePath): 
            os.makedirs(filePath)
       

    def inputFiles(self) -> list:

        #Iterate over the input dir
        self.__inputFiles = [join(self.__inputDir, file) for file in os.listdir(self.__inputDir) if os.path.isfile(join(self.__inputDir, file)) ]

        return self.__inputFiles

    def outputFiles(self) -> list:
        
        #Create the input dir if not exists
        self.__createFileIfNotExists(self.__outputDir)

        #Create output file base on input file
        self.__outputFiles = [file.replace('input', 'output') for file in self.__inputFiles]

        return self.__outputFiles

class Parser:

    __kb: set
    __alpha: Clause

    def __init__(self) -> None:
        __kb = set()
        __alpha = None

    def kb(self) -> set: 
        return self.__kb

    def alpha(self) -> Clause: 
        return self.__alpha

    #Read file from path, and parse into kb and alpha
    def read(self, path: str) -> None:

        #Clear old data
        self.__alpha = None
        self.__kb = set()

        file = open(path, 'r+')
        try:

            #Read raw data
            alphaBuffer = file.readline().strip()
            n = int(file.readline().strip())
            kbBuffer = []
            for i in range(n):
                kbBuffer.append(file.readline().strip())

            #parse the alpha literals
            alphaLiterals = set()
            for literal in alphaBuffer.split(' OR '):
                if (len(literal) > 0):
                     alphaLiterals.add(Literal(literal))
            self.__alpha = Clause(alphaLiterals, True)

            #parse the kb
            for clauseBuffer in kbBuffer:
                clauseLiterals = set()
                for literal in clauseBuffer.split(' OR '):
                    clauseLiterals.add(Literal(literal))
                self.__kb.add(Clause(clauseLiterals, True))


        except:
            print('Error in reading file: ', path)
            self.__alpha = None
            self.__kb = set()

        finally:
            file.close()

    def write(self, path: str, result: list, conclusion: str) -> None:

        file = open(path, 'w+')
        try:
            for stepResult in result:
                print(len(stepResult), file = file)
                for clause in stepResult:
                    print(clause, file = file)
            
            print(conclusion, file = file)

        except:
            print('Error in writing file: ', path)
            
        finally:
            file.close()

