"Koral sereb 207972282"
"Lin Tibi 318232139"

def findLongestIncreasingSubSequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(findLongestIncreasingSubSequence(arr))


"The time complexity of this function is O(n^2)"
"The space complexity of this function is O(n)"








def subset_sum_exists(S):
    n = len(S)
    totalsum = sum(S)
    if totalsum % 2 != 0:
        return False
    targetsum = totalsum // 2
    dp = [False] * (targetsum + 1)
    dp[0] = True
    for i in range(n):
        for j in range(targetsum, S[i]-1, -1):
            dp[j] = dp[j] or dp[j - S[i]]
    return dp[targetsum]

S = [1, 2, 3]
print(subset_sum_exists(S)) # True
S = [4, 1, 2]
print(subset_sum_exists(S)) # False

"The time complexity of this function is O(n * targetsum)"

"The space complexity of this function is O(targetsum)"



