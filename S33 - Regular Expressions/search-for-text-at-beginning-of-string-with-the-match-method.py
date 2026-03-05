import re

pattern = re.compile("flower")

match = pattern.match("a red flower in the field")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())