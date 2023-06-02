result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більшим за b")
        if b > 100:
            raise IndexError("b не може бути більшим за 100")
        return a / b
    except ValueError as ve:
        print("ValueError:", ve)
    except IndexError as ie:
        print("IndexError:", ie)
    except Exception as e:
        print("Exception:", e)
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)