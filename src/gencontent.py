import os
from block_markdown import markdown_to_html_node

def generate_page(frm,template, dest):
    print(f"Generating page from {frm} to {dest} using {template}")
    from_file = open(frm, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template, "r")
    template_content = template_file.read()
    template_file.close()
    

    html_string = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    
    template_content = template_content.replace("{{ Title }}", title )
    template_content = template_content.replace("{{ Content }}", html_string)
    print(template_content)
    dest_dir_path = os.path.dirname(dest)
    
    ##if dest_dir_path != "":
    ##    os.makedirs(dest_dir_path)
    to_file = open(dest, "w")
    to_file.write(template_content)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        raise Exception("Not found title")