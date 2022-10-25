def zip(a:list[str] , b: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    assert len(a) == len(b)
    for i in range(0, len(b)):
            result[a[i]] = b[i]
    return result
    print(result)

zip(["hi" , "he"], ["bonjou" , "ta"])
