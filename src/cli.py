from urllib.parse import urlparse

import inquirer

from bookmark.parsers.common import fetch_metadata
from note.templating import TemplateEngine
from storage.abstract_storage import Storage, Template


def get_template_by_name(templates: list[Template], template_name: str) -> Template:
    for t in templates:
        if t.name == template_name:
            return t
    raise Exception('template not found')


def note_creation_prompt(storage: Storage, template_engine: TemplateEngine):
    templates = storage.list_templates()

    questions = [
        inquirer.List(
            'template',
            message="Choose a template",
            choices=list(map(lambda f: f.name, templates))
        ),
        inquirer.Text('name', message='Enter the title')
    ]

    answers = inquirer.prompt(questions)
    template = get_template_by_name(templates, answers.get('template'))
    print(dir(template), type(template))
    template_content = template.read_template()
    note_name = answers.get('name')
    note_content = template_engine.format(template_content, {'title': note_name})

    storage.create_note(note_content, note_name, folder='notes')


def is_valid_url(_, url: str):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc


def bookmark_prompt(storage: Storage, template_engine: TemplateEngine):
    url = inquirer.text('Enter the url', validate=is_valid_url)
    metadata = fetch_metadata(url)
    note = template_engine.format([], metadata=metadata)
    storage.create_note(note, url, folder='bookmarks')


def cli(storage: Storage, template_engine: TemplateEngine):
    feature = inquirer.list_input('Select the feature you want to use', choices=['note', 'bookmark'])
    if feature == 'note':
        return note_creation_prompt(storage, template_engine)
    else:
        return bookmark_prompt(storage, template_engine)
