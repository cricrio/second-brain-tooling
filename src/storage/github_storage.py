import os

import requests
from dotenv import load_dotenv

from storage.abstract_storage import Storage, Template

load_dotenv()

AUTH_TOKEN = os.getenv('GITHUB_AUTH_TOKEN')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')

headers = {'Authorization': f'bearer {AUTH_TOKEN}'}

queryReadRepository = """
{
  viewer {
    login
    repository(name: "second-brain-tooling-testing") {
      name
      object(expression: "HEAD:") {
        ... on Tree {
          entries {
            name
            type
            mode
            object {
              ... on Blob {
                byteSize
                text
                isBinary
              }
              ... on Tree {
                entries {
                  name
                  type
                  mode
                  object {
                    ... on Blob {
                      byteSize
                      text
                      isBinary
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
"""
queryReadTemplate = """"""


def github_request(query: str):
    content = requests.post('https://api.github.com/graphql', headers=headers, json={'query': query})
    json_data = content.json()
    return json_data.get('data').get('viewer')


# class Template:
#     name: str
#     content: list[str]
#
#     def __init__(self, data: dict):
#         self.name = data.get('name')
#         self.content = data.get('object').get('text').split('\n')
#
#     def __str__(self):
#         return f'name: {self.name}, content:{self.content}'


def get_template_list(data: dict) -> list[Template]:
    root = data.get('repository').get('object').get('entries')
    template_folder = list(filter(lambda node: node.get('name') == 'templates', root))[0]
    templates = template_folder.get('object').get('entries')
    return list(map(Template, templates))


class GithubStorage(Storage):
    templates: list[Template]

    def __init__(self):
        repo = github_request(queryReadRepository)
        self.templates = get_template_list(repo)
        print(f'{self.templates}')

    def list_templates(self):
        return self.templates

    def read_template(self, template: str):
        print(path)
        return path

    def create_note(self, content: list[str], title: str, folder: str = None):
        pass
