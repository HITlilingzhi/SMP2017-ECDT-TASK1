# -*- coding: utf-8 -*-
import time
import requests
import json


def test():
    """
    此函数为测试函数，将ServerDemo.py运行在服务器端后，用该程序在另一网络测试
    """

    # 此URL中IP地址为参赛者的服务器地址，应为可达的公网IP地址，端口默认21628
    url = "http://104.224.185.21:21628/smp2017_ecdt"
    sentencesList = [{'id': 121, 'content': "帮我订一张火车票好吗？"},
                     {'id': 122, 'content': "好难过啊"},
                     {'id': 123, 'content': "晚上吃饭了吗？"},
                     {'id': 124, 'content': "好饿啊！"}]
    parameter = {'sentencesList': sentencesList}
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.post(url, data=json.dumps(
            parameter), headers=headers, timeout=4)
        if r.status_code == 200:
            data = r.json()
            resultsList = data['resultsList']
            for result in resultsList:
                print result['id'], result['result']
        else:
            print "wrong,status_code: ", r.status_code
    except Exception as e:
        print Exception, ' : ', e


if __name__ == '__main__':
    test()
