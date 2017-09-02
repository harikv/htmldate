htmldate: find the creation date of HTML pages
==============================================

.. image:: https://img.shields.io/pypi/v/htmldate.svg
    :target: https://pypi.python.org/pypi/htmldate

.. image:: https://img.shields.io/pypi/l/htmldate.svg
    :target: https://pypi.python.org/pypi/htmldate

.. image:: https://img.shields.io/pypi/pyversions/htmldate.svg
    :target: https://pypi.python.org/pypi/htmldate

.. image:: https://img.shields.io/pypi/status/htmldate.svg
    :target: https://pypi.python.org/pypi/htmldate


Description
-----------

Seamless extraction/scraping of dates in web pages. *htmldate* provides following ways to date documents, based on HTML parsing:

1. Starting from the header of the page, it uses common patterns to identify date fields.
2. If this is not successful, it then scans the whole document.
3. If no date cue could be found, it finally run a series of heuristics on the content.

Pull requests are welcome.


Usage
-----

The module is programmed with python3 in mind. It takes the HTML document as input (string format) and returns a date when a valid cue could be found in the document. The output string defaults to `ISO 8601 YMD format <https://en.wikipedia.org/wiki/ISO_8601>`_.

Install from package repository: ``pip3 install htmldate``

Direct installation of the latest version over pip is possible (but not thoroughly tested):

``pip3 install git+https://github.com/adbar/htmldate.git``


Within Python
~~~~~~~~~~~~~

All the functions of the module are currently bundled in *htmldate*, the examples below use the external module `requests <http://docs.python-requests.org/>`_.

In case the web page features clear metadata, the extraction is straightforward:

.. code-block:: python

    >>> import requests
    >>> import htmldate
    >>> r = requests.get('r = requests.get('https://www.theguardian.com/politics/2016/feb/17/merkel-eu-uk-germany-national-interest-cameron-justified')

    >>> htmldate.find_date(r.text)
    '2016-02-17'

A more advanced analysis is sometimes needed:

.. code-block:: python

    >>> r = requests.get('http://blog.python.org/2016/12/python-360-is-now-available.html')
    >>> core.find_date(r.text)
    '# DEBUG analyzing: <h2 class="date-header"><span>Friday, December 23, 2016</span></h2>'
    '# DEBUG result: 2016-12-23'
    '2016-12-23'

In the worst case, the module resorts to a wild guess:

.. code-block:: python

    >>> r = requests.get('https://creativecommons.org/about/')
    >>> htmldate.find_date(r.text)
    '2016-05-01'

There are however pages for which no date can be found, ever:

.. code-block:: python

    >>> r = requests.get('https://example.com')
    >>> htmldate.find_date(r.text)
    >>>


Command-line
~~~~~~~~~~~~

A basic command-line interface is included:

.. code-block:: bash

    $ wget -qO- "http://blog.python.org/2016/12/python-360-is-now-available.html" | htmldate
    2016-12-23


Additional information
----------------------

Context
~~~~~~~

There are webpages for which neither the URL nor the server response
provide a reliable way to date the document, i.e. find when it was
written.

This module is part of methods to derive metadata from web documents in
order to build text corpora for (computational) linguistic analysis. For
more information:

-  Barbaresi, Adrien. "`Efficient construction of metadata-enhanced web corpora <https://hal.archives-ouvertes.fr/hal-01348706/document>`_", Proceedings of the `10th Web as Corpus Workshop (WAC-X) <https://www.sigwac.org.uk/wiki/WAC-X>`_, 2016.

Kudos to...
~~~~~~~~~~~

-  `lxml <http://lxml.de/>`_
-  `dateparser <https://github.com/scrapinghub/dateparser>`_ (although it's is still a bit slow)
-  A few patterns are derived from
   `python-goose <https://github.com/grangier/python-goose>`_,
   `metascraper <https://github.com/ianstormtaylor/metascraper>`_,
   `newspaper <https://github.com/codelucas/newspaper>`_ and
   `articleDateExtractor <https://github.com/Webhose/article-date-extractor>`_.
   This module extends them significantly.

Contact
~~~~~~~

See my `contact page <http://adrien.barbaresi.eu/contact.html>`_ for details.