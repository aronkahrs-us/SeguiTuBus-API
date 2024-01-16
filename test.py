from SeguiTuBus import STB

client = STB()

companies = client.list_arrays()['response']['empresas']
print(companies)