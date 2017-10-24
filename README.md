# python-magic-win64

`python-magic-win64` is a transparent layer on top of
[python-magic](https://github.com/ahupp/python-magic) that comes with
its own DLLs and magic file for Windows x64. It is motivated by the
difficulties I had in getting `python-magic` to work on windows with a
decently recent version of libmagic.

### Usage
    >>> from winmagic import magic

This transparently patches in the required files on Windows x64, 
and does nothing apart from `import magic` on other platforms.

For usage of python-magic, see [https://github.com/ahupp/python-magic](https://github.com/ahupp/python-magic).

### About

The Windows DLL and magic files used by this project are built from [https://github.com/nscaife/file-windows](https://github.com/nscaife/file-windows).
See that project's page for details.

### Licensing

According to [https://github.com/nscaife/file-windows](https://github.com/nscaife/file-windows):
* `file/libmagic` has a license which allows its copying in both source and binary form, provided its license file accompanies it. See `nscaife/COPYING.file` for more information.
* `libgnurx` is LGPL 2.1.
* Everything else in the repository is public domain. Use it at your own risk.