# OpenStreetMap
`openstreetmap` is a pure Python library that provides an easy way to extracting ([OpenStreetMap](www.openstreetmap.org)) coordinates by name or relation id.
Life is short, be cool.


### Installation
---

`openstreetmap ` is hosted on [PYPI](https://pypi.python.org/pypi/OpenStreetMap) and can be installed as such:

```
$ pip install openstreetmap
```

Alternatively, you can also get the latest source code from [GitHub](https://github.com/xlzd/xart) and install it manually:

```
$ git clone git@git.rtbasia.com:galen/openstreetmap.git
$ cd openstreetmap
$ python setup.py install
```

For update:

```
$ pip install openstreetmap --upgrade
```


### License
---



wgs84_to_gcj02
gcj02_to_bd09
bd09_to_gcj02
gcj02_to_wgs84

wgs84:
gcj-02:Mars coordinate system 
BD-09:Baidu coordinate system

wgs84: True; gcj02: Mars; bd09:Baidu


    c = Crawler()
    # c.name_parse('安徽省', 'state')
    # c.name_parse('合肥市', 'city')
    boundary = c.name_parse('合肥市蜀山区', 'county')
    # boundary = c.id_parse("2458199", csys='gcj02', coo_order=True)
    print(boundary.info)


Galen @__20180521__