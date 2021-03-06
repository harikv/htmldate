"""
Seamlessly extract the date of web pages based on header or body.
http://github.com/adbar/htmldate
"""

# workaround for open() with encoding=''
from codecs import open

from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))
packages = ['htmldate']


# some problems with installation solved this way
extras = {
    'all': [
        'ciso8601 >= 2.1.2',
        'dateparser >= 0.7.2',  # 0.5.0 could be faster
        'regex >= 2020.1.8',
        ],
}


def readme():
    with open(path.join(here, 'README.rst'), 'r', 'utf-8') as readmefile:
        return readmefile.read()

setup(
    name='htmldate',
    version='0.6.1',
    description='Find the creation date of web pages using a combination of tree traversal, common structural patterns, text-based heuristics and robust date extraction.',
    long_description=readme(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    keywords=['datetime', 'date-parser', 'entity-extraction', 'html-extraction', 'html-parsing', 'metadata-extraction',  'webarchives', 'web-scraping'],
    url='http://github.com/adbar/htmldate',
    author='Adrien Barbaresi',
    author_email='barbaresi@bbaw.de',
    license='GPLv3+',
    packages=packages,
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=[
        'lxml == 4.3.5; python_version == "3.4"',
        'lxml >= 4.4.2; python_version > "3.4"',
        'python-dateutil >= 2.8.1',
        'requests == 2.21.0; python_version == "3.4"',
        'requests >= 2.22.0; python_version > "3.4"',
    ],
    extras_require=extras,
    entry_points = {
        'console_scripts': ['htmldate=htmldate.cli:main'],
    },
    # platforms='any',
    tests_require=['pytest'],
    zip_safe=False,
)
