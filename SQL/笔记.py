'''P10'''

登录 MySQL 两种方法：
    1. 通过开始的 MySQL 自带登录端口登录
    2. windows+r 输入cmd后：输入 mysql -hlocalhost -P3306 -uroot -proot
    3. 可以简写为 mysql -uroot -proot

'''P12'''

结尾记得; 或者/g
显示数据库： show databases;
进去其中一个数据库： uese test;
显示库中的表格： show tables;
显示另外一个库的数据： show tables from mysql;
查看库位置： select database();
创建表： create table stuinfo(
				id int # 名称和类型
				name varchar(20));# 名称，类型
查看表的结构：desc stuinfo;
查看表中是否有数据：select * from stuinfo;
表中插入数据：insert into stuinfo(id,name) values(1,'lyp')
              insert into stuinfo(id,name) values(2,'zll')
修改数据：update stuinfo set name='lch' where id=1;
删除数据：delete from stuinfo where id=1;

'''P13'''

查询当前版本：exit
              mysql --version #不用加括号
              mysql -V

'''P14常见命令'''
1. 查看当前所有的数据库
show databases;
2. 打开指定的库
use+库名;
3. 查看当前库的所有表
show tables;
4. 查看其它库的所有表
show tables from 库名;
5. 创建一个表
create table 表名(
    列名，列类型，
    列名，列类型，
    ……;) #最后一个不用加逗号
6. 查看表结构
desc 表名；
7. 查看服务器的版本
方式一：登录到mysql服务端
select version();
方式二：没有登录到mysql服务端
mysql --version
mysql -V

'''P15语法规范'''
1. 不区分大小写，但是建议关键字大写，表名，列名小写
2. 每条命令最好用；结尾
3. 每条命令根据需要，可以进行缩进或者换行
    SELECT
    *
    FROM
    stuinfo;
4. 注释
        单行注释：#注释文字
        单行注释：-- 注释文字 #要加一个空格' '
        多行注释：/*注释文字*/
        
        
'''P16图形用户化界面'''
sqlyog字体编辑：1. 工具-首选项-字体编辑器
               2. ctrl+鼠标滑轮

'''P17'''
每条语句之后加上；

'''P18'''
DQL: Data Query Language(数据查询语言)
DWL：Data Manipulation Language (数据操作语言)
DDL: 数据定义语言 Data Define Language(数据定义语言)
TCL: Transaction Control Language(事物控制语言)

salary 月薪
commission_pct 奖金率(年薪=月薪*12)(年终奖=年薪*commission_pct)

'''P19'''
DQL: 
# 进阶1： 基础查询
'''
语法：
select 查询列表 form 表名；

类似于： system.out.printin;

特点：

1. 查询列表可以是：表中的字段
2. 查询的结果是一个虚拟的表格
'''
use myemployees;(打开某个数据库)(库名！)

1. 查询表中的单个字段

select last_name from employees;

2. 查询表中的多个字段

select last_name,salary,email from employees;

3. 查询表中的所有字段

    1. select (双击对象) from 表名;
    2. select * from employees;

字段名直接引用会加着重号'`'，可以用于区分字段：
    select `select`

4. 查询常量值
select 100;
select 'lyp';

5. 查询表达式
select 100*90;
select 100%98;

6. 查询函数

select version():

7. 起别名
    1. 便于理解
    2. 如果要查询的字段有重名的情况，使用别名可以区分开来

方式一：使用 as
select 100&98 as 结果；
select last_name as 姓， first_name as 名 from employees;

方式二：使用空格
select last_name 姓,first_name 名 from employees；

example: 查询salary,显示结果为out put
    select salary as `out put` from employees;
    select salary as "out put" from employees;
    #着重号是用于区分标签的

8. 去重

example: 查询员工表中涉及到的所有的部门编号

select departments_id from employees;

关键字：distinct 
select distinct departments_id from employees;

