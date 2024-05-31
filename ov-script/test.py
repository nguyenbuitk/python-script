clusters =  [{'cluster': 'sqa-4k', 'url': 'https://sqa-sca.manage.ovcirrus.com'}, {'cluster': 'prod-us',          'url': 'https://us.manage.ovcirrus.com'}, {'cluster': 'prod-eu', 'url': 'https://eu.manage.ovcirrus.com'}]

cluster_name = "prod-us"
url = [cluster["url"] for cluster in clusters if cluster["cluster"] == cluster_name][0]

print(url)
