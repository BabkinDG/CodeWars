url = 'http://google.co.jp'  # --> 'google'


def domain_name(url):
    url_prot = ['http://www.', 'www.', 'https://www.', 'http://', 'https://']
    for i in url_prot:
        dom_name = url.replace(i, '')
        if dom_name != url:
            break
    return dom_name.split('.')[0]


print(domain_name(url))
