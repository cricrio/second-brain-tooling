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


def rename_key(key: str):
    """
    Replace the : in the key by _

    Ex: og:title -> og_title
    """
    return key.replace(':', '_')


def inject_metadata(template: Sequence[str], metadata: dict[str, date | str | float]) -> list[str]:
    data = ['---\n']
    for k, v in metadata.items():
        data.append(f'  - {rename_key(k)}: {v}\n')
    data.append('---\n')
    data.extend(template)
    return data


def inject_variables(template: Sequence[str], variables: dict[str, date | str | float]):
    return list(map(replace_variables(variables), template))


class TemplateEngine:
    @staticmethod
    def format(
            template: list[str],
            variables: dict[str, date | str | float] = None,
            metadata: dict[str, date | str | float] = None
    ):
        """
        Inject the metadata with the yaml format then inject the variables in the template
        """
        temp = inject_metadata(template, metadata) if metadata else template
        return inject_variables(temp, variables) if variables else temp
