import parserPDF


if __name__ == "__main__":
    import sys 

    prog = open(sys.argv[1]).read()
    result = parserPDF.yacc.parse(prog, debug=True)
    result.execute()