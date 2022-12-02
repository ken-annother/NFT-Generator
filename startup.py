from src import CollectionGenerator
from src import CollectionPartLoader
import time


def start_gen(collection_name: str, resource_directory: str, output_directory: str, collection_size: tuple, limit=None):
    """
    执行生成步骤
    :param collection_name: 数字藏品名
    :param resource_directory: 原始资源目录
    :param output_directory: 输出目录
    :param collection_size: 数字藏品的分辨率
    :param limit: 生成的数量
    :return:
    """
    # 加载组件
    parts = CollectionPartLoader.load(resource_directory)
    # 初始化数字藏品生成器
    collection_generator = CollectionGenerator(collection_name, collection_size, parts, limit)
    # 生成并输出到对应的目录
    collection_generator.generate(output_directory)


if __name__ == '__main__':
    start_time = time.time()
    start_gen('HipsterDogs', 'assets/HipsterDogs', 'output', collection_size=(490, 740), limit=100)
    end_time = time.time()
    print("cost time", end_time - start_time)
