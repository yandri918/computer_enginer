import re

# Read the file
with open('pages/7_🔢_MA102_Linear_Algebra.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all <div class="theory-box">, <div class="theorem-box">, etc. and their closing </div>
content = re.sub(r'<div class="[^"]*">\s*', '', content)
content = re.sub(r'\s*</div>', '', content)

# Replace <strong>...</strong> with **...**
content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)

# Replace <br> and <br> with newlines
content = re.sub(r'<br><br>', r'\n\n', content)
content = re.sub(r'<br>', r'  \n', content)

# Remove unsafe_allow_html=True since we're not using HTML anymore
content = content.replace(', unsafe_allow_html=True', '')

# Write back
with open('pages/7_🔢_MA102_Linear_Algebra.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Converted all HTML to Markdown!")
