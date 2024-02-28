from datetime import date
from typing import Iterable, Sequence

common_variables = ('title',)
common_variable_placeholders = tuple[str]


def format_variable(variable: str) -> str:
    return '{' + variable + '}'


def templating(variables: Iterable[str]) -> list[str]:
    return list(map(format, variables))


def replace_variables(variables: dict[str, date | str | float]):
    def replacer(content: str):
        res = content
        for k, v in variables.items():
            if k in common_variables:
                res = res.replace(format_variable(k), v)
            else:
                print(f"unknown variable: {k}")
        return res

    return replacer


def replace_metadata(template: Sequence[str], metadata: dict[str, date | str | float] = None) -> list[str]:
    head, *tail = template
    if '{metadata}' in head:
        if metadata:
            data = ['---']
            for k, v in metadata.items():
                data.append(f'  - {k}: {v}')
            data.append('---')
            return [data, tail]
    return tail


class TemplateEngine:
    @staticmethod
    def format(template: list[str], variables: dict[str, date | str | float], metadata: dict[str, date | str | float]):
        return list(map(replace_variables(variables), template))
