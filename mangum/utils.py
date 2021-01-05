import typing

def get_header(headers: typing.Dict[str, typing.List[str]], key: str, default: any =None) -> typing.Union[str, any]:
    values = headers.get(key, [])
    return (
        values[0]
        if len(values) > 0
        else default
    )
