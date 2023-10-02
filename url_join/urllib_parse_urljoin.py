import unittest
import urllib.parse
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):
    base_url = 'https://foo.bar/'

    def test_absolute_url(self) -> None:
        payload = '//attacker.local/test'
        url: str = urllib.parse.urljoin(self.base_url, payload)
        self.assertEqual(url, 'https://attacker.local/test')
        self.print_summary(
            title='Testing urllib.parse.urljoin with absolute path',
            payload=payload, 
            result=url
        )

    def test_absolute_url_with_schema(self) -> None:
        payload = 'scheme://attacker.local/test'
        url: str = urllib.parse.urljoin(self.base_url, payload)
        self.assertEqual(url, 'scheme://attacker.local/test')
        self.print_summary(
            title='Testing urllib.parse.urljoin with absolute path and scheme',
            payload=payload, 
            result=url
        )

    def print_summary(self, title: str, payload: str, result: str) -> None:
        msg = f'{title}\n' + \
            f'Base URL:\t{self.base_url}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Joined URL:\t{result}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
