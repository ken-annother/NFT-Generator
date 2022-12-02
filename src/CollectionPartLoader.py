import os

from CollectionPart import CollectionPart
from CollectionSpecies import CollectionSpecies


class CollectionPartLoader:

    def __init__(self):
        pass

    @staticmethod
    def load(resource_directory: str):
        """
        加载目录
        :param resource_directory:
        :return:
        """
        category_list = os.listdir(resource_directory)
        category_list.sort()

        parts: [CollectionPart] = []

        for cate_cat in category_list:
            species_: [CollectionSpecies] = []

            # 获取部件的种类
            species_list = os.listdir(resource_directory + os.path.sep + cate_cat)
            species_list.sort()
            for species in species_list:
                cs_ = CollectionSpecies(species, resource_directory + os.path.sep + cate_cat + os.path.sep + species)
                species_.append(cs_)

            # 新增part
            p = CollectionPart(cate_cat, species_)
            parts.append(p)
        return parts
