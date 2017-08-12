# message-api-python

[![Build Status](https://travis-ci.org/message-api/message-api-python.svg?branch=master)](https://travis-ci.org/message-api/message-api-python)  


```python
from message_api import channel

channel.setup("<project_id>", "<api_key>")

token = channel.create_channel("channel_1")

channel.send_message("channel_1", "message")
```
