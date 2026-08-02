import re
import os

# The contact/details/stats section aligned perfectly to the right side (61-character total line length)
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
<tspan x="390" y="430" class="cc">. </tspan>
<tspan x="390" y="450">- GitHub Stats</tspan> -—————————————————————————————————————————-—-
<tspan x="390" y="470" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .................... </tspan><tspan class="value" id="repo_data">462</tspan> | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">3800</tspan>
<tspan x="390" y="490" class="cc">. </tspan><tspan class="key">Following</tspan>:<tspan class="cc" id="following_data_dots"> ................ </tspan><tspan class="value" id="following_data">134</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan><tspan class="value" id="follower_data">1137</tspan>
<tspan x="390" y="510" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> ............... </tspan><tspan class="value" id="commit_data">23,100</tspan> | <tspan class="key">Forks</tspan>:<tspan class="cc" id="fork_data_dots"> ............. </tspan><tspan class="value" id="fork_data">694</tspan>
<tspan x="390" y="530" class="cc">. </tspan><tspan class="key">Issues</tspan>:<tspan class="cc" id="issue_data_dots"> .................... </tspan><tspan class="value" id="issue_data">89</tspan> | <tspan class="key">Pull Requests</tspan>:<tspan class="cc" id="pr_data_dots"> ..... </tspan><tspan class="value" id="pr_data">811</tspan>
<tspan x="390" y="550" class="cc">. </tspan><tspan class="key">Lines of Code</tspan>:<tspan class="cc" id="loc_data_dots"> ...... </tspan><tspan class="value" id="loc_data">1,304,000</tspan> ( <tspan class="addColor" id="loc_add">1,564,800</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">260,800</tspan><tspan class="delColor">--</tspan> )
</text>"""

def update_svg(filename, text_color, ascii_block):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add xlink namespace to root svg element if not present
    if 'xmlns:xlink' not in content:
        content = content.replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"')
        
    # Scale height to 570px to provide bottom padding and prevent baseline text clipping
    content = content.replace('height="510px"', 'height="570px"')
    content = content.replace('height="510"', 'height="570"')
    content = content.replace('height="530px"', 'height="570px"')
    content = content.replace('height="530"', 'height="570"')
    content = content.replace('height="1180px"', 'height="570px"')
    content = content.replace('height="1180"', 'height="570"')
    content = re.sub(r'height="\d+px"', 'height="570px"', content)
    content = re.sub(r'height="\d+"', 'height="570"', content)
    
    # Update style block to include .ascii font size
    if '.ascii {' not in content:
        content = content.replace('text, tspan {white-space: pre;}', '.ascii {font-size: 7px;}\ntext, tspan {white-space: pre;}')
    else:
        content = re.sub(r'\.ascii\s*\{[^}]*\}', '.ascii {font-size: 7px;}', content)
        
    # Make sure background rect is also 570px height
    content = re.sub(r'<rect width="985px" height="\d+px"', '<rect width="985px" height="570px"', content)
    content = re.sub(r'<rect width="985px" height="\d+"', '<rect width="985px" height="570"', content)
    
    # Replace the ASCII block or image block with the new ASCII block from ascii-art.svg
    colored_ascii_block = re.sub(r'fill="[^"]+"', f'fill="{text_color}"', ascii_block)
    
    pattern_left = re.compile(r'(<text\s+[^>]*class="ascii">.*?</text>|<image\s+[^>]*/>)', re.DOTALL)
    content = pattern_left.sub(colored_ascii_block, content)
    
    # Replace the right-side text block (up to the end of the text element)
    pattern_right = re.compile(r'<text\s+x="390"\s+y="30"\s+fill="[^"]+">.*?</text>', re.DOTALL)
        
    right_block = get_right_side_block(text_color)
    content = pattern_right.sub(right_block, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} successfully.")

def main():
    # Read the ASCII art block from ascii-art.svg (no inlining in python)
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
