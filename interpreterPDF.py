from pathlib import Path
import parserPDF
import utils.interfacer

PROJECT_FOLDER = Path(__file__).parent

if __name__ == "__main__":
    import sys
    input_file = Path(sys.argv[1])
    output_file = PROJECT_FOLDER / 'generated' / input_file.with_suffix('.pdf').name

    prog = input_file.read_text()
    result = parserPDF.yacc.parse(prog)

    parserPDF.AST.INTERFACER = utils.interfacer.Interfacer(str(output_file))
    result.execute()

    parserPDF.AST.INTERFACER.c.save()
