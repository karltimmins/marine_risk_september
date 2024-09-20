import searoute as sr

origin = [0.3515625, 50.064191736659104]

destination = [117.42187500000001, 39.36827914916014]

route = sr.searoute(origin, destination)

print("{:.1f} {}".format(route.properties['length'], route.properties['units']))