9. +号的作用
    '''一个功能：运算符
    select 100+90; 两个操作数都为数值型，做加法运算
    select '123'+90; 有其中一个为字符型，试图将字符型数值转换为数值型
                    如果转换成功，继续加法运算
                    如果转换失败，则将字符型数值换为0
    select  'lyp' + 90;
    select null+10; 只要其中一方为null, 则结果肯定为null;'''

example: 查询员工名和姓连接成一个字段，并显示为 姓名

select last_name+first_name as 姓名 from employees;

函数 concat 用于 mysql 拼接字段
select concat ('a','b','c') as result;

'''P27作业'''
1. 下面语句是否可以执行成功
select last_name,job_id,salary as sal form employees;
    No
    '''select concat(,) as sal from employees;'''
    
2. -
select * from employees;
    Yes

3. 找出下列语句的错误
select employee_id, last_name,salary *12 "ANNUAL SALARY" from employees;
    改为 select employee_id, last_name,salary *12 "ANNUAL SALARY" from employees;

4. 显示表departments的结构，并查询其中的所有数据
show departments;
    '''DESC departments;'''

select * from departments;

5. 显示表employees中的全部jobs_id（不能重复）
select distict jobs_id from employees;

6. 显示表employees中的全部列，各个列之间用逗号连接，列头显示成OUT_PUT
select concat(*,",") as "OUT_PUT" from employees;

ifnull(a,b)
a为判断的字段
b为返回的值

select ifnull(commission_pct,0) 奖金率,
        commission_pct
from employees;

'''P28'''
进阶2： 条件查询

语法：
(括号内为程序进行的顺序)
    select 
            查询列表(3)
    from
            表名(1)
    where
            筛选条件(2);

分类：
1. 按条件表达式筛选
    条件运算符： < > = != <> >= <=

2. 按逻辑表达式筛选
    逻辑运算符： && || !
                and or not(与 或 非)

3. 模糊查询
    like; between and; in; is null


1. 按条件表达式筛选

example: 查询工资>12000的员工信息

select
    concat(first_name,last_name) as "name",
    salary
from 
    employees 
where 
    salary > 12000;

select
    *
from
    employees
where
    salary>12000;

example: 查询部门编号不等于90号的员工名和部门编号

select
    concat(first_name,",",last_name),
    department_id 
from 
    employees
where
    department_id <> 90;

'''P30'''
逻辑表达式筛选
逻辑运算符：
作用： 用于连接条件表达式
    && || !
    and or not : better

&& = and
|| = or
! = not 

example1: 查询工资在10000-20000之间的员工名、工资以及奖金

select 
    concat(first_name," ",last_name) as 姓名,
    salary as 工资,
    commission_pct as 奖金
from
    employees
where
    salary <=12000 and salary >= 10000;

example2: 查询部门编号不是在90-110之间的，或者工资高于15000的员工信息

select
    concat(first_name," ",last_name)
from
    employees
where
    department_id<=90 or department_id >=110 or salary >= 15000;
    # not(department_id>=90 and department_id<=110) or salary>= 15000;

'''P31'''
模糊查询

(like,between and,in,is null|is not null)

1. like
特点：
    1. 一般和通配符搭配使用
    通配符：
        % 任意多个字符(包括0个字符)
        _ 任意单个字符
example: 查询员工名中包含字符a的员工信息

select
    concat(first_name,last_name)
from
    employees
where
    "a" in first_name;

SELECT
    *
from
    employees
where
    last_name like '%a%'；
    # 这里的百分号是通配符的意思，大小写不区分

example: 查询员工名中第三个字符为e,第五个字符为a的员工名和工资

SELECT
    concat(first_name," ",last_name),
    SALARY
from 
    employees
where
    last_name like '__e_a%';


example: 查询员工名中第二个字符为_的员工名

select
    concat(first_name," ",last_name)
from
    employees
where
    last_name like '_\_%';
    # last_name like '_$_%' escape '$';
    # escape 这里相当于注释$ 为转译符号

