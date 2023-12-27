import socket


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MySingletonClass:
    def __init__(self, data):
        self.data = data


singleton_instance1 = MySingletonClass("instance1")
singleton_instance2 = MySingletonClass("instance2")

print(singleton_instance1.data)
print(singleton_instance2.data)

print(singleton_instance1 is singleton_instance2)


def current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == "__main__":
    # import random
    # import string
    #
    #
    # def id_generator(length=12):
    #     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    #
    #
    # # 示例：生成长度为 8 的随机字符串
    # print(id_generator(20))  # 输出类似于 "2B7D9F5E"
    import random
    import string

    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(15))

    print(random_string)
