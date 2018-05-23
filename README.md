# OpenStreetMap

Extracting OpenStreetMap coordinates by name or relation id.

OpenStreetMap：
> www.openstreetmap.org


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