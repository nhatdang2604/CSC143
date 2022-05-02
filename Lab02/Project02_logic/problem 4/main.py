from source.FileReader import FileReader

def main() -> None:

    #TODO:
    reader = FileReader('/input', '/output')
    reader.inputFiles()
    reader.outputFiles()

if __name__ == '__main__':
    main()