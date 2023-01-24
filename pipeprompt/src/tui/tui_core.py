import curses
from typing import List
from argparse import ArgumentParser
from pipeprompt.src.classes.row import Row
from pipeprompt.src.classes.menu import BaseMenu





def entry_point(rows: List[Row]):
    menu = BaseMenu(rows)

    key = ""
    while key != 'q':
        menu.refresh_menu()
        key = menu.get_key()
        event_loop(menu, key)

        menu.stdscr.addstr(10, 20, key)



def event_loop(menu: BaseMenu, key: str):
    if key == '/':
        menu.search()



