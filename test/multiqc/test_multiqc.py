
from sequana import sequana_data
from multiqc.utils import report



try:
    # Since sept 2017 and a bioconda travis integrationupdate, 
    # this test fails due to an error in spectra/colormath:
    #   self.conversion_graph.add_edge(start_type, target_type,
    #   {'conversion_function': conversion_function})
    #E   TypeError: add_edge() takes 3 positional arguments but 4 were given
    from sequana.multiqc import pacbio_qc, quality_control, coverage

    def test_pacbio():
        # When calling multiqc on the command line, it scans the directory
        # to identify the files to include in the singleton "report"; 
        # HEre, because we do not use the standalone app, the report.files is empty
        # so we populate it by hand. Moreovoer, the path are altered to look for
        # files in the sequana/resources/testing directory instead of local
        # directory. Because we populate the report.files ourself, we can put
        # whatever name except it the MultiqcModule expects a specific name

        report.files = {"sequana/pacbio_qc":
            [{'filesize': 5913, 'fn': sequana_data('summary_pacbio_qc1.json'), 'root': '.'},
             {'filesize': 5731, 'fn': sequana_data('summary_pacbio_qc2.json'), 'root': '.'},
             {'filesize': 5820, 'fn': sequana_data('summary_pacbio_qc3.json'), 'root': '.'}]
        }
        pacbio_qc.MultiqcModule()

    def test_quality_control():
        report.files = {"sequana/quality_control":
            [ { 'fn': sequana_data('summary_qc.json'), 'root': '.'}]
        }
        quality_control.MultiqcModule()


    def test_coverage():
        report.files = {"sequana/coverage":
            [ { 'fn': sequana_data('summary_coverage1.json'), 'root': '.'},
              { 'fn': sequana_data('summary_coverage1.json'), 'root': '.'}]
        }
        coverage.MultiqcModule()

except TypeError:
    pass
except:
    raise IOError
