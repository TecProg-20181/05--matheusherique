import pytest
import cStringIO
import sys
from diskspace.diskspace import *
LARGEST_SIZE = 6
TOTAL_SIZE = 4

class Test(object):
    def test_subprocess_check_output(self):
        command_user = 'du'
        result_of_du = subprocess.check_output(command_user)
        result = subprocess_check_output(command_user)
        assert result_of_du == result

    def test_bytes_to_readable(self):
        # test case for block size of B
        result = '512.00B'
        blocks = 1
        assert bytes_to_readable(blocks) == result
        # test case for block size of Kb
        blocks = 1024
        result = '512.00Kb'
        assert bytes_to_readable(blocks) == result
        # test case for block size of Mb
        blocks = 1048576
        result = '512.00Mb'
        assert bytes_to_readable(blocks) == result
        # test case for block size of Gb
        blocks = 1073750000
        result = '512.00Gb'
        assert bytes_to_readable(blocks) == result
        # test case for block size of Tb
        blocks = 1099504999000
        result = '512.00Tb'
        assert bytes_to_readable(blocks) == result


    def test_print_tree(self):
        fulldepth = 0
        path = '/home/teste'
        path = path.split("/")[-1]
        result = '{}{}'.format('   '*fulldepth, os.path.basename(path))
        assert result == path

    def test_show_space_list(self):
        assert show_space_list() == None
