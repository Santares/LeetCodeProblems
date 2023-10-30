import re


def parse_json(json_string):
    json_dict = {}

    string = json_string[1:-1] + ','
    pattern = r'"[a-zA-Z0-9\]+"\s*:[^,]+?,'
    pairs = re.findall(pattern, string)
    for pair in pairs:
        pair = pair.split(':')
        key = pair[0].strip().strip('"')
        value = pair[1].strip().strip(',')

        if value[0] == '"':
            json_dict[key] = value.strip('"')
        else:
            json_dict[key] = True if value == 'true' else False

    return json_dict


if __name__ == '__main__':
    test1 = '{   "he\"llo"  :   true, "foo": "false"}'
    test2 = '{"foo": "false"}'
    print(parse_json(test1))
