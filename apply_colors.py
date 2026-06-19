import re

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'r') as f:
    content = f.read()

vars_replacements = {
    "--bg:#FFF7DD": "--bg:#0D0905",
    "--bg2:#FBF2D0": "--bg2:#1A1208",
    "--bg3:#F5ECC5": "--bg3:#1A1208",
    "--surface:#F0E7BE": "--surface:#2A1D0E",
    "--surface2:#EBE2B7": "--surface2:#2A1D0E",
    "--accent:#80A1BA": "--accent:#FF6B2B",
    "--accent2:#6B8FA8": "--accent2:#FF9A5C",
    "--accent3:#5A7E97": "--accent3:#FF9A5C",
    "--teal:#91C4C3": "--teal:#FF6B2B",
    "--teal2:#B4DEBD": "--teal2:#FF9A5C",
    "--teal-glow:rgba(145,196,195,.15)": "--teal-glow:rgba(255,107,43,.15)",
    "--coral:#C67A7A": "--coral:#FF6B2B",
    "--coral2:#B06A6A": "--coral2:#FF9A5C",
    "--black:#2A3A4A": "--black:#F5ECD7",
    "--white:#2A3A4A": "--white:#0D0905",
    "--offwhite:#3D4F5F": "--offwhite:#9C8E7A",
    "--muted:#7A8E9E": "--muted:#9C8E7A",
    "--muted2:#9AABB8": "--muted2:#9C8E7A",
    "--mint:#B4DEBD": "--mint:#FF6B2B",
}

for k, v in vars_replacements.items():
    content = content.replace(k, v)

# Update RGBAs
rgba_replacements = {
    "rgba(128,161,186": "rgba(255,107,43",
    "rgba(145,196,195": "rgba(255,107,43",
    "rgba(180,222,189": "rgba(255,154,92",
    "rgba(42,58,74": "rgba(13,9,5",
    "rgba(255,247,221": "rgba(13,9,5",
    "rgba(255,255,255": "rgba(245,236,215"
}
for k, v in rgba_replacements.items():
    content = content.replace(k, v)

# Update #fff
content = re.sub(r'(?i)#ffffff', '#F5ECD7', content)
content = content.replace('.btn-s{background:var(--accent);color:#fff', '.btn-s{background:var(--accent);color:#0D0905')
content = content.replace('.mk-t2{position:absolute;bottom:32px;right:-20px;background:var(--accent);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);color:#fff', '.mk-t2{position:absolute;bottom:32px;right:-20px;background:var(--accent);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);color:#0D0905')
content = content.replace('.sc-tag{position:absolute;top:18px;right:18px;background:rgba(245,236,215,.18);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(245,236,215,.22);color:#fff', '.sc-tag{position:absolute;top:18px;right:18px;background:rgba(245,236,215,.18);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(245,236,215,.22);color:#F5ECD7')
content = content.replace('.ba-lbl-a{right:22px;background:var(--accent);color:#fff', '.ba-lbl-a{right:22px;background:var(--accent);color:#0D0905')
content = content.replace('.form-submit{width:100%;background:var(--accent);color:#fff', '.form-submit{width:100%;background:var(--accent);color:#0D0905')
content = content.replace('.btt{position:fixed;bottom:40px;right:40px;width:44px;height:44px;background:rgba(255,107,43,.90);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);color:#fff', '.btt{position:fixed;bottom:40px;right:40px;width:44px;height:44px;background:rgba(255,107,43,.90);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);color:#0D0905')
content = content.replace('.testi-avatar{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--teal));display:flex;align-items:center;justify-content:center;font-family:var(--fd);font-weight:700;font-size:16px;color:#fff', '.testi-avatar{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--teal));display:flex;align-items:center;justify-content:center;font-family:var(--fd);font-weight:700;font-size:16px;color:#0D0905')
content = content.replace('stroke="#fff"', 'stroke="#0D0905"')
content = content.replace('#fff', '#F5ECD7')
content = content.replace('#FFF', '#F5ECD7')

