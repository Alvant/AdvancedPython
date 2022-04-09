import json
import os
from datetime import datetime


class JsonDatabase:
	def __init__(self, file_path: str):
		self._data = list()
		self._file_path = file_path

		self._load()

	def save_comment(self, comment: str):
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		# TODO: Comment as dataclass
		self._data.append(
			(comment, time)
		)

		# Can be saved at intervals
		self._save()

	@property
	def comments(self):
		return self._data

	def _load(self):
		if not os.path.isfile(self._file_path):
			return

		self._data = json.loads(open(self._file_path).read())

	def _save(self):
		with open(self._file_path, 'w') as f:
			f.write(json.dumps(self._data))
