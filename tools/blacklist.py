import re


def check_string_structure(s):
    # 正则表达式：以普通文字开始，后面是被"[]"包裹的文字（包含引号）
    pattern = r'^.{1,10}"\[\w+\]"$'
    return bool(re.match(pattern, s))