
from mapping.core.sql_lite_handler import Database
from mapping.bulkupdate import sql
import logging
logger = logging.getLogger(__name__)


class DeviceHandler:
    def __init__(self):
        self._db = Database(database_name='devices')

    def _create_table(self):
        logger.info('creating device table')
        self._db.create_table(create_statement=sql.device_table)

    def add_device(self, device_name: str, ip: str, port: int = 5555, arch: int = 64, pd_version: str = "", pogo_version: str = ""):
        logger.info(f"adding device with {ip=}")
        entry = {'name': device_name,
                 'ip': ip,
                 'port': port,
                 'arch': arch,
                 'pd_version': pd_version,
                 'pogo_version': pogo_version}
        self._db.insert_data(table_name='devices', entry=entry)
        logger.info("successfully added device")

    def update_pd_version(self, device_ip, pd_version):
        logger.info(f'Updating {device_ip=} to {pd_version=}')
        sql = "UPDATE devices SET pd_version = ? WHERE ip = ?;"
        self._db.update(sql, [pd_version, device_ip])

    def update_pogo_version(self, device_ip, pogo_version):
        logger.info(f'Updating {device_ip=} to {pogo_version=}')
        sql = "UPDATE devices SET pogo_version = ? WHERE ip = ?;"
        self._db.update(sql, [pogo_version, device_ip])

    def access_devices(self):
        sql = "SELECT * from devices"
        device_list = self._db.query(sql)
        for device in device_list:
            logger.info(device)

        return device_list


if __name__ == "__main__":
    from mapping.core.base_logger import BaseLogger
    conf = BaseLogger(tags=['DeviceHandler'])
    device = DeviceHandler()
    device._create_table()
    #device.add_device(device_name='SpielerNogard21', ip='192.168.44.25')
    device_list = device.access_devices()
    for devices in device_list:
        device.update_pogo_version(device_ip=devices[2], pogo_version='0.239.1')
