import subprocess
import logging
import os
logger = logging.getLogger(__name__)


class Commander:
    def __init__(self):
        "set PATH = %PATH%"
        r"C: \your\path\hereimport os"

    def _check_os(self):
        os_name = os.name
        logger.info(f'found os {os_name}')
        return os_name

    def command(self, command: str):
        if self._check_os() == 'nt':
            shell = False
        else:
            shell = True
        logger.info(f'{command}')
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
        stdout, stderr = p.communicate()
        return stdout.decode("utf-8"), stderr.decode("utf-8")
