import logging
from employee_computation.models.company import Company
from employee_computation.models.employee import Employee
from employee_computation.models.multi_company import Companies

logging.basicConfig(filename="../../view.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


class CompanyView:
    def __init__(self):
        self.companies = Companies()

    def add_company(self):
        try:
            comp_name = input('Enter Company name')
            if comp_name in self.companies.company_data:
                print('Company already exists')
                return None
            self.companies.add_data(Company(comp_name))
            print('employee_computation added successfully !!!')

        except Exception as e:
            logging.error(e)

    def inside_company(self):
        comp_name = input('Enter Company name')
        comp = self.companies.get_data(comp_name)
        print(f'COMPANY NAME: {comp.name.upper()}')
        emp_view = EmployeeView()
        if comp is None:
            print('Company not found')
        while True:
            user_input = input('''Enter the following choice
            1) Add Employee
            2) Employee Details
            3) Delete Employee
            4) Get Monthly Wage   
            5) Exit 
            ''')
            choice = {
                '1': emp_view.add_employee,
                '2': emp_view.get_employee,
                '3': emp_view.del_employee,
                '4': emp_view.get_monthly_wage
            }
            if user_input == '5':
                print(f'Exit from {comp.name}')
                print('==================================')
                break
            elif user_input not in choice:
                print('invalid input')
                continue
            else:
                choice.get(user_input)(comp)

    def get_company_details(self):
        try:
            comp_name = input('Enter Company name')
            comp = self.companies.get_data(comp_name)
            if comp is not None:
                print(comp.employee_dict)
            else:
                print("employee_computation name not found")
        except Exception as e:
            logging.error(e)

    def delete_company(self):
        try:
            comp_name = input('Enter Company name')
            comp = self.companies.get_data(comp_name)
            if comp is not None:
                self.companies.del_data(comp_name)
                print("employee_computation delete successfully")
            else:
                print('Company not found')
        except Exception as e:
            logging.error(e)


class EmployeeView:
    def __init__(self):
        # employee_computation=Company()
        pass

    def add_employee(self, company):
        # name, wage_per_hr, num_of_working_days, max_hrs_in_month
        emp_name = input('Enter employee name')
        emp_wage_per_hour = int(input('Employee wage per hr'))
        emp_max_work_days = int(input('Employee maximum working days'))
        emp_max_work_hrs = int(input('Employee maximum working hours'))
        emp = Employee(emp_name, emp_wage_per_hour, emp_max_work_days, emp_max_work_hrs)
        company.add_data(emp)
        return emp

    def del_employee(self, company):
        emp_name = input('Enter employee name')
        is_deleted = company.del_data(emp_name)
        if is_deleted is True:
            print('Employee deleted successfully')
        else:
            print('Employee is not deleted or not found')

    def get_employee(self, company):
        emp_name = input('Enter employee name')
        emp_details = company.get_data(emp_name)
        print(f"employee details {emp_details}")
        return emp_details

    def get_monthly_wage(self, company):
        emp_details = self.get_employee(company)
        print(f'employee name: {emp_details} \nemployee wage:{emp_details.calc_emp_wage()}')
