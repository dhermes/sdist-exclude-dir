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

1. `global-exclude *.so *.dylib *.dylib.dSYM` (see `outputs/01.txt`)
2. `prune *.dylib.dSYM` (see `outputs/02.txt`)
3. `recursive-exclude *.dylib.dSYM *` (see `outputs/03.txt`)
4. `recursive-exclude * *.dylib.dSYM` (see `outputs/04.txt`)
5. `recursive-exclude example *.dylib.dSYM` (see `outputs/05.txt`)
6. `recursive-exclude example/.lib *.dylib.dSYM` (see `outputs/06.txt`)
9. `global-exclude *.so *.dylib *.dylib.dSYM/` (see `outputs/09.txt`)
10. `global-exclude *.so *.dylib *.dylib.dSYM/*` (see `outputs/10.txt`)

The following have succeeded, but they are overly specific:

- `prune example/.lib/libexample.dylib.dSYM` (see `outputs/07.txt`)
- `global-exclude *.so *.dylib *.plist` (succeeds because
  `*.dylib` and `*.plist` are the only extensions present in
  the `*.dylib.dSYM` directory, see `outputs/08.txt`)

There isn't much difference in the output:

```
$ diff -s outputs/01.txt outputs/02.txt
Files outputs/01.txt and outputs/02.txt are identical
$ diff -s outputs/01.txt outputs/03.txt
Files outputs/01.txt and outputs/03.txt are identical
$ diff -s outputs/01.txt outputs/04.txt
Files outputs/01.txt and outputs/04.txt are identical
$ diff -s outputs/01.txt outputs/05.txt
Files outputs/01.txt and outputs/05.txt are identical
$ diff -s outputs/01.txt outputs/06.txt
Files outputs/01.txt and outputs/06.txt are identical
$ diff -s outputs/01.txt outputs/09.txt
Files outputs/01.txt and outputs/09.txt are identical
$ diff -s outputs/01.txt outputs/10.txt
Files outputs/01.txt and outputs/10.txt are identical
$ diff -s outputs/07.txt outputs/08.txt
Files outputs/07.txt and outputs/08.txt are identical
$ diff outputs/07.txt outputs/01.txt
--- outputs/07.txt      2017-08-23 12:30:47.089347853 -0700
+++ outputs/01.txt      2017-08-23 12:30:47.089347853 -0700
@@ -6,6 +6,10 @@
 ./example
 ./example/example.f90
 ./example/example_fortran.pxd
+./example/.lib
+./example/.lib/libexample.dylib.dSYM
+./example/.lib/libexample.dylib.dSYM/Contents
+./example/.lib/libexample.dylib.dSYM/Contents/Info.plist
 ./example/include
 ./example/include/example.h
 ./example/__init__.py
```

## Issue Filed

See https://github.com/pypa/packaging-problems/issues/100
