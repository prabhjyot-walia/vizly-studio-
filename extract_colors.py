import re

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'r') as f:
    content = f.read()

colors = re.findall(r'#[0-9a-fA-F]{3,6}|rgba?\([^)]+\)', content)
colors = sorted(list(set(colors)))
print('\n'.join(colors))
