
# What is the smalles change I CAN'T give back from coins that I have ?
# Example: [1,2,5] : The answer is 4. I can't construct 4 out those coins (numbers)
# Solution: let [1,2,5] will be [a,b,k] and I am looking for 'x'
# Are all sums + 1 untill k  (a+b..)+1 > k ? If so :
# I am not missing any coin and I can generate all numbers untill I get to k
# if (a+b..) +1 < k then I am missing something and that is my 'x'
# Example 1 (1+2) + 1 = 4 ... 4 < 5 then I can't give back 4
# Example 2 : [1,1,2,3,4,5,6,30] (1+1+2+3+4+5+6) + 1 = (22) + 1 = 23 < 30 I can't give back 23  
def changeICantGiveBack(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    return currentChange + 1

# Tests
print("\nTest 1")
coins = [5, 7, 1, 1, 2, 3]
print("I can't give back coin : " , changeICantGiveBack(coins)) # 20

print("\nTest 2")
coins = [1, 1, 2, 3, 4, 5, 6]
print("I can't give back coin : " , changeICantGiveBack(coins)) # 23

print("\nTest 3")
coins = [1, 1, 2, 5, 10]
print("I can't give back coin : " , changeICantGiveBack(coins)) # 20