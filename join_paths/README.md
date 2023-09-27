# Pitfalls of joining paths

Python provides several standard functions to join paths:

- [os.path.join(path, *paths)](https://docs.python.org/3/library/os.path.html#os.path.join)
- [pathlib.PurePath(*pathsegments)](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath)
- [pathlib.PurePath.joinpath(*pathsegments)](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath)

> Note: `pathlib.PurePath` is a parent class for other classes in `pathlib`, such as `Path` or `PosixPath`. It means that they all inherit the described behaviour from `PurePath`.

Typically these functions are used to craft a path within a base path, like this:

```python
filename = request.POST['filename']
path = os.path.join(base_path, filename)
```

However, there are pitfalls in path joining that can lead to unexpected results:

1. Path traversal. Since the logic of the functions is fairly straightforward when joining a base path and a path with `../` together, the path with `../` will simply be appended to the base path without any additional processing or resolution. For example, joining `/base/path` and `../payload` will result in `/base/path/../payload`; as a result, passing the crafted path to `open()` will lead to the path traversal vulnerability.
1. Handling absolute paths. If one of the arguments starts with `/`, this argument is treated as an absolute path by these functions and all previous arguments including a base path are removed. For example, joining `/base/path` and `/payload` will result in `/payload`

## Playground

There are test cases for each function:

- [os_path_join.py](./os_path_join.py)
- [pathlib_purepath.py](./pathlib_purepath.py)
- [pathlib_purepath_joinpath.py](./pathlib_purepath_joinpath.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 os_path_join.py
```
