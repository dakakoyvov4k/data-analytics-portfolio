N, C, R = map(int, input().split())
forgot_set = set(map(int, input().split()))
reserve_set = set(map(int, input().split()))

have_lst = [i not in forgot_set for i in range(1, N + 1)]

for i in forgot_set & reserve_set:
    have_lst[i - 1] = True

donors = [i for i in reserve_set - forgot_set]
best = sum(have_lst)


def f(num, current, get):
    global best
    if num == len(donors):
        best = max(best, sum(current))
        return

    f(num + 1, current[:], get[:])

    donor = donors[num]
    for i in (donor - 1, donor + 1):
        if 1 <= i <= N and i in forgot_set and not current[i - 1] and not get[i - 1]:
            new_current = current[:]
            new_get = get[:]
            new_current[i - 1] = True
            new_get[i - 1] = True
            f(num + 1, new_current, new_get)


f(0, have_lst[:], [False] * N)
print(best)
