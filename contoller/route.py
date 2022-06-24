from employee_computation.views.views import CompanyView


def main():
    company_view = CompanyView()
    print('''=================================================
==============Employee Computation===============
=================================================
    ''')
    while True:
        user_input = input('''Enter the following choice
            1)Add Company
            2)Update Company
            3)Get Company
            4)Delete Company 
        ''')
        choice = {
            '1': company_view.add_company,
            '2': company_view.inside_company,
            '3': company_view.get_company_details,
            '4': company_view.delete_company
        }
        choice.get(user_input, None)()
        print('========================================')


if __name__ == '__main__':
    main()
