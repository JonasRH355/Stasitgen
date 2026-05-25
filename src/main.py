from textnode import TextNode, TextType
from os import path, listdir, mkdir
from shutil import copy, rmtree 

from copystatic import *
from gencontent import *

dir_static = "./static"
dir_public = "./public"
dir_content = "./content"
template_path = "./template.html"

def main():
    if path.exists(dir_public):
        rmtree("./public")
    copy_files_recursive(dir_static, dir_public)

    generate_page(
        path.join(dir_content, "index.md"),
        template_path,
        path.join(dir_public, "index.html")
    )


main()