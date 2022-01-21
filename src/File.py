from abc import ABC
import os
from os import PathLike
from pathlib import PurePath, Path
from typing import Union

from datetime import datetime

from .common.constants import EXCEPTIONS


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
    def size(self) -> int:
        return self._size

    @property
    def last_modification_datetime(self) -> datetime:
        return self._last_modification_datetime

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def full_path(self) -> PurePath:
        return self._full_path

    def _set_size(self, unit: str = 'B') -> int:
        """ Sets the _size attribute with a value that represents the file size.

        Args:
            unit (str, optional): The meaurement unit to return the size in.
              Defaults to 'B'. Possible values: (B, KB, MB, GB)

        Returns:
            int: the file size converted to the specified measurement unit.
        """

        if unit == 'B':
            self._size = self._file.stat().st_size
        elif unit == 'KB':
            self._size = self._file.stat().st_size / 1000
        elif unit == 'MB':
            self._size = self._file.stat().st_size / 1000000
        elif unit == 'GB':
            self._size = self._file.stat().st_size / 1000000000
        else:
            raise ValueError(
                EXCEPTIONS.MESSAGES.VALUE_ERROR.format(
                    param='unit',
                    restr=(
                        'it must be equal to some of these values:'
                        + ' (B, KB, MB, GB)'
                    )
                )
            )

    def _set_last_modification_datetime(self):
        self._last_modification_datetime = datetime.fromtimestamp()

    def __check_file_integrity(self):
        if not self._file.is_file():
            raise NotAFileError()


File('myfile', '~/Documentos', 'txt')
