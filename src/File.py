from abc import ABC
from datetime import datetime
import os
from os import PathLike
from pathlib import PurePath, Path
from typing import Union

from .common.constants import EXCEPTIONS, DATETIME_INFO


class NotAFileError(Exception):
    def __init__(
        self,
        message: str = "The given file name doesn't repressent a file."
    ):
        super().__init__(message)


class File(ABC):

    def __init__(
        self,
        name: str,
        directory_path: Union[str, PathLike, PurePath, bytes],
        extension: str = ''
    ):
        self.name = name
        self.directory_path = directory_path
        self.extension = extension

        if self.extension:
            self._full_name = f'{self.name}.{self.extension}'
        else:
            self._full_name = self.name

        self._file = Path(os.path.join(self.directory_path,
                                       self.full_name))

        if self._file.exists():
            self.__check_file_integrity()

        self._full_path = self._file.absolute()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name
        elif name is None:
            self.__name = None
        else:
            raise TypeError(
                EXCEPTIONS.MESSAGES.TYPE_ERROR.format(
                    param='name', tp=str, inst=type(name)
                )
            )

    @property
    def directory_path(self) -> Union[str, PathLike, PurePath, bytes]:
        return self.__directory_path

    @directory_path.setter
    def directory_path(
        self,
        directory_path: Union[str, PathLike, PurePath, bytes]
    ):
        if isinstance(directory_path, (str, PathLike, PurePath, bytes)):
            self.__directory_path = directory_path
        elif directory_path is None:
            self.__directory_path = None
        else:
            raise TypeError(
                EXCEPTIONS.MESSAGES.TYPE_ERROR.format(
                    param='directory_path',
                    tp=Union[str, PathLike, PurePath, bytes],
                    inst=type(directory_path)
                )
            )

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        if isinstance(extension, str):
            self.__extension = extension
        elif extension is None:
            self.__extension = None
        else:
            raise TypeError(
                EXCEPTIONS.MESSAGES.TYPE_ERROR.format(
                    param='extension', tp=str, inst=type(extension)
                )
            )

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def full_path(self) -> PurePath:
        return self._full_path

    def size_in_bytes(self) -> int:
        return self._file.stat().st_size

    def size_in_kilobytes(self) -> int:
        return self._file.stat().st_size / 1000

    def size_in_megabytes(self) -> int:
        return self._file.stat().st_size / 1000000

    def size_in_gigabytes(self) -> int:
        return self._file.stat().st_size / 1000000000

    def last_modification(self) -> datetime:
        return datetime.fromtimestamp(
            self._file.stat().st_mtime,
            DATETIME_INFO.LOCAL_TIMEZONE
        )

    def __check_file_integrity(self):
        if not self._file.is_file():
            raise NotAFileError()
