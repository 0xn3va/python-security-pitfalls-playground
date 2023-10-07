# Pitfalls of using mutable default objects

Mutable default values are quite a useful feature provided in Python but they can cause unexpected behavior if not used carefully. Consider the function below, which defines the list of scopes available to a user.

```python
def list_scopes(user_id: str, default_scopes: List[str] = []) -> List[str]:
    scopes = default_scopes
    if get_user_role(user_id) == 'ADMIN':
        scopes.append('write')
    return scopes
```

The function above takes a list of default scopes in the optional argument `default_scopes` with a default value `[]`. The snippet below shows the result of running the function for users with admin and with non-admin roles.

```python
admin_user_id = '0'
scopes = list_scopes(admin_user_id)
# scopes == ['write']

non_admin_user_id = '1337'
scopes = list_scopes(non_admin_user_id)
# scopes == ['write']
```

In this example, the function returns the same scope for a non-admin user as for an admin user. This happens because instead of creating a new empty list as expected, it continues to use the list defined in the default value.

Python's default arguments are evaluated once when the function is defined, not each time the function is called. This means that if a mutable default argument is used and mutated, this object will be and have been mutated for all future calls to the function as well.

## Playground

There are test cases for a default list object:

- [default_list_object.py](./default_list_object.py)

Use the following command to run tests:

```bash
# python3 <test_case>
python3 default_list_object.py
```
