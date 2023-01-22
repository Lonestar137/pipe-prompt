from re import Pattern
import re
from pipeprompt.src.classes.row import Row, ROW_KWARGS
from typing import List, Tuple

#  Default Regex:   @#[a-z]{3,6}:.+#@
#  This regex is used to find if there is a field in the row.  {3,6} looks for a word[a-z] that's 3-6 chars long followed by :
#  TODO arg to override the regex @# part.
def parse_standard_data(raw_data: str, str_delimiter_regex: str="@#[a-z]{3,6}:.+#@")->List[Row]:
    delimited_rows: List[str] = [""]
    delimiter: Pattern = re.compile(str_delimiter_regex)
    for row in raw_data.split('\n'):
        new_row: Row = get_new_row([], row, delimiter)
        delimited_rows.append(new_row)

    filtered_rows: List[Row] = remove_nulls(delimited_rows)
    
    return filtered_rows

def get_new_row(collected_fields: List[Row], row: str, delimiter: Pattern)->Row:
    matched_text = delimiter.search(row)
    if not matched_text:
        return map_raw_data_to_row_class(row, collected_fields)
    else:
        matched_text = matched_text.group()
        fields_from_match: List[str] = matched_text.split(delimiter.pattern[2:])
        new_field_appended: List[str] = collected_fields + fields_from_match
        row_with_field_removed: str = row.replace(matched_text, "")

        return get_new_row(new_field_appended, row_with_field_removed, delimiter)

def map_raw_data_to_row_class(row_data: str, special_fields_in_row: List[str])->Row:
    kwargs = ROW_KWARGS
    kwargs["row_data"] = row_data
    for special_field in special_fields_in_row:
        tag = extract_tag_from_special_field(special_field)
        value = extract_value_from_special_field(special_field)
        if tag in kwargs.keys():
            kwargs[tag]=value
    return Row(**kwargs)

# @param field:  "tag: value #@"
# @return tag
def extract_tag_from_special_field(field: str)-> str:
    return field.split(':')[0][2:]

#@param field: "tag: value #@"
#@return  value 
def extract_value_from_special_field(field: str)-> str:
    return field.split(':')[1][:-2].strip()

def remove_nulls(rows: List[Row])->List[Row]:
    filtered_rows: List[Row] = list(filter(None, rows))
    return filtered_rows

