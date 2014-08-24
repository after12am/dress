import re

def strip_extra_singlequote(value):
    if type(value) == unicode:
        m = re.match(r"'(.*)'", value)
        if m:
            return m.group(1)
    return value