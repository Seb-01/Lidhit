import requests
import sys

def main():
    """

    :return:
    """
    # читаем файл с формой
    print(sys.argv[1])
    with open(sys.argv[1], 'r') as f:
        payload=f.read()

    headers = {'content-type': 'application/json'}
    # делаем запрос
    ret = requests.post('http://127.0.0.1:5000/get_form', data=payload, headers=headers)

    print(ret.text)

if __name__ == "__main__":
    main()