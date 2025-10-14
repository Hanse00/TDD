class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = False
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = False
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        self.test.run()
        assert "setUp testMethod " == self.test.log



def main():
    TestCaseTest("testTemplateMethod").run()


if __name__ == "__main__":
    main()
