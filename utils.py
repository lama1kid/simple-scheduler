import pprint
from marko import Markdown
from marko.ast_renderer import ASTRenderer

default_md_path = "tests/task pool.md"

def print_element_tree_ast(md_path=default_md_path):
    md = Markdown(renderer=ASTRenderer)
    with open(md_path, mode="r", encoding="utf-8") as f:
        md_text = f.read()
        doc = md.parse(md_text)
        ast_out = md.render(doc)
        pprint.pprint(ast_out)

def print_element_tree(md_path=default_md_path):
    md = Markdown(renderer=ASTRenderer)
    with open(md_path, mode="r", encoding="utf-8") as f:
        md_text = f.read()
        doc = md.parse(md_text)
        pprint.pprint(doc)

