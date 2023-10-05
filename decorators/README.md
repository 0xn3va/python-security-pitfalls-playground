# Pitfalls of implementing decorators

When implementing decorators, it is extremely important to remember that the call to an external function of a decorator occurs at the moment it is applied to a target function. Therefore, the code of the external decorator function will be executed even if the target function has not been called. Consider the example below:

```python
def decorator(func):
    print(f'The decorator has been applied to {func.__name__}')
    def wrapper():
        func()
    return wrapper

@decorator
def never_called():
    pass
```

Despite the fact that the `never_called` function was not called, the following message will appear in the console:

```
The decorator has been applied to never_called
```

## Playground

- [never_called_decorators.py](./never_called_decorators.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 never_called_decorators.py
```
