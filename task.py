"""
Write code on your own without trying to look up solutions from Google. Upload your assignment in google drive or dropbox
and send the link in the answer.
1. Create a list with 5 tuples. Each tuple should have the following elements
('Book Name', 'Published Year', 'Price'). a. Sort the list based on Price and Book Name. b. In the resulting list,
reshuffle each tuple to have the following order of elements ('Published Year', 'Price', 'Book Name')
Use list comprehension wherever possible.
"""

z = [("Pawn of Prophecy", 1982, 699.99), ('Queen of Sorcery', 1984, 499.99),
     ("Magician's Gambit", 1983, 1099.99), ('Castle of Wizardry', 1985, 749.99),
     ("Enchanter's End Game", 1989, 699.99)]


def sortTuple(tup):
    tup.sort(key=lambda x: x[0])
    tup.sort(key=lambda x: x[2])
    return tup


def rearrange(tup):
    for x in tup:
        print(x[1],x[2],x[0], sep=" , ")


print("**************After Sorting: **************")
print(sortTuple(z))
print("**************After Rearranging: **************")
rearrange(z)
print("*"*100)

"""
2. Find all quadruplets that add to 2 Example: Input: list1 = [0, -1, 2, 3, -2, 4, 5] Output: [-1, 2, 3, -2], [0, -1, -2, 5]
"""

def findElements (arr, n, X):

    # Stores sum of all pairs in a hash table
    mp = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    # Traverse through all pairs and search
    # for X - (current pair sum1).
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum1 = arr[i] + arr[j]

            # If X - summ is present in hash table,
            if (X - sum1) in mp:

                # Making sure that all elements are
                # diff array elements and an element
                # is not considered more than once.
                p = mp[X - sum1]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                    print(arr[i],", ",arr[j],", " , arr[p[0]],", ",arr[p[1]],sep="")
                    return

# Driver code
arr = [0, -1, 2, 3, -2, 4, 5]
n = len(arr)
X = 2
findElements(arr, n, X)

#Code written by DHRUV ANAND(dhruvanand27@gmail.com)
