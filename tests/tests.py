import pytest
from diskspace.diskspace import *

class Test(object):
    def test_subprocess_check_output(self):
        command_user = 'du'
        result_of_du = subprocess.check_output(command_user)
        result = subprocess_check_output(command_user)
        assert result_of_du == result

    def test_bytes_to_readable(self):
        result = '0.00B'
        blocks = 0
        assert bytes_to_readable(blocks) == result

    def test_print_tree(self):
        fulldepth = 0
        path = '/home/teste'.split("/")[-1]
        result = '{}{}'.format('   '*fulldepth, os.path.basename(path))
        assert result == path
