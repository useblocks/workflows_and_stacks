Test results in Sphinx
======================

.. workflow:: [[copy('section_name')]]
   :id: TESTS2SPHINX

   Goal
   ----
   Get test results of a test-framework like pycharm into :need:`SPHINX`.

   Solution
   --------
   Store results in a junit-based xml file and import it via sphinx-test-report.

   Steps
   -----

   #. :need:`SPHINX_INSTALL`
   #. Install sphinx-test-reports::

         pip install sphinx-test-reports
   #. :need:`SPHINX_EXTENSION`
      Add ``sphinxcontrib-test-reports``
   #. On any page, import the exported junit file via::

         .. test_report: my_junit_file
   #. :need:`SPHINX_BUILD_HTML`
