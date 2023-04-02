import dataclasses
import json
import os

from datetime import datetime
from dataclasses import dataclass


@dataclass
class Comment:
	date: str
	text: str


# https://stackoverflow.com/questions/51286748/make-the-python-json-encoder-support-pythons-new-dataclasses
class Encoder(json.JSONEncoder):
		def default(self, o):
			if dataclasses.is_dataclass(o):
				return dataclasses.asdict(o)

			return super().default(o)


class CommentsDatabase:
	def __init__(self, file_path: str):
		# TODO: do not keep all comments in memory (load + security)
		self._data = list()

		self._file_path = file_path
		self._date_format = '%Y-%m-%d %H:%M:%S'

		self._load()

	def save_comment(self, text: str):
		date = datetime.now().strftime(self._date_format)
		self._data.append(Comment(date=date, text=text))

		# Can be saved at intervals
		self._save()

	@property
	def comments(self):
		return self._data

	def _load(self):
		if not os.path.isfile(self._file_path):
			return

		raw_data = json.loads(open(self._file_path).read())
		self._data = [
			Comment(date=c['date'], text=c['text']) for c in raw_data
		]  # TODO: decode to dataclass like encode?

	def _save(self):
		# TODO: append not rewrite
		with open(self._file_path, 'w') as f:
			f.write(json.dumps(self._data, cls=Encoder))
