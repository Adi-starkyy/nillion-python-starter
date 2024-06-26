from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Perform the computation (addition between two numbers..)
    result_sum = my_int1 + my_int2
    
    
    # Return the result
    return [Output(result_sum, "sum_output", party1)]
   