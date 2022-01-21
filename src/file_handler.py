from os import PathLike
from pathlib import Path
from pathlib import PurePath
import platform
from typing import Union

from .File import File


ENVIRONMENT = platform.system()
CURRENT_DIR = Path.cwd()
print(CURRENT_DIR)


def create_file(
    name: str,
    directory_path: Union[str, PathLike, PurePath, bytes],
    extension: str
) -> File:
    """ Creates a new File object

    Args:
        name (str): the file name
        directory_path (Union[str, PathLike, PurePath, bytes]): the directory
          where the file muts be created
        extension (str): the file extension

    Returns:
        File: a new File object containing the file information
    """
    return File(name, directory_path, extension)


def create(
        file_name: str = 'document',
        file_directory: str = CURRENT_DIR,
        file_extension: str = 'txt',
        file: File = None) -> bool:
    pass


def delete(self) -> bool:
    pass


def copy(
    self,
    to: Union[str, PathLike, PurePath, bytes]
) -> Union[str, PathLike, PurePath, bytes]:
    pass


def move(
    self,
    to: Union[str, PathLike, PurePath, bytes],
    overwrite_if_exists: bool = True
) -> Union[str, PathLike, PurePath, bytes]:
    pass


def rename(self, new_name: str, new_extension: str = None):
    pass


def get_content(self, all: bool) -> object:
    pass
