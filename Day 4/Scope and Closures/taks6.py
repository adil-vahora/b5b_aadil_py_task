def make_validator(min_value):

    def validate(number):
        if number >= min_value:
            return True
        else:
            return False

    return validate


validator1 = make_validator(10)
validator2 = make_validator(50)

print(validator1(15))
print(validator1(5))
 
print(validator2(60))
print(validator2(30))