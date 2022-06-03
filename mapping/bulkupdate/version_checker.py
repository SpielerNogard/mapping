import logging
import json
import requests
from mapping.core.base_logger import BaseLogger

conf = BaseLogger(tags="['BulkUpdate']['VersionChecker']")
logger = logging.getLogger(__name__)

url = 'https://raw.githubusercontent.com/SpielerNogard/mapping/bulkupdate/versions.json'
resp = requests.get(url)
data = json.loads(resp.text)
logger.info(data)
