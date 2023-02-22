## ------------------------------------- ##
## --- Built In Functions => Reduce ---- ##
## ------------------------------------- ##

# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

### reduce (Function ,  iterable )

from functools import reduce


def sumAll(num1, num2):
    return num1 + num2

numbers = [1,2,3,4,5]  
 
result = reduce(sumAll,numbers)  ##  reduce :((((1+2)+3)+4)+5) = 15
print(result)


## using Lambda

print(reduce((lambda n1,n2 : n1+n2 ), numbers)) ## reduce :((((1+2)+3)+4)+5) = 15