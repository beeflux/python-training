"""
    Company class consist of:
            * Name, Registration date, PAN Number, Head Office Location are the
              important parameters
            * Company type is set by default to "Software and IT"
            * Maximum Salary, Minimum Salary and Average Salary is non important
              parameters.
            * Investment and Profit Information is also non important parameters

            * Constructor __init__ sets all the important and non important
              parameters.
            * Company Type set up is set by the method set_company_type().
            * Company salary info is set by the method salary_info().
            * Company transaction info is set by the method transaction_info().
            * Whole Company information is printed by print_info() method.

    Testing:
            * c1 object test without salary information which is set to default.
            * c2 object test with all the parameters set.

"""
class Company:
    def __init__(self, name, registration, pan_number,
                    head_office):
        self.name = name
        self.registration = registration
        self.pan_number = pan_number
        self.head_office = head_office
        self.company_type()

        # setting default value
        self.max_salary = None
        self.min_salary = None
        self.mean_salary = None
        self.investment = None
        self.profit = None

    def company_type(self):
        self.type_of_company = "Software and IT"

    def set_company_type(self, company_type_info):
        self.type_of_company = company_type_info

    def salary_info(self, max_salary, min_salary, mean_salary):
        self.max_salary = max_salary
        self.min_salary = min_salary
        self.mean_salary = mean_salary

    def transaction_info(self, investment, profit):
        self.investment = investment
        self.profit = profit

    def print_info(self):
        print("Company name is {}").format(self.name)
        print("Head Office : {}").format(self.head_office)
        print("Company Type : {}").format(self.type_of_company)
        print("Registration : {}").format(self.registration)
        print("PAN Number : {}").format(self.pan_number)
        print("Maximum salary if {} \nMinimum salary is {} \nAverage salary is {}").format(self.max_salary,self.min_salary,self.mean_salary)
        print("Annual Investment : {}" ).format(self.investment)
        print("Annual profit : {}").format(self.profit)


c1 = Company("Beeflux","12-12-2010","12450979234","Budanilkantha")
# c1.salary_info(80000,20000,65000)
c1.transaction_info("12M","1M")
c1.print_info()

print("\n")
c2 = Company("Nepal Bank","1-1-1990","12678733543","Kathmandu")
c2.salary_info(100000,12000,90000)
c2.transaction_info("100B","100M")
c2.set_company_type("Banking")
c2.print_info()
