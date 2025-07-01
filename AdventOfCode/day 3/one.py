import re


result = 0
with open("day 3/corrupted.txt", "r") as f:
    text = f.read()
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, text)

for match in matches:
    to_mult = re.findall(r"\d{1,3}", match)
    result += int(to_mult[0]) * int(to_mult[1])
print(result)
