class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def addClass(self, testClass):
        testMethods = [method for method in dir(testClass) if callable(getattr(testClass, method)) and method.startswith("test")]
        for method in testMethods:
            self.add(testClass(method))

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, TestCase) and self.name == other.name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed(self.name)
        self.tearDown()

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.failed = []

    def testStarted(self):
        self.runCount += 1

    def testFailed(self, name):
        self.errorCount += 1
        self.failed.append(name)

    def summary(self):
        if self.errorCount > 0:
            return f"{self.runCount} run, {self.errorCount} failed\n\nFailed:\n" + "\n".join(self.failed)
        return f"{self.runCount} run, {self.errorCount} failed"


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception("broken method")

    def tearDown(self):
        self.log += "tearDown "


class TestSuiteTest(TestCase):
    def testSuiteAddsFromClass(self):
        suite = TestSuite()
        suite.addClass(TestSuiteTest)
        assert [TestSuiteTest("testSuiteAddsFromClass")] == suite.tests



class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed\n\nFailed:\ntestBrokenMethod" == self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed("testSomething")
        assert "1 run, 1 failed\n\nFailed:\ntestSomething" == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert "2 run, 1 failed\n\nFailed:\ntestBrokenMethod" == self.result.summary()

    def testEquality(self):
        assert WasRun("testMethod") == WasRun("testMethod")


def main():
    suite = TestSuite()
    suite.addClass(TestCaseTest)
    suite.addClass(TestSuiteTest)
    result = TestResult()
    suite.run(result)
    print(result.summary())


if __name__ == "__main__":
    main()
