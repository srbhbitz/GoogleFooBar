def solution(s):
    i = 0
    j = 0
    high = -1000
    count = 0
    c = 0
    sol = 1
    
    # if length of list is zero
    if len(s) == 0:
        return str(0)
    
    #if length of list is 1
    if len(s) == 1:
        return(str(s[i]))
    
    #Counting negative numbers
    while j < len(s):
        if s[j] < 0:
            count = count + 1
            if high < s[j]:
                high = s[j]
        j += 1
    
    #multiplying solution when element is not 0 and counting 0 in else part
    while i < len(s):
        if s[i] != 0:
             sol = sol * s[i]
        else:
            c += 1
        i +=1
    
    #if negative count is even and count of zero is not equals to length of list
    if count % 2 == 0 and c != len(s):
        return str(sol)
    
    #if count of zero is length of list
    elif c == len(s):
        return str(0)
    
    else:
        # if count of zero and count of negative number is equal to lenght of list and count of negative number is less than or equal to one
        if c+count == len(s) and count <= 1:
            return str(0)
        
        #if count of negative number is odd, then dividing the solution with highest negative number
        else:
            return str(sol//high)
