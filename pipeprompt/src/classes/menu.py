import curses
from typing import List
from argparse import ArgumentParser
from pipeprompt.src.classes.row import Row

class HelperFunctions:
    def get_midpoint(self):
        content_length = len(self.content)
        if content_length < self.height:
            return content_length/2
        else:
            return self.height/2

    def get_current_selected_item_index(self):
        return self.content[int(self.menu_midpoint)+1]

class CurseFunctions:

    def enable_cursor(self):
        curses.curs_set(1)

    def highlight_line(self, stdscr, curse_style, height: int, width: int, text: str):
        if height > curses.LINES:
            height = curses.LINES

        if width > curses.COLS:
            width = curses.COLS
        
        stdscr.move(height, width)
        stdscr.clrtoeol()
        stdscr.addstr(height, width, text, self.underline | curse_style | curses.color_pair(1))

class MenuFunctions(CurseFunctions, HelperFunctions):
    def down(self):
        first_element = self.content.pop(0)
        self.content.insert(-1, first_element)

        self.current_selected_item: int = self.get_current_selected_item_index()

    def up(self):
        last_element = self.content.pop(-1)
        self.content.insert(0, last_element)

        self.current_selected_item: int = self.get_current_selected_item_index()

    def execute():
        pass

    def refresh_menu(self):
        self.stdscr.clear()
        self.refresh_dimensions()

        self.midpoint: int = self.get_midpoint()
        indent_padding = ""
        for i, row in enumerate(self.content):
            not_out_of_bounds: bool = (self.height - 5 > i)
            starting_text_line = self.content_menu_line + i
            middle_of_menu: bool = (int(self.midpoint+1) == i)


            if not_out_of_bounds:
                if middle_of_menu:
                    # self.show_selected_item_cmd(row.cmd)
                    self.stdscr.addstr(starting_text_line, self.base_x, f"{indent_padding}{row.indent}{row.row_data[:self.width-15]}", curses.A_STANDOUT)
                    self.highlight_line(self.stdscr, curses.A_UNDERLINE, self.search_bar_line, self.search_bar_width, f"CMD: {row.cmd}")
                else:
                    self.stdscr.addstr(starting_text_line, self.base_x, f"{indent_padding}{row.indent}{row.row_data[:self.width-15]}")


            if i < self.midpoint and self.padding:
                indent_padding += " "
            else:
                indent_padding = indent_padding[:-1]


        self.stdscr.refresh()

    def show_selected_item_cmd(self, item: Row):
        self.highlight_line(self.stdscr, curses.A_ITALIC, self.search_bar_line, self.search_bar_width, f"CMD: {item.cmd}")

    
    def search(self):
        self.refresh_menu()

        prompt_text = "FILTER: "
        search_text = ""
        key = ""
        self.highlight_line(self.stdscr, curses.A_STANDOUT, self.search_bar_line, self.search_bar_width, "FILTER: ")
        while key != 'q':
            key = self.get_key()
            self.stdscr.refresh()

            search_text_not_too_long: bool = (len(search_text) < 30 and len(search_text) < self.width)
            is_backspace_key: bool = (ord(key) == 8 and len(search_text) > 0)
            is_enter_key: bool = (key == '\n')

            if is_backspace_key:
                search_text = search_text[:-2]
                self.stdscr.clear()
                self.refresh_menu()
            elif is_enter_key:
                return search_text
            elif search_text_not_too_long:
                search_text += key
                self.highlight_line(self.stdscr, curses.A_UNDERLINE, self.search_bar_line, len(prompt_text)+self.search_bar_width, search_text)

        return None
    
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
        self.menu_midpoint = self.get_midpoint()
        self.search_bar_width = 0 + self.base_x
        self.search_bar_line = 2 + self.base_y
        self.content_menu_line = self.search_bar_line + 1
        self.current_selected_item = self.get_current_selected_item_index()
        
        # Options
        self.padding = True
        curses.noecho()
        curses.curs_set(0)

        # Styling
        self.bold = curses.A_BOLD
        self.underline = curses.A_UNDERLINE
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        curses.init_pair(2, curses.COLOR_YELLOW, -1)
        curses.init_pair(3, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_RED, -1)
        self.green_one = curses.color_pair(1)
        self.yellow_one = curses.color_pair(2)
        self.red_one = curses.color_pair(3)

