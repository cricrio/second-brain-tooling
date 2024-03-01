import abc


class Template(metaclass=abc.ABCMeta):
    name: str
    content: list[str] = None

    @abc.abstractmethod
    def read_template(self) -> list[str]:
        pass


class Storage(metaclass=abc.ABCMeta):
    _instance: 'Storage' = None

    def __new__(cls, *kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @abc.abstractmethod
    def list_templates(self) -> list[Template]:
        pass

    @abc.abstractmethod
    def create_note(self, content: list[str], title: str, folder: str = None):
        pass
