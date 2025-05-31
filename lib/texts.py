from typing import List, Dict
import random
import json
from dataclasses import asdict
from lib.meta import Manager
from lib.exceptions import ManagerReadOnlyAttributteError
from lib.types import Text, TextT

_adjectives = [
    "страшний",
    "неперевершениий",
    "анімє",
    "засмаглива",
    "аборигенний",
    "смачний",
    "антропометричний",
    "щільний",
    "гейський",
    "ангорський",
    "аґро",
    "няшка",
    "вумен",
    "мен",
    "звільненний",
    "недоторканний",
    "на Бахмут",
    "на Авдіївку",
    "зековський",
    "кліматичний",
]
_nouns = [
    "гей",
    "порося",
    "кішечка",
    "мама",
    "юра",
    "карев",
    "саня",
    "азов",
    "камера",
    "семпай",
    "с-300",
    "крим наш",
    "геноцид",
    "бандера",
    "придатний на війну",
    "чмобік",
    "олех",
    "мобілка",
    "світ",
    "коханий",
]


def get_random_joke():
    joke = random.choice(TextManager().jokes)
    return joke.text


def get_random_quote():
    quote = random.choice(TextManager().quotes)
    return quote.text


def generate_custom_name():
    adjective = random.choice(_adjectives)
    noun = random.choice(
        _nouns,
    )
    return f"{adjective} {noun}"


class TextManager(Manager):
    _texts: List[Text]
    _raw_texts: Dict

    def __init__(self, *, config=None):
        super().__init__(config=config)
        self.__texts_config_path = config.pop("texts_path")
        # end
        self._read_texts()

    @property
    def jokes(self):
        """The jokes property."""
        jokes = [joke for joke in self._texts if joke.type == "joke"]
        return jokes

    @jokes.setter
    def set_jokes(self, value):
        raise ManagerReadOnlyAttributteError(
            "Writing to read only attribute 'jokes' is not allowed"
        )

    @property
    def quotes(self):
        """The jokes property."""
        quotes = [quote for quote in self._texts if quote.type == "quote"]
        return quotes

    @jokes.setter
    def set_quotes(self, value):
        raise ManagerReadOnlyAttributteError(
            "Writing to read only attribute 'quotes' is not allowed"
        )

    def get_text(self, text_id: int):
        text = self._raw_texts[text_id]
        return Text(**text)

    def add_text(self, text: str, t_type: TextT):
        max_id = int(max(self._raw_texts.keys()))
        new_id = max_id + 1
        text_dc = Text(
            text=text,
            type=t_type,
            id=new_id,
        )
        self._texts.append(text_dc)
        self._raw_texts[new_id] = asdict(text_dc)
        self._write_texts()
        self._read_texts()

    def remove_text(self, text_id: int):
        del self._raw_texts[text_id]
        self._write_texts()
        self._read_texts()

    def _read_texts(self):
        """Initialises self._texts and self._raw_texts in place"""
        with open(self.__texts_config_path, "r") as members_file:
            texts_mapping = json.load(members_file)

        texts_dcs = []
        for text_id in texts_mapping:
            texts_dcs.append(Text(**texts_mapping[text_id]))
        self._texts = texts_dcs
        self._raw_texts = texts_mapping

    def _write_texts(self):
        with open(self.__texts_config_path, "w") as file:
            file.write(json.dumps(self._raw_texts))

