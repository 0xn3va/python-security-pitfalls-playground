import unittest
import logging
from unittest.mock import Mock


logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):

    def test_never_called_decorators(self) -> None:
        mock_f = Mock()

        def decorator(func):
            logger.info(f'The decorator has been applied to {func.__name__}')
            mock_f()
            def wrapper():
                func()
            return wrapper

        @decorator
        def never_called():
            pass

        mock_f.assert_called_once()


if __name__ == '__main__':
    unittest.main()
