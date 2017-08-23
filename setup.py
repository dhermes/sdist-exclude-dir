from __future__ import unicode_literals

import os

import setuptools


FAKE_DIRS = (
    os.path.join(
        'example',
        '.lib',
        'libexample.dylib.dSYM',
        'Contents',
        'Resources',
        'DWARF',
    ),
)
FAKE_FILES = (
    'example.mod',
    os.path.join('example', '.lib', 'libexample.dylib'),
    os.path.join(
        'example',
        '.lib',
        'libexample.dylib.dSYM',
        'Contents',
        'Info.plist',
    ),
    os.path.join(
        'example',
        '.lib',
        'libexample.dylib.dSYM',
        'Contents',
        'Resources',
        'DWARF',
        'libexample.dylib',
    ),
    os.path.join('example', 'example.o'),
)


def fake_compile():
    for dir_name in FAKE_DIRS:
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

    for filename in FAKE_FILES:
        with open(filename, 'w') as file_obj:
            file_obj.write('GENERATED\n')


def main():
    fake_compile()

    setuptools.setup(
        name='example',
        version='0.0.1',
        description='Frotz',
        author='Danny Hermes',
        author_email='daniel.j.hermes@gmail.com',
        long_description='Did you read me? Get it? README?',
        url='https://github.com/dhermes/foreign-fortran',
        packages=['example'],
        include_package_data=True,
        zip_safe=False,
    )


if __name__ == '__main__':
    main()
