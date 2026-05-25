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

    generate_pages_recursive(
        dir_content,
        template_path,
        dir_public
    )


main()