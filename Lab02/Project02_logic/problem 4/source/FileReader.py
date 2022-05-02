import os
from os import listdir
from os.path import isfile, join

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

        #Create the input dir if not exists
        self.__createFileIfNotExists(self.__inputDir)
        
        #Iterate over the input dir
        self.__inputFiles = [file for file in listdir(self.__inputDir) if isfile(join(self.__inputDir, file))]
        
        return self.__inputFiles

    def outputFiles(self) -> list:
        
        #Create the input dir if not exists
        self.__createFileIfNotExists(self.__outputDir)

        #Create output file base on input file
        self.__outputFiles = [file.replace('input', 'output') for file in self.__inputFiles]

        return self.__outputFiles