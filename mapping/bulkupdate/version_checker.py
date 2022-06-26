import logging
import json
import requests

logger = logging.getLogger(__name__)


class VersionChecker:
    """
    Class to access different software versions.
    Parameters
    ----------
    branch: str, optional (default main)
        git hub branch, where the information is stored.
    """

    def __init__(self, branch='main'):
        self._url = f'https://raw.githubusercontent.com/SpielerNogard/mapping/{branch}/versions.json'

    def _get_versions(self):
        response = requests.get(self._url)
        data = json.loads(response.text)
        return data

    def access_pogodroid_version(self):
        """Method to access the current pogodroid version

        Returns
        -------
        str
            current pogodroid version
        """
        version_data = self._get_versions()
        return version_data['PogoDroid']

    def access_pogo_version(self, stable=False):
        """Method to access the current Pogo version.

        Parameters
        ----------
        stable : bool, optional (default False)
            if `True` return current forced version
            if `False`return current  highest supported version

        Returns
        -------
        str
            version found for pogo
        """
        version_data = self._get_versions()
        if stable:
            return version_data['ForcedPogo']
        return version_data['SupportedPogo']
