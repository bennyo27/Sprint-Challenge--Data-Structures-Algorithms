Exercise 1:
Add your answers to the Algorithms exercises here.

a) This piece of code has a runtime of O(N) because the while loop is of O(1) \* O(N)

b) This has the following O(N) \* O(N) \* O(N) \* O(1) = O(N^3)

c) This is O(N) because O(1) \* O(N) = O(N)

Exercise 2 Strategy:

Since both n and f are unknown I would take n and divide by 2 then check with egg, similar to a binary search tree. If it breaks then I know it is somewhere less than n/2. If it doesn't then I know it is above that number. So now the value can only be within
f > n or f < n I would keep calulating the value in the middle of either upper or lower range until the egg either breaks or doesnt break to see if I am close. This has a runtime of O(log n)).
