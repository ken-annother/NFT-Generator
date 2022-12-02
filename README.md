# 数字藏品NFT生成工具

# 1. 安装

安装好 python3 环境。

执行如下命令

    pip install -r requirements.txt

# 2. 运行

(1) 用数字藏品的名称建立文件夹并放在assets目录下，如 HipsterCats， HipsterDogs

(2) 将各个组件按照图层从里到外的顺序依次编号，建立对应的组件目录

(3) 将同一组件下的部件按照顺序编号放在对应的组件目录下

(4) 修改 startup.py 下 start_gen 函数的参数

    
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
        pass

