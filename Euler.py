from EulerUtils import *
def problem_1():
    x=0
    for i in range(0,1000,3):
        if not (i % 3 and i % 5): x+=i
    return x

def problem_2():
    s=0
    x=[1,1]
    while x[1] < 4000000:
        n=sum(x)
        if not n % 2: s+=n
        x=[x[1],n]
    return s

def problem_3():
    n=600851475143
    for i in Primes(2,n):
        if not n % i: n = n / i
        if n==1:
            return i
            
        
def problem_4():
    D=range(999,99,-1)
    for i in xrange(998000,0,-1):
        s=str(i)
        if s==s[::-1]:
            for t in D:
                if not i % t and len(str(i/t))==3:
                    return s
                    
def problem_5():
    p=1  
    for i in range(1,21):
        p=LCM(i,p)
    return p


def problem_6():
    x,y=0,0
    for i in range(1,101):
        x+=i**2
        y+=i
    y=y**2
    return y-x

def problem_7():
    i=0
    for x in Primes(2,1000000000):
        i+=1
        if i==10001:
            return x

def problem_8():
    n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    k=0
    for i in range(0,len(n)-4): 
        t=1
        for x in n[i:i+5]: t=t*int(x)
        if t>k: k=t
    return k

def problem_9():
    for c in range(0,1000):
        for a in range(0,c-1):
            b=(c**2-a**2)**.5
            if not b%1 and a>b and c+a+b==1000: return int(a*b*c)
                    
            

def problem_10():
    s=0
    for x in Primes(2,2000000):
        s+=x
    return s

def problem_11():
    import csv
    Max=0
    x = list(csv.reader(open('data/data_11.csv'), delimiter=' '))
    for i in range(0,len(x)):
        row = x[i]        
        for n in range(0,len(row)):
            Mult=[]
            #to the right
            Mult.append(row[n:n+4])
            #down
            y=[]
            for o in range(i,min(i+4,len(x))):
                y.append(x[o][n])
            Mult.append(y)
            #down and to the right
            y=[]
            for o in range(0,min(4,len(x)-i,len(row)-n)):
                y.append(x[i+o][n+o])
            Mult.append(y)            
            #down and to the left
            y=[]
            for o in range(0,min(4,len(x)-i,n+1)):
                y.append(x[i+o][n-o])
            Mult.append(y)
            for r in Mult:
                if len(r)==4:
                    Prod=1
                    for q in r:
                        Prod=Prod*int(q)
                    if Prod>Max: Max=Prod
    return Max


def problem_12():
    Sum,d=0,1
    while True:
        Sum+=d
        d+=1
        if NumFactors(Sum)>=500:
            return Sum


def problem_13():
    f = open('data/data_13.csv','r').readlines()
    Sum,Answer=0,[]
    for i in range(0,50):
        for line in f:
            Sum+= int(line.strip()[49-i])
        Answer.append(str(Sum%10))
        Sum=(Sum-Sum%10)/10
    for i in str(Sum)[::-1]:
        Answer.append(i)
    Answer.reverse()
    return ''.join(Answer)[0:10]

def problem_14():
    t={1:0}
    for n in xrange(1,1000000):
        c,d=0,n
        while n not in t:
            if n%2:n=3*n+1
            else:n=n/2
            c+=1
        c+=t[n]
        t[d]=c
    x=[1,1]
    for q in t:
        if t[q]>x[0]:x=[t[q],q]
    return x[1]


def problem_14B():
    t={1:0}
    for n in xrange(1000000,0,-1):
        seq=[n]
        while seq[-1] not in t:
            if seq[-1]%2:seq.append(3*seq[-1]+1)
            else:seq.append(seq[-1]/2)
        c=len(seq)-1
        q=t[seq[-1]]
        for s in seq[0:-1]:
            t[s]=c+q
            c-=1
    x=[1,1]
    for q in t:
        if t[q]>x[0]:x=[t[q],q]
    return x[1]
            
def problem_15():
    from math import factorial
    return factorial(40)/factorial(20)**2
    
def problem_16():
    s=0
    for x in str(2**1000):
        s+=int(x)
    return s

