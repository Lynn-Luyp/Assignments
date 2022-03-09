import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime



%matplotlib

'''%matplotlib inline'''


def add_numbers(a,b):
    return a+b


def f(x,y,z):
    return (x+y)/z

a=5
b=6
c=7.5
result=f(a,b,c)


x=5
y=7
if x>5:
    x+=1
    y=8
    
    
a=np.random.randn(100,100)   # 添加注释
%timeit np.dot(a,a)

a=[1,2,3]
b=a
c=a.copy()
a.append(4)
print(b)
print(c)


判断数据类型
a=5
isinstance(a,int) 

a=5;b=4.5
isinstance(a,(int,float))

a=[1,2,3]
b=a
c=list(a)
a is b


def add_and_maybe_multiply(a,b,c=None):
    result=a+b
    if c is not None:
        result=result*c
    
    return result

sequence=[1,2,None,4,None,5]
total=0
for value in sequence:
    if value is None:
        continue;
    else:
        total+=value
print(total)

sequence=[1,2,0,4,6,5,2,1]
total_until_5=0
for value in sequence:
    if value==5:
        break
    total_until_5+=value

seq=[1,2,3,4]
for i in range(len(seq)):
    val=seq[i]
    print(val)

a=[1,2,3,4]


some_list=['zero','one','two']
mapping={}
for i,v in enumerate(some_list):
    mapping[v]=i


empty_dict={}
d1={'a':'value','b':'lyp','pig':'zll'}


mapping={}
key_list=['1','2','3']
value_list=['one','two','three']
for key,value in zip(key_list,value_list):
    mapping[key]=value


words=['apple','bat','bar','atom','book']
by_letter={}
for word in words:
    letter=word[0]
    if letter not in by_letter:
        by_letter[letter]=[word]
    else:
        by_letter[letter].append(word)
        
words=['apple','bat','bar','atom','book']
by_letter={}
for word in words:
    letter=word[0]
    by_letter.setdefault(letter,[]).append(word)
    
strings=['a','as','bat','car','dove','python']

all_data_name=[]
all_data=[['John','Emily'],['Stevene','Mariaee']]
for names in all_data:
    for name in names:
        if name.count('e')>2:
            all_data_name.append(name)
            
all_data_name=[]
all_data=[['John','Emily'],['Stevene','Mariaee']]
for names in all_data:
    name_e=[name for name in names if name.count('e')>2]
all_data_name.extend(name_e)

result=[name for names in all_data for name in names if name.count('e')>2]

 
some_tuples=[(1,2,3),(4,5,6),(7,8,9)]
flattened=[x for tup in some_tuples for x in tup]
print(flattened)


def my_func_test(a,b,c=1):
    if c==1:
        return 0
    else:
        return a+b+c;
    
    
a=[]
def func():
    for i in range(5):
        a.append(i)


strings=['foo','card','bar','aaaa','abab']
strings.sort(key=lambda x:len(set(list(x))))
strings.sort(key=lambda x:len(x))


def attempt(x):
    try:
        return float(x)
    except:
        return x
    
def temp(x):
    try:
        print(int(x))
    except:
        print(x)
    else:
        print(1)
    finally:
        print('end')
    
numpy 
np.zeros(10)


names=np.array(['Bob','Joe','Will'])
names=='Bob'
data=np.random.randn(3,4)

切片过程用"|"或者"&"
data[(names=='Bob')|(names=='Joe')]


xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])

result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]

result_temp=np.where(cond,xarr,yarr)


values=np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])


position=0
N=1000
new_pos=[]
for i in range(N):
    position+=np.random.randint(0,2)*2-1
    new_pos.append(position)


sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=pd.Series(sdata)
states=['California','Ohio','Oregon','Texas']

sdata={'Ohio':[35000],'Texas':[71000],'Oregon':[16000],'Utah':[5000]}

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)

pd.DataFrame(data,columns=['year','state','pop'])

frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])

val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])


pop={'Nevada':{2001:2.4,2002:2.9},
     'Ohio':{2000:1.5,2001:1.7,2002:3.6}}

frame3=pd.DataFrame(pop)

labels=pd.Index(np.arange(3))
obj2=pd.Series([1.5,-2.5,0],index=labels)


obj=pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])

frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['Ohio','Texas','California'])
frame2=frame.reindex(['a','b','c','d'])

states=['Texas','Uath','California']
frame.reindex(columns=states)

obj=pd.Series(np.arange(5),index=['a','b','c','d','e'])


data=pd.DataFrame(np.arange(16).reshape(4,4),index=['Ohio','Colorado','Uath','New York'],columns=['one','two','three','four'])

data.drop(['Colorado','Ohio'])

data.drop(['two'],axis=1)
data.drop(['one','two'],axis='columns')


obj=pd.Series(np.arange(4),index=['a','b','c','d'])



ser=pd.Series(np.arange(3))

ser2=pd.Series(np.arange(3),index=['a','b','c'])


