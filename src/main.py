from pathlib import Path

from cli import cli
from note.storage import Storage
from note.templating import TemplateEngine

storage = Storage(Path('../docs'))
template_engine = TemplateEngine()

cli(storage, template_engine)