'''P32'''
2. betwwen and 
特点：
    1. 可以提高语句的简洁程度
    2. 包含临界值(100,120)
    2. 两个临界值不可以调换顺序(>= 前者, <= 后者)

example: 查询员工编号在100-120之间的所有的员工信息

    1. 
    select
        concat(first_name,' ',last_name)
    from
        employees
    where
        employee_id>=100 and employee_id<=120;

    2.
    select
        concat(first_name,' ',last_name)
    from
        employees
    where
        employee_id between 100 and 120;

'''P33'''
3. in
用于判断某字段的值是否属于in列表中的某一项
特点：
    1. 使用in比or提高了语句的简洁程度
    2. in列表的值类型必须统一或者兼容
    3. in列表中不可以加上通配符
        #employee_id in ("ab%")


example: 查询员工的工种编号是 IT_PROG、AD_VP、AD_PRES 中的一个的员工名和工种编号
select 
    last_name,
    job_id
from 
    employees
where
    job_id in ('IT_PROT','AD_VP','AD_PRES')

'''P34'''
4. is null
=或者<>不能用于判断null值
is null或者is not null 可以判断null值

example: 查询没有奖金的员工名和奖金率
select 
    first_name,
    commission_pct
from 
    employees
where
    commission_pct is null;

example: 查询有奖金的员工名和奖金率
select 
    first_name,
    commission_pct
from 
    employees
where
    commission_pct is not null;

'''P35'''
安全等于  <=>

example: 查询没有奖金的员工名和奖金率
select 
    first_name,
    commission_pct
from 
    employees
where
    commission_pct <=> null;

example: 查询工资为12000的员工信息
select 
    last_name,
    salary
from
    employees
where
    salary <=> 12000;

is null: 仅仅可以判断null值，可读性高
<=>: 即可以判断null值，又可以判断普通的数值，可读性低

'''P36'''
example: 查询员工号为176的员工的姓名和部门号的年薪
select 
    concat(first_name,' ',last_name),
    department_id,
    salary*12*(1+ifnull(commission_pct,0)) as 年薪
from 
    employees
where
    employee_id=176;

[TEST1]
1. 
SELECT 
    concat(first_name,' ',last_name),
    SALARY
from 
    employees
where
    salary > 12000;

2.
select 
    concat(first_name,' ',last_name),
    department_id,
    salary*12 
from
    employees
where
    employee_id=176

3.
select 
    concat(first_name,' ',last_name),
    salary 
from
    employees
where
    salary not between 5000 and 12000;

4.
select
    concat(first_name,' ',last_name),
    department_id
from 
    employees
where
    department_id=20 or department_id=50;

5.
select 
    concat(first_name,' ',last_name),
    job_id
from
    employees
where
    manager_id is null;

6.
select
    concat(first_name,' ',last_name),
    salary,
    commission_pct
from
    employees
where
    commission_pct is not null;

7.
select 
    concat(first_name,' ',last_name)
from   
    employees
where
    last_name like '__a%';

8.
SELECT
    concat(first_name,' ',last_name)
from 
    employees
where
    last_name like '%a%' and last_name like '%e%';

9.
select
    *
from 
    employees
where
    last_name like '%e';

10.
select 
    concat(first_name,' ',last_name),
    job_id 
from 
    employees
where 
    department_id between 80 and 100;

11. 
select  
    concat(first_name,' ',last_name),
    job_id,
    manager_id
from 
    employees
where 
    manager_id in (100,101,110)

'''P37'''
[test]

1. 
select 
    last_name,
    salary
from 
    employees
where
    commission_pct is null and salary<18000

2.
select 
    *
from 
    employees
where
    job_id <> 'IT' or salary = 12000;
    # not job id = 'IT' or salary = 12000;


3.
DESC department;

4.
select 
    distinct location_id
from 
    departments;

5.
commission_id is null

