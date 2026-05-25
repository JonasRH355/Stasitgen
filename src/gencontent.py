import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def generate_page(frm,template, dest, basepath):
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
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest, "w")
    to_file.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(
                from_path, 
                template_path, 
                dest_path, 
                basepath)
        else:
            generate_pages_recursive(
                from_path, 
                template_path, 
                dest_path, 
                basepath)
       

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        raise Exception("Not found title")