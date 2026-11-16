def umkehren_2(var_string):
    retvalue = ""
    # ????
    '''
    retvalue += var_string[5]
    retvalue += var_string[4]
    retvalue += var_string[3]
    retvalue += var_string[2]
    retvalue += var_string[1]
    retvalue += var_string[0]
    '''

    retvalue = ""
    i = len(var_string) - 1
    while i >= 0:
        retvalue += var_string[i]
        i -= 1


    return retvalue

def umkehren(var_string):
    retvalue = ""
    # ????
    '''
    retvalue =  var_string[0] + retvalue
    retvalue =  var_string[1] + retvalue
    retvalue =  var_string[2] + retvalue
    
    '''

    retvalue = ""
    i = 0
    while i <= len(var_string) - 1:
        retvalue  =  var_string[i] + retvalue
        i += 1


    return retvalue


if __name__ == '__main__':

    var_string = "dsfxx"

    # V ??
    # for i in range(len(var_string)):
    #    print(var_string[i])
    print(var_string)
    reverse = umkehren_2(var_string)
    print(reverse )