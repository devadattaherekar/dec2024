"""
This is arithmetic module to perform arithmetic calculations
like addition and subraction
"""
from typing import Union

def add(var_1:Union[int,float],var_2:Union[int,float])->Union[int,float]:
    """
    :param var_1: you can pass int / float / str
    :param var_2: you can pass int / float / str
    :return: will return int / float / str
    """
    return var_1+var_2


def sub(var_1:Union[int,float],var_2:[float])->Union[int,float]:
    """
    :param var_1: int or float
    :param var_2: int or float
    :return: int or float after performing subtraction of both values!
    """
    print("sub from arithmetic module")
    return var_1-var_2
