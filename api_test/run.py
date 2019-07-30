import unittest
from BSTestRunner import BSTestRunner
import time

test_dir='./test_case'
report_dir='./reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='weather_api_unittest.py')

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'

with open(report_name, 'wb') as f:
 runner = BSTestRunner(stream=f, title="Weather API Test Report", description="China City Weather Test Report")
 runner.run(discover)