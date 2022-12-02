import json
import os
import random

from PIL import Image

from CollectionPart import CollectionPart


class CollectionGenerator:
    """
    数字藏品生成器
    """
    _name: str = None
    _limit = None
    _size: tuple = (1240, 1754)
    _parts: [CollectionPart] = []
    _collections = []

    def __init__(self, name: str, size: tuple, parts: [CollectionPart], limit=None):
        """
        构造函数
        :param name: 藏品名
        :param size: 藏品图片的大小
        :param parts: 藏品的部件列表
        :param limit: 藏品的数量，如果为None表示生成全局的排列组合
        """
        self._name = name
        self._size = size
        self._parts = parts
        self._limit = limit
        self._prepare()

    def _prepare(self):
        """
        初始化藏品列表
        :return:
        """
        full_collection_list = self._prepare_gen_full_collection_list()
        self._prepare_collection_list(full_collection_list)

    def _prepare_gen_full_collection_list(self):
        """
        预生成排列组合列表
        :return:
        """
        container = [j for j in self._collections]
        for cp in self._parts:
            # 获取部件种类的个数
            new_collections = []
            for s_tmp in cp.get_species_list():
                if len(container) != 0:
                    for n in container:
                        new_n = [k for k in n]
                        new_n.append(s_tmp)
                        new_collections.append(new_n)
                else:
                    new_collections.append([s_tmp])
            container = new_collections
        return container

    def _prepare_collection_list(self, container: list):
        """
        做初步筛选和生成清单信息
        :param container: 全序列的藏品列表
        :return:
        """
        if len(container) <= self._limit:
            self._collections = container
        else:
            random.shuffle(container)
            self._collections = container[:self._limit]

    def _prepare_collection_list_manifest_info(self, output_directory):
        """
        生成数字藏品清单信息
        :param output_directory: 输出目录
        :return:
        """
        output_directory_app = output_directory + os.sep + self._name
        if not os.path.exists(output_directory_app):
            os.makedirs(output_directory_app)

        collection_info = []
        for i in range(len(self._collections)):
            c = self._collections[i]
            collection_info.append({
                'index': i,
                'file_name': str(i) + '.png',
                'file_path': output_directory_app + os.sep + str(i) + '.png',
                'parts': [
                    k.get_file_path() for k in c
                ]
            })

        with open(output_directory_app + os.sep + 'manifest.json', 'w+') as f:
            f.write(json.dumps(collection_info, indent=2))
        return collection_info

    def generate(self, output_directory):
        """
        生成藏品到指定的目录
        :param output_directory: 输出目录
        :return:
        """
        collection_info = self._prepare_collection_list_manifest_info(output_directory)
        for i in range(len(collection_info)):
            c = collection_info[i]
            final = Image.new('RGBA', self._size)
            for species_file_path in c['parts']:
                layer = Image.open(species_file_path).convert('RGBA')
                final = Image.alpha_composite(final, layer)
            final = final.convert('RGB')
            final.save(c['file_path'])
