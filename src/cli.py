from urllib.parse import urlparse

import inquirer

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

    storage.create_note(note_content, note_name)


def is_valid_url(url: str):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc


def bookmark_prompt():
    return inquirer.text('url', message='Enter the url', validate=is_valid_url)


def cli(storage: Storage):
    feature = inquirer.list_input('Select the feature you want to use', choices=['note', 'bookmark'])
    if feature == 'note':
        return note_creation_prompt(storage)
    else:
        return bookmark_prompt()
