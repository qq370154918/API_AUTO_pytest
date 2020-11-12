import pytest
from tools.login_session import login

#声明它是一个fixture
@pytest.fixture(scope="class")
def do_login():
    #前置操作
    print("=========所有测试用例之前的，setup===整个测试类只执行一次========")
    s=login()
    yield (s)    #分隔线 ；#后面接返回值
    #后置操作
    print("=========所有测试用例之后的，teardwon===整个测试类只执行一次========")
    pass
