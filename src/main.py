from cli import cli
from note.templating import TemplateEngine
from storage.github_storage import GithubStorage

storage = GithubStorage()
template_engine = TemplateEngine()

cli(storage, template_engine)
