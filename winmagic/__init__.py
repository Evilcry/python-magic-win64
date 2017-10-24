import os

import sys

MAGIC_LIBRARY = 'nscaife'
WINMAGIC_PATH = os.path.dirname(os.path.realpath(__file__))
MAGIC_LIBRARY_PATH = os.path.join(WINMAGIC_PATH, MAGIC_LIBRARY)
MAGIC_FILE = os.path.join(MAGIC_LIBRARY_PATH, 'magic.mgc')

# if we are not running on 64-bit windows with 64-bit python, do nothing except import python-magic
_activate = os.name == 'nt' and sys.maxsize > 2 ** 32

if _activate:
    # import magic will try to load magic1.dll from the windows PATH, so add our dll directory before importing
    os.environ["PATH"] += os.pathsep + MAGIC_LIBRARY_PATH

import magic

if _activate:
    # we also need to monkey-patch the Magic class to tell it where to find
    # the default magic file - there is no system default magic on windows
    old_init = magic.Magic.__init__


    def new_init(self, mime=False, magic_file=None, mime_encoding=False, keep_going=False, uncompress=False):
        """
        Create a new libmagic wrapper.

        mime - if True, mimetypes are returned instead of textual descriptions
        mime_encoding - if True, codec is returned
        magic_file - use a mime database other than the system default
        keep_going - don't stop at the first match, keep going
        uncompress - Try to look inside compressed files.
        """
        if magic_file is None:
            magic_file = MAGIC_FILE
        old_init(self, mime, magic_file, mime_encoding, keep_going, uncompress)


    magic.Magic.__init__ = new_init
__all__ = ('magic',)
