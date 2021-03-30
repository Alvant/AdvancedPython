import os
import json

from typing import Dict


class BaseDatabase:
    def save(self, username: str, password: int) -> None:
        raise NotImplementedError()

    def find(self, username: str) -> Dict:
        raise NotImplementedError()


class JsonDatabase(BaseDatabase):
    def __init__(self, path: str):
        self._path = path

        os.makedirs(
            os.path.dirname(self._path),
            exist_ok=True,
        )

    def save(self, username: str, password: int) -> None:
        with open(self._path, 'a') as f:
            f.write(
                json.dumps({'username': username, 'password': password}) + '\n'
            )

    def find(self, username: str) -> Dict:
        lines = open(self._path).readlines()

        for line in lines:
            user = json.loads(line)

            if user['username'] == username:
                return user

        raise KeyError(f'No such user in the DB "{username}"!')


class SqlDatabase(BaseDatabase):
    pass
