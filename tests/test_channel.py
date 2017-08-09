import sys

if sys.version_info[0] == 2:
    import mock
else:
    from unittest import mock
from unittest import TestCase
from uuid import uuid4

from message_api.channel import MessageApi

class TestChannelCreate(TestCase):
    def setUp(self):
        self.project_id = str(uuid4().hex)
        self.api_key = str(uuid4().hex)
        self.message_api = MessageApi(
            project_id=self.project_id,
            api_key=self.api_key
        )

    def test_channel_create_success(self):
        channel_token = str(uuid4().hex)
        self.message_api._send_request = mock.Mock()
        self.message_api._send_request.return_value = {
            "token":  channel_token
        }
        client_id = str(uuid4().hex)
        result = self.message_api.create_channel(client_id)
        self.assertEqual(channel_token, result)
        params = {
            "project_id": self.project_id
        }
        body = {
            "channel_id": client_id
        }

        self.message_api._send_request.assert_called_once_with(
            "post",
            params=params,
            json=body
        )

    def test_send_message_success(self):
        self.message_api._send_request = mock.Mock()
        client_id = str(uuid4().hex)
        message = str(uuid4().hex)
        self.message_api.send_message(client_id, message)
        params = {
            "project_id": self.project_id
        }
        body = {
            "channel_id": client_id,
            "message": message
        }

        self.message_api._send_request.assert_called_once_with(
            "post",
            params=params,
            json=body
        )