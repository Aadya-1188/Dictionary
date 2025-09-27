country_code = { 'India' : '0091' , 
                    'Australia' : '0025' , 
                    'Nepal' : '0977'}

#Search for Inida's Coutry code in Dictionary
print("Country code for India is :" )
print(country_code.get('India' , 'Not Found'))


#Search for Japan's Coutry code in Dictionary
print("Country code for Japan is :" )
print(country_code.get('Japan' , 'Not Found'))