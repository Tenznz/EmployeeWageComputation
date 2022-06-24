from random import randint


class Employee:
    def __init__(self, name, wage_per_hr, num_of_working_days, max_hrs_in_month):
        self.name = name
        self.emp_rate_per_hour = wage_per_hr
        self.num_of_working_days = num_of_working_days
        self.max_hrs_in_month = max_hrs_in_month
        self.total_wage = 0

    def get_wage(self):
        """
        get the calcutated wage
        :return:
        """
        return self.total_wage

    def calc_emp_wage(self):
        """

        :return:total_wage
        """
        total_hours = 0
        self.total_wage = 0
        for i in range(self.num_of_working_days):
            emp_hour = self.is_present()
            total_hours = total_hours + emp_hour
            if total_hours > self.max_hrs_in_month:
                break

            emp_wage = emp_hour * self.emp_rate_per_hour
            self.total_wage = self.total_wage + emp_wage
        return self.total_wage

    def is_present(self):
        """
        check employee is present
        :return: employee hours
        """
        is_present = randint(0, 2)
        switch = {
            1: 8,
            2: 4,
            0: 0
        }
        emp_hour = switch.get(is_present)
        return emp_hour

    def __str__(self):
        return self.name
