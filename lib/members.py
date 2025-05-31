import json

from lib.meta import Manager


class MembersManager(Manager):
    member_ids = set()

    def __init__(self, *, config=None):
        super().__init__(config=config)
        self.__members_config_path = config.pop("members_path")
        self._read_members()

    def update_member_id(self, member_id):
        if member_id not in self.member_ids:
            self.member_ids.add(member_id)
            with open(self.__members_config_path, "w") as file:
                file.write(json.dumps(list(self.member_ids)))

    def _read_members(self):
        """Initialises self.member_ids in place"""
        with open(self.__members_config_path, "r") as members_file:
            members_list = json.load(members_file)
        self.member_ids = set(members_list)
