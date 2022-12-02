class CollectionSpecies:
    """
    藏品组件的对应的图片
    """
    _name = None
    _file_path = None

    def __init__(self, name: str, file_path: str):
        """
        构造函数
        :param name: 组件名
        :param file_path: 组件的路径
        """
        self._name = name
        self._file_path = file_path

    def get_name(self):
        """
        组件名
        :return:
        """
        return self._name

    def get_file_path(self):
        """
        组件的路径
        :return:
        """
        return self._file_path
