import typing
import json
from aiogram.dispatcher.storage import BaseStorage
from utils.db_api.database import DbContext


class DbStorage(BaseStorage):
    def __init__(self):
        self.db = DbContext()

    async def close(self):
        self.db.close()
        pass

    async def wait_closed(self):
        pass

    async def get_state(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                        default: typing.Optional[str] = None) -> typing.Optional[str]:
        _user = self.db.get_user(user=user, chat=chat)
        if _user.state == '' or _user.state is None:
            return default
        return _user.state

    async def get_data(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                       default: typing.Optional[typing.Dict] = None) -> typing.Dict:
        _user = self.db.get_user(user=user, chat=chat)
        if _user.data == '' or _user.data is None:
            return default
        return _user.data
        pass

    async def set_state(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                        state: typing.Optional[typing.AnyStr] = None):
        _user = self.db.get_user(user=user, chat=chat)
        _user.state = self.resolve_state(state)
        self.db.update_user(_user)
        pass

    async def set_data(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                       data: typing.Dict = None):
        _user = self.db.get_user(user=user, chat=chat)
        _user.data = json.dumps(data)
        self.db.update_user(_user)
        pass

    async def update_data(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                          data: typing.Dict = None, **kwargs):
        _user = self.db.get_user(user=user, chat=chat)
        _user.data = json.dumps(data)
        self.db.update_user(_user)
        pass

    async def get_bucket(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                         default: typing.Optional[dict] = None) -> typing.Dict:
        pass

    async def set_bucket(self, *, chat: typing.Union[str, int, None] = None, user: typing.Union[str, int, None] = None,
                         bucket: typing.Dict = None):
        pass

    async def update_bucket(self, *, chat: typing.Union[str, int, None] = None,
                            user: typing.Union[str, int, None] = None, bucket: typing.Dict = None, **kwargs):
        pass