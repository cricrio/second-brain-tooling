from pathlib import Path
from urllib.parse import urlparse

import inquirer

from bookmark.parsers.common import fetch_metadata
from note.storage import Storage
from note.templating import TemplateEngine


def note_creation_prompt(storage: Storage, template_engine: TemplateEngine):
    paths = storage.list_templates()

    questions = [
        inquirer.List(
            'template',
            message="Choose a template",
            choices=list(map(lambda f: f.name, paths))
        ),
        inquirer.Text('name', message='Enter the title')
    ]

    answers = inquirer.prompt(questions)
    template_path = list(filter(lambda x: x.name == answers.get('template'), paths))[0]
    template = storage.read_template(template_path)
    note_name = answers.get('name')
    note_content = template_engine.format(template, {'title': note_name})

    storage.create_note(note_content, note_name, folder=Path('notes'))


def is_valid_url(_, url: str):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc


def bookmark_prompt(storage: Storage, template_engine: TemplateEngine):
    url = inquirer.text('Enter the url', validate=is_valid_url)
    metadata = fetch_metadata(url)
    note = template_engine.format([], metadata=metadata)
    storage.create_note(note, url, folder=Path('bookmarks'))


def cli(storage: Storage, template_engine: TemplateEngine):
    feature = inquirer.list_input('Select the feature you want to use', choices=['note', 'bookmark'])
    if feature == 'note':
        return note_creation_prompt(storage, template_engine)
    else:
        return bookmark_prompt(storage, template_engine)
