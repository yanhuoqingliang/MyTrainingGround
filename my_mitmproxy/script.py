from mitmproxy import http
import json


def request(flow: http.HTTPFlow) -> None:
    flow.request.headers["User-Agent"] = "My Custom User Agent"


def response(flow: http.HTTPFlow) -> None:
    """
    数据统计：内容数据
    """
    if "/BASEURL/hozo/api/stats/common/focus" in flow.request.pretty_url:

        request_data = json.loads(flow.request.text)
        response_data = json.loads(flow.response.text)

        for item in response_data['params']:
            if item['metricGroup'] == 'pc:album:album:album':
                for item_a in item['metrics']:
                    if item_a['metricName'] == 'album_pub_num':
                        item_a['value'] = '100299'
                        item_a['todayInc'] = '100299'
                        item_a['yesterdayInc'] = '10299'
                    if item_a['metricName'] == 'album_share_count':
                        item_a['value'] = '100299'
                    if item_a['metricName'] == 'album_view_count':
                        item_a['value'] = '100299'
            if item['metricGroup'] == 'pc:album:album:mkt':
                for item_a in item['metrics']:
                    if item_a['metricName'] == 'mkt_share_count':
                        item_a['value'] = '100299'

        response_text = json.dumps(response_data)
        flow.response.text = response_text

    if "/BASEURL/hozo/api/stats/common/graph" in flow.request.pretty_url:

        request_json = flow.request.json()
        response_json = flow.response.json()

        with open("../aric.txt", "a") as f:
            f.write(f'请求数据：{request_json}，响应数据：{response_json}')
            f.write("\n")

        if "graphType" in request_json and request_json.get("graphType") == "priceExcept":
            response_data = json.loads(flow.response.text)
            for item in response_data['params']:
                if item['tagName'] == '3万以下':
                    item['count'] = 5
                if item['tagName'] == '3~6万':
                    item['count'] = 10
                if item['tagName'] == '6~10万':
                    item['count'] = 15
                if item['tagName'] == '10~15万':
                    item['count'] = 20
                if item['tagName'] == '15~30万':
                    item['count'] = 25
                if item['tagName'] == '30~50万':
                    item['count'] = 30
                if item['tagName'] == '50万以上':
                    item['count'] = 35
                if item['tagName'] == '其他':
                    item['count'] = 5

            response_text = json.dumps(response_data)
            flow.response.text = response_text

        if "graphType" in request_json and request_json.get("graphType") == "style":
            response_data = json.loads(flow.response.text)

            response_list = response_data['params']
            response_list.append({"tagName": "东南亚", "count": 10})
            response_list.append({"tagName": "中式", "count": 10})

            response_text = json.dumps(response_data)
            flow.response.text = response_text

    if '/BASEURL/hozo/api/stats/common/trend' in flow.request.pretty_url:

        request_data = json.loads(flow.request.text)
        response_data = json.loads(flow.response.text)

        if request_data['dimType'] == 'ALBUM' and request_data['metricName'] == 'album_pub_num' and request_data['type'] == '1':
            response_data['params']['values'][0] = 1000
            response_data['params']['values'][5] = 1100
            response_data['params']['values'][6] = 1000
            response_data['params']['values'][10] = 1200
            response_data['params']['values'][15] = 1300
            response_data['params']['values'][20] = 1400
            response_data['params']['values'][25] = 1500

        response_text = json.dumps(response_data)
        flow.response.text = response_text

    if '/BASEURL/hozo/api/stats/album/report' in flow.request.pretty_url:

        request_data = json.loads(flow.request.text)
        response_data = json.loads(flow.response.text)

        response_data['params']['total'] = 10001

        # ablum_data = response_data['params']['list'][0]
        #
        # with open("a.txt", "a") as f:
        #     f.write(f'数据：{ablum_data}')
        #     f.write("\n")
        #
        # for num in range(1, 10000):
        #     response_list = response_data['params']['list']
        #     response_list.append(ablum_data)

        response_text = json.dumps(response_data)
        flow.response.text = response_text

    if '/BASEURL/hozo/api/stats/mkt/report' in flow.request.pretty_url:

        request_data = json.loads(flow.request.text)
        response_data = json.loads(flow.response.text)

        response_data['params']['total'] = 10001

        response_text = json.dumps(response_data)
        flow.response.text = response_text

    if '/BASEURL/hozo/api/stats/album/ref' in flow.request.pretty_url:
        pass

    if '/BASEURL/hozo/api/stats/mkt/svr/apply' in flow.request.pretty_url:
        pass

    """
    数据统计：客户数据
    """
    if '/BASEURL/hozo/api/stats/cust/report' in flow.request.pretty_url:

        request_data = json.loads(flow.request.text)
        response_data = json.loads(flow.response.text)

        response_data['params']['total'] = 10001

        response_text = json.dumps(response_data)
        flow.response.text = response_text
