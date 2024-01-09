from mitmproxy import http


def write_data(filepath, data):
    with open(filepath, 'a') as f:
        f.write(data)
        f.write("\n")


def request(flow: http.HTTPFlow) -> None:
    flow.request.headers['User-Agent'] = "My Custom User Agent"


def response(flow: http.HTTPFlow) -> None:

    if '/hozo-main/servicehall/servicepage/list' in flow.request.pretty_url:

        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('service_hall.txt', str(response_json))
        pass

    if '/hozo-main/servicehall/servicepage/query' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo-main/servicehall/defaultdata' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('service_hall.txt', str(response_json))
        pass

    if '/hozo-main/servicehall/servicepage/save' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo/servicehall/servicepage/delete' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo-customer/servicehall/servicepage/query' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo-customer/servicehall/defaultdata' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo-customer/servicehall/order/query' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        write_data('./service_hall.txt', str(response_json))
        pass

    if '/hozo-customer/servicehall/compatible/queryservice/old2new' in flow.request.pretty_url:
        request_json = flow.request.json()
        response_json = flow.response.json()
        pass
