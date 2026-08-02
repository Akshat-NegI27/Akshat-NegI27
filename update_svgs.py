import re
import os

# The contact section matches dark.svg's y-coordinates exactly
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
<tspan x="390" y="310">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">akshatnegi27@gmail.com</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">me-akshat-negi</tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">LeetCode</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">AkshatNegi27</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">GFG</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">akshatnegi27</tspan>
<tspan x="390" y="410" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">akshatnegi.vercel.app</tspan>
\n"""

def update_svg(filename, text_color):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Revert height back to 530px (matching dark.svg)
    content = content.replace('height="510px"', 'height="530px"')
    content = content.replace('height="510"', 'height="530"')
    
    # 2. Replace the ASCII block or old image block with the new PNG image element
    # Dimensions 350x450 scaled to fit 360px width beautifully on the left
    image_block = '<image x="20" y="40" width="350" height="450" href="https://raw.githubusercontent.com/Akshat-NegI27/Akshat-NegI27/main/art.png"/>'
    pattern_left = re.compile(r'(<text\s+[^>]*class="ascii">.*?</text>|<image\s+[^>]*/>)', re.DOTALL)
    content = pattern_left.sub(image_block, content)
    
    # 3. Replace the right-side text block (up to GitHub Stats line)
    pattern_right = re.compile(r'<text\s+x="390"\s+y="30"\s+fill="[^"]+">.*?(?=<tspan\s+x="390"\s+y="450">- GitHub Stats</tspan>)', re.DOTALL)
    right_block = get_right_side_block(text_color)
    content = pattern_right.sub(right_block, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} successfully.")

def main():
    # Dark Mode SVG update
    update_svg("dark_mode.svg", "#c9d1d9")
    
    # Light Mode SVG update
    update_svg("light_mode.svg", "#24292f")

if __name__ == '__main__':
    main()
