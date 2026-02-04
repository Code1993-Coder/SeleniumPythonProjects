import pytest


@pytest.fixture(scope="class")
def setup():
    print("Precondition-I get executed first and this includes invoking browsers and pre-requisite steps")
    yield
    print("PostCondition-I get executed at last and this includes closing browser and clearing cache")

@pytest.fixture()
def testData():
    print("Data setup steps")
    return ['Rahul','Shetty','RahulShetty.accademy.com']

@pytest.fixture(params=[("Chrome","Rahul"),("Firefox","Tina"),("IE","Miya")])  #paramterize test with multiple data sets using fixtures
def crossBrowser(request):#use this request instance only when you have params
    return request.param
