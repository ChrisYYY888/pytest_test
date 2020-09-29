import requests


def post(url, data=None, **kwargs):
    response = requests.post(url, data=data, **kwargs)
    print('Request URL:\n%s\n' % url)
    print('Request Body:\n%s\n' % data)
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            print('%s:\n%s\n' % (key, value))
    print('Response Body:\n%s\n' % response.text)
    return response


def get(url, data=None, **kwargs):
    response = requests.get(url, params=data, **kwargs)
    print('Request URL:\n%s\n' % url)
    print('Request Body:\n%s\n' % data)
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            print('%s:\n%s\n' % (key, value))
    print('Response Body:\n%s\n' % response.text)
    return response


if __name__ == '__main__':
    pass
