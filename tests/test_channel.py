import sys

if sys.version_info[0] == 2:
    import mock
else:
    from unittest import mock
from unittest import TestCase
from uuid import uuid4

import vcr

from message_api.channel import MessageApi

class TestChannelCreate(TestCase):
    def setUp(self):
        self.project_id = str(uuid4().hex)
        self.api_key = str(uuid4().hex)
        self.message_api = MessageApi(
            project_id=self.project_id,
            api_key=self.api_key
        )
        self.api_url = self.message_api.api_url

    def test_channel_create_success(self):
        channel_token = str(uuid4().hex)
        self.message_api._send_request = mock.Mock()
        self.message_api._send_request.return_value = {
            "token":  channel_token
        }
        client_id = str(uuid4().hex)
        result = self.message_api.create_channel(client_id)
        self.assertEqual(channel_token, result)
        body = {
            "channel_id": client_id
        }
        url = self.api_url + "/projects/" + self.project_id + "/create_channel"

        self.message_api._send_request.assert_called_once_with(
            "post",
            url,
            json=body
        )

    @vcr.use_cassette('tests/vcr/test_create_channel.yaml', record_mode="once")
    def test_create_channel_vcr(self):
        client_id = "test-channel"
        message_api = MessageApi(
            project_id="test",
            api_key="1234"
        )
        result = message_api.create_channel(client_id)

    def test_send_message_success(self):
        self.message_api._send_request = mock.Mock()
        client_id = str(uuid4().hex)
        message = str(uuid4().hex)
        self.message_api.send_message(client_id, message)
        body = {
            "channel_id": client_id,
            "message": message
        }
        url = self.api_url + "/projects/" + self.project_id + "/send_message"

        self.message_api._send_request.assert_called_once_with(
            "post",
            url,
            json=body
        )