# Update hex values
content = content.replace('#2A3A4A', '#FF6B2B') # Wait, I need text to be F5ECD7, icons to be FF6B2B
# Let's revert that logic. Text:
# Original root black was: --black:#2A3A4A
# I already replaced --black:#2A3A4A with --black:#F5ECD7
# Any other #2A3A4A is in the SVGs: stroke="#2A3A4A" -> stroke="#FF6B2B"
content = content.replace('stroke="#2A3A4A"', 'stroke="#FF6B2B"')

# Fix shadows
content = content.replace('box-shadow:0 16px 48px rgba(255,107,43,.30)', 'box-shadow:0 0 20px rgba(255, 107, 43, 0.4)')
content = content.replace('box-shadow:0 12px 36px rgba(255,107,43,.25)', 'box-shadow:0 0 20px rgba(255, 107, 43, 0.4)')
content = content.replace('box-shadow:0 12px 36px rgba(255,107,43,.12)', 'box-shadow:0 0 20px rgba(255, 107, 43, 0.4)')
content = content.replace('box-shadow:0 12px 40px rgba(255,107,43,.10)', 'box-shadow:0 0 24px rgba(255, 107, 43, 0.15)')

# Specific sections that used to be dark need adjustment
# .why section
content = content.replace('.why{background:var(--black);color:#FFF7DD', '.why{background:var(--bg2);color:var(--black)')
# .offer section
content = content.replace('.offer{padding:220px 96px;background:var(--black)', '.offer{padding:220px 96px;background:var(--bg2)')
# footer
content = content.replace('footer{background:var(--black);color:#FFF7DD', 'footer{background:#1A1208;color:#9C8E7A')
# color #FFF7DD -> var(--black) (which is now #F5ECD7)
content = content.replace('color:#FFF7DD', 'color:var(--black)')

# Specific texts
content = content.replace('color:rgba(13,9,5,.25)', 'color:#9C8E7A')
content = content.replace('color:rgba(13,9,5,.30)', 'color:#F5ECD7')
content = content.replace('color:rgba(13,9,5,.15)', 'color:#9C8E7A')
content = content.replace('color:rgba(13,9,5,.38)', 'color:#9C8E7A')
content = content.replace('color:rgba(13,9,5,.22)', 'color:#9C8E7A')
content = content.replace('color:rgba(13,9,5,.32)', 'color:#9C8E7A')
content = content.replace('color:rgba(13,9,5,.35)', 'color:#9C8E7A')

# Form input borders
content = content.replace('border-bottom:1px solid rgba(255,107,43,.14)', 'border-bottom:1px solid #2A1D0E')
content = content.replace('.form-group input:focus,.form-group textarea:focus{border-color:var(--accent)}', '.form-group input:focus,.form-group textarea:focus{border-color:#FF6B2B}')
# Form group input colors
content = content.replace('background:transparent;font-family:var(--fb);font-size:14px;border-radius:0;outline:none;transition:border-color .35s;color:var(--black)', 'background:#1A1208;font-family:var(--fb);font-size:14px;border-radius:0;outline:none;transition:border-color .35s;color:#F5ECD7')

# Card hover state: Card backgrounds -> #2A1D0E
content = content.replace('.testi-card{width:420px;flex-shrink:0;background:rgba(245,236,215,.50)', '.testi-card{width:420px;flex-shrink:0;background:#2A1D0E')
content = content.replace('.testi-card:hover{border-color:rgba(255,107,43,.22);background:rgba(245,236,215,.70)', '.testi-card:hover{border-color:rgba(255,107,43,.22);background:#1A1208')
content = content.replace('.mk-t1{position:absolute;top:-18px;left:-22px;background:rgba(13,9,5,.96)', '.mk-t1{position:absolute;top:-18px;left:-22px;background:#2A1D0E')

# Modal Background
content = content.replace('.modal{background:var(--bg)', '.modal{background:#1A1208')

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'w') as f:
    f.write(content)

print("Done")
