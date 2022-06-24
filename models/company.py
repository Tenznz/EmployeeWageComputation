from .abstract_class import CompanyABC


class Company(CompanyABC):
    def __init__(self, name=None):
        self.name = name
        self.employee_dict = {}

    def add_data(self, employee):
        """
        Add employee to the employee_computation

        :param employee: employee object
        :return: None
        """
        self.employee_dict.update({employee.name: employee})

    def get_data(self, employee_name):
        """
        this function return employee object from employee_dict dictionary

        :param employee_name: employee name
        :return: employee object
        """
        return self.employee_dict.get(employee_name, None)

    def update_data(self, args):
        pass

    def del_data(self, args):
        if self.employee_dict.get(args):
            self.employee_dict.pop(args)
            return True
        return False

    def __str__(self):
        return self.name
