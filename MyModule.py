import random

def minimum(arr): #returns minimal number from arr
    minimal = arr[0]
    for i in arr[1::]:
        if minimal > i:
            minimal = i
    return minimal

def maximum(arr):
    maximal=arr[0]
    for i in arr[1::]:
        if maximal < i:
            maximal = i
    return maximal

def minind(arr): #returns index of minimal number from arr
    minimal=arr[0]
    minind=0
    for i in range(1,len(arr)):
        if minimal>arr[i]:
            minimal=arr[i]
            minind=i
    return minind

def maxind(arr):
    maximal = arr[0]
    max_ind = 0
    for i in range(1, len(arr)):
        if maximal < arr[i]:
            maximal = arr[i]
            max_ind = i
    return max_ind

def qsort(arr): #sorts arr
    if len(arr) < 2:
        return arr
    else:
        stand = arr[0]
        less = [i for i in arr[1:] if i <= stand]
        more = [i for i in arr[1:] if i > stand]
        return qsort(less) + [stand] + qsort(more)

def selsort(arr): #sorts arr NOT RECOMMENDED
    sortarr=[]
    min_ind = 0
    for _ in range(len(arr)):
        min_ind=minind(arr)
        sortarr.append(arr.pop(min_ind))
    return sortarr



def spiral(n): #Func that prints spiral of numbers from 1 to n^2
    i, m, tr, td, tl, tu = 0, 1, 0, 0, 0, 0
    a = [[int(0) for _ in range(n)] for k in range(n)]
    for g in range(1, 2*n):
    
        i=0
        # To right
        if g%4==1:               
            while (n-2*tr>i) :           
                a[tr][i+tr]=m
                i+=1
                m+=1
            tr+=1
        
        i=1
        # To down
        if g%4==2:               
            while (n-1-2*td>i-1) :        
                a[i+td][n-td-1]=m
                i+=1
                m+=1
            td+=1
            
        i=1
        k=2+tl
        # To left
        if g%4==3:               
            while (n-2*tl>i) :       
                a[n-1-tl][-k]=m
                k+=1
                m+=1
                i+=1
            tl+=1
            
        i=1
        k=2+tu
        # To up
        if g%4==0:               
            while n-2*tu-1>i:         
                a[-k][tu]=m
                m+=1
                i+=1
                k+=1
            tu+=1

    # Output spiral
    #for i in range(len(a)):      
    #    print()
    #    for j in range(len(a)):
    #        print(a[i][j], end=' ')
    #print()
    return a

def cycsum(arr):   #Faster than Recursive
    total=0
    for x in arr:
        total+=x
    return total

def recsum(arr):   #Slower than Cyclic
    tot=0
    if arr!=[]:
        r=arr[0]
    if arr==[]:
        r=0
        return r
        r=int(r)
    else:
        arr.remove(arr[0])
        return tot+r+recsum(arr)

def binsearch(in_list, item): #finds 'item' in 'in_list'
    in_list = selsort(in_list)
    low=0
    high=len(in_list) - 1
    while high>=low:
        mid=int((low+high) / 2)
        guess=in_list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return str(item)+' is not in  list '+str(in_list)

def pythagorian_triangle(n):
    diff,double,summ=[],[],[]
    for i in range(1, n + 5):
        for j in range(1, i):
            if len(diff) != n:
                diff.append(min([abs(i*i-j*j), 2*i*j]))
                double.append(max([abs(i*i-j*j), 2*i*j]))
                summ.append(i*i + j*j)
                if len(diff) > 1:
                    for k in range(len(diff) - 1):
                        if diff[-1]<diff[k]:
                            diff[-1],diff[k]=diff[k],diff[-1]
                            double[-1],double[k]=double[k],double[-1]
                            summ[-1],summ[k]=summ[k],summ[-1]
    c=1
    for i,j,k in zip(diff,double,summ):
        if n!=0:
            print(str(c)+". ({0} {1} {2})".format(i,j,k))
            n-=1
            c+=1

def reverse(arr):
    #la-la-la
    return arr[::-1]

def numsys(source_number, numsys_sn, numsys_rn):
    result_number , counttmp , decimal_number = [] , 0 , 0
    source_number = reverse(str(source_number))
    num_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
            '6':6,'7':7,'8':8,'9':9,'A':10,'B':11,
            'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,
            'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,
            'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,
            'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

    if numsys_sn < 37 and numsys_rn < 37:
        if numsys_sn<=10:
            for i in source_number:
                decimal_number+=num_dict.get(i)*numsys_sn**counttmp
                counttmp+=1
                
        elif numsys_sn>10:
            for i in source_number:
                decimal_number+=num_dict.get(i)*numsys_sn**counttmp
                counttmp+=1
            
        if numsys_sn == 10 or i!=0:
            while decimal_number!=0:
                result_number.append(str(num_dict[str(decimal_number%numsys_rn)]))
                decimal_number //= numsys_rn
            
        print(''.join(reverse(result_number)))

    else:
        print('Too big numeral system')

def fact(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value

def list_generator(n, m):
    arr = list()
    i = 1
    while len(arr) <= n:
        a = random.randint(1, m)
        for _ in range(a):
            arr.append(i)
            i += random.randint(1, 5)
    return arr