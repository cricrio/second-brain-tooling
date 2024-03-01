from templating import TemplateEngine
from templating import replace_variables, inject_metadata


def test_inject_template_variables():
    assert replace_variables({'title': 'Machu Pichu'})('# {title}') == '# Machu Pichu'


def test_replace_metadata():
    assert inject_metadata(
        [],
        {"date": 'today', 'author': 'me'}
    ) == ['---\n', '  - date: today\n', '  - author: me\n', '---\n']
    assert inject_metadata(
        ['', 'Barback'],
        {"date": 'today', 'author': 'me'}
    ) == ['---\n', '  - date: today\n', '  - author: me\n', '---\n', '', 'Barback']


def test_template_engine_format():
    template_engine = TemplateEngine()
    assert template_engine.format(
        ['', '{title}', 'Barback'],
        {'title': 'Machu Pichu'},
        {'date': 'now'}
    ) == ['---\n',
          '  - date: now\n',
          '---\n',
          '',
          'Machu Pichu',
          'Barback']
