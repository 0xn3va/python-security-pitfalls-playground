import unittest
import re
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):
    pattern = '..'

    def test_match(self) -> None:
        payload = '../path/traversal/payload'
        match = re.match(self.pattern, payload)
        self.assertIsNotNone(match)
        self.print_summary(
            title='Testing re.match with one liner',
            payload=payload,
            match=str(match)
        )

    def test_match_multiline(self) -> None:
        payload = '\n../path/traversal/payload'
        match = re.match(self.pattern, payload)
        self.assertIsNone(match)
        self.print_summary(
            title='Testing re.match with multi liner',
            payload=payload.replace('\n', '\\n'),
            match=str(match)
        )

    def test_search(self) -> None:
        payload = '../path/traversal/payload'
        match = re.search(self.pattern, payload)
        self.assertIsNotNone(match)
        self.print_summary(
            title='Testing re.search with one liner',
            payload=payload,
            match=str(match)
        )

    def test_search_multiline(self) -> None:
        payload = '\n../path/traversal/payload'
        match = re.search(self.pattern, payload)
        self.assertIsNotNone(match)
        self.print_summary(
            title='Testing re.search with multi liner',
            payload=payload.replace('\n', '\\n'),
            match=str(match)
        )

    def print_summary(self, title: str, payload: str, match: str) -> None:
        msg = f'{title}\n' + \
            f'Pattern:\t{self.pattern}\n' + \
            f'Payload:\t{payload}\n' + \
            f'Match:\t\t{match}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
