#import SeleniumTests

#from SeleniumTests.main import find_pet_by_id, return_pet_name
from main import check_pet_id_status_code, check_pet_name
#import SeleniumTests.main
#export PYTHONPATH="/Users/nikolaimaltcev/Documents/PythonProjects/Tests"

def test_check_pet_id_status_code():
    """
    Проверка, что питомец был успешно найден. Код ответа, в таком случае, должен быть 200.
    """
    expected_code = 200
    actual_code = check_pet_id_status_code()
    assert expected_code == actual_code
    print("Status code check successful")
    
def test_check_pet_name():
    """
    Проверка, что имя питомца соответствует нашим ожиданиям.
    """
    expected_name = 'snowflake'
    actual_name = check_pet_name()
    assert expected_name == actual_name, \
        f"Got {actual_name}, but expected {expected_name}"
    print("Pet name check successful")

print("Initializing tests:")
test_check_pet_id_status_code()
test_check_pet_name()
print("Tests completed")
