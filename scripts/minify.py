import re

input_file = "../public/index.html"
output_file = "../index.html"

lines = []
with open(input_file, 'r', encoding='utf-8') as f:
  lines = f.readlines()
  f.close()

with open(output_file, 'w', encoding='utf-8') as f:
  for line in lines:
    line = re.sub(r'^\s*', "", line)
    line = re.sub(r'$\n+', "", line)
    f.write(line)
  f.close()