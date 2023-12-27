from mitmproxy import ctx


def response(flow):
    with open("requests.txt", "a") as f:
        f.write("==============================\n")
        f.write(f"URL: {flow.request.url}\n")
        f.write("-----------------------------\n")
        f.write("Headers:\n")
        for key, value in flow.request.headers.items():
            f.write(f"{key}: {value}\n")
        f.write("-----------------------------\n")
        f.write("Content:\n")
        f.write(flow.response.text)
        f.write("\n\n")

        