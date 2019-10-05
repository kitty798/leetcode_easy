def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    cleanlist = []
    for c in s.lower():
        if c.isalnum():
            cleanlist.append(c)
    print (cleanlist)
    return cleanlist == cleanlist[::-1]
q = "Amana , planac , analPa  ,nama"
print (isPalindrome(q))



