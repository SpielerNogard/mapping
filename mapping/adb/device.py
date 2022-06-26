from mapping.adb.commander import Commander
from mapping.core import errors
import logging

logger = logging.getLogger(__name__)


class Device:
    def __init__(self, ip: str, port: int = 5555, on_device: bool = False):
        self._commander = None

        self._on_device = on_device
        if not self._on_device:
            self._commander = Commander()

        self._ip = ip
        self._port = port
        self._connected = False

    def _start_server(self):
        if self._commander:
            command = 'adb start-server'
            self._commander.command(command=command)

    def connect(self):
        logger.info(f'connecting to {self._ip}:{self._port}')
        if self._commander:
            command = f"adb connect {self._ip}:{self._port}"
            out, err = self._commander.command(command=command)
            logger.info(f'{out=} {err=}')
            if 'connected' in out:
                logger.info(f'Successfully connected to {self._ip}')
                return True
            logger.error('Cant connect to device')
            errors.CantConnectError('Cant connect to device')
            return False
        return False

    def disconnect(self):
        logger.info(f'disconnecting from {self._ip}')
        if self._commander:
            command = f"adb disconnect {self._ip}"
            out, err = self._commander.command(command=command)
            logger.info(f'{out=} {err=}')
            if 'disconnected' in out:
                logger.info(f'Successfully disconnected from {self._ip}')
                return True

        return False


if __name__ == "__main__":
    from mapping.core.base_logger import BaseLogger
    conf = BaseLogger(tags=['Device'])
    device = Device(ip='192.168.44.25')
    device.connect()
    device.disconnect()
