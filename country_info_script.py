from country_info_script import CountryInfo

count = input("Enter your country: ")
country = CountryInfo(count)

# Correct method calls
print("Capital is: ", country.capital())
print("Currency is: ", country.currencies())
print("Language is: ", country.languages())
print("Borders are: ", country.borders())
print("Other names: ", country.alt_spellings())
