import re


def preprocess_json(file_str):
    pattern = re.compile(': ?"([^"]*?\n)[^"]*?"')
    pos = 0
    while re.search(pattern, file_str[pos:]) is not None:
        span = re.search(pattern, file_str[pos:]).span()
        file_str = file_str.replace(file_str[pos + span[0]:pos + span[1]],
                                    file_str[pos + span[0]:pos + span[1]].replace("\t", "\\t"))

        span = re.search(pattern, file_str[pos:]).span()
        pos_ = span[0] + len(file_str[pos + span[0]:pos + span[1]].replace("\n", "\\n"))
        file_str = file_str.replace(file_str[pos + span[0]:pos + span[1]],
                                    file_str[pos + span[0]:pos + span[1]].replace("\n", "\\n"))
        pos = pos_
    return file_str
