from typing import Union

my_list: list[Union[str, int]] = [3, 5, "do"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()