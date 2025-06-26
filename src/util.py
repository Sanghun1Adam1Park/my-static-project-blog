import os
import shutil
from markdown_blocks import markdown_to_html_node

def cp(source: str, destination: str) -> None:
    if not os.path.exists(source) and not os.path.exists(destination):
        raise FileNotFoundError("Given file path does not eixst.")
    
    shutil.rmtree(destination, ignore_errors=True)
    os.mkdir(destination)

    files = os.listdir(source)
    for file in files:
        if os.path.isfile(os.path.join(source, file)):
            shutil.copy(os.path.join(source, file), destination)
        else:
            os.makedirs(os.path.join(destination, file), exist_ok=True)
            cp(os.path.join(source, file), os.path.join(destination, file))
    
def extract_title(markdown: str) -> str:
    if not markdown.startswith('#'):
        raise ValueError("Invlaid title, should start with '#'.")
    return markdown.lstrip('#').strip()

def generate_page(src: str, template_path: str, dest: str): 
    print(f"Generating page from {src} to {dest} using {template_path}.")
    with open(src, 'r') as f: md = f.read()
    with open(template_path, 'r') as f: template = f.read()
    html = markdown_to_html_node(md).to_html()
    title = extract_title(md.split("\n\n")[0])
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html) 
    dest_dir_path = os.path.dirname(dest)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest, "w")
    to_file.write(template)

def generate_page_recursively(src: str, template_path: str, dest: str):
    files = os.listdir(src)
    for f in files:
        src_path = os.path.join(src, f)
        dest_path = os.path.join(dest, f)
        print(f"Processing {src_path}")
        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_page_recursively(src_path, template_path, dest_path)
        elif src_path.endswith(".md"):
            generate_page(src_path, template_path, dest_path.replace(".md", ".html"))
        else: 
            shutil.copy(src_path, dest_path)
