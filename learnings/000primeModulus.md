The prime modulus works to reduce the chances of collision for creating hashes of numeric numbers, becuase of the below fact:


>  koi 2 values h V1 and V2

* Agr non prime number lete h, let's say X, toh V1 aur V2 ke proper divide hone(modulus resulting in 0) ki possibilities ke set hoga ye:
```
{X, any numbers in the world, X ke apne factors(especially chote factors)}
```

* Whi agr prime number lete h, let's say X, toh V1 aur V2 ke proper divide hone(modulus resulting in 0) ki possibilities ke 
```
{X, any numbers in the world}
```

Toh basically V1 and V2 ka modulus X(big prime number) karne ke baad same output pr land hona bht unlikely ho jata h because ab woh khud `X ke apne factors(especially chote factors)` numbers se bach h gye h divide hone se



## HENCE, USING A BIG PRIME FOR MODULO HELPS IN REDUCING THE POTENTIAL EASY COLLISIONS

### However, collisions can still happen, and we should know the collision handling strategies, for ex if V1 and V2 are numbers bigger than X prime number and V1, V1 both are multiples of X.
