from abc import ABC, abstractmethod
from os import PathLike
from pathlib import PurePath
from typing import Union

from datetime import datetime
from datetime import date
from datetime import time

from .common.constants import CONSTANTS

class File(ABC):

    def __init__(
        self,
        name: str,
        directory_path: Union[str, PathLike, PurePath, bytes],
        extension: str
    ):
        self.name = name
        self.directory_path = directory_path
        self.extension = extension
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError(
                CONSTANTS['MESSAGES']['EXCEPTIONS']['TYPE_ERROR'].format(
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
        else:
            raise TypeError(
                CONSTANTS['MESSAGES']['EXCEPTIONS']['TYPE_ERROR'].format(
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
        else:
            raise TypeError(
                CONSTANTS['MESSAGES']['EXCEPTIONS']['TYPE_ERROR'].format(
                    param='extension', tp=str, inst=type(extension)
                )
            )
    
    @property
    def size(self) -> int:
        return self.__size
    
    @property
    def last_modification_datetime(self) -> datetime:
        return self.__last_modification_datetime
    
    @property
    def last_modification_date(self) -> date:
        return self.__last_modification_date
    
    @property
    def last_modification_time(self) -> time:
        return self.__last_modification_time
    
    @abstractmethod
    def create(self) -> bool:
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        pass
    
    @abstractmethod
    def copy(
        self,
        to: Union[str, PathLike, PurePath, bytes]
    ) -> Union[str, PathLike, PurePath, bytes]:
        pass

    @abstractmethod
    def move(
        self,
        to: Union[str, PathLike, PurePath, bytes],
        overwrite_if_exists: bool=True
    ) -> Union[str, PathLike, PurePath, bytes]:
        pass

    @abstractmethod
    def rename(self, new_name: str, new_extension: str=None):
        pass

    @abstractmethod
    def get_content(self, all: bool) -> object:
        pass
