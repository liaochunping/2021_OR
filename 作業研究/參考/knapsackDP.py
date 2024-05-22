
import test as knapsackDP

reload(knapsackDP)

final = knapsackDP.KnapsackDPResult()
final.knapsackDP(4,[2,3,1], [31,47,14])

print 'objective value: ', final.optf
print 'combinations are: ', final.result
