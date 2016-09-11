from sequana.scripts import coverage
from nose.plugins.attrib import attr
from sequana import sequana_data

@attr("skip")
class TestPipeline(object):

    @attr("skip")
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        klass.prog = "sequana_coverage"
        klass.params = {'prog': klass.prog}

    @attr("skip")
    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""
        import os
        # local nosetests execution
        try:os.remove('README')
        except:pass
        try:os.remove('quality.rules')
        except:pass
        try:os.remove('config.yaml')
        except:pass


    @attr("skip")
    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        pass
    @attr("skip")
    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def _test_version(self):
        coverage.main([self.prog, '--version'])

    def test_help(self):
        try:
            coverage.main([self.prog, '--help'])
            assert False
        except SystemExit:
            pass
        else:
            raise Exception

    def _test_input(self):
        filename = sequana_data('virus.bed', 'data')
        reference = sequana_data('tofill.fa', 'data')
        coverage.main([self.prog, '-i', filename, "-o", "-r", reference])


