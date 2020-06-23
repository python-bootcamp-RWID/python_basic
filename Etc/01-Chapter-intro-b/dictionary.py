# belajar dictionary

manusia = {}
manusia['name'] = 'danil'
manusia['genre'] = 'male'
manusia['status'] = 'married'

print(manusia)

manusia['name'] = 'danil syah'
manusia['address'] = 'Perum. Telaga Surya'
print(manusia)

# cara konversi ke json
import json
print(json.dumps(manusia))
