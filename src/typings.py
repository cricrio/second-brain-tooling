from dataclasses import dataclass
from pathlib import Path


@dataclass
class File:
    name: str
    path: str


@dataclass
class NoteCreation:
    template: Path
    name: str


@dataclass
class TemplateVariables:
    title: str
