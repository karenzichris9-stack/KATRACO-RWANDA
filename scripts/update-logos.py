import os
import re

# The new logo URL
new_logo_url = "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/204C03A2-6C9F-460C-8EE4-55C05559832C.PNG-4MCtBhXB9bL3SoX1Zx2pnWqAsj4OPf.png"

# Files to update
files = [
    '/vercel/share/v0-project/KATRACO-RWANDA.html',
    '/vercel/share/v0-project/index.html'
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace base64 image src with new logo URL
        # Use a pattern that finds src="data:image/jpeg;base64,/9j... and replaces with new URL
        pattern = r'src="data:image/jpeg;base64,/9j[^"]*"'
        new_src = f'src="{new_logo_url}"'
        
        updated_content = re.sub(pattern, new_src, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated {filepath}")
    else:
        print(f"File not found: {filepath}")

print("Logo update complete!")
