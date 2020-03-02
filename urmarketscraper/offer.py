class Offer:
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = int(id)

    @property
    def level_price_dict(self):
        return self.__level_price_dict

    @level_price_dict.setter
    def level_price_dict(self, lpd):
        self.__level_price_dict = lpd if isinstance(lpd, dict) else None

    def __init__(self, id, level_price_dict):
        self.id = id
        self.level_price_dict = level_price_dict
        if hasattr(self, 'level_price_dict'):
            self.sort_level_price_dict()

    def sort_level_price_dict(self):
        self.level_price_dict = {k: v for k, v in sorted(self.level_price_dict.items(),
                                                         key=lambda item: item[1])}

    def get_min_price(self):
        return self.level_price_dict[self.get_min_level()]

    def get_min_level(self):
        return next(iter(self.level_price_dict))

    def get_rel_price(self, target_level):
        return self.level_price_dict.get(target_level, self.get_min_price())

    def get_rel_level(self, target_level):
        return target_level if target_level in self.level_price_dict \
            else self.get_min_level()