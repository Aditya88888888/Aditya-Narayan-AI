#Python Program to Illustrate Set Operations
A={0,1,2,3,4,5,6}
B={4,6,7,8,9}
Union=A.union(B)
print("Union of A and B : ",Union)
Intersection=A.intersection(B)
print("Intersection of A and B : ",Intersection)
Difference=A.difference(B)
print("Difference of A and B = ",Difference)
Symmetric_Difference=A.symmetric_difference(B)
print("Symmetric Difference of A and B = ",Symmetric_Difference)