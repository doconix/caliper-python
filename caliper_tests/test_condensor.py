# -*- coding: utf-8 -*-
# Caliper-python testing package (testing condensor cases)
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from future.utils import with_metaclass
from builtins import *

import sys, os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper
import caliper_tests.util as util


class AnnotationProfile(unittest.TestCase):
    def setUp(self):
        pass
    
    def testBookmarkAnnotationEvent(self):
        fixture = 'caliperEventAnnotationBookmarked'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
    
    def testHighlightAnnotationEvent(self):
        fixture = 'caliperEventAnnotationHighlighted'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testSharedAnnotationEvent(self):
        fixture = 'caliperEventAnnotationShared'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testTagAnnotationEvent(self):
        fixture = 'caliperEventAnnotationTagged'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


class AssessmentProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssessmentEvent(self):
        fixture = 'caliperEventAssessmentStarted'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testAssessmentItemStartedEvent(self):
        fixture = 'caliperEventAssessmentItemStarted'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testAssessmentItemCompletedEvent(self):
        fixture = 'caliperEventAssessmentItemCompleted'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


class AssignableProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssignableEvent(self):
        fixture = 'caliperEventAssignableActivated'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

class MediaProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testVideoMediaEvent(self):
        fixture = 'caliperEventMediaPausedVideo'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

class OutcomeProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssessmentOutcomeEvent(self):
        fixture = 'caliperEventOutcomeGraded'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
        
class ReadingProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testNavigationEvent(self):
        fixture = 'caliperEventNavigationNavigatedTo'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
    
    def testViewEvent(self):
        fixture = 'caliperEventViewViewed'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

class SessionProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testSessionLoginEvent(self):
        fixture = 'caliperEventSessionLoggedIn'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
    
    def testSessionLogoutEvent(self):
        fixture = 'caliperEventSessionLoggedOut'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
    
    def testSessionTimeoutEvent(self):
        fixture = 'caliperEventSessionTimedOut'
        self.assertEqual(util.rebuild_event(fixture), util.get_fixture(fixture))
        self.assertEqual(util.rebuild_event(fixture, thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))
        
if __name__ == '__main__':
    unittest.main()

