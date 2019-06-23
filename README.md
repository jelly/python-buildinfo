# python-buildinfo

A simple Python BUILDINFO parsing library.

## Dependencies

* parse

## Usage

The buildinfo module exposes one function called `parse_buildinfo` which
returns a tuple containing parsed data and possible errors.

```
foo = """buildinfo = /build
buildenv = !distcc
buildenv = color
"""
data, errors = parse_buildinfo(buildinfo)
print(data)
```
