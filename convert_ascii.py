import html

def main():
    input_file = "ascii-art (2).txt"
    output_file = "ascii_art_tspan.txt"
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    tspan_lines = []
    y_start = 35
    line_height = 8
    
    for i, line in enumerate(lines):
        content = line.rstrip('\r\n')
        escaped_content = html.escape(content)
        y_val = y_start + i * line_height
        tspan_lines.append(f'<tspan x="15" y="{y_val}">{escaped_content}</tspan>')
        
    svg_block = '<text x="15" y="35" fill="#c9d1d9" class="ascii">\n' + '\n'.join(tspan_lines) + '\n</text>'
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg_block)
        
    print(f"Successfully generated {output_file} with {len(lines)} lines.")

if __name__ == '__main__':
    main()
