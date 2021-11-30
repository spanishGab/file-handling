from abc import ABC, abstractmethod

from .interfaces.File import File


class BaseFileHandler(ABC):

    @staticmethod
    def create_file(
        name: str,
        directory_path: Union[str, PathLike, PurePath, bytes],
        extension: str
    ) -> File:
        return File(name, directory_path, extension)

