from math import ceil

n = int(input())
tees = list(map(int, input().split()))
t, p = map(int, input().split())

# 인당 티셔츠 1장, 펜 1자루
# 펜 P자루 1묶음 or 1자루
# 티셔츠는 남아도 되지만 펜은 남으면 안됨
# 출력 티 t장 몇묶음\펜p자루 몇묶음

t_cnt = 0
for tee in tees:
    t_cnt += ceil(tee / t)

p_cnt = n // p
print(t_cnt)
print(p_cnt, n - (p_cnt * p))