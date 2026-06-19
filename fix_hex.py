with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'r') as f:
    content = f.read()

content = content.replace('.why{background:var(--black);color:#F5ECD77DD', '.why{background:var(--bg2);color:#F5ECD7')
content = content.replace('footer{background:var(--black);color:#F5ECD77DD', 'footer{background:#1A1208;color:#9C8E7A')
content = content.replace('stroke="#F5ECD77DD"', 'stroke="#FF6B2B"')
content = content.replace('#F5ECD77DD', '#F5ECD7')

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'w') as f:
    f.write(content)
