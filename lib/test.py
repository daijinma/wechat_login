import requests

# 定义请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


# 爬取文章列表
def crawl_article_list(public_account):
    url = f'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz={public_account}&f=json'

    print(url)

    cookie = {}

    response = requests.get(url, headers=headers, cookies=cookie)
    data = response.json()
    general_msg_list = data['general_msg_list']
    print(public_account, general_msg_list)
    # 解析文章列表数据
    articles = data['list']
    for article in articles:
        app_msg_ext_info = article['app_msg_ext_info']
        title = app_msg_ext_info['title']
        url = app_msg_ext_info['content_url']
        
        # 保存文章信息到 Redis
        print(public_account, title, url)

    # 判断是否还有更多文章
    has_next = data['can_msg_continue']
    if has_next:
        next_offset = data['next_offset']
        crawl_article_list(public_account, next_offset)


# 指定微信公众号的 Biz 号
public_account_biz = ''
crawl_article_list(public_account_biz)