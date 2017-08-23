This demonstrates a "failure" of `MANIFEST.in` to
exclude a directory.

The `setup.py` file simulates building a shared library
on Mac OS X by creating the same file structure.

```
$ rm -fr dist/ && \
>   python setup.py sdist > /dev/null 2>&1 && \
>   tar xzf dist/example-0.0.1.tar.gz -C dist/ && \
>   find dist/example-0.0.1
dist/example-0.0.1
dist/example-0.0.1/MANIFEST.in
dist/example-0.0.1/setup.py
dist/example-0.0.1/setup.cfg
dist/example-0.0.1/PKG-INFO
dist/example-0.0.1/example
dist/example-0.0.1/example/example.f90
dist/example-0.0.1/example/example_fortran.pxd
dist/example-0.0.1/example/.lib
dist/example-0.0.1/example/.lib/libexample.dylib.dSYM
dist/example-0.0.1/example/.lib/libexample.dylib.dSYM/Contents
dist/example-0.0.1/example/.lib/libexample.dylib.dSYM/Contents/Info.plist
dist/example-0.0.1/example/include
dist/example-0.0.1/example/include/example.h
dist/example-0.0.1/example/__init__.py
dist/example-0.0.1/example/fast.c
dist/example-0.0.1/example.egg-info
dist/example-0.0.1/example.egg-info/dependency_links.txt
dist/example-0.0.1/example.egg-info/SOURCES.txt
dist/example-0.0.1/example.egg-info/not-zip-safe
dist/example-0.0.1/example.egg-info/top_level.txt
dist/example-0.0.1/example.egg-info/PKG-INFO
```
