from setuptools import setup

setup(
    name='python-magic-win64',
    packages=['winmagic'],
    package_dir={'winmagic': 'winmagic'},
    package_data={'winmagic': ['nscaife/*']},
    version='0.4.13',
    install_requires=['python-magic==0.4.13'],
    include_package_data=True,
    description='python-magic bundled with win64 dlls',
    long_description="""This module uses python-magic to access libmagic functionality.
It also distributes and automatically injects the magic library for 64-bit Windows & python.
Can be used as a drop-in replacement for python-magic by using `from winmagic import magic`.
""",
    license='MIT',
    author='Cristian Vîjdea',
    author_email='cristi@cvjd.me',
    url='https://github.com/axnsan12/python-magic-win64',
    download_url='https://github.com/axnsan12/python-magic-win64/archive/0.4.13.tar.gz',
    keywords=['mime', 'magic', 'file', 'windows', 'win64', 'dll'],  # arbitrary keywords
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
