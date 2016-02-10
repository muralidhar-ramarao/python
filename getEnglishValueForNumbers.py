import sys

ones={	
	1:'One ',2:'Two ',
	3:'Three ',4:'Four ',
	5:'Five ',6:'Six ',
	7:'Seven ',8:'Eight ',
	9:'Nine ',10: 'Ten ',
	11:'Eleven ',12:'Twelve ',
	13:'Thirteen ',14:'Fourteen ',
	15:'Fifteen ',16:'Sixteen ',
	17:'Seventeen ',18:'Eighteen ',
	19:'Nineteen '}
tens={20:'Twenty ',30:'Thirty ',40:'Fourty ',50:'Fifty ',60:'Sixty ',70:'Seventy ',
	80:'Eighty ',90:'Ninety ',100:'Hundred '}
hundred=['','Thousand ','Million ','Billion ','Trillion ','Quadrillion ','Quintillion ']

def getList(num):
    '''
        int->lst
        This function takes the number as an input, and splits the number into small numbers of 3 digits starting from right.
        returns the number list.
        e.g.:
        >>> getList(1234567)
        [1,234,567]
    '''
    k=[]
    while num > 0:
        k.append(num % 1000)
        num=num//1000
    k.reverse()
    return [ int(i) for i in k ]

def getText(num):
    '''	num->str
	
	This function will take the number as an input and return a string which is spelled out number.
	
	e.g.:
	>>> getText(1)
	'One'
    '''
    if num==0: return ''
    if num < 20:
        return ones[num]#+ones[100/p]
    elif num>=20 and num <=99:
        return tens[num-(num%10)] + getText(num%10)
    elif num>=100:
        return ones[num//100]+tens[(num-(num%100))/(num//100)] + getText(num%100)
    else:
        return getText(int(str(num)[0]))+getText(int(str(num)[1:]))#+getText(num%100)

def getResult(num):
    ''' num->str
	This function accepts the number and returns the string for the numbers using the sub funtions getText and getList.
	
	e.g.:
	>>> getResult(1234567)
	'One Million Two Hundered ThirtyFour Thousand Five Hundered Sixty Seven'
    '''
    result=''
    a=[ getText(i) for i in getList(num) ]
    for i in range(len(a)-1,-1,-1):
        if a[len(a)-1-i].strip()!='':
            result+=str(a[len(a)-1-i]+hundred[i])
    
    return result.strip()

if __name__=='__main__':
    '''
	The below function accepts the input from stdin. Call the script from command line with the number as param.
    '''
    if len(sys.argv)>1 and type(eval(sys.argv[1])) in [int,long] :
        k=int(sys.argv[1])
        #print 'You entered: ',k# <----Enable this if you would like to print the number you have passed.
        print getResult(k)
    else:
        print '''Please enter a valid number. Use the below syntax to run the program.

	python getEnglishValueForNumbers.py <number>
    '''
