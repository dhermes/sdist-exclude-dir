This demonstrates a "failure" of `MANIFEST.in` to
exclude a directory.

The `setup.py` file simulates building a shared library
on Mac OS X by creating the same file structure.

```
$ rm -fr dist/ && \
>   python setup.py sdist > /dev/null 2>&1 && \
>   tar xzf dist/example-0.0.1.tar.gz -C dist/ && \
>   (cd dist/example-0.0.1 && find .)
.
./MANIFEST.in
./setup.py
./setup.cfg
./PKG-INFO
./example
./example/example.f90
./example/example_fortran.pxd
./example/.lib
./example/.lib/libexample.dylib.dSYM
./example/.lib/libexample.dylib.dSYM/Contents
./example/.lib/libexample.dylib.dSYM/Contents/Info.plist
./example/include
./example/include/example.h
./example/__init__.py
./example/fast.c
./example.egg-info
./example.egg-info/dependency_links.txt
./example.egg-info/SOURCES.txt
./example.egg-info/not-zip-safe
./example.egg-info/top_level.txt
./example.egg-info/PKG-INFO
```

The following have been attempted and failed to exclude the directory:

- `global-exclude *.so *.dylib *.dylib.dSYM`
- `prune *.dylib.dSYM`
- `recursive-exclude *.dylib.dSYM *`
- `recursive-exclude * *.dylib.dSYM`
- `recursive-exclude example *.dylib.dSYM`
- `recursive-exclude example/.lib *.dylib.dSYM`

The following is the only one that has succeeded:

- `prune example/.lib/libexample.dylib.dSYM`
