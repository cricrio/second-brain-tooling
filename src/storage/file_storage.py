import urllib.parse
from pathlib import Path

from storage.abstract_storage import Storage, Template


class FileTemplate(Template):
    def __init__(self, path: Path):
        self.path = path
        self.name = path.name

    def read_template(self) -> list[str]:
        file = Path(self.path).open('r')
        lines = file.readlines()
        file.close()
        return lines


def list_markdown_files(path: Path) -> list[FileTemplate]:
    return list(map(FileTemplate, path.rglob("*.md")))


def get_filename(title: str):
    return urllib.parse.quote_plus('-'.join(title.casefold().split(' ')))


class FileStorage(Storage):
    doc_path: Path
    templates: list[FileTemplate]

    def __init__(self, doc_path: str):
        self.doc_path = Path(doc_path)
        self.templates = list_markdown_files(self.doc_path / "templates")

    def list_templates(self):
        return self.templates

    def create_note(self, content: list[str], title: str, folder: str = None):
        path = self.doc_path / Path(folder) if folder else self.doc_path
        path = path / f"{get_filename(title)}.md"
        file = path.open('w+')
        file.writelines(content)
        file.close()