s1=pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2=pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])


df1=pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))

df2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))

arr=np.arange(12).reshape(3,4)

frame=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])



f = lambda x:x.max() - x.min()

format_percent = lambda x: '%.2f' %x


obj = pd.Series(range(4),index = ['d','a','b','c'])

frame.sort_index(axis=1)

obj=pd.Series([7,-5,7,4,2,0,4])



string_data=pd.Series(['aardvark','artichoke',np.nan,'avocado'])


data=pd.DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3]])


data = pd.DataFrame({'food':['bacon','pulled pork','bacon'],'ounces':[4,3,12]})

meat_to_animal = {'bacon' : 'cow',
                  'pulled pork' : 'pig'}

frame=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])

transform = lambda x: x[:4].upper()

data = pd.DataFrame(np.random.randn(1000,4))

df = pd.DataFrame(np.arange(20).reshape(5,4))



val = 'a,b, guido'


data = {'Dave': 'dave@google.com','Steve':'steve@gmail.com',
        'Rob':'rob@gmail.com','Wes':np.nan}



data = pd.Series(np.random.randn(9),index = [['a','a','a','b','b','c','c','d','d'],
                                             [1,2,3,1,3,1,2,2,3]])



frame = pd.DataFrame({'a':range(7),'b':range(7,0,-1),
                      'c':['one','one','one','two','two','two','two'],
                      'd':[0,1,2,0,1,2,3]})


frame2 = frame.set_index(['c','d'])



s1 = pd.Series([0,1],index = ['a','b'])
s2 = pd.Series([2,3,4],index = ['c','d','e'])
s3 = pd.Series([5,6],index = ['f','g'])


pd.concat([s1,s2,s3],keys = ['one','two','three'])

data = pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['Ohio','Colorado'],name='state'),
                    columns=pd.Index(['one','two','three'],name='number'))



df = pd.DataFrame({'left':result,'right':result+5},columns=pd.Index(['left','right'],name='side'))


df.unstack()


df = pd.DataFrame({'key':['foo','bar','baz'],
                   'A':[1,2,3],
                   'B':[4,5,6],
                   'C':[7,8,9]})

pd.melt(df,id_vars=['key'],value_vars=['A','B'])


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,4)
plt.plot([1.5,3.5,-2,1.6])
plt.plot(np.random.randn(50).cumsum(),'k--')




fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())


ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'],
                            rotation =  30,fontsize = 'small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

rect = plt.Rectangle((0.2,0.75), 0.4, 0.15, color = 'k',alpha = 0.3)


ax.add_patch(rect)



s = pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))


fig,axes = plt.subplots(2,1)
data = pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))


df=pd.DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'],columns=pd.Index(['A','B','C','D'],name='Genus'))


comp1 = np.random.normal(0,1,size=200)
comp2 = np.random.normal(10,2,size=200)
values = pd.Series(np.concatenate([comp1,comp2]))

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                'ley2':['one','two','one','two','one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)})

a = df['data1'].groupby(df['key1'])



for name,group in df.groupby('key1'):
    print(name)

grouped = df.groupby(df.dtypes,axis=1)
for dtype,group in grouped:
    print(dtype)
    print(group)


grouped = df.groupby('key1')

grouped['data1'].quantile(0.9)


def top(df,n = 5,column = 'data1')


def top(df,n = 5,column = 'data1'):
    return df.sort_values(by=column)[-n:]



s = pd.Series(np.random.randn(6))


grouped.apply(lambda x:x['data1'].mean())

from pandas.tseries.offsets import Hour,Minute


pd.date_range('2000-01-01','2000-01-03 23:59',freq = '4h')


ts = pd.Series(np.random.randn(4),
               index = pd.date_range('1/1/2000',periods=4,freq = 'M'))



from pandas.tseries.offsets import Day,MonthEnd


ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000',periods=20,freq='4d'))


rng = pd.date_range('3/9/2012 9:30',periods=6,freq='D')


frame = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2000',periods=2,freq='W-WED'),
                     columns=['Colorado','Texas','New York','Ohio'])



frame = pd.DataFrame(np.random.randn(24,4),index = pd.period_range('1-2000','12-2001',freq = 'M'),columns = ['A','B','C','D'])

values = pd.Series(['apple','orange','apple','apple']*2)


fruits = ['apple','orange','apple','apple']*2

df = pd.DataFrame({'fruit':fruits,
                  'basket_id':np.arange(N),
                  'count':np.random.randint(3,15,size = N),
                  'weight':np.random.uniform(0,4,size = N)},
                  columns = ['basket_id','fruit','count','weight'])


categories = ['foo','bar','baz']
codes = [0,1,2,0,0,1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)


df = pd.DataFrame({'key':['a','b','c']*4,
                   'value':np.arange(12.)})


N = 15
times = pd.date_range('2017-05-20 00:00',freq = '1min', periods = N)
df = pd.DataFrame({'time':times,
                   'value':np.arange(N)})