'''P38'''
[复习课]
一、数据库的相关概念
    一、数据库的好处
        1. 可以持久化数据到本地
        2. 结构化查询

    二、数据库的常见概念
        1. DB：     数据库，存储数据的容器
        2. DNMS:    数据库管理系统，数据库软件，数据库产品
        3. SQL:     结构化查询语言，用于和数据库通信的语言

    三、数据库存储数据的特点
        1. 数据存放到表中，表放到库中
        2. 一个库有多张表，每张表有唯一的表名
        3. 表中有一个或者多个列，列称为“字段”
        4. 表中的每一行数据相当于“对象”

    四、常见的数据库管理系统
    mysql

二、MySql的介绍
    一、MySql的背景
    二、MySql的优点
        1. 开源、免费、成本低
        2. 性能高、移植性也好
        3. 体积小，便于安装
    三、MySql的安装
    四、MySql服务的启动和停止
        方式一：通过命令行
            net start 服务名
            net stop 服务名
        方式二：计算机--右击--管理--服务
    五、MySQL服务的登录和退出
        登录：mysql 【-h主机名 -P端口号】 -u用户名 -p密码
        退出：exit或者ctrl+c

三、DQL语言
    一、基础查询语言
        1.语法：
            select 查询列表
                from 表名
        2.特点：
            1.查询列表可以是字段、常亮、表达式、函数，也可以是多个
            2. 查询结果是一个虚拟表
        3.实例
            1.查询单个字段
                select 字段名 from 表名
            2.查询多个字段
                select 字段名，字段名 from 表名
            3.查询所有字段 
                select * from 表名
            4.查询常量
                select 常量值
                注意：字符型和日期型的常量值必须用单引号引起来，数值型不需要
            5.查询函数
                select 函数名(实参列表)；
            6.查询表达式
                select 100/1234;
            7.起别名
                1. as #提高可读性
                2. ''
            8.去重
                select distinct 字段名 from 表名;
                不可以：select distinct a.b from 表名;
            9.+
                作用：做加法运算
                select 数值+数值：直接运算
                select 字符+数值：先试图将字符转换成数值
                select null+值：结果都为null
            10.【补充】concat函数
                功能：拼接字符
                select concat(字符1，字符2，字符3)
            11.【补充】ifnull函数
                功能：判断某字段或者表达式是否为null,如果为null返回指定值，否则返回原本的值
                select ifnull(commission_pct,0) from employees;
            12.【补充】isnull函数
                功能：判断某字段或者表达式是否为null,如果是，则返回为1，否则返回0

    二、条件查询语言
        1. 语法：
            select 查询列表 from 表名 where 筛选条件
        2. 筛选条件的分类
            1. 简单条件运算符
                < > = <> <=> >= <=
            2. 逻辑运算符
                and or not 
            3. 模糊查询
                like, between and, in, is null, is not null      
                like: 一般搭配通配符使用，用于判断字符型数值
                    example: select * from employees where department_id like '1__';
                通配符： %任意多个字符，_任意单个字符
                between and 
                in 
                is null/is not null: 用于判断null值

'''P39'''
进阶3：排序查询

    引入：
        select * from employees;
    语法：
        3 select 查询列表
        1 from 表
        2 where 筛选条件
        4 order by 排序列表【asc|desc】
                        # 升序|降序
                        # asc升序排列可以省略
    特点：
        1. asc代表升序，desc代表降序
        2. 不写的话默认升序(asc可省略)
        3. order by 子句中可以支持单个字段、多个字段、表达式
        4. order by 子句一般是放在查询语句的最后面，limit子句除外

example: 查询员工信息，要求工资从高到低排序
select
    *
from
    employees
order by salary desc;

example: 查询部门编号大于等于90的员工信息，按照入职时间的先后进行排序

select * 
from employees
where department_id>=90
order by hiredate;

example: 按照年薪的高低显示员工的信息和年薪【按照表达式排序】
select 
    *,
    salary*12*(1+ifnull(commission_pct,0)) as 年薪
from 
    employees
