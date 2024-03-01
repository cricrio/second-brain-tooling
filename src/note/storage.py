import urllib.parse
from pathlib import Path


def list_markdown_files(path: Path) -> list[Path]:
    return list(path.rglob("*.md"))


def get_filename(title: str):
    return urllib.parse.quote_plus('-'.join(title.casefold().split(' ')))


class Storage:
    doc_path: Path
    templates: list[Path]

    def __init__(self, doc_path: Path):
        self.doc_path = doc_path
        self.templates = list_markdown_files(doc_path / "templates")

    def list_templates(self):
        return self.templates

    @staticmethod
    def read_template(path: Path):
        file = path.open('r')
        lines = file.readlines()
        file.close()
        return lines

    def create_note(self, content: list[str], title: str, folder: Path = None):
        path = self.doc_path / folder if folder else self.doc_path
        path = path / f"{get_filename(title)}.md"
        file = path.open('w+')
        file.writelines(content)
        file.close()
