
#Any pytest file should start with test_ or end with _test
#pytest methods should start with test
#any code written must be wrapped in methods
#To run pytest file you have to make use of test runner ,select edit configuration and add Python tests
#you can mark the (tag) tests @pytest.mark.smoke and then run with -m
#you can mark the (tag) tests @pytest.mark.skip and then run with -m
#The below command flags is mainly for executing the code in command line:
    #-k is for regex to identify method ,-v for more info such as result status as pass or failed,-s for showing logs in output
    #to run one test case at time-py.test <filename>
#fixtures are used as setup and teardown methods for test
# cases -conftest files to generalize fixtures and make it available across all pytest files
#pytest files(files which begin with test_ or end with _test and methods should begin with test_)
#usefixtures -allows you to set scope of fixtures before class is initiated which allows the precondition step and postcondition
#to be executed only once after all the test case/methods in a class get executed
#Datadriven and parametrization can be done with return statements in list format
#To generate html report which shows the execution logs ->install this plugin-pip install pytest-html
#To run the pytest file to get html report you can use the following command-pytest --html=report.html
# to run a  test case make use of py.test filename -v -s
#fixtures can bse used to load data and also for setup and teardown methods as well


import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_first_program(self):
        print("This is my first program")

    #def test_first_program(self):
        #print("Overriding my first program")

    @pytest.mark.xfail #this will get executed but it won't report the status of execution(pass,fail or skipped),it will show as xpass
    def test_second_program(self):
        print("This is my second program")



    def test_credit_card_personal_details(self):
        print("This is my credit card personal details")

