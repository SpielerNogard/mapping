"""This module includes a basic logger"""
import logging
import os


class BaseLogger:
    """Class to create the logger config.

        Parameters
        ----------
        tags : str, optional
            this will be added to every log message
        log_level : int, optional
            log level to use.
    """

    def __init__(self, tags: str = "", log_level: int = logging.NOTSET):
        self._log_level = log_level
        self._tags = tags
        self.set_logger()

    def set_logger(self, environs: list = None):
        """Method to create the logger config.

        Parameters
        ----------
        evirons : list, optional
            list of variable names that can be foudn in environ.
            to set by every log message.
        """
        if not environs:
            environs = []
        tags = ""
        for env in environs:
            tags += f'{os.environ.get(env, "")} '
        base_format = (f'[%(levelname)s] '
                       f'[{tags}%(name)s.%(funcName)s line:%(lineno)d]'
                       f' {self._tags} %(message)s')
        logging.basicConfig(format=base_format,
                            datefmt='%Y-%m-%d %H:%M:%S%z',
                            level=self._log_level,
                            force=True)
