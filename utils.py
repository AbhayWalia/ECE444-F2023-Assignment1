class utils:
    def reversed(number):
            
            reversed = 0
            count = 0
            if isinstance(number, int):
                while number > 0:
                    count = count + 1 
                    digit = number % 10 #last digit
                    if (count > 0):
                        reversed = reversed * 10 + digit
                    else:
                        reversed = reversed * 10 + digit
                    number = number // 10 # floor and divide
                return reversed
            else:
                return "Please enter a int"
                
            
    def formatter(number):
        if isinstance(number, int):
            numBin = bin(int(number))
            numOct = oct(int(number))
            return(numBin, numOct)
        else:
            return "Please enter a int"









    # reverString = x[::-1]
    # reverInt = int(reverString)
    # return rever
        
        
        
