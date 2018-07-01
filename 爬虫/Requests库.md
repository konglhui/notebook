# Requests库

- 基本使用方法

  - ```
    import requests
    
    response = requests.get('https://www.baidu.com')
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    ```

  - 各种请求方法

    - ```
      url = 'https://www.baidu.com'
      requests.post(url)
      requests.get(url)
      ```

  - 基本get请求

    - ```
      import requests
      
      response = requests.get('https://httpbin.org/get')
      print(response.text)
      ```

  - 带参数get请求

    - ```
      import requests
      
      response = requests.get('https://httpbin.org/get?name=germey&age=22')
      print(response.text)
      ```

    - ```
      import requests
      
      data={
          'name':'germey',
          'age':22}
      response = requests.get('https://httpbin.org/get',params=data)
      print(response.text)
      ```

- 文件上传

- 获取cookies

  - ```
    response = requests.get('https://httpbin.org/get')
    print(response.cookies)
    ```

- 会话维持

  - ```
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/number/123456789')
    response = s.get('https://httpbin.org/cookies')
    print(response.text)
    ```

- 证书验证

  - ```
    from requests.packages import urllib3
    urllib3.disable_warnings()
    response = requests.get('https://www.12306.cn',verify=False)
    print(response.status_code)
    ```