order by salary*12*(1+ifnull(commission_pct,0))  desc;

example: 按照年薪的高低显示员工的信息和年薪【按照表达式排序】
select 
    *,
    salary*12*(1+ifnull(commission_pct,0)) as 年薪
from 
    employees
order by 年薪 desc;
    
example: 按照姓名的长度显示员工的姓名和工资【按函数排序】
select
    length(last_name) as 字节长度,
    last_name,
    salary 
from 
    employees
order by 字节长度;

example: 查询员工信息，按照工资排序，再按照员工编号排序【按照多个字段排序】
select 
    *
from 
    employees
order by salary asc, employee_id desc;

'''P42'''

[test]
1. 查询员工的姓名和部门号的年薪，按照年薪降序，按照姓名升序
select 
    concat(first_name,' ',last_name) as 姓名,
    department_id,
    salary*12*(1+ifnull(commission_pct,0)) as 年薪
from 
    employees
order by 年薪 desc, 姓名;

2. 选择工资不在8000-170000的员工的姓名和工资，按照工资降序
select 
    concat(first_name,' ',last_name) as 姓名,
    salary
from 
    employees
where 
    salary not between 8000 and 17000
order by salary desc;

3. 查询邮箱中包含e的员工信息，并且先按照邮箱的字节数降序，再按照部门号升序
select 
    *,
    length(email) as 邮箱字节数
from 
    employees
where 
    email like '%e%'
order by 邮箱字节数 desc, department_id;

'''P43'''
进阶4： 常见函数

概念：将一组逻辑语句封装在方法体中，对外暴露方法名
好处：
    1. 隐藏了实现细节
    2. 提高代码的重用性
调用：
    select 函数名(实参列表) 【from 表】;
    # 如果函数用到了表中的字段就加from 表
特点：
    1. 叫什么(函数名)
    2. 干什么的(函数功能)
分类：
    1. 单行函数
        如 concat、length、ifnull等
    2. 分组函数
        功能：做统计使用，又称统计函数、聚合函数、组函数
    
'''P44'''
常见函数：
一、单行函数：
    字符函数：
        length
        concat
        substr
        instr
        trim
        upper
        lower
        lpad
        rpad
        replace

    数学函数：
        round
        ceil
        floor
        truncate
        mod

    日期函数：
        now
        curdate
        curtime
        year(now())
        monthname
        str_to_date
        date_format

    其他函数：
        version
        database
        user

    流程控制函数：
        if 
        case

'''P45'''
一、字符函数：
    1. length 获取参数值的字节个数
    select length('john');
    select length('张三丰hahaha');
                # 一个汉字占据3个字节

    2. concat 拼接字符串
    select 
        concat(last_name,' ',first_name)
    from 
        employees;

    3. upper、lower
    select upper('john');
    select lower('JOHN');

    example: 姓变大写，名变小写，然后拼接
    select
        concat(upper(last_name),' ',lower(first_name)) as 姓名
    from 
        employees;

    4. substr、substring(提取字符串)
    注意：索引从1开始
        1.select substr('李莫愁爱上了lyp',7) as out_put;
        #截取从某一个字符长度之后的所有字符
        2.select substr('李莫愁爱上了lyp',1,3) as out_put;
        #截取从指定索引处指定字符长度的字符(包括前后)
        example: 姓名中首字符大写，其他字符小写然后用_拼接，显示出来
        select 
            concat(upper(substr(last_name,1,1)),'_',lower(substr(last_name,2)))
        from
            employees;
    5. instr
    返回子串第一次出现的索引，如果找不到返回0
        select instr('杨不悔又爱上了lyp','zll') as out_put

    6. trim
    trim 中间不能加空格
    去除的是目标前后的指定字符
    select length(trim ('    lyp       ')) as out_put;
    select trim('a' from 'aaaaaaaa111aaaaaaa555aaaaaaacaaaa') as out_put;

    7. lpad
    用指定的字符实现左填充指定长度
    select lpad('lyp',10,'*') as out_put;

    8. rpad
    select rpad('就这',10,'?') as out_put;

    9. replace 替换
    第二个参数是目标参数，第三个参数是替换后的参数
    select replace('lyplyplyplyp','lyp','gq') as out_put;

