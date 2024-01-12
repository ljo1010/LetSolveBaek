def solve(a:list) -> int:
    ans = 0
    for i in range(a+1):
        ans += i
    return ans