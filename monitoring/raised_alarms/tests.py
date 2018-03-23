#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from django.core import urlresolvers
from mock import patch, call  # noqa

from monitoring.test import helpers
from monitoring.raised_alarms import constants


INDEX_URL = urlresolvers.reverse(
    constants.URL_PREFIX + 'index')
ALARMS_URL_BY_DIMENSION = urlresolvers.reverse(
    constants.URL_PREFIX + 'alarm', args=('nova',))
ALARMS_URL = urlresolvers.reverse(
    constants.URL_PREFIX + 'alarm', args=('all',))


class AlarmsTest(helpers.TestCase):
    def test_alarms_get_by_dimension(self):
        with patch('monitoring.api.monitor', **{
            'spec_set': ['alarm_list_by_dimension'],
            'alarm_list_by_dimension.return_value': [],
        }) as mock:
            res = self.client.get(ALARMS_URL_BY_DIMENSION)
            self.assertEqual(mock.alarm_list_by_dimension.call_count, 2)

        self.assertTemplateUsed(
            res, 'monitoring/alarms/alarm.html')

    def test_alarms_get(self):
        with patch('monitoring.api.monitor', **{
            'spec_set': ['alarm_list'],
            'alarm_list.return_value': [],
        }) as mock:
            res = self.client.get(ALARMS_URL)
            self.assertEqual(mock.alarm_list.call_count, 2)

        self.assertTemplateUsed(
            res, 'monitoring/alarms/alarm.html')
