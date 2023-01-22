from typing import List
from argparse import ArgumentParser
from pipeprompt.src.constants import CWD
from pipeprompt.src.args import args_core
from pipeprompt.src.classes.row import Row
from pipeprompt.src.stdin import standard_core


def main():
    try:
        arg_json_directory = f"{CWD}/args/json/"

        args: ArgumentParser = args_core.build_args_and_parse(arg_json_directory)


        std_input: str = ""
        if args.debug:
            # std_input: str = "hello_world@#color: testing command #@"
            std_input: str = "hello_world@#cmd: testing command #@"
            # std_input: str = "hello_world"
        else:
            std_input: str = standard_core.collect_pipe_input()

        rows: List[Row] = standard_core.entry_point(std_input, args)

    except KeyboardInterrupt:
        print("Process closed due to keyboard interrupt.")

if __name__ == "__main__":
    main()
