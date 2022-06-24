from abc import ABC, abstractmethod


class CompanyABC(ABC):
    @abstractmethod
    def add_data(self, args):
        pass

    @abstractmethod
    def get_data(self, args):
        pass

    @abstractmethod
    def update_data(self, args):
        pass

    @abstractmethod
    def del_data(self, args):
        pass
    
