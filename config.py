first_page = {'url':'https://www.rightmove.co.uk/',
              'for_sale':'For Sale',
              'to_rent': 'rent'}
rent_page = {'url':'https://www.rightmove.co.uk/property-to-rent.html',
             'search_field':'//input[@id="searchLocation"]',
             'search_button':'//input[@id="search"]'}

choose_location = ''
search_radius_options = '//select[@id="radius"]/*'
search_radius = 10
search_radius_string = f'Within {search_radius} miles'  
price_range = {'min':0, 'max':2500}
price_range_min_option = f'{price_range["min"]:,} PCM'
price_range_max_option = f'{price_range["max"]:,} PCM'
price_range_option = {'min':price_range_min_option, 'max':price_range_max_option}
num_bedrooms = {'min': 2, 'max':2}
bedrooms_range_min_option = f'{num_bedrooms["min"]}'
bedrooms_range_max_option = f'{num_bedrooms["max"]}'
bedrooms_options = {'min':bedrooms_range_min_option, 'max':bedrooms_range_max_option}

search_xpath = ''
for_sale_click = ''
for_rent_click = ''