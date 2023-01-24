
class RowFunctions:
    def __init__():
        pass

    def rowFunc1():
        pass

class Row:
    def __init__(self, row_data: str="", color: str = "", cmd: str = "", indent: str = ""):
        self.row_data: str = row_data
        self.color: str = color
        self.cmd: str = cmd
        self.indent: str = indent

        self.show = True
    

# This is used as a constructor for row data at parse time.
ROW_KWARGS = {"row_data": "", "color": "", "cmd": "", "indent": ""}