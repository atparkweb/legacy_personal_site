import os, re

path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(path, "../public/index.html")
output_file = os.path.join(path, "../index.html")

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