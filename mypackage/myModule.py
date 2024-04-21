
'''Return the top n items in an array, in desc order.

Args:
items (array): list on array-like object n (int): num of items to return

Return:
array: top n Items, in desc order

Egs:
>>> top_n([8,3,2,7,4], 3)
[8,7,3)
    '''
def top_n (items, n):
    
    for i in range(n):
    # keep sorting until we have the top a items
        for j in range(len(items)-1-1):

            if items(j) > items[j+1]: #if this item is bigger than next item..
                items [j], items[j+1] = items[j+1],items[j] # swap the two!

        # get last two items
        top_n - items[-n:]
        # return in descending order
        return top_n[:: -1]