import allure, pytest


class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)  # 阻塞性bug
    @allure.step(title="这是测试步骤")
    def test_001(self):
        allure.attach("描述", "我是描述的具体内容")

        with open("./image/1.jpg", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.JPG)
        assert True
