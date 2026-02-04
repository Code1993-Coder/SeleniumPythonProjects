import pytest
#Data driven fixtures to load data into tests

@pytest.mark.usefixtures("testData")
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_registration(self,testData):
        print("Registration steps")
        print('FirstName:',testData[0],",",'LastName:',testData[1],",",'Email:',testData[2])