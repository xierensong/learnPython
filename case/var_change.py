#coding=utf-8



def evaluate():
    print('eval')
    return 1


maxEvalScore = 0

a1, a2, a3, a, b = 1.0, 1.0, 1.0, 1.0, 1.0

for index, var in enumerate([a1, a2, a3, a, b]):
    for k in range(10, 0, -1):
        # m = var
        var = k / 10
        m = [a1, a2, a3, a, b][index]
        [a1, a2, a3, a, b][index] = k / 10
        print([a1, a2, a3, a, b])
        evalScore = evaluate()
        if maxEvalScore < evalScore:
            maxEvalScore = evalScore
            [a1, a2, a3, a, b][index] = m

initval = 1.0
# a[5] = [initval for i in range(5)]
a = [1.0, 1.0, 1.0, 1.0, 1.0]
for index in range(5):
    for k in range(10, 0, -1):
        var = k/10
        m = a[index]
        a[index] = k / 10
        print(a)
        evalScore = evaluate()
        if maxEvalScore < evalScore:
            maxEvalScore = evalScore
            a[index] = m

