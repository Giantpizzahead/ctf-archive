C = 662178077766850669017081350960675450866626410487472657824995902301105803722865348887729103273744687670210856986599238137474085960295114513760740459966676968724059253631174968661523798907425129282443090650164545463626029461082969497875692014457004225717365910895448395848366075795340200687913298280242095382525036144114016031219566025811690397457751710205831881264970203496990471920252496591183024372151716464558164880484132477323539535074128408150345238486324792149344120782499202626551432220593741763642887712274782107015422634257977732769993591778746851282860279285493

E = 7

low = 0
high = 10 ** 100
mid: int

while low < high:
    mid = (low + high) // 2
    print(mid)
    ans = mid ** E
    if ans < C:
        low = mid + 1
    elif ans > C:
        high = mid - 1
    else:
        break

print("P =", mid)