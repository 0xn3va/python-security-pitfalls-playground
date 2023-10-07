import unittest
import logging
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(message)s', level = logging.INFO)


class Tests(unittest.TestCase):

    def append_to(self, element: str, arr: List[str] = []) -> List[str]:
        arr.append(element)
        return arr

    def test_append_to_without_default_list(self) -> None:
        elements_to_append = ['a', 'b', 'c']
        for element in elements_to_append[:-1]:
            self.append_to(element)
        arr = self.append_to(elements_to_append[-1])
        self.assertListEqual(arr, elements_to_append)
        self.print_summary(
            title='Testing append_to(element)',
            append_to_invokes=[
                f'append_to(\'{e}\')'
                for e in elements_to_append
            ],
            result=arr
        )

    def test_append_to_with_default_list(self) -> None:
        initial_arr = ['1', '2', '3']
        elements_to_append = ['a', 'b', 'c']
        arr = list(initial_arr)
        intermediate_arrs = []
        for element in elements_to_append:
            intermediate_arrs.append(list(arr))
            self.append_to(element, arr=arr)
        self.assertListEqual(arr, initial_arr + elements_to_append)
        self.print_summary(
            title='Testing append_to(element, arr=arr)',
            append_to_invokes=[
                f'append_to(\'{e}\', arr={a})'
                for e, a in zip(elements_to_append, intermediate_arrs)
            ],
            result=arr
        )

    def print_summary(self, title: str, append_to_invokes: List[str], result: List[str]) -> None:
        invokes = '\n'.join([
            f'  {invoke}'
            for invoke in append_to_invokes
        ])
        msg = f'{title}\n' + \
            f'Invokes: \n{invokes}\n' \
            f'Result:\t{result}\n'
        logger.info(msg)


if __name__ == '__main__':
    unittest.main()
