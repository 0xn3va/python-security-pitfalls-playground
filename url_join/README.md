# Pitfalls of joining URLs

There is the [urllib.parse.urljoin(base, url, allow_fragments=True)](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin) that constructs a full URL by combining a base URL with another URL.

However, if a URL is an absolute URL (that is, it starts with `//` or `scheme://`), the URL's hostname and/or scheme will be present in the result. For example, joining `https://foo.bar` and `//localhost/test` will result in `https://localhost/test`.

## Playground

There are test cases for `urllib.parse.urljoin`:

- [urllib_parse_urljoin.py](./urllib_parse_urljoin.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 urllib_parse_urljoin.py
```
