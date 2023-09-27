import unittest
from pathlib import PurePath
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):
    base_path = '/path/to/base/folder'

    def test_path_traversal(self) -> None:
        payload = '../../etc/passwd'
        path = PurePath(self.base_path).joinpath(payload)
        self.assertEqual(str(path), f'{self.base_path}/../../etc/passwd')
        self.print_summary(
            title='Testing pathlib.PurePath.joinpath with path traversal',
            payload=payload, 
            result=str(path)
        )

    def test_absolute_path(self) -> None:
        payload = '/etc/passwd'
        path = PurePath(self.base_path).joinpath(payload)
        self.assertEqual(str(path), '/etc/passwd')
        self.print_summary(
            title='Testing pathlib.PurePath.joinpath with absolute path',
            payload=payload, 
            result=str(path)
        )

    def print_summary(self, title: str, payload: str, result: str) -> None:
        msg = f'{title}\n' + \
            f'Base path:\t{self.base_path}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Joined path:\t{result}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
