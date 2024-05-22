import knapsackDP  as dp
#if __name__ == '__main__':
f, result =dp.knapsackDP(4, [2,3,1], [31,47,14])
print('objective value:' , f)
print('combinations are: ', result)
f, result =dp.knapsackDP(8, [3,8,5], [4,6,5])
print('objective value:' , f)
print('combinations are: ', result)