import regex


def preprocess_json_multilines(file_str):
    pattern = regex.compile(': ?"([^"]*?\n)[^"]*?"')
    pos = 0
    while regex.search(pattern, file_str[pos:]) is not None:
        item = regex.search(pattern, file_str[pos:])
        span = item.span()
        pos_ = span[0] + len(file_str[pos + span[0]:pos + span[1]].replace("\n", "\\n"))
        file_str = file_str.replace(file_str[pos + span[0]:pos + span[1]],
                                    file_str[pos + span[0]:pos + span[1]].replace("\n", "\\n"))
        pos = pos_
    return file_str
