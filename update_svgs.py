import re
import os

# 1. Downscale the ASCII art
def downscale_ascii(input_file, target_width=35, target_height=25):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]
    
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
        
    orig_height = len(lines)
    if orig_height == 0:
        return [" " * target_width] * target_height
    orig_width = 50
    
    output = []
    for y in range(target_height):
        orig_y = int(y * orig_height / target_height)
        orig_line = lines[orig_y]
        new_line = ""
        for x in range(target_width):
            orig_x = int(x * orig_width / target_width)
            if orig_x < len(orig_line):
                new_line += orig_line[orig_x]
            else:
                new_line += " "
        output.append(new_line)
    return output

def format_ascii_svg(ascii_lines, text_color):
    tspan_template = '  <tspan x="15" y="{y}">{line}</tspan>'
    formatted_lines = []
    for i, line in enumerate(ascii_lines):
        line_escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        y_val = 30 + i * 20
        formatted_lines.append(tspan_template.format(y=y_val, line=line_escaped))
    
    block = f'<text x="15" y="30" fill="{text_color}" class="ascii">\n' + '\n'.join(formatted_lines) + '\n</text>'
    return block

# The contact section has perfectly aligned values starting at column 32
def get_right_side_block(fill_color):
    return f"""<text x="390" y="30" fill="{fill_color}">
<tspan x="390" y="30">akshat@negi</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Windows 11, Android 14, Linux</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots"> ...................... </tspan><tspan class="value" id="age_data">2 years, 5 months, 29 days</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">Student / Developer</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Pentester &amp; Security Researcher</tspan>
<tspan x="390" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">VS Code, Neovim</tspan>
<tspan x="390" y="150" class="cc">. </tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">JavaScript, Python, C, Java</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">HTML, CSS, SQL, JSON</tspan>
<tspan x="390" y="210" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">English, Hindi</tspan>
<tspan x="390" y="230" class="cc">. </tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">Cybersecurity, Web Dev</tspan>
<tspan x="390" y="270" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">PC Building, Gaming</tspan>
<tspan x="390" y="290">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="310" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">akshatnegi27@gmail.com</tspan>
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">me-akshat-negi</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">LeetCode</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">AkshatNegi27</tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">GFG</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">akshatnegi27</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">akshatnegi.vercel.app</tspan>
\n"""

def update_svg(filename, ascii_block, text_color):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ensure height is set to 510px
    content = content.replace('height="530px"', 'height="510px"')
    content = content.replace('height="530"', 'height="510"')
    
    # 2. Replace the ASCII block
    pattern_ascii = re.compile(r'<text\s+[^>]*class="ascii">.*?</text>', re.DOTALL)
    content = pattern_ascii.sub(ascii_block, content)
    
    # 3. Replace the right-side text block (up to GitHub Stats line)
    # The lookahead target matches the stats header line y="430"
    pattern_right = re.compile(r'<text\s+x="390"\s+y="30"\s+fill="[^"]+">.*?(?=<tspan\s+x="390"\s+y="430">- GitHub Stats</tspan>)', re.DOTALL)
    right_block = get_right_side_block(text_color)
    content = pattern_right.sub(right_block, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} successfully.")

def main():
    ascii_lines = downscale_ascii("ascii-art (2).txt", target_width=35)
    
    # Dark Mode SVG update
    dark_ascii_block = format_ascii_svg(ascii_lines, "#c9d1d9")
    update_svg("dark_mode.svg", dark_ascii_block, "#c9d1d9")
    
    # Light Mode SVG update
    light_ascii_block = format_ascii_svg(ascii_lines, "#24292f")
    update_svg("light_mode.svg", light_ascii_block, "#24292f")

if __name__ == '__main__':
    main()
