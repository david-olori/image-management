from src.core.category import Category


class Covid(Category):
    def __init__(self, base_path):
        super().__init__('Normal', base_path + '/COVID', base_path + '/COVID.metadata.csv')
