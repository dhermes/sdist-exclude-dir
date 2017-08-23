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

1. `global-exclude *.so *.dylib *.dylib.dSYM` (see `output1.txt`)
2. `prune *.dylib.dSYM` (see `output2.txt`)
3. `recursive-exclude *.dylib.dSYM *` (see `output3.txt`)
4. `recursive-exclude * *.dylib.dSYM` (see `output4.txt`)
5. `recursive-exclude example *.dylib.dSYM` (see `output5.txt`)
6. `recursive-exclude example/.lib *.dylib.dSYM` (see `output6.txt`)

The following have succeeded, but they are overly specific:

7. `prune example/.lib/libexample.dylib.dSYM` (see `output7.txt`)
8. `global-exclude *.so *.dylib *.plist` (succeeds because
   `*.dylib` and `*.plist` are the only extensions present in
   the `*.dylib.dSYM` directory, see `output8.txt`)

There isn't much difference in the output:

```
$ diff -s output1.txt output2.txt
Files output1.txt and output2.txt are identical
$ diff -s output1.txt output3.txt
Files output1.txt and output3.txt are identical
$ diff -s output1.txt output4.txt
Files output1.txt and output4.txt are identical
$ diff -s output1.txt output5.txt
Files output1.txt and output5.txt are identical
$ diff -s output1.txt output6.txt
Files output1.txt and output6.txt are identical
$ diff -s output7.txt output8.txt
Files output7.txt and output8.txt are identical
$ diff output7.txt output1.txt
--- output7.txt 2017-08-23 11:54:02.447821958 -0700
+++ output1.txt 2017-08-23 11:52:46.608594694 -0700
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