def problem_17():
    D=[3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    H=10
    T=[6,6,5,5,5,7,6,6]
    s=0
    for c in range(0,10):
        h=H+D[c-1]
        if c==0: h=0
        s+=max(0,h-3)
        for i in range(0,len(D)): s+=(D[i]+h)
        for q in range(0,len(T)):
            s+=T[q]+h
            for x in range(0,9): s+=(T[q]+D[x]+h)
    s+=11
    return s


def problem_18():
    import csv
    x = list(csv.reader(open('data/data_18.csv'), delimiter=' '))
    s=[int(x[0][0])]
    for row in x[1::]:
        q=[]
        for y in range(1,len(row[1:])):
            q.append(max(s[y-1],s[y])+int(row[y]))
        s =[s[0]+int(row[0])]+q+[s[-1]+ int(row[-1])]
    return max(s)      
    
def problem_19():
    D=[31,28,31,
        30,31,30,
        31,31,30,
        31,30,31]
    d,n=0,0
    for i in range(0,101):
        if (not (1900+i)%4 and (1900+i)%100) or not (1900+i)%400: D[1]=29
        else: D[1]=28
        for t in D:             
            if not (d-1)%7 and i>=1:
                n+=1
            d+=t
             
    return n

def problem_20():
    from math import factorial
    s=0
    for i in str(factorial(100)):s+= int(i)
    return s

def problem_21():
    s,i=0,0
    while i <=10000:
        x=sum(Factor(i)[0:-1])
        t=sum(Factor(x)[0:-1])
        if t==i and i!=x:          
            s +=(i+x)
            i=x+1
        i+=1
    return s

def problem_22():
    import csv
    x = list(csv.reader(open('data/data_22.csv'), delimiter=','))[0]
    x.sort()
    s=0
    for i in range(0,len(x)):
        c=0
        for t in x[i]:
            c+=(ord(t)-64)
        s+=c*(i+1)
    return s

def problem_23():
    #crappy
    a,s=dict.fromkeys(Abundant(0,28123),1),0
    for i in xrange(0,28123):
        t=True        
        for x in a:
            if x>i:break
            if a.get(i-x):
                t=False
                break
        if t: s+=i
    return s

def problem_24():
    from math import factorial
    n,d=999999,0
    D=range(0,10)
    for i in range(1,10)[::-1]:
        y=factorial(i)
        x=n/y
        d=d*10+D.pop(x)          
        n=n-(x*y)
    d=d*10+D[0]
    return d

def problem_25():
    from math import log10
    a,b=log10((1+5**.5)/2),log10(5)/2
    n=2
    while True:
        if n*a-b>=999:return n
        n+=1
        
def ten(n):
    i=1
    while True:
        if n<=10**i: return 10**i
        i+=1

def divide(x,y):
    while x>y:y=y*10
    return y/x,y%x

def problem_26():
    Max=[0,0]
    for i in range(2,1000):
        q,t=divide(i,ten(i))
        x=[[q,t]]
        while t:
            q,t=divide(i,t)            
            if x.count([q,t])==0:x.append([q,t])
            else:
                if len(x)-x.index([q,t])>Max[0]:Max=[len(x)-x.index([q,t]),i]
                break
    return Max[1]

def problem_27():
    Max=[0,[0,0,0]]
    P=dict.fromkeys([x*i for x in Primes(3,1000) for i in [1,-1]])
    for p in P:
        for t in range(-1000,1000):
            x=0
            while True:
                if x**2+t*x+p*i in P:x+=1
                else: break
            if x>Max[0]: Max=[x,[p,i,t]]
    t=1
    for i in Max[1]: t=t*i
    return t

def problem_28():
    s=1
    for i in range(3,1002,2): s+=4*i**2-6*(i-1)
    return s

def problem_29():
    return len(set([i**t for i in range(2,101) for t in range(2,101)]))

def problem_30():
    i=2
    TotalSum=0
    while True:
        Sum=0
        for x in str(i): Sum+=int(x)**5
        if Sum==i: TotalSum+=Sum
        i+=1
        if i>=354294: return TotalSum

    

def problem_31():   
    def Loop(m,x):
        C,s=[200,100,50,20,10,5,2,1],0
        if x==7: return 1
        for i in range(x,8):
            if m-C[i]==0:s+=1
            if m-C[i]>0:s+=Loop(m-C[i],i)
        return s
    return Loop(200,0)
        
def problem_32():
    Sum=0
    g=set('123456789')
    for i in range(2340,9999):
        if len(str(i))==len(set(str(i))):
            for x in Factor(i)[1:-1]:
                d= set(str(i)+str(x)+str(i/x))
                if g==d:
                    Sum+=i
                    break
    return Sum


def problem_33():
    num,den=1,1
    for i in range(10,100):
        if i%10:
            a,b,=i/10,i%10
            x=set(range(i+1,(a+1)*10)+range((a+1)*10+1,100,10)+range(b*10+1,(b+1)*10)+range(i+10,100,10))
            if i in x: x.remove(i)
            for t in x:
                frac=float(i)/t
                c,d=t/10,t%10
                r=[[a,c,b,d],[a,d,b,c],[b,c,a,d],[b,d,a,c]]
                for q in r:
                    if q[0]==q[1] and frac==float(q[2])/q[3]:
                        num,den=num*i,den*t
                        break
    return Reduce(num,den)[1]
            
def problem_34():
    from math import factorial
    T=0
    for i in xrange(3,100000):
        s=0
        for x in str(i):
            s+=factorial(int(x))
            if s>i:break
        if s==i:
            T=T+i
    return T

def problem_35():
    x=dict.fromkeys(Primes(1,1000001),1)
    c=0
    for t in x:
        m=True
        for q in range(0,len(str(t))):
            if int(str(t)[q::]+str(t)[0:q]) not in x:
                m=False
                break
        if m:
            c+=1
    return c

def problem_36():
    s=0
    for i in xrange(1,1000001,2):
        if str(i)==str(i)[::-1] and bin(i)[2::]==bin(i)[2::][::-1]:
            s+=i
    return s

def problem_37():
    X=dict.fromkeys(Primes(1,1000001),1)
    s,Sum=0,0
    for i in [x for x in X if x>8]:
        p=True        
        for x in range(0,len(str(i))):
            if int(str(i)[0:len(str(i))-x]) not in X or int(str(i)[x::]) not in X:
                p=False
                break
        if p:
            s+=1
            Sum+=i
            if s>=11:return Sum

            
def problem_38():
    T=set([])
    for i in xrange(1,10000):
        t=str(i)
        if len(set(t))==len(t) and '0' not in t:
            n=2
            while len(set(t))==len(t) and '0' not in t:
                if len(t)==9: T.add(t)
                t+=str(n*i)
                n+=1
    return max(T)

def problem_39():
    M=[0,0]
    for x in range(1,1000):
        n=0
        for i in range(1,x/3):
            for t in range(i,(x-i)/2):
                if i**2+t**2==(x-i-t)**2:n+=1
        if n>M[0]:
            M=[n,x]
    return M[1]


def problem_40():
    i,t,s=1,1,''
    while len(s)<1000000:
        s+=str(i)
        i+=1
    for i in range(0,7):
        t=t*int(s[10**i-1])
    return t

def problem_41():
    from itertools import permutations
    x=range(7,0,-1)
    for q in permutations(x):
            if len(set(PrimeFactor(getnum(q))))==2: return getnum(q)
def problem_42():
    import csv
    x = list(csv.reader(open('data/data_42.csv'), delimiter=','))[0]
    t=dict.fromkeys([n*(n+1)/2 for n in range(1,40)],1)
    n=0
    for w in x:
        c=0
        for l in w: c+=(ord(l)-64)
        if c in t:n+=1
    return n



def problem_43():
    from itertools import permutations
    def Loop(l,n):
        p=list(Primes(3,17))
        d,poss=set(range(10)),[]
        if n<=5:
            for t in l:
                for r in d^set(t):
                    if not getnum(t[-2::]+(r,))%p[n]: poss.append(t+(r,))
            n+=1
            return Loop(poss,n)
        elif l: return getnum(l[0])
        return 0
    s=0
    
    for t in filter(lambda x: not getnum(x) % 2,permutations(range(0,10),4)):
        s+=Loop([t],0)   
    return s


def problem_44():
    t = map(lambda n: n*(3*n-1)/2,xrange(1,3000))
    T=dict.fromkeys(t,1)
    for i in xrange(0,1500):
        for q in t[i+1:-1]:
            if t[i]+q in T and q-t[i]in T:
                return q-t[i]

def problem_45():
    def Hexagonal(m,x):
        for i in xrange(m,x+1): yield i*(2*i-1)
    def isTriangle(n): return not(-1+(1+8*i)**.5)/2%1
    def isPentagonal(n): return not (1+(1+24*i)**.5)/6%1
    for i in Hexagonal(144,10**5):
        if isTriangle(i) and isPentagonal(i): return i

def problem_46():
    n,x=1,10000
    P=dict.fromkeys(Primes(n,x))
    C=[t for t in xrange(3,x,2) if t not in P]
    for r in C:
        for g in xrange(1,int(r**.5)+1):
            if r-2*g**2 in P: break
        else: return r

def problem_47():
    for i in xrange(644,10**6):
        for t in range(0,4):
            if len(set(PrimeFactor(i+t)[1::]))!=4: break
        else: return i

def problem_48():
    s=0
    for i in xrange(1,1001):
        s+=i**i
        s=s%10**10
    return s
def problem_49():
    P=[x for x in Primes(1000,10000)]
    for p in xrange(0,len(P)):
        c=str(P[p])
        for q in range(1,3):
            z=P[p]+q*3330
            if z in P and set(str(P[p]))==set(str(z)): c+=str(z)
        if len(c)==12 and c!='148748178147': return c

def problem_50():
    P=list(Primes(3,1000001))
    seq=[3]
    for i in P:
        if seq[0]+i>1000000:break
        seq.insert(0,seq[0]+i)
    Max=0
    for n in range(0,4):
        for t in seq:
            if t-P[n] in P:
                Max=max(Max,t-P[n])
                break
    return Max       

def f(n): #goes with problem 51
    #ugly as sin
    l,s,digs=[],str(n),'0123456789'
    for d in digs:
        if d in s:
            l.append(s.replace(d,'*'))
            if s.count(d)>1:
                for i in range(len(s)):
                    if s[i]==d:l.append(s[0:i]+'*'+s[i+1::])
                if s.count(d)>2:
                    e=[]
                    perm=[[0,1],[0,2],[1,2]]
                    for i in range(len(s)):
                        if s[i]==d:e.append(i)
                    for i in perm:
                          t=s
                          for q in i:
                              t=t[0:e[q]]+'*'+t[ e[q]+1::]
                          l.append(t)
                    if s.count(d)>3:
                        e=[]
                        perm=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
                        for i in range(len(s)):
                            if s[i]==d:e.append(i)
                        for i in perm:
                              t=s
                              for q in i:
                                  t=t[0:e[q]]+'*'+t[e[q]+1::]
                              l.append(t)
        
    return l





def problem_51():
    P=Primes(100000,1000000)
    l=[]
    p=[x for x in P if len(str(x))-2>len(set(str(x)))]
    for i in p:
        l+=f(i)
    for i in set(l):
        if l.count(i)==8:
            for k in range(10):
                e=int(str(i).replace('*',str(k)))
                if e in p: return e
def problem_52():
    def f(n,m):
        if len(set(n))==len(set(m)):
            for i in set(n):
                if n.count(i)!=m.count(i):return 0
            return 1
        return 0

    for i in range(1,60):
        #for some reason the # must be divisible by 9
        for t in xrange(10**i+8,10**(i+1)/6,9):
            for e in range(2,7):
                if not f(str(t),str(t*e)): break
            else: return t    

            
def problem_53():
    from math import factorial as fact
    c=0
    for n in range(1,101):
        for r in range(1,n):
            if fact(n)/(fact(r)*fact(n-r))>1000000:c+=1
    return c

def problem_54():
    import csv
    def Winner(m,n):
        for i in range(len(m)):
            if m[i]>n[i]: return 1
            if n[i]>m[i]: return 0
        return 0

    def GetCards(l):
        Rank={'T':10,'J':11,'Q':12,'K':13,'A':14}
        h=[]
        for i in l:
            if i[0] not in 'TQJKA': h.append(int(i[0]))
            else:h.append(Rank[i[0]])
        return h,[x[1] for x in l]
            
    x = list(csv.reader(open('data/data_54.csv'), delimiter=' '))
    s=0
    for t in x:
        s+=Winner(HandValue(GetCards(t[0:5])),HandValue(GetCards(t[5::])))
    return s

def problem_55():
    c=0
    for i in xrange(1,10001):
        t=i
        for g in xrange(0,50):
            t=t+int(str(t)[::-1])
            if str(t)==str(t)[::-1]: break
        if g==49:c+=1
    return c

def problem_56():
    x=0
    for a in range(1,100):
        for b in range(1,100):
            s=0
            for i in str(a**b):s+=int(i)
            x=max(s,x)
    return x
def problem_57():
    n,d,c=[3,7],[2,5],0
    for x in xrange(1000):
        n,d=[n[1],2*n[1]+n[0]],[d[1],2*d[1]+d[0]]
        if len(str(n[1]))>len(str(d[1])):c+=1
    return c

       
def problem_58():
    c=[0,1]
    for i in xrange(3,200000,2):
        c[1]+=4
        for t in xrange(i**2-(i-1),i**2-3*i+2,-(i-1)):
            if isPrime(t): c[0]+=1
        if c[1]/c[0]>=10:return i
    return c

def problem_59():
    import csv
    from itertools import permutations
    x = list(csv.reader(open('data/data_59.csv'), delimiter=','))[0]                 
    for k in permutations(range(97,123),3):
        s=''
        for i in range(len(x)):
            c=int(x[i])^k[i%3]
            if c>126:break
            s+=chr(c)
        if ' the ' in s: return sum([ord(i) for i in s])
        
def problem_60():
    P=dict.fromkeys([str(x) for x in Primes(2,1000000)])
    C,T=[],{}
    for p in P: 
        for i in range(1,len(p)):
            if p[0:i] in P and p[i::] in P and p[i::]+p[0:i] in P:
                C.append(int(p[0:i])+int(p[i::]))
                T[int(p[0:i])+int(p[i::])]=p
    C.sort()

    return len(C)

def problem_61():
    pass

def problem_62():
    n,N=0,{}
    while True:
        s=str(n**3)
        t=''.join(sorted(s))
        try:
            N[t].append(s)
            if len(N[t])==5:
                return min(N[t])
        except KeyError:N[t]=[s]
        n+=1
        if not n%5000:
            print n

def problem_63():
    p,b,n=1,1,0
    while True:
        if b**p>=10**p:
            p+=1
            b=1
        elif b**p>=10**(p-1):
            n+=1
        b+=1
        if p>100:return n

def problem_63B():
    from math import log10
    n = [int(1.0/(1-log10(i))) for i in range(1,10)]
    return sum(n)

#not finished

def problem_66():#Pell Equations, same crap as 64/65 continued fractions
    d=[]        #brute force method takes ages..probably would crap out too 
    Nums=range(1,1000)
    for i in range(1,32):
        Nums.remove(i**2)
        
    for D in Nums:
        y=1
        while True:
            n=(D*y**2+1)**.5
            if int(n)==n:
                d.append([D,n])
                print D,y,n
                break
            y+=1
    def f (n):
        return n[1]
    return max(d,key=f)
    
def problem_67():
    import csv
    x = list(csv.reader(open('data/data_67.csv'), delimiter=' '))
    s=[int(x[0][0])]
    for row in x[1::]:
        q=[]
        for y in range(1,len(row[1:])):
            q.append(max(s[y-1],s[y])+int(row[y]))
        s =[s[0]+int(row[0])]+q+[s[-1]+ int(row[-1])]
    return max(s) 

def problem_68():
    from numpy import array; from itertools import permutations
    def f(n): return n[0]
    MAX,n,result=(0),0,''
    for outer in permutations(range(6,11)):
        for inner in permutations(range(1,6)):
            config=inner+outer                        
            key,ps=array([5,1,0]),0
            n+=1
            for i in range(5):
                s=0
                for x in key: s+=config[x]
                if s==ps or ps==0: ps,m=s,True
                else: m=False;break
                key+=1; key[1]=key[1]%5
            if m:
                key,s=array([5,1,0]),[]
                for r in range(5):
                    t=[]
                    for k in key: t.append(config[k])
                    s.append(t)
                    key+=1; key[1]=key[1]%5
                s.reverse()
                x=s.index(min(s, key=f))
                C=s[x::]+s[0:x]
                MAX=max(MAX,C)  
    for i in MAX:
        for t in i: result+=str(t)
    return result

def problem_69():
    h={}
    for i in range(2,1000000):
        h[i]=set(PrimeFactor(i))
    return

def problem_73():
    from itertools import combinations
    s = set([])
    x= 0
    for n,d in combinations(range(12001),2):
        if d:
            f = float(n)/d
            if f > 1./3 and f<1./2:
                s.add(f)
        x+=1
        if not x%1000000: print x
    return len(s)
    
def problem_74():
    from math import factorial as fact
    cnt = 0
    c=0
    for i in xrange(1000000):
        c+= 1
        if not c%10000: print c,cnt
        l = []
        while i not in l:
            l.append(i)
            reduce(lambda a,b: a + fact(int(n)),string(i))
            i = sum([fact(int(n)) for n in str(i)])
        if len(l)==60:cnt+=1

    return cnt

def problem_96():
    from Sudoku import Solve
    s=0
    for grid in file('data/data_96.txt').read().strip().split('Grid')[1::]:
        P=[int(a) for a in grid.strip().replace('\n','')[2::]]
        s+=getnum(Solve([P])[0:3])
    return s

if __name__ == '__main__':
    from timeit import Timer
    for n in range(1,63):
        t = Timer("problem_%d()"%n, "from __main__ import problem_%d"%n)
        print "problem_%d: %.4f" % (n,t.timeit(number=1)*1000)
