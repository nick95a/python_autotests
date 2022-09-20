import requests


HOST = 'https://petstore.swagger.io/v2/pet'
HOST_FIND = 'https://petstore.swagger.io/v2/pet'

PARAMETERS_CREATE_PET = {"id": 10,"category": {"id": 0,"name": "string"},"name": "niko","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}
PARAMETERS_UPDATE_PET = {"id": 10,"category": {"id": 0,"name": "string"},"name": "snowflake","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}

response_CREATE_PET = requests.post(url = HOST, json = PARAMETERS_CREATE_PET)
response_UPDATE_PET = requests.post(url = HOST, json = PARAMETERS_UPDATE_PET)
response_FIND_PET_BY_ID = requests.get(url = "https://petstore.swagger.io/v2/pet/10")

data_CREATE_PET = response_CREATE_PET.json()
data_UPDATE_PET = response_UPDATE_PET.json()
data_FIND_PET_BY_ID = response_FIND_PET_BY_ID.json()

if __name__ == "__main__":

    print("Создание питомца: \n", data_CREATE_PET, "\n")
    print("Смена имени питомца или его тегов: \n", data_UPDATE_PET, "\n")
    print("Нахождение питомца по айди: \n", data_FIND_PET_BY_ID)

def check_pet_id_status_code():
    return response_FIND_PET_BY_ID.status_code 

def check_pet_name():
    return data_FIND_PET_BY_ID['name']