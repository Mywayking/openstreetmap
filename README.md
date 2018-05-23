# OpenStreetMap
`openstreetmap` is a pure Python library that provides an easy way to extracting [OpenStreetMap](www.openstreetmap.org) coordinates by name or relation id.


**Code example**

```python
# encoding=utf-8
from openstreemap import Crawler

c = Crawler()
boundary = c.name_parse('合肥市蜀山区', level='county')
# level: country state city county town
print(boundary.info)
boundary = c.id_parse("2458199", csys='wgs84', coo_order=True)
# csys(Coordinate System): wgs84 gcj02 bd09
print(boundary.info)
```


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


Galen @__20180521__