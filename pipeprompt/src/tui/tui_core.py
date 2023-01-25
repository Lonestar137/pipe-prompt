import subprocess
import curses
from typing import List
from argparse import ArgumentParser
from pipeprompt.src.classes.row import Row
from pipeprompt.src.classes.menu import BaseMenu
from pipeprompt.src.constants import PLATFORM





def entry_point(rows: List[Row]):
    menu = BaseMenu(rows)

    key = ''
    while key not in ['q', '\n']:
        menu.refresh_menu()
        key = menu.get_key()
        event_loop(menu, key)

        menu.stdscr.addstr(10, 20, key)



def event_loop(menu: BaseMenu, key: str):
    if key == '/':
        menu.search()
    elif key == 'j':
        menu.down()
    elif key == 'k':
        menu.up()
    elif key == "\n":
        return_row(menu.current_selected_item)
        curses.endwin()
    elif key == "p":
        # print current index for debugging
        curses.endwin()
        print(str(menu.current_selected_item.row_data))


def return_row(row: Row)->None:
    if row.cmd != '':
        run_command(row)
    else:
        print(row.row_data)


    
def run_command(row: Row)->None:
    result = ""
    if PLATFORM.startswith('win'):
        try:
            powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.01\\powershell.exe"
            result = subprocess.run([powershell_path, "/c", row.cmd], capture_output=True, text=True)
        except:
            cmd_path = "C:\\Windows\\System32\\cmd.exe"
            result = subprocess.run([cmd_path, "/c", row.cmd], capture_output=True, text=True)
    else:
        result = subprocess.run(row.cmd.split(' '), capture_output=True, text=True)

    print(result.stdout)





