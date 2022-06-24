from .abstract_class import CompanyABC


class Companies(CompanyABC):
    def __init__(self):
        self.company_data = dict()

    def add_data(self, company_obj):
        """
        add a employee_computation
        :param company_obj: employee_computation object
        :return: None
        """
        if company_obj.name not in self.company_data:
            self.company_data.update({company_obj.name: company_obj})
            return 1
        # temp = self.company_data.get(company_obj.name)
        # # self.company_data.update({**temp, **company_obj.employee_dict})
        # data = {**temp, **company_obj.employee_dict}
        # company_obj.employee_dict(data)
        # self.company_data.update({company_obj.name: company_obj})

    def update_data(self, company_obj):
        """
        update the add employee to specific employee_computation
        :param company_obj: employee_computation object
        :return:
        """
        temp = self.company_data.get(company_obj.name, None)
        if not None:
            data = {**temp, **company_obj.employee_dict}
            company_obj.employee_dict(data)
            self.company_data.update({company_obj.name: company_obj})
            return True
        return False

    def del_data(self, company_name):
        """
        delete the employee_computation
        :param company_name: employee_computation name
        :return: None
        """
        self.company_data.pop(company_name)

    def get_data(self, company_name):
        """
        get employee_computation employees
        :param company_name: employee_computation name
        :return: None
        """
        data = self.company_data.get(company_name, None)
        if data is not None:
            return data
        return None
