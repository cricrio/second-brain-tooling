from pathlib import Path

from cli import cli
from note.storage import Storage

storage = Storage(Path('../docs'))
cli(storage)
