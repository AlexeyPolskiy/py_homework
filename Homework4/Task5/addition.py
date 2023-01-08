def addition(eq_first: dict, eq_second: dict):
    eq_result = {}
    eq_result.update(eq_first)
    eq_result.update(eq_second)
    for key in eq_result:
        eq_result[key] = eq_first.get(key, 0) + eq_second.get(key, 0)
    return eq_result