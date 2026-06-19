import re

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'r') as f:
    content = f.read()

# CSS Variables
vars_replacements = {
    "--bg:#0D0905": "--bg:#131A5C",
    "--bg2:#1A1208": "--bg2:#131A5C",
    "--bg3:#1A1208": "--bg3:#131A5C",
    "--surface:#2A1D0E": "--surface:#131A5C",
    "--surface2:#2A1D0E": "--surface2:#131A5C",
    "--accent:#FF6B2B": "--accent:#3A4AC4",
    "--accent2:#FF9A5C": "--accent2:#7B8AE0",
    "--accent3:#FF9A5C": "--accent3:#7B8AE0",
    "--teal:#FF6B2B": "--teal:#3A4AC4",
    "--teal2:#FF9A5C": "--teal2:#7B8AE0",
    "--teal-glow:rgba(255,107,43,.15)": "--teal-glow:rgba(58,74,196,.15)",
    "--coral:#FF6B2B": "--coral:#3A4AC4",
    "--coral2:#FF9A5C": "--coral2:#7B8AE0",
    "--black:#F5ECD7": "--black:#F0F2FF",
    "--white:#0D0905": "--white:#F0F2FF",
    "--offwhite:#9C8E7A": "--offwhite:#C2C9F5",
    "--muted:#9C8E7A": "--muted:#C2C9F5",
    "--muted2:#9C8E7A": "--muted2:#C2C9F5",
    "--mint:#FF6B2B": "--mint:#3A4AC4",
}
for k, v in vars_replacements.items():
    content = content.replace(k, v)

# Update RGBAs
rgba_replacements = {
    "rgba(255,107,43": "rgba(58,74,196", # Fire Orange -> Primary Blue
    "rgba(255, 107, 43": "rgba(58, 74, 196", # Fire Orange with spaces -> Primary Blue
    "rgba(255,154,92": "rgba(123,138,224", # Amber Glow -> Medium Blue
    "rgba(13,9,5": "rgba(19,26,92", # Charred Black -> Darkest Blue
    "rgba(245,236,215": "rgba(240,242,255" # Warm White -> Lightest Blue
}
for k, v in rgba_replacements.items():
    content = content.replace(k, v)

# Hardcoded hex replacements
# Backgrounds
content = content.replace('#1A1208', '#131A5C')
content = content.replace('#2A1D0E', '#131A5C')
content = content.replace('#0D0905', '#F0F2FF') # For text elements like buttons that were black, now they need to be white for contrast against blue
# But wait, earlier I replaced #fff with #0D0905 for button text. Let's make it #F0F2FF so it's readable.

# Primary Accents
content = content.replace('#FF6B2B', '#3A4AC4')

# Text
content = content.replace('#F5ECD7', '#F0F2FF')
content = content.replace('#9C8E7A', '#C2C9F5')

# Ensure button text is bright
content = content.replace('.btn-s{background:var(--accent);color:#F0F2FF', '.btn-s{background:var(--accent);color:#F0F2FF')

with open('/Users/sohammaggo/.gemini/antigravity/scratch/vizley-studio/index.html', 'w') as f:
    f.write(content)
    
with open('/Users/sohammaggo/.gemini/antigravity/html_artifacts/index.html', 'w') as f:
    f.write(content)

print("Done")
