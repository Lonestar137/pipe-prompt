import sys
from pipeprompt.src.logger import *
from pipeprompt.src.stdin.input_processor.processor import parse_standard_data
from pipeprompt.src.classes.row import Row
from argparse import ArgumentParser
from typing import List

# TODO make this function non-blocking if there is no std input.
def collect_pipe_input()->str:
    """Collect platform specific standard input text, i.e. from | 

    Returns:
        str: Mutliline str of data from pipe.
    """
    std_in_text = ""
    for line in sys.stdin:
        std_in_text += line
    return std_in_text

def get_rows(std_in_text: str, args: ArgumentParser)->List[Row]:

        if args.delimiter:
            parse_standard_data(std_in_text, args.delimiter)
        else:
            parse_standard_data(std_in_text)

def entry_point(std_in_text: str, args: ArgumentParser):
    """Commandline args to pass to the program.
    Examples: --vi enables vim keybinds.
    Or standard input from | char

    Args:
        args (List[str]): program arguments to enable certain settings.
    """
    if std_in_text == "":
        print("no input text")
        if args.debug:
            logging.info("Starting w/ no std input")
    else:
        print("input text detected")
        rows: List[Row] = get_rows(std_in_text, args)

        print("Result: ", rows[0].row_data)

        
