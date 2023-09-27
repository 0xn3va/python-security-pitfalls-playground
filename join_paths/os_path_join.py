import unittest
import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):
    base_path = '/path/to/base/folder'

    def test_path_traversal(self) -> None:
        payload = '../../etc/passwd'
        path: str = os.path.join(self.base_path, payload)
        self.assertEqual(path, f'{self.base_path}/../../etc/passwd')
        self.print_summary(
            title='Testing os.join.path with path traversal',
            payload=payload, 
            result=path
        )

    def test_absolute_path(self) -> None:
        payload = '/etc/passwd'
        path: str = os.path.join(self.base_path, payload)
        self.assertEqual(path, '/etc/passwd')
        self.print_summary(
            title='Testing os.join.path with absolute path',
            payload=payload, 
            result=path
        )

    def print_summary(self, title: str, payload: str, result: str) -> None:
        msg = f'{title}\n' + \
            f'Base path:\t{self.base_path}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Joined path:\t{result}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
