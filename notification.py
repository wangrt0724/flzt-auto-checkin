import requests
from env import SERVER_KEY
from loguru import logger


class Notification:
    def notify(self):
        pass


class ServerChanNotification(Notification):
    def __init__(self, title, content):
        super().__init__()
        self.title = title
        self.content = content

    def notify(self):
        if SERVER_KEY:
            payload = {'title': self.title, 'desp': self.content}
            requests.post(
                f'https://sctapi.ftqq.com/{SERVER_KEY}.send', data=payload)
        else:
            logger.warning('未设置 SERVER_KEY')
