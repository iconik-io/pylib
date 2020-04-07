#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2020-04-07 18:02:26 +0100 (Tue, 07 Apr 2020)
#
#  https://github.com/harisekhon/pylib
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback
#  to help improve or steer this or other code I publish
#
#  https://www.linkedin.com/in/harisekhon
#

"""
# ============================================================================ #
#                   PyUnit Tests for HariSekhon.StatusNagiosPlugin
# ============================================================================ #
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys
import unittest
libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(libdir)
# pylint: disable=wrong-import-position
from harisekhon.utils import log
from harisekhon.nagiosplugin import StatusNagiosPlugin

class StatusNagiosPluginTester(unittest.TestCase):

    # must prefix with test_ in order for the tests to be called

    # Not using assertRaises >= 2.7 and maintaining compatibility with Python 2.6 servers

    class SubStatusNagiosPlugin(StatusNagiosPlugin):
        def __init__(self):
            # Python 2.x
            #StatusNagiosPlugin.__init__(self)
            super(StatusNagiosPluginTester.SubStatusNagiosPlugin, self).__init__()
            # Python 3.x
            # super().__init__()
            self.name = 'test'
            self.default_port = 80

    #def setUp(self):
    #    self.plugin = self.SubStatusNagiosPlugin()

    def test_exit_0(self):
        plugin = self.SubStatusNagiosPlugin()
        plugin.get_status = lambda: 'pretending to be OK'
        try:
            plugin.main()
            raise Exception('StatusSub plugin failed to terminate')
        except SystemExit as _:
            if _.code != 0:
                raise Exception('StatusNagiosPlugin failed to exit OK (0), got exit code {0} instead'
                                .format(_.code))

    def test_plugin_abstract(self):  # pylint: disable=no-self-use
        try:
            StatusNagiosPlugin()  # pylint: disable=abstract-class-instantiated
            #raise Exception('failed to raise a TypeError when attempting to instantiate abstract class ' +
            #                'StatusNagiosPlugin')
        #except TypeError:
        except SystemExit as _:
            if _.code != 0:
                raise Exception('StatusNagiosPlugin failed to exit UNKNOWN (3), got exit code {0} instead'
                                .format(_.code))


def main():
    # increase the verbosity
    # verbosity Python >= 2.7
    #unittest.main(verbosity=2)
    log.setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(StatusNagiosPluginTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
