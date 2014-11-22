# -*- coding: utf-8 -*-
# Caliper-python testing package (testing util functions)
#
# Copyright (c) 2014 IMS Global Learning Consortium, Inc. All Rights Reserved.
# Trademark Information- http://www.imsglobal.org/copyright.html

# IMS Global Caliper Analytics™ APIs are publicly licensed as Open Source
# Software via GNU General Public License version 3.0 GPL v3. This license
# contains terms incompatible with use in closed-source software including a
# copyleft provision.

# IMS Global also makes available an Alternative License based on the GNU Lesser
# General Public License. LGPL v3 Licensees (via the Alternative License) are
# required to be IMS Global members. Membership in IMS is a commitment by a
# supplier to the IMS community for ongoing support for achieving "plug and play"
# integration.  IMS Membership dues pay for ongoing maintenance for the
# Alternative License to be applicable to updates to the Caliper Analytics
# APIs. The rationale for this dual-license approach and membership component is
# to help assure a requisite level of ongoing development, project management,
# and support for the software.

# Licensees of IMS Global Caliper Analytics APIs are strongly encouraged to
# become active contributors to the Caliper Analytics project and other projects
# within IMS Global. Prospective licensees should understand that their initial
# base contribution and ongoing membership fees are insufficient to fully fund
# the ongoing development and maintenance of Caliper APIs and that voluntary
# contributions are the primary "fuel" ensuring any open source project's
# viability. Contributions can include development, bug fixing, bug reporting,
# performance analysis, and other aspects of the overall development process.

# Contributor status at the "github" level will be individual-based. Contributors
# will need to sign an IMS Global Contributor License Agreement (CLA) that grants
# IMS Global a license to contributions.

# If you are interested in licensing the IMS Global Caliper Analytics APIs please
# email licenses@imsglobal.org

import sys, os
sys.path.insert(0, os.path.abspath('..'))
import caliper, caliper_tests

import json


_LMT = 1402965614516
_SAT = 1402965614516

## general state and utility functions used by many tests
def getTestingOptions():
    return caliper.base.HttpOptions(
        host='http://httpbin.org/post',
        api_key='6xp7jKrOSOWOgy3acxHFWA')

def getFixtureStr(fixture=None):
    return json.dumps(json.loads(fixture), sort_keys=True)


## build a test learning context
def buildLearningContext():
    return caliper.entities.LearningContext(
        agent = caliper.entities.Person(
            entity_id = 'https://some-university.edu/user/554433',
            lastModifiedTime = _LMT
            ),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://github.com/readium/readium-js-viewer',
            name = 'Readium',
            lastModifiedTime = _LMT
            ),
        lisOrganization = caliper.entities.CourseSection(
            entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
            semester = 'Spring-2014',
            courseNumber = 'AmRev-101',
            label = 'Am Rev 101',
            name = 'American Revolution 101',
            lastModifiedTime = _LMT
            )
        )

## Reading Profile related funcs
def buildReadingProfile(learning_context=buildLearningContext()):
    return caliper.profiles.ReadingProfile(
        learningContext = learning_context,
        reading = caliper.entities.EpubVolume(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)',
            name = 'The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)',
            lastModifiedTime = _LMT
            ),
        )

def navigateToReadingTarget(reading_profile=buildReadingProfile()):
    reading_profile.add_action(caliper.actions.Action.ReadingActions['NAVIGATED_TO'])
    reading_profile.add_target(
        new_target = caliper.entities.Frame(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
            name = 'Key Figures: George Washington',
            partOf = reading_profile.reading,
            lastModifiedTime = _LMT,
            index = 1
            )
        )
    reading_profile.add_fromResource(
        new_from_resource = caliper.entities.WebPage(
            entity_id = 'AmRev-101-landingPage',
            name = 'American Revolution 101 Landing Page',
            partOf = reading_profile.learningContext.lisOrganization,
            lastModifiedTime = _LMT
            )
        )
    return reading_profile
    
def viewReadingTarget(reading_profile=buildReadingProfile()):
    reading_profile.add_action(caliper.actions.Action.ReadingActions['VIEWED'])
    reading_profile.add_target(
        new_target = caliper.entities.Frame(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
            name = 'Key Figures: George Washington',
            partOf = reading_profile.reading,
            lastModifiedTime = _LMT,
            index = 1
            )
        )
    return reading_profile

def buildNavigationEvent(reading_profile=navigateToReadingTarget()):
    return caliper.events.NavigationEvent(
        action = reading_profile.actions[-1],
        edApp = reading_profile.learningContext.edApp,
        group = reading_profile.learningContext.lisOrganization,
        actor = reading_profile.learningContext.agent,
        event_object = reading_profile.reading,
        navigatedFrom = reading_profile.fromResources[-1],
        target = reading_profile.targets[-1],
        startedAtTime = _SAT
        )
    
def buildViewEvent(reading_profile=viewReadingTarget()):
    return caliper.events.ViewEvent(
        action = reading_profile.actions[-1],
        edApp = reading_profile.learningContext.edApp,
        group = reading_profile.learningContext.lisOrganization,
        actor = reading_profile.learningContext.agent,
        event_object = reading_profile.reading,
        target = reading_profile.targets[-1],
        startedAtTime = _SAT
        )

