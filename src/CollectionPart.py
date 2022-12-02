from CollectionSpecies import CollectionSpecies


class CollectionPart:
    """
    数字藏品组件
    """
    _name = None
    _species_list: [CollectionSpecies] = []

    def __init__(self, name: str, species_list: [CollectionSpecies]):
        """
        构造函数
        :param name: 部件名
        :param species_list: 部件包含的不同风格组件列表
        """
        self._name = name
        self._species_list = species_list

    def get_name(self):
        """
        获取部件名
        :return:
        """
        return self._name

    def get_kinds_count(self):
        """
        获取组件数量
        :return:
        """
        return len(self._species_list)

    def get_species(self, idx):
        """
        获取对应的组件
        :param idx:
        :return:
        """
        return self._species_list[idx]

    def get_species_list(self):
        """
        获取包含的组件列表
        :return:
        """
        return self._species_list
