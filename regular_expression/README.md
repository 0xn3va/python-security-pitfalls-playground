# Pitfalls of using regular expressions

Python offers different primitive operations based on regular expressions:

- [re.match()](https://docs.python.org/3/library/re.html#re.match) checks for a match only at the beginning of the string.
- [re.search()](https://docs.python.org/3/library/re.html#re.search) checks for a match anywhere in the string.

As can be seen from the descriptions above, the difference between the two functions is that `re.match()` looks for a match only at the beginning of the string, even in the [miltiline](https://docs.python.org/3/library/re.html#re.MULTILINE) mode, while `re.search()` looks for a match anywhere in the string.

```python
# re.match
re.match('c', 'abcdef') # No match
re.match('a', 'abcdef') # Match
re.match('c', 'a\nb\nc', re.MULTILINE) # No match
re.match('a', 'a\nb\nc', re.MULTILINE) # Match
# re.search
re.search('c', 'abcdef') # Match
re.search('a', 'abcdef') # Match
re.search('c', 'a\nb\nc') # Match
```

As a result, using `re.match` to implement the validation may lead to the possibility of bypassing it with the new line `\n`.

## Playground

There are test cases for using `re.match` and `re.search`:

- [re_match_and_search.py](./re_match_and_search.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 re_match_and_search.py
```
