from src.note.templating import replace_variables, replace_metadata


def test_inject_template_variables():
    assert replace_variables(
        '# {title}',
        {'title': 'Machu Pichu'}
    ) == '# Machu Pichu'


def test_replace_metadata():
    assert replace_metadata(['{metadata}']) == []
    assert replace_metadata(['{metadata}'], {"date": 'today', 'author': 'me'}) == ['---', '   - date: today',
                                                                                   '   - author: me']
