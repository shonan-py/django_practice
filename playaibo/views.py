from django.shortcuts import render
from django.views.generic import View
import requests

API_Key = 'XXXXXXXXXXXXXXXXXXXX'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def top(request):
    return render(request, 'playaibo/index.html')


class ForecastView(View):
    """API実行結果の表示
    """
    template_name = 'playaibo/forecast.html'
    city = 'Tokyo,jp'

    def post(self, request, *args, **kwargs):
        if request.POST['city']:
            self.city = request.POST['city']
        url = BASE_URL
        query = {
            'units': 'metric',
            'q': self.city,
            'cnt': '30',
            'appid': API_Key
        }
        r = requests.get(url, params=query)
        print('Weather forecast in Tokyo at UTC(needs +9h): ')
        result = []
        for line in r.json()['list']:
            # print('x: ', x)
            result.append(
                "date: {}, emp: {}, weather: {}\n".format(
                    line['dt_txt'],
                    line['main']['temp'],
                    line['weather'][0]['main'],
                    # line['weather'][0]['description']
                ))

        mapped_num = map(str, result)  # 格納される数値を文字列にする
        result_string = ' '.join(mapped_num)
        ctx = {'city': self.city}
        ctx['result'] = result_string
        return render(request, self.template_name, ctx)
