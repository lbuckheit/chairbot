from craigslist import CraigslistForSale
cl_fs = CraigslistForSale(site='newyork', filters={'query': 'aeron', 'max_price': 375, 'min_price': 11})

for result in cl_fs.get_results(sort_by='newest', limit=5):
    print(result)