'''P46'''
二、数学函数
    1. round 四舍五入
    # 正负数相同
    select round(1.65);

    select round(1.567,2);
    # 小数点后保留2位

    2. ceil 向上取整
    返回>=该参数的最小整数
    select ceil(1.52);
    # ceil(1.00)结果为1
    select ceil(-1.02);
    # 结果为-1

    3. floor 向下取整，返回<=该参数的最大整数
    select floor(-9.99);

    4. truncate 截断
    目标数值的某一位直接截断
    select truncate(1.69999,1);
    # 结果为1.6

    5. mod 取余
    select mod(10,3);
    = select 10%3;
    select mod(-10,-3);
    # 结果为-1
    # 被除数和结果的正负号是相同的
    # 本质上为mod(a,b)=a-a//b*b

'''P47'''
三、日期函数
    1. now 返回当前系统日期+时间
    select now();
    
    2. curdate 返回当前日期，不包含时间
    select curdate();

    3. curtime 返回当前时间，不包含日期
    select curtime():

    4. 可以获取指定的部分，年、月、日、小时、分钟、秒
    select year(now()) 年;

    select year('1998-1-1') 年;

    select year(hiredate) 年 from employees;

    5. str_to_date: 将日期格式的字符通过指定格式转为日期类型
    都需要加双引号
    select str_to_date('1998-3-2','%Y-%c-%d') as out_put;

    examlple: 查询入职日期为1992-4-3 的员工信息
    select * 
    from
        employees
    where 
        hiredate = '1992-04-03';
    
    select * 
    from
        employees
    where 
        hiredate = str_to_date('1992-04-03','%c-%d-%Y');

    6. date_format: 将日期转换成字符
    都需要加双引号

    date_format('2018/6/6','%Y年%c月%d日')
    select date_format(now(),'%Y年%m月%d日')

    examlple: 查询有奖金的员工名和入职日期(xx月/xx日/xx年)
    select 
        last_name, date_format(hiredate, '%c月/%d日/%Y年')
    from
        employees
    where
        commission_pct is not null;
    
四、其他函数
select version();
# 查询当前版本号

select datebase();
# 查询当前的库

select user();
# 查询当前的用户

