import curses
from typing import List
from argparse import ArgumentParser
from pipeprompt.src.classes.row import Row

class CurseFunctions():

    def enable_cursor(self):
        curses.curs_set(1)

    def highlight_line(self, stdscr, curse_style, height: int, width: int, text: str):
        if height > curses.LINES:
            height = curses.LINES

        if width > curses.COLS:
            width = curses.COLS
        
        stdscr.addstr(height, width, text, self.underline | curse_style)
        
        
        

class MenuFunctions(CurseFunctions):
    def up():
        pass

    def down():
        pass

    def execute():
        pass

    def refresh_menu(self):
        self.stdscr.clear()
        self.refresh_dimensions()

        midpoint: int = int(len(self.content)/2)
        indent_padding = ""
        for i, row in enumerate(self.content):
            starting_text_line = self.content_menu_line + i
            if self.height != i:
                self.stdscr.addstr(starting_text_line, self.base_x, f"{indent_padding}{row.indent}{row.row_data}")

            if i < midpoint and self.padding:
                indent_padding += " "
            else:
                indent_padding = indent_padding[:-1]


        self.stdscr.refresh()
    
    def search(self):
        self.refresh_menu()

        prompt_text = "FILTER: "
        search_text = ""
        key = ""
        self.highlight_line(self.stdscr, curses.A_STANDOUT, self.search_bar_line, self.search_bar_width, "FILTER: ")
        while key != 'q':
            key = self.get_key()
            self.stdscr.refresh()

            if ord(key) == 8 and len(search_text) > 0:#curses.KEY_BACKSPACE:
                search_text = search_text[:-2]
                self.stdscr.clear()
                self.refresh_menu()

            if len(search_text) < 30 and len(search_text) < self.width:

                search_text += key
                self.highlight_line(self.stdscr, curses.A_UNDERLINE, self.search_bar_line, len(prompt_text)+self.search_bar_width, search_text)

        return search_text
    
    def quit(self):
        self.stdscr.endwin()

    def get_key(self):
        return self.stdscr.getkey()

    def refresh_dimensions(self):
        self.height = curses.LINES
        self.width = curses.COLS


class BaseMenu(MenuFunctions):
    def __init__(self, content: List[Row]) -> None:
        # Data
        self.content = content

        # Screen values
        self.stdscr = curses.initscr()
        self.height = curses.LINES
        self.width = curses.COLS

        # Positioning
        self.base_x = 1
        self.base_y = 1
        self.search_bar_width = 0 + self.base_x
        self.search_bar_line = 2 + self.base_y
        self.content_menu_line = self.search_bar_line + 1
        
        # Styling
        self.bold = curses.A_BOLD
        self.underline = curses.A_UNDERLINE
        # self.green_one = curses.init_pair(1, curses.COLOR_GREEN, -1)
        # self.yellow_one = curses.init_pair(2, curses.COLOR_YELLOW, -1)
        # self.red_one = curses.init_pair(3, curses.COLOR_RED, -1)

        # Options
        self.padding = True
        curses.curs_set(0)
