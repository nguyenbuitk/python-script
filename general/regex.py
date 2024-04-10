import re

pattern = re.compile("of")
book = "Every man takes the limits of his own field of vision for the limits of the world."
findings = re.findall(pattern, book)
print(findings)