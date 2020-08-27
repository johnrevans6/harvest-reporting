import os
import unittest
import unittest.mock

from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.secretmanager_v1.types import (AccessSecretVersionResponse,
                                                 SecretPayload)

import reporting.notifications

class TestNotificationManager(unittest.TestCase):
    def test_send(self):
        pass

    def _test_send_customer_notifications(self):
        pass

    def _test_send_global_notifications(self):
        pass

    def _test_senf_exception_channels(self):
        pass

    def _test_send_slack_channels(self):
        pass

    def _test_send_teams_channels(self):
        pass

    def _test_send_email_channels(self):
        pass

    def _test_get_slack_payload(self):
        pass

    def _test_get_teams_sections(self):
        pass

    def _test_teams_exception_sections(self):
        pass

    def _test_get_email_payload(self):
        pass

    def _test_get_color_code_for_utilization(self):
        pass