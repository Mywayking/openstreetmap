"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/23
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from openstreemap import Crawler
if __name__ == '__main__':
    c = Crawler()
    # c.name_parse('安徽省', 'state')
    # c.name_parse('合肥市', 'city')
    boundary = c.name_parse('合肥市蜀山区', 'county')
    # boundary = c.id_parse("2458199", csys='gcj02', coo_order=True)
    print(boundary.info)
