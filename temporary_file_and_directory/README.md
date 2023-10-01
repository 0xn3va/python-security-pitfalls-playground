# Pitfalls of using temporary files and directories

Python provides a standard module `tempfile` to create temporary files and directories that has the following functions and classes:

- [tempfile.TemporaryFile(...)](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile)
- [tempfile.NamedTemporaryFile(...)](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)
- [class tempfile.SpooledTemporaryFile(...)](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile)
- [class tempfile.TemporaryDirectory(...)](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory)
- [tempfile.mkstemp(...)](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp)
- [tempfile.mkdtemp(...)](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp)

Among the arguments accepted by the functions and classes above there are two `prefix` and `suffix` that are used for the file or directory name generation, which looks like this:

```python
prefix + name + suffix
```

Under the hood, `tempfile` relies on `os.path.join` to craft a path to a temporary file or directory. Using `os.path.join` for joining paths may lead to unexpected results as described in the [join_paths](/join_paths/README.md) section.

There are pitfalls in using `prefix` that can lead to unexpected results:

1. `prefix` and path traversal. Since `prefix` is used before the random part at the beginning of the name, the path traversal in `prefix` will lead to the creation of a temporary file or directory in an arbitrary location. For example, passing `../../payload` to `prefix` will result in `/var/folders/86/81p8ttj157nfv1r2g323w3z40000gn/T/tmpw7hrvb0u/../../payload.5lif771a`.
1. `prefix` and absolute paths. Since `prefix` is used before the random part at the beginning of the name, a payload that starts with `/` will force `os.path.join` to treat it as an absolute path. For example, passing `/tmp/payload` to `prefix` will result in `/tmp/payload.5lif771a`.

However, the behaviour for `suffix` is different. Since `suffix` is added after the random part, using path traversal or absolute paths results in `FileNotFoundError` while creating a file or directory. This happens because cutting off the random part leads to the appearance of a directory in the path that does not exist. As a result, `os.open` and `os.mkdir` throw an error because a parent directory in the path does not exist. For example, passing `/../payload` to `suffix` results in `/var/folders/86/81p8ttj157nfv1r2g323w3z40000gn/T/tmpw7hrvb0u/../payload` where the parent directory `tmpw7hrvb0u` (the random part of the name) does not exist.

## Playground

There are test cases for the creation of temporary files and directories:

- [tempfile_temporarydirectory.py](./tempfile_temporarydirectory.py)
- [tempfile_namedtemporaryfile.py](./tempfile_namedtemporaryfile.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 tempfile_temporarydirectory.py
```
