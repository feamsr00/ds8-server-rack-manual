Workflow
========

Issues
------

You've found a mistake in this manual, or maybe you'd like a new section. You can help us by `submitting an issue on GitHub <https://github.com/feamsr00/ds8-server-rack-manual/issues>`_. But before you create a new issue, please make sure to search the issue archive first -- your issue may have already been addressed!

Please try to create bug reports that are:

- *Reproducible*. Include steps to reproduce the problem.
- *Specific.* Include as much detail as possible: which version, what environment, etc.
- *Unique.* Do not duplicate existing opened issues.
- *Scoped to a Single Bug.* One bug per report.

**Even better: Submit a pull request with a fix or new section!**

On DCOs and Sign-offs
---------------------

This project uses `Developer Certificate of Origin <https://developercertificate.org/>`_. The reasons to do so are `various and sundry <https://bssw.io/items/the-developer-certificate-of-origin>`_, and we ultimately believe they are an easy way to assure license integrity from the project and copyright compliance from developers.

Compliance is simple and consists of making commit messages like so:

.. code-block:: text

	This is the commit message

	Signed-off-by: First M. Last <first.last@someurl.org>

Tests
-----

Our check is `Sphinx <https://www.sphinx-doc.org/>`_ with warnings treated as errors, which catches broken cross-references and malformed tables. Run it before you open a pull request:

.. code-block:: shell

	sphinx-build -W -b dirhtml docs/man/source docs/man/build/dirhtml

Pull Requests
-------------

1. Search our repository for open or closed `Pull Requests <https://github.com/feamsr00/ds8-server-rack-manual/pulls>`_ that relate to your submission, *first*. You don't want to duplicate efforts.
2. Fork the project
3. Create your feature branch (``git checkout -b feat/amazing_feature``)
4. Commit your changes (``git commit -m 'feat: add amazing_feature'``) This project uses `conventional commits <https://www.conventionalcommits.org>`_, so please follow the specification in your commit messages.
5. Push to the branch (``git push origin feat/amazing_feature``)
6. `Open a Pull Request <https://github.com/feamsr00/ds8-server-rack-manual/compare?expand=1>`_

Release Builds
--------------

Builds are automatically built via CI with `Read the Docs <https://about.readthedocs.com>`_. Tag each edition with the mod version it describes, such as ``v5.12.7``, so that readers on an older version can still find their manual. Tag a later revision for the same mod version as a post-release, such as ``v5.12.7.post1``, so that the site's stable version picks it up.
