import unittest
import datetime

from tests.test import *

class CustomTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.test_results = []
        self.test_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def addSuccess(self, test):
        # Запись успешного результата
        self.test_results.append({
            "Test Case": test._testMethodName,
            "Situation": test.shortDescription() or "No description",
            "Result": "Success",
            "Date": self.test_date,
            "Verdict": "OK"
        })

    def addFailure(self, test, err):
        # Запись информации об ошибке, если тест не пройден
        self.test_results.append({
            "Test Case": test._testMethodName,
            "Situation": test.shortDescription() or "No description",
            "Result": str(err[1]),
            "Date": self.test_date,
            "Verdict": "NOT OK (High)"
        })

    def addError(self, test, err):
        # Запись информации об ошибке при выполнении теста
        self.test_results.append({
            "Test Case": test._testMethodName,
            "Situation": test.shortDescription() or "No description",
            "Result": str(err[1]),
            "Date": self.test_date,
            "Verdict": "ERROR (Critical)"
        })

    def printReport(self):
        # Формирование таблицы вручную с динамическими размерами колонок
        headers = ["Test Case", "Situation", "Result", "Date", "Verdict"]
        
        # Определение ширины каждой колонки
        col_widths = [max(len(str(row[col])) for row in self.test_results + [dict(zip(headers, headers))]) for col in headers]

        # Формат строки с учетом ширины колонок
        row_format = " | ".join(f"{{:<{w}}}" for w in col_widths)
        line = "-+-".join("-" * w for w in col_widths)
        
        # Вывод таблицы
        print("\nTest Report:\n")
        print(row_format.format(*headers))
        print(line)
        for result in self.test_results:
            print(row_format.format(
                result["Test Case"],
                result["Situation"],
                result["Result"],
                result["Date"],
                result["Verdict"]
            ))
        print()

class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resultclass = CustomTestResult

    def run(self, test):
        # Запуск тестов с кастомным результатом
        result = self.resultclass()
        test(result)
        result.printReport()
        return result


if __name__ == "__main__":
    runner = CustomTestRunner(verbosity=2)
    unittest.main(testRunner=runner)