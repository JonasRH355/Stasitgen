from textnode import TextNode, TextType
from os import path, listdir, mkdir
from shutil import copy, rmtree 

def copy_files_recursive(dir_path_static, dir_path_public):
    if not path.exists(dir_path_public):
        mkdir(dir_path_public)
    
    for filename in listdir(dir_path_static):
        fr = path.join(dir_path_static,filename)
        dest = path.join(dir_path_public, filename)

        if path.isfile(fr):
            copy(fr,dest)
        else:
            copy_files_recursive(fr, dest)