五、流程控制函数
    1. if函数： 实现if else 的效果
    select if(a,b,c)
    a是判断条件，如果a成立返回b.不成立返回c

    select if(10>5, 'big','small');

    select last_name,commission_pct,if(commission_pct is not null,'有','无')
    from employees;

    2. case函数的使用一： 
    # case 使用整体相当于一个对象，需要在select句尾加上逗号
    # case 执行顺序：顺序执行，符合条件得出结果就跳过后续步骤
    case 要判断的字段或者表达式
    when 常量1 then 要显示的值1或语句1;
    when 常量2 then 要显示的值2或语句2;
    ...
    else 要显示的  值n或语句n;
    end

    example: 查询员工的工资，要求：
        1. 部门号=30，显示的工资为1.1倍
        2. 部门号=40，显示的工资为1.2倍
        3. 部门号=50，现实的工资为1.3倍
        其他部门，显示的工资为原工资

    select salary as 原始工资, department_id,
    case department_id 
    when 30 then salary*1.1
    when 40 then salary*1.2
    when 50 then salary*1.3
    else SALARY
    end as 新工资
    from 
        employees;

    3. case函数的使用二：
    case
    when 条件1 then 要显示的值1或语句1
    when 条件2 then 要显示的值2或语句2
    ...
    else 要显示的值n或者语句n
    end

    example: 查询员工的新工资：
    如果工资>20000,显示a级别
    如果工资>15000,显示b级别
    如果工资>10000,显示c级别
    否则，显示d级别

    select salary,
    case
    when salary > 20000 then 'a'
    when salary between 15000 and 20000 then 'b'
    when salary between 10000 and 15000 then 'c'
    else 'd'
    end as 新工资

    '''P52'''
    [test]
    1. 显示系统时间(注：日期+时间)
    select now();

    2. 查询员工号，姓名，工资，以及工资提高20%后的结果(new salary)
    select employee_id, concat(first_name,' ',last_name),salary,salary*1.2
    from employees;

    3. 将员工的姓名按首字母排序，并写出姓名的长度(length)
    select last_name,length(last_name)
    from employees
    order by substr(last_name,1,1) asc;

    4. 做一个查询，产生下面的结果
    <last_name> earns <salary> monthly but wants <salary*3> dream salary
    select concat(last_name,' earns ',salary,' monthly but wants ',salary*3,'.') as 'dream salary'
    from employees;

    5. 使用case-when，按照下面的条件：
    job                   grade
    AD_PRES               A
    ST_MAN                B
    IT_PROG               C
    SA_REP                D
    ST_CLERK              E
    产生下面的结果
    Last_name   Job_id    Grade  
    king         AD_PRES    A  

    select last_name, job_id,
    case job_id 
    when 'AD_PRES' then 'A'
    when 'ST_MAN' then 'B'
    when 'IT_PROG' then 'C'
    when 'SA_REP'  then 'D'
    when 'ST_CLERK' then 'E'
    end as Grade
    from employees;

'''P53'''
二、分组函数
    功能：用作统计使用，又称为聚合函数或者统计函数或者组函数
    分类：
    sum 求和、avg 平均值、max 最大值、min最小值、count计算个数
    datediff(a,b)：a,b之间的天数差值,a,b是日期格式
                   a>b 
    特点：
    1. sum、avg一般用于处理数值型
        max、min、count 可以处理任何类型
    2. 是否忽略null值：以上分组函数都忽略null值
    3. 可以和关键字搭配使用
    4. count函数的单独介绍
    一般使用count(*)统计行数
    5. 和分组函数一同查询的字段要求是group by后的字段


    1. 简单的使用
    select sum(salary) from employees;
    数值型
    select avg(salary) from employees;
    数值型
    select min(salary) from employees;
    字符型、日期型
    select max(salary) from employees;
    字符型、日期型
    select count(salary) from employees;
    字符型、日期型

    select sum(salary), round(avg(salary),2) 平均, max(salary) 最高,min(salary) 最低
    from employees;

    2. 参数类型支持哪些类型
    select sum(last_name), avg(last_name) from employees;
    select max(last_name), min(last_name),count(last_name) from employees;
    select max(last_name), min(last_name),count(last_name) from employees;
    select count(commission_pct) from employees;

    3. 忽略null

    select sum(commission_pct), avg(commission_pct) from employees;

    select sum(commission_pct), min(commission_pct) from employees;

    4. 和distinct搭配

    select sum(distinct salary), sum(salary) from employees;

    select count(distince,salary), count(salary) from employees;

    5. count函数的详细介绍
    select count(salary) from employees;

    select count(*) from employees;
    # 统计个数
    select count(1) from employees;
    # 给数据表中加了一列1，统计1的个数

    效率：
    myisam存储引擎下，count(*)的效率高
    innodb存储引擎下，count(*)和count(1)差不多，比count(字段)高

    6. 和分组函数一同查询的字段有限制

    select avg(salary), employee_id from employees;
    # avg结果是1个值，employess_id 是107个值

'''P58'''
[test]
1. 查询员工工资的最大值，最小值，平均值，总和
select max(salary), min(salary),round(avg(salary),2),sum(salary)
from employees;

2. 查询员工表中最大入职时间和最小入职时间的相差天数(diffrence)
select max(hiredate),min(hiredate),datediff(max(hiredate),min(hiredate))
from employees;

3. 查询部门编号为90的员工个数





    