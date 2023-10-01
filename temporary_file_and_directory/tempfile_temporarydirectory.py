import unittest
import tempfile
import logging
from pathlib import Path


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):

    def test_path_traversal_prefix(self) -> None:
        payload = '../payload.'
        with tempfile.TemporaryDirectory() as dir:
            with tempfile.TemporaryDirectory(dir=dir, prefix=payload) as tmp_dir:
                path = tmp_dir
                relative_path = str(Path(path).relative_to(dir))
        self.assertTrue(relative_path.startswith(payload))
        self.print_summary_for_prefix(
            title='Testing the prefix argument of tempfile.TemporaryDirectory with path traversal',
            payload=payload,
            result=path
        )

    def test_absolute_path_prefix(self) -> None:
        payload = '/tmp/payload.'
        with tempfile.TemporaryDirectory(prefix=payload) as tmp_dir:
            path = tmp_dir
        self.assertTrue(path.startswith(payload))
        self.print_summary_for_prefix(
            title='Testing the prefix argument of tempfile.TemporaryDirectory with absolute path',
            payload=payload,
            result=path
        )

    def test_path_traversal_suffix(self) -> None:
        payload = '/../../payload.'
        with self.assertRaises(FileNotFoundError) as context:
            _ = tempfile.TemporaryDirectory(suffix=payload)
        self.print_summary_for_suffix(
            title='Testing the suffix argument of tempfile.TemporaryDirectory with path traversal',
            payload=payload,
            exception_msg=str(context.exception)
        )

    def test_absolute_path_suffix(self) -> None:
        payload = '/tmp/payload.'
        with self.assertRaises(FileNotFoundError) as context:
            _ = tempfile.TemporaryDirectory(suffix=payload)
        self.print_summary_for_suffix(
            title='Testing the suffix argument of tempfile.TemporaryDirectory with absolute path',
            payload=payload,
            exception_msg=str(context.exception)
        )

    def print_summary_for_prefix(self, title: str, payload: str, result: str) -> None:
        msg = f'{title}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Temp directory:\t{result}\n'
        logger.info(msg)

    def print_summary_for_suffix(self, title: str, payload: str, exception_msg: str) -> None:
        msg = f'{title}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Exception:\t{exception_msg}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
