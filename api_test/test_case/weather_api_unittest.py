import unittest
import requests
from time import sleep
from urllib import parse

class WeatherTest(unittest.TestCase):
    def setUp(self):
        # self.url='http://t.weather.sojson.com/api/weather/city/101030100'
        self.url='http://v.juhe.cn/weather/index'

    def test_weather_hangzhou(self):
        data={'cityname':'杭州','key':'f345dd703ae48c26dcbb49fa4bf0944f'}
        city = parse.urlencode(data).encode('utf-8')
        r=requests.get(self.url,city)
        result=r.json()
        self.assertEqual(result['resultcode'],'200')
    def test_weather_param_error(self):
        data={'cityname':'123456','key':'f345dd703ae48c26dcbb49fa4bf0944f'}
        r=requests.get(self.url,data)
        result=r.json()
        self.assertEqual(result['resultcode'], '202')
        self.assertEqual(result['reason'],'查询不到该城市的信息')
    def test_weather_no_param(self):
        data={'key':'f345dd703ae48c26dcbb49fa4bf0944f'}
        r=requests.get(self.url,data)
        result=r.json()
        self.assertEqual(result['reason'],'Error Cityname!')


if __name__ == '__main__':
    unittest.main()