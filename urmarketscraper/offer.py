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
        if self.level_price_dict is not None and not self.is_level_price_dict_sorted():
            self.sort_level_price_dict()

    def __init__(self, id=0, level_price_dict=None):
        self.id = id
        self.level_price_dict = level_price_dict

    # Sorts by lowest price first
    def sort_level_price_dict(self):
        if self.level_price_dict is not None:
            self.level_price_dict = {k: v for k, v in sorted(self.level_price_dict.items(),
                                                             key=lambda item: item[1])}

    def is_level_price_dict_sorted(self):
        values = list(self.level_price_dict.values())
        return all(values[i] <= values[i + 1] for i in range(len(values) - 1))

    def get_min_price(self):
        return self.level_price_dict[self.get_min_level()]

    def get_min_level(self):
        return next(iter(self.level_price_dict))

    def get_rel_price(self, target_level):
        return self.level_price_dict.get(int(target_level), self.get_min_price())

    def get_rel_level(self, target_level):
        return target_level if int(target_level) in self.level_price_dict \
            else self.get_min_level()