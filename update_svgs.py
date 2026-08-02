import re
import os

# The contact/details section aligned perfectly to the right side (60-character total line length)
def get_right_side_block(fill_color):
    return f"""<text x="390" y="30" fill="{fill_color}">
<tspan x="390" y="30">akshat@negi</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">Windows 11, Android 14, Linux</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots"> ....................... </tspan><tspan class="value" id="age_data">2 years, 5 months, 29 days</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ................................. </tspan><tspan class="value">Student / Developer</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">Pentester &amp; Security Researcher</tspan>
<tspan x="390" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ...................................... </tspan><tspan class="value">VS Code, Neovim</tspan>
<tspan x="390" y="150" class="cc">. </tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">JavaScript, Python, C, Java</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">HTML, CSS, SQL, JSON</tspan>
<tspan x="390" y="210" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">English, Hindi</tspan>
<tspan x="390" y="230" class="cc">. </tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">Cybersecurity, Web Dev</tspan>
<tspan x="390" y="270" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">PC Building, Gaming</tspan>
<tspan x="390" y="310">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">akshatnegi27@gmail.com</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................................. </tspan><tspan class="value">me-akshat-negi</tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">LeetCode</tspan>:<tspan class="cc"> .................................... </tspan><tspan class="value">AkshatNegi27</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">GFG</tspan>:<tspan class="cc"> ......................................... </tspan><tspan class="value">akshatnegi27</tspan>
<tspan x="390" y="410" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">akshatnegi.vercel.app</tspan>
"""

def update_svg(filename, text_color, ascii_block):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add xlink namespace to root svg element if not present (optional for text-only, but good practice)
    if 'xmlns:xlink' not in content:
        content = content.replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"')
        
    # Revert height back to 530px (matching dark.svg / ascii-art.svg)
    content = content.replace('height="510px"', 'height="530px"')
    content = content.replace('height="510"', 'height="530"')
    content = content.replace('height="1180px"', 'height="530px"')
    content = content.replace('height="1180"', 'height="530px"')
    content = re.sub(r'height="\d+px"', 'height="530px"', content)
    content = re.sub(r'height="\d+"', 'height="530"', content)
    
    # Update style block to include .ascii font size
    if '.ascii {' not in content:
        content = content.replace('text, tspan {white-space: pre;}', '.ascii {font-size: 7px;}\ntext, tspan {white-space: pre;}')
    else:
        # If it exists but might have wrong font-size, replace it
        content = re.sub(r'\.ascii\s*\{[^}]*\}', '.ascii {font-size: 7px;}', content)
        
    # Make sure background rect is also 530px height
    content = re.sub(r'<rect width="985px" height="\d+px"', '<rect width="985px" height="530px"', content)
    content = re.sub(r'<rect width="985px" height="\d+"', '<rect width="985px" height="530"', content)
    
    # 2. Replace the ASCII block or image block with the new ASCII block
    # Modify fill attribute in the ascii block
    colored_ascii_block = re.sub(r'fill="[^"]+"', f'fill="{text_color}"', ascii_block)
    
    pattern_left = re.compile(r'(<text\s+[^>]*class="ascii">.*?</text>|<image\s+[^>]*/>)', re.DOTALL)
    content = pattern_left.sub(colored_ascii_block, content)
    
    # 3. Replace the right-side text block (up to GitHub Stats line)
    pattern_right = re.compile(r'<text\s+x="390"\s+y="30"\s+fill="[^"]+">.*?(?=<tspan\s+x="390"\s+y="450">- GitHub Stats</tspan>)', re.DOTALL)
    right_block = get_right_side_block(text_color)
    content = pattern_right.sub(right_block, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} successfully.")

def main():
    # Read the new ASCII art block from ascii-art.svg
    with open("ascii-art.svg", "r", encoding="utf-8") as f:
        ascii_svg_content = f.read()
        
    ascii_block_match = re.search(r'<text\s+[^>]*class="ascii">.*?</text>', ascii_svg_content, re.DOTALL)
    if not ascii_block_match:
        print("Error: Could not find ASCII block in ascii-art.svg")
        return
        
    ascii_block = ascii_block_match.group(0)
        
    # Dark Mode SVG update
    update_svg("dark_mode.svg", "#c9d1d9", ascii_block)
    
    # Light Mode SVG update
    update_svg("light_mode.svg", "#24292f", ascii_block)

if __name__ == '__main__':
    main()
