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
        now()
        curdate()
        curtime()
        year(now())
        month/day/week/yearweek (now())当前月份/天数/星期
        monthname
        str_to_date
        date_format(date,format)
        datediff(A,B)


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
select count(department_id=90)
from employees;
# count(*)为正确格式,使用where进行条件判断
select count(*)
from employees
where department_id=90;

'''P59'''
进阶5：分组查询
    语法：
        select 分组函数，列(要求出现在group by 后面)
        from 表
        【where 筛选条件】
        group by 分组的列表
        【order by 子句】
    注意：
        查询列表必须特殊，要求是分组函数和group by后出现的字段
    特点：
        1. 分组查询中的筛选条件分为2类
                    数据源              位置                    关键字
        分组前筛选   原始表              group by 子句的后面     where
        分组后筛选   分组后的结果集       group by 子句的后面     having

            1.分组函数做条件肯定是放在having子句中
            # 进行过操作的数据都是放在having子句中
            2.能用分组前筛选的，就优先考虑使用分组前筛选
        2. group by子句支持单个字段分组，也支持多个字段分组(多个字段之间用逗号隔开，没有顺序要求)，函数或者函数表达式(较少)
        3. 也可以添加排序(排序放在整个分组查询之后)


引入：查询每个部门的平均工资
select avg(salary) from employees;

example1: 查询每个工种的最高工资
select max(salary), department_id
from employees
group by department_id;

example2: 查询每个位置上的部门个数
select location_id,count(*)
from departments
group by location_id;

添加分组前的筛选条件
example1: 查询邮箱中包含A字符的，每个部门的平均工资
select round(avg(salary),2) as 平均工资,department_id
from employees
where email like '%a%'
group by department_id;

example2: 查询有奖金的每个领导手下员工的最高工资
select manager_id,max(salary)
from employees
where commission_pct is not null
group by manager_id;

添加分组后的筛选条件
example1: 查询哪个部门的员工个数>2
步骤:
1. 查询每个部门的员工个数
select count(*),department_id
from employees
group by department_id;

2. 查询  
# 如果筛选条件在表中找不到，不能直接筛选
select department_id
from employees
where count(*)>2
group by department_id;
# 这样筛选会直接报错，因为员工表里面没有count(*)这个字段

select count(*),department_id
from employees
group by department_id
having count(*)>2;

example2: 查询每个工种有奖金的员工的最高工资>12000 的工种编号和最高工资
select job_id,max(salary)
from employees
where commission_pct is not null
group by job_id
having max(salary)>12000;

example3: 查询领导编号>102 的每个领导手下的最低工资>5000 的领导的编号是哪个，以及其最低工资
select min(salary),manager_id
from employees
where manager_id>102
group by manager_id
having min(salary)>5000;

按照表达式或者函数分组

    example: 按照员工姓名的长度分组，查询每一组的员工个数，筛选员工个数>5 的有哪些
    select length(last_name) as 姓名长度,count(*) as 员工个数
    from employees
    group by 姓名长度
    having count(*)>5;

按照多个字段分组

    example: 查询每个部门每个工种的员工的平均工资
    select round(avg(salary),2),department_id,job_id
    from employees
    group by department_id,job_id;

添加排序
example: 查询每个部门每个工种的员工的平均工资， 并且按平均工资的高低显示
select round(avg(salary),2) as 平均工资,department_id,job_id
from employees
where department_id is not null
group by department_id, job_id
having 平均工资>10000
order by 平均工资 desc;

'''P68'''
[test]

1. 查询各个job_id的员工工资的最大值，最小值，平均值，总和，并且按照job_id升序
select job_id, max(salary), min(salary),round(avg(salary),2),sum(salary)
from employees
group by job_id
order by job_id;

2. 查询员工最高工资和最低工资的差距(difference)
select max(salary)-min(salary) as difference
from employees


3. 查询各个管理者手下员工的最低工资，其中最低工资不能低于6000, 没有管理者的员工不计算在内
select min(salary),manager_id
from employees
where manager_id is not null
group by manager_id
having min(salary)>= 6000;

4. 查询所有部门的编号，员工数量和工资平均值，并且按照平均工资降序
select department_id,round(avg(salary),2) as 平均工资,count(*)
from employees
group by department_id
order by 平均工资 DESC;

5. 选择具有各个job_id 的员工个数
select count(*) as 员工个数,job_id
from employees
group by job_id; 

'''P69'''
进阶6 连接查询
    含义：多表查询，当查询的字段设计到多个表时
    笛卡尔乘积现象：表1有m行，表2有n行，结果=m*n行
    发生原因： 没有有效的连接条件
    如何避免： 添加有效的连接条件

    分类：
        按年代分类：
        sql92标准:仅仅支持内连接
        sql99标准【推荐】：支持内连接+外连接(左外和右外)+交叉连接


        按功能分类：
            内连接：
                等值连接
                非等值连接
                自连接
            外连接：
                左外连接
                右外连接
                全外连接
            交叉连接

    select name,boyname from boys,beauty 
    where beauty.boyfriend_id=boys.id

一、sql92标准
1. 等值连接
    1. 多表等值连接的结果为多表的交集部分
    2. n表连接，至少需要n-1个 连接条件
    3. 多表的顺序没有要求
    4. 一般需要为多表起别名
    5. 可以搭配前面介绍的所有子句使用，比如排序、分组、筛选
example1: 查询女神名和对应的男神名
select name,boyname
from boys,beauty
where beauty.boyfriend_id=boys.id;

example2: 查询员工名和对应的部门名
select last_name,department_name
from employees,departments
where employees.department_id=departments.department_id;

2. 为表起别名
    1. 提高语句的简洁度
    2. 区分多个重名的字段

    注意：如果为表起了别名，则查询的字段不能用原来的表名限定

    example: 查询员工名、工种号、工种名
    select last_name,e.job_id,job_title
    from employees as e,jobs as j
    where e.job_id=j.job_id;

    3. 两个表的顺序可以调换

    4. 可以加筛选吗？ 可以
    where 条件中使用and 进行条件连接
    example1: 查询有奖金的员工名和部门名
    select last_name,department_name
    from employees as e,departments as d
    where e.department_id = d.department_id and commission_pct is not null;

    example2: 查询城市名字中第二个字符为o的部门名字和城市名字
    select department_name, city
    from departments as d,locations as l
    where d.location_id=l.location_id and city like '_o%';

    5. 可以加分组吗？ 可以
    example1: 查询每个城市的部门个数
    select count(*),l.city
    from locations as l, departments as d
    where d.location_id=l.location_id
    group by l.city

    example2: 查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资
    select department_name, d.department_id,d.manager_id,min(salary)
    from departments as d, employees as e 
    where d.department_id = e.department_id and commission_pct is not null
    group by department_id;

    6. 可以加排序吗？ 可以
    example: 查询每个工种的工种名和员工的个数，并且按照员工个数降序
    select job_title,count(*) as 员工个数
    from jobs as j,employees as e
    group by job_id
    where j.job_id=e.job_id
    order by 员工个数 DESC;

    7. 可以实现三表连接吗？
    example: 查询员工名、部门名、所在的城市
    select last_name,department_name,city 
    from employees as e,departments as d,locations as l
    where l.location_id=d.location_id and d.department_id=e.department_id
    and city like's%';

2. 非等值连接
example: 查询员工的工资和工资级别
SELECT salary,grade_level
FROM job_grades,employees
WHERE salary BETWEEN lowest_sal AND highest_sal AND grade_level='A';

3. 自连接
自己和自己连接，把一张表当成两张表命名和使用
example: 查询 员工名和上级的名称
select e1.last_name, e1.employee_id,e2.last_name,e2.employee_id
from employees as e1, employees as e2
where e1.manager_id=e2.employee_id;

'''P75'''
[test]
1. 显示员工表的最大工资，工资平均值
select max(salary),round(avg(salary),2)
from employees;
2. 查询工资表的员工id，工作id,姓名，按照部门id降序，salary升序
select employee_id,job_id,last_name
from employees
order by department_id DESC, salary ASC;

3. 查询员工表的job_id中包含a和e的，并且a在e的前面
select job_id
from employees
where job_id like '%a%e%';

4. 已知表student 里面有id，name, gradeid
已知表grade 里面有id,name
已知表result 里面有id,score,studentNo
要求查询姓名、年级名、成绩
select s.name,g.name, r.score
from student as s,grade as g,result as r
where s.gradeid=g.id and s.id=r.studentNo;

5.显示当前日期，以及去前后空格，截取子字符串的函数
select now();
select trim();
select substr(str,startIndex,length);

'''P76'''
复习课，跳过

'''P77'''
[test]
1. 显示所有员工的姓名，部门号和部门名称
select last_name, d.department_id, department_name
from  employees as e,departments as d
where e.department_id = d.department_id;

2. 查询90号部门员工的job_id和部门的location_id；
select job_id, location_id
from employees as e,departments as d
where e.department_id = d.department_id = 90;
# 这里不能连续等于，需要分开写，用e.department_id=d.department_id and d.department_id=90;

3. 查询所有有奖金的员工的last_name,department_name,location_id,city
select last_name, department_name,d.location_id,city
from employees as e,departments as d,locations as l
where commission_pct is not null and l.location_id = d.location_id and d.department_id = e.department_id;

4. 选择city在Toronto工作的员工的last_name,job_id,department_id,department_name
select last_name,job_id,e.department_id,department_name
from employees as e,departments as d,locations as l
where city = 'Toronto' and l.location_id = d.location_id and e.department_id = d.department_id;

5. 查询每个工种、每个部门的部门名、工种名和最低工资
select job_title,department_name,min(salary)
from jobs as j,departments as d,employees as e
where j.job_id = e.job_id and d.department_id = e.department_id
group by job_title,department_name;
6. [难题]查询每个国家下的部门个数>2 的国家编号
select country_id,count(*) as 部门个数
from locations as l,departments as d
where d.location_id = l.location_id and 部门个数>2;

答案：
SELECT country_id,COUNT(*) AS 部门个数
FROM locations AS l,departments AS d
WHERE d.location_id = l.location_id
GROUP BY country_id
HAVING 部门个数>2;

7. 选择指定员工的姓名，员工号，以及他的管理者的姓名和员工号，类似于下面的格式
employees        emp       manager       
kochhar  101    king         100
select e1.employee_id,e1.last_name,e2.employee_id,e2.last_name
from employees as e1,employees as e2
where e1.manager_id=e2.employee_id;

'''P78'''
二、sql99语法
    语法：
        select 查询列表
        from 表1 别名
        【连接类型】join 表2 别名
        on 连接条件
        【where 筛选条件】
        【group by 分组】
        【habing 筛选条件】
        【order by 排序列表】

    分类：
    内连接：inner
    外连接
        左外：left【outer】
        右外：right【outer】
        全外：full【outer】
    交叉连接：cross

一、内连接
    语法：
    select 查询列表
    from 表1 别名
    inner join 表2 别名
    on 连接条件;

    分类：
    等值
    非等值
    自连接

    特点：
    1. 添加排序、分组、筛选
    2. inner可以省略
    3. 筛选条件放在where 后面，连接条件放在on的后面，提高分离性，便于阅读
    4. inner join连接和sql92语法中的等值连接效果是一样的，都是多表查询的交集
    

    1. 等值连接
    example1: 查询员工名、部门名
    select last_name,department_name
    from employees as e
    inner join departments as d
    on d.department_id = e.department_id;

    example2: 查询名字中包含e的员工名和工种名(添加筛选)
    select last_name,job_title
    from employees as e
    inner join jobs as j
    on e.job_id=j.job_id
    where last_name like '%e%';

    [难题]example3: 查询部门个数>3 的城市名和部门个数(添加分组+筛选)
    select city,count(*) as 部门个数
    from locations as l
    inner join departments as d
    on d.location_id = l.location_id
    having 部门个数>3; 

    select city,count(*) as 部门个数
    from locations as l
    inner join departments as d
    on d.location_id = l.location_id
    group by city
    having 部门个数>3; 
    # 需要对city进行分组

    example4: 查询哪个部门的员工个数>3 的部门名和员工个数，并按照个数降序(添加排序)
    select department_name,count(*) as 员工个数
    from departments as d
    inner join employees as e
    on e.department_id = d.department_id
    group by department_name
    having 员工个数>3
    order by 员工个数 desc;

    example5: 查询员工名、部门名、工种名，并按部门名降序
    select last_name, department_name,job_title
    from employees as e
    inner join departments as d
    on d.department_id=e.department_id
    inner join jobs as j
    on j.job_id=e.job_id
    order by department_name desc;

    2. 非等值连接
    example1: 查询员工的工资级别
    select salary, grade_level
    from employees as e
    【inner】join job_grades as g
    on e.salary between g.lowest_sal and highest_sal;

    example2: 查询工资级别个数>2 的个数并且按照工资级别进行降序
    select salary, grade_level,count(*)
    from employees as e
    【inner】join job_grades as g
    on e.salary between g.lowest_sal and highest_sal
    group by grade_level 
    having count(*) > 20
    order by grade_level DESC;

    3. 自连接
    example: 查询姓名中包含k的员工的名字和上级的名字
    select e1.last_name, e2.last_name
    from employees as e1
    inner join employees as e2
    on e1.manager_id = e2.employee_id
    where e1.last_name like '%e%';

二、外连接
    应用场景：用于查询一个表中有，一个表中没有的场景
    特点：
        1.  外连接的查询结果为主表中的所有记录
            如果从表中有和它匹配的，则显示匹配的值
            如果从表中没有和它匹配的，则显示为null
            外连接查询结果=内连接结果+主表有而从表没有的结果
        2.  左外连接，left左边的是主表
            右外连接，right join右边的是主表
        3.  左外和右外交换两个表的顺序，可以实现同样的结果
        4.  全外连接=内连接的结果+表1有表2没有+表2没有表1有
    引入：查询没有男朋友的女神名
    
    左外连接
    select b.name,boys.*
    from beauty as b
    left outer join boys 
    on b.boyfriend_id = boys.id
    where boys.id is null;
    # 没有分组，表没有进行改变
    # 选用id是因为id有个钥匙，不为空

    右外连接
    select b.name,boys.*
    from boys
    right outer join beauty as b
    on b.boyfriend_id = boys.id
    where boys.id is null;

    example1: 查询哪个部门没有员工
    select d.*,e.employee_id
    from departments as d
    left outer join employees as e
    on d.department_id=e.department_id
    where e.employee_id is not null

    select d.*,e.employee_id
    from employees as e
    right outer join departments as d
    on d.department_id=e.department_id
    where e.employee_id is not null

    全外连接(不支持)
    use girls;
    select b.*,boys.*
    from beauty as b
    full outer join boys
    on b.boyfriend_id = boys.id

    交叉连接(笛卡尔乘积)
    select b.*,boys.*
    from beauty as b
    cross join boys;

    sql92和sql99 pk
    功能：sql99支持的较多
    可读性：sql99实现连接条件和筛选条件的分离，可读性较高
    
    连接的5种情况：
    # 这里的a和b指的是a-a与b的交集
    1. a*b(a与b的交集)
    select 
    from a
    inner join b
    on a.key=b.key;

    2. a+a*b(a+a与b的交集)
    select 
    from a 
    left join b 
    on a.key=b.key 

    3. b+a*b 
    select 
    from b 
    right join a 
    on a.key=b.key

    4. a 
    select 
    from a 
    left join b
    on a.key=b.key
    where b.key is null

    5. 
    select 
    from b
    right join a
    on a.key = b.key
    where a.key is null

    '''P86'''
    [test]
    1. 查询编号>3 的女神的男朋友信息，如果有则列出详细信息，如果没有则用null填充
    select b.*
    from beauty as b
    left outer join boys
    on b.boyfriend_id = boys.id
    where b.id>3;

    2. 查询哪个城市没有部门
    select d.location_id,l.city
    from locations as l
    left outer join departments as d
    on d.location_id=l.location_id
    where d.location_id is null;

    3. 查询部门名为SAL或IT的员工信息
    select d.department_name, e.*
    from departments as d
    left outer join employees as e
    on d.department_id=e.department_id
    where d.department_name='SAL' or d.department_name= 'IT';

'''P87'''
进阶7：子查询
    含义：
        出现在其他语句中的select语句，称为子查询或者内查询
        外部的查询语句，称为主查询或外查询
    分类：
        按子查询出现的位置：
            select 后面：
                仅仅支持标量子查询
            from 后面
                支持表子查询
            [重要]where或having 后面
                支持标量子查询
                列子查询
                行子查询
            exists 后面(相关子查询)
                表子查询
        结果集的行列数不同：
            标量子查询(结果集只有一行一列)
            列子查询(结果集只有一列多行)
            行子查询(结果集有一行多列或者多列多行)
            表子查询(结果集无限制，一般为多行多列)

一、where或者having后面
    1. 标量子查询(单行子查询)
    2. 列子查询(多行子查询)
    3. 行子查询(较少，多列多行)
        特点：
            1. 子查询放在小括号内
            2. 子查询一般放在条件的右侧
            3. 标量子查询，一般搭配着单行操作符使用 > < = <= >= <>
            4. 子查询的执行优先于主查询的执行(主查询的条件用到了子查询的结果)
    4. 列子查询：一般搭配着多行操作符使用 in, any/some, all

1. 标量子查询
example1： 谁的工资比Abel高？
    1. 查询Abel的工资
        select salary from employees where last_name='Abel'
    2. 查询员工的工资，工资>1 的结果
        select * from employees where salary > 1 的结果
        select * from employees where salary > (
            select salary 
            from employees 
            where last_name='Abel'
        );

example2: 返回job_id与141号员工相同，salary 比143号员工多的员工 姓名，job_id和工资
select last_name,job_id,salary
from employees
where job_id=(
    select job_id
    from employees
    where employee_id=141
) and salary>(
    select salary
    from employees
    where employee_id=143
);

example3: 返回公司工资最少的员工的last_name,job_id,salary
select last_name,job_id,salary
from employees
where salary=( 
    select min(salary)
    from employees
);

example4: 查询最低工资大于50号部门最低工资的部门id和其最低工资
select department_id,min(salary)
from employees
where min(salary)>(
    select min(salary)
    from employees
    where department_id=50
)
# 缺少group by depantment_id

思路：
    1. 查询50号部门的最低工资
    select min(salary)
    from employees
    where department_id=50
    2. 查询每个部门的最低工资
    select min(salary)
    from employees
    group by department_id
    3. 筛选2，满足min(salary)>1 的结果
    select department_id,min(salary)
    from employees
    group by department_id
    having min(salary) > (
        select min(salary)
        from employees
        where department_id=50
    ) ;

    非法使用标量子查询
    1. # 将上题min(salary)改成salary
    select department_id,min(salary)
    from employees
    group by department_id
    having min(salary) > (
        select salary
        from employees
        where department_id=50
    ) ;
    2. 子查询的结果不是一行一列，如departmeng_id=200;

2. 列子查询(多行子查询)
    [重要]in/not in: 等于列表中的任意一个
    any/some: 和子查询返回的某一个值比较
    # a>any(10,20,30)=a>min(10,20,30)，大于最小的那个就行
    all：和子查询返回的所有值比较
    # a>all(10,20,30)=a>max(10,20,30)

    example1: 返回location_id是1400或1700的部门中的所有员工姓名
    select last_name
    from employees
    where department_id in (
        select distinct department_id
        from departments
        where location_id in (1400,1700)
    )

    example2: 返回其他部门中比job_id为'IT_PROG'部门任一工资低的员工的员工号、姓名、job_id以及salary
    select department_id,employee_id,last_name,job_id,salary
    from employees
    where salary< any (
        select salary
        from employees
        where job_id='IT_PROG'
    ) and job_id <> 'IT_PROG';
    # in 也可以用=any来表示
    # not in 可以用<>all来表示

    example3: 返回其他部门中比job_id为'IT_PROG'部门所有工资低的员工的员工号、姓名、job_id以及salary
    select department_id,employee_id,last_name,job_id,salary
    from employees
    where salary<  (
        select min(salary)
        from employees
        where job_id='IT_PROG'
    ) and job_id <> 'IT_PROG';

3. 行子查询
example: 查询员工编号最小并且工资最高的员工信息
select * from employees
where (employee_id,salary)=(
    select min(employee_id),max(salary)
    from employees
)





1. 查询最小的员工编号
select min(employee_id)
from employees

2. 查询最高工资
select max(salary)
from employees

3. 查询员工信息
selec * from employees
where employee_id = (
    select min(employee_id)
    from employees
) and salary =(
    select max(salary)
    from employees
)

二、select 后面
example1: 查询每个部门的员工个数
select departments.*,(
    select count(*)
    from employees as e
    group by e.department_id
    where e.department_id=departments.department_id
) 
from departments;

example2: 查询员工号=102 的部门名
select department_name
from departments
where department_id = (
    select department_id
    from employees
    where employee_id = 102
)

三、from 后面
example: 查询每个部门的平均工资的工资等级
sql99:
    1. 查询每个部门的平均工资
    select round(avg(salary),2),department_id
    from employees
    group by department_id;

    2. 连接1的结果集合Job_grades表，筛选条件是平均工资在范围之内
    select avg.*,g.grade_level
    from (
        select round(avg(salary),2) as ag,department_id
        from employees
        group by department_id
    ) as avg
    inner join job_grades as g
    on avg.ag between g.lowest_sal and highest_sal

sql92:
    select a.*, grade_level
    from (
        select round(avg(salary),2) as 平均工资,department_id
        from employees
        group by department_id
    ) as a,job_grades as j
    where a. 平均工资 between j.lowest_sal and highest_sal;

四、exists后面(相关子查询)
    语法：
        exists(完整的查询语句);
        结果：1或0

    select exists(select employee_id from employees where salary = 2)

    example1: 查询有员工的部门名
    select department_name
    from departments as d
    where d.department_id in (
        select department_id
        from employees
    )

    select department_name
    from departments as d
    where exists(
        select *
        from employees as e
        where d.department_id=e.department_id
    )

    example2: 查询没有女朋友的男神信息
    1. in
        select bo.*
        from boys as bo
        where bo.id not in (
            select boyfriend_id
            from beauty
        )

    2. exists
        select bo.*
        from boys as bo
        where not exists(
            select boyfriend_id
            from beauty
            where bo.id=beauty.boyfriend_id
        )

'''P94'''
[test] 
1. 查询和Zlotkey相同部门的员工姓名和工资
select last_name,salary
from employees as e
where department_id=(
    select department_id
    from employees
    where last_name = 'Zlotkey'
)
2. 查询工资比公司平均工资高的员工的员工号，姓名和工资
select employee_id,last_name,salary
from employees
where salary>(
    select round(avg(salary),2)
    from employees
)
3. 查询各部门中工资比本部门平均工资高的员工的员工号，姓名和工资

select employee_id,salary,last_name
from employees as e1,(
    select round(avg(salary),2) as 平均工资,department_id as 部门
    from employees
    group by department_id
) as sal
where e1.salary>sal.平均工资 and e1.department_id=sal.部门;

4. 查询和姓名中包含字母u的员工在相同部门的员工的员工号和姓名
select employee_id,last_name
from employees
where department_id in (
    select department_id
    from employees
    where last_name like '%u%'
)

5. 查询在部门的location_id为1700的部门工作的员工的员工号
select employee_id,last_name
from employees
where department_id in (
    select department_id
    from departments
    where location_id=1700
)
6. 查询管理者是King的员工姓名和工资
select last_name,salary
from employees
where manager_id in (
    select employee_id
    from employees
    where last_name='King'
)
7. 查询工资最高的员工的姓名，要求first_name和last_name显示为一列，列名为姓.名
select concat(first_name,' ',last_name) as `姓.名`
from employees
where salary=(
    select max(salary)
    from employees
)

'''P95'''
进阶8: 分页查询
    应用场景：当要显示的数据，一页显示不全，需要分页提交sql请求
    语法：
        [7]select 查询列表
        [1]from 表
        [2]【join type】 join 表2
        [3]on 连接条件
        [4]where 筛选条件
        [5]group by 分组字段
        [6]having 分组后的筛选
        [8]order by 排序的字段
        [9]limit 【offset】,size

        offset 代表要显示条目的起始索引(起始索引从0开始)
        size   代表要显示的条目个数
    特点：
        1. limit语句放在查询语句的最后
        2. 公式
            要显示的页数page,每页的条目数size

            select 查询列表
            from 表
            limit size*(page-1),size;
            size = 10
            page   起始信息
            1        0
            2        10
            3        20
example1: 查询前5条的员工信息
select * 
from employees
limit 0,5

select * 
from employees
limit 5

example2: 查询第11条到第25条
select * from employees
limit 10,15

example3: 有奖金的员工信息，并且工资较高的前10名显示出来
select *
from employees
where commission_pct is not null
order by salary DESC
limit 10

'''P96'''
[test]
1. 
select name,substr(email,1,instr(email,'@')-1)
from stuinfo

2.
select count(*),sex
from stuinfo as s
group by sex

3. 
select name,gradeid
from stuinfo as s,grade as g
where s.gradeid=g.id and s.age>18;

4.
select gradeid
from stuinfo as s
where min(age)>20
group by gradeid
# having 才对
select min(age),gradeid
from stuinfo as s
group by gradeid
having min(age)>20

5. 
7 select *
1 from 表
2 inner join 表
3 on 连接条件
4 where 筛选条件
5 group by 分组
6 having 筛选
8 order by 排序
9 limit 取值

'''P97'''
[复习课],跳过


'''P98'''
[test]
1. 查询工资最低的员工信息：last_name,salary
select last_name,salary
from employees
where salary=(
    select min(salary)
    from employees
)

2. [难题]查询平均工资最低的部门信息
select d.*
from departments as d
where department_id=(
    select department_id
    from employees
    group by department_id
    having avg(salary)=(
    select min(ag)
    from(
        select avg(salary) as ag,department_id
        from employees
        group by department_id
    ) as sal
)
);

select d.*
from departments as d
where d.department_id=(
    select department_id
    from employees
    group by department_id
    order by avg(salary) ASC
    limit 1
)
3. 查询平均工资最低的部门信息和该部门的平均工资
select sal.r,d.*
from departments as d,(
    SELECT department_id,AVG(salary) as r
    FROM employees
    GROUP BY department_id
    ORDER BY AVG(salary) ASC
    LIMIT 1
    ) as sal
where d.department_id=sal.department_id

4. 查询平均工资最高的job信息
select j.*
from jobs as j
where j.job_id=(
    select job_id
    from employees
    group by job_id
    order by avg(salary) desc
    limit 1
)

5. 查询平均工资高于公司平均工资的部门有哪些？

select department_id
from employees
group by department_id
having avg(salary)>(
    select avg(salary)
    from employees
)

select d.*
from departments as d
where department_id in (
    select department_id
    from employees
    group by department_id
    having avg(salary)>(
    select avg(salary)
    from employees
)
)
6. 查询出公司中所有manager的详细信息
select *
from employees
where employee_id in (
    select distinct manager_id
    from employees
)

7. 各个部门中最高工资中最低的那个部门的最低工资是多少
select min(salary)
from employees
where department_id=(
    select department_id
    from employees
    group by department_id
    order by max(salary) ASC
    limit 1
)

8. 查询平均工资最高的部门的manager的详细信息：last_name,department_id,email,salary
select deaprtment_id
from employees
group by department_id
order by avg(salary) DESC
limit 1

select manager_id
from employees
where department_id=(
    select department_id
    from employees
    group by department_id
    order by avg(salary) DESC
    limit 1
)

select last_name,department_id,email,salary
from employees
where employee_id in (
    select manager_id
    from employees
    where department_id=(
        select department_id
        from employees
        group by department_id
        order by avg(salary) DESC
        limit 1
)
)

'''P98'''
[test]
1. 查询每个专业的学生人数
select majorid,count(*)
from student
group by majorid
2. 查询参加考试的学生中，每个学生的平均分、最高分
select studentno,avg(score),max(score)
from result
group by studentno
3. 查询姓张的每个学生的最低分大于60的学号、姓名
    1. select b.studentno,s.studentname
    from (
        select *
        from result
        where studentno in (
        select studentno
        from student
        where studentname like '张%'
    )
    ) as b,student as s
    where b.studentno = s.studentno
    group by studentno
    having min(score)>60

    2. SELECT s.`studentno`,s.`studentname`
    FROM student AS s,result AS r
    WHERE studentname LIKE '张%' AND s.studentno=r.studentno
    GROUP BY s.studentno
    HAVING MIN(score)>60
4. 查询每个专业生日在'1988-1-1'后的学生姓名、专业名称
SELECT studentname,majorname
FROM student AS s,major AS j
WHERE DATE(s.borndate) > '1988-01-01' AND s.majorid=j.majorid
5. 查询每个专业的男生人数和女生人数分别是多少
    1. select majorid,sex,count(*)
    from student
    group by majorid,sex
    
    2. select majorid,
        (select count(*) from student where sex='男' and majorid = s.majorid) as 男,
        (select count(*) from student where sex='女' and majorid = s.majorid) as 女
        from student as s
        group by majorid
6. 查询专业和张翠山一样的学生的最低分
select min(score)
from result as r
where studentno in (
    select studentno
    from student
    where majorid=(
        select majorid
        from student
        where studentname='张翠山'
)
)
7. 查询大于60分的学生的姓名、密码、专业名
select studentname,loginpwd,majorname
from student as s,major as m
where s.majorid=m.majorid and studentno in (
    select studentno
    from result
    where score>60
)
8. 按邮箱位数分组，查询每组的学生个数
select count(*),length(email)
from student
group by length(email)
9. 查询学生名、专业名、分数
select studentname,majorname,score
from student as s,result as r,major as m
where s.studentno=r.studentno and m.majorid=s.majorid
10. 查询哪个专业没有学生，分别用左连接和右连接实现
select m.majorid,m.majorname,s.studentno
from major as m
left join student as s on m.majorid = s.majorid
where s.studentno is null

11. 查询没有成绩的学生人数
select count(*)
from student
where studentno not in (
    select distinct studentno
    from result
)

'''P100'''
进阶9：联合查询
    union 联合/合并：将多条查询语句的结果合并成一个结果

    语法：   查询语句1
            union
            查询语句2
            union
    应用场景：要查询的结果来自于多个表且多个表没有直接的连接关系，但是查询的信息一致时

    特点：
        1. 要求多条查询语句的查询列数是一致的
        2. 要求多条查询语句的查询的每一列的类型和顺序是一致的
        3. 使用union关键字默认去重，如果使用union all关键字可以包����������重复项

    引入的案例：查询部门编号>90 或者邮箱中包含a的员工信息
    select * from employees where email like '%a%' or deppartment_id>90

    select * from employees where email like '%a%'
    union 
    select * from employees where department_id>90

    example1: 查询中国用户男性的信息，以及外国用户男性的信息
    select id,cname,csex from t_ca where sex='男'
    union
    select t_id,tName.tGender from t_ua where tGender='male'

'''P102'''
DML语言
    数据操作语言：
    插入：insert
    修改：update
    删除：delete

一、插入语句
方式一：经典的插入
    语法：
        insert into 表名(列名，...) values(值，...);
        int 数值，varchar,char字符型数值，用单引号，datetime需要用合法日期形式,blob保存图片的类型

1. 插入的值的类型要与列的类型一致或者兼容
insert into beauty(id,name,sex,borndate,phone,photo,boyfriend_id)
values(13,'唐易迅','1990-04-23','189888',null,2)

2. 不可以为null的列必须插入值，可以为null的列是如何插入值的？
    方式一：
    insert into beauty(id,name,sex,borndate,phone,photo,boyfriend_id)
    values(13,'唐易迅','女','1990-04-23','189888',null,2)
    方式二：
    insert into beauty(id,name,sex,borndate,phone,boyfriend_id)
    values(14,'唐易','女'，'1990-04-23','189888',2)
    # 列也不行，null也不写 

3. 列的顺序是否可以调换[可以]
insert into beauty(name,sex,id,phone)
values('lyp','man','lll','1999')

4. 列数和值的个数必须一致

5. 可以省略列名，默认所有列，并且列的顺序和表中顺序一致
insert into beauty
values(18,'zz','nan',null,'119',null,'zzz');
# null的值必须要加上null，不能不写

方式二：
    语法：
    insert into 表名
    set 列名=值，列名=值。

insert into beauty
set id=19,name='lch',phone='0000'

两种方式大pk

1. 方式一支持插入多行,方式二不支持
    insert into beauty
    values(28,'zz','nan',null,'119',null,'zzz')
    ,(38,'zz','nan',null,'119',null,'zzz')
    ,(48,'zz','nan',null,'119',null,'zzz');

2. 方式一支持子查询，方式二不支持
insert into beauty(id,name,phone)
select 26,'宋茜','11809866';

insert into beauty(id,name,phone)
select id,boyname,'1234567'
from boys where id<3;

二、修改语句

    1. [重要]修改单表的记录
        语法：
        update 表名
        set 列=新值，列=新值
        where 筛选条件;
    2. 修改多表的记录【补充】
        语法：
        sql92语法：
        update 表1 别名,表2 别名
        set 列=值
        where 连接条件
        and 筛选条件

        sql99语法：
        update 表1 别名
        inner|left|right join 表2 别名
        on 连接条件
        set 列=值
        where 筛选条件

1. 修改单表的记录
example1: 修改beauty表中姓唐的女神的电话为138999999999
update beauty
set phone = '138999999999'
where name like '唐%';

example2: 修改boys表中id号为2的名称为张飞，魅力值10
update boys
set boyName='张飞',userCP=1800
where id=2;

2. 修改多表的记录

example1: 修改张无忌的女朋友的手机号为114
update beauty as b
inner join boys
on boys.id=b.boyfriend_id
set b.phone='114'
where b.boyfriend_id=(
    select id
    from boys
    where boyName='张无忌'
);

example2: 修改没有男朋友的女神的男朋友编号都为2号
update beauty as b,boys
set boyfriend_id=2
where boyfriend_id not in (
    select id
    from boys 
)

三、删除语句
    方式一：delete
    语法：
    1. 单表的删除[重要]
        delete from 表名 where 筛选条件
    2. 多表的删除【补充】
        sql92语法：
        delete 表1的别名，表2的别名
        from 表1 别名，表2 别名
        where 连接条件
        and 筛选条件;

        sql99语法：
        delete 表1的别名，表2的别名
        from 表1 别名，表2 别名
        inner|left|right join 表2 别名 连接条件
        where 筛选条件
    方式二：truncate 
    语法：truncate table 表名;
    # 整表删除,不允许增加where，一删全删

方式一： delete 
    1. 单表的删除
    example1：删除手机尾号为9的信息
    delete from beauty where phone like '%9'

    2. 多表的删除
    example: 删除张无忌的女朋友的信息
    delete from beauty 
    where boyfriend_id=(
        select id
        from boys
        where boyName='张无忌'
    )

    2. 删除黄晓明的信息以及他女朋友的信息
    delete b,boys
    from beauty as b,boys
    where b.boyfriend_id=boys.id and
    boys.boyName='黄晓明'

方式二：
example: 将魅力值大于100的男神信息删除
truncate table boys;

delete PK truncate
1. delete 可以加where 条件，truncate不能加

2. truncate删除，效率高一些

3.  假如要删除的表中有自增长列，
    用delete删除后，再插入数据，自增长列的值从断点开始
    而truncate删除后，再插入数据，自增长列的值从1开始

4. truncate删除没有返回值，delete删除有返回值
# truncate删除，0行受影响，delete删除，a行受影响

5. truncate删除不能回滚，delete删除可以回滚

'''P110'''
[test]
[test_lesson10 数据处理]
2. desc my_employees;

3. insert into my_employees
values(1,'patel','ralph','rpatel',895),
(2,'dancs','betty','bdancs',860),
(3,'biri','ben','bbiri',1100),
(4,'newman','chad','cnewman',750),
(5,'ropeburn','audery','aropebur',1550)

4. insert into users
values(1,'rpatel',10),
(2,'bdancs',10),
(3,'bbiri',20),
(4,'cnewman',30),
(5,'aropebur',40);

5. update my_employees
set last_name='drelxer'
where id=3;

6. update my_employees
set salary = 1000
where salary <= 900;

7. delete m,u 
from my_employees as m,users as u
where m.id=u.id and m.userid='bbiri';

8. truncate table my_employees,users

'''P111'''
DDL语言
数据定义语言
    库和表的管理
    一、库的管理
        创建、修改、删除
    二、表的管理
        创建、修改、删除

    创建：create
    修改：alter
    删除：drop

一、库的管理
1. 库的创建
    语法：
    create database 库名
    example: 创建库books
    create database books;

2. 库的修改
    rename database books to 新库名;
    # 新版本已不能使用，一般不会去修改
    更改库的字符集
    alter database books character set gbk;

3. 库的删除
    drop database if exists books;

二、表的管理
1. 表的创建[重要]
    create table 表名(
        列名 列的类型【(长度) 约束】,
        列名 列的类型【(长度) 约束】,
        列名 列的类型【(长度) 约束】,
        列名 列的类型【(长度) 约束】
    )
    # 最后一个字段不用加逗号
    # 列名不用加''

example: 创建表book
create table book(
    id int,
    bname varchar(20),
    price double,
    author varchar(20),
    publishdate datetime
)

example: 创建表author
create table author(
    id int,
    au_name varchar(20),
    nation varchar(10)
)

2. 表的修改
    语法：
    alter table 表名 add|drop|change|modify|rename column 列名 【列类型 约束】
    
    1. 修改列名
    alter table book change 【column】 publishdate pubdate datetime;
    2. 修改列的类型或者约束
    alter table book modify column pubdate timestamp
    3. 添加新列
    alter table author add column annual double;
    4. 删除列
    alter table author drop column annual;
    5. 修改表名
    alter table author rename to book_author;

3. 表的删除
drop table if exists book_author;


通用的写法：
drop database if exists 旧库名;
create database 新库名;

drop table if exists 旧表名
create table 表名();

4. 表的复制
insert into author values
(1,'村上春树','日本')，
(2,'莫言','中国')，
(3,'冯唐','中国')，
(4,'金庸','中国')；

    1. 仅仅复制表的结构
    create table aut like author;

    2. 复制表的结构+数据
    create table aut2
    select * from author;
    只复制部分数据
    create teable copy3
    select id,name
    from author
    where nation='中国'

    仅仅复制某些字段(结构)
    create table a4
    select id,au_name
    from author
    where 0;

'''P117'''
[test]
1. use books
    create table dept1(
        'id' int(7),
        'name'  varchar(25)
    )

2. create table dept2 
select department_id,department_name
from myemployees.departments

3. create table emp5(
    id int(7),
    first_name varchar(25),
    last_name varchar(25),
    dept_id int(7)
)

4. alter table emp5
modify column last_name varchar(50)

5. create table employees2
select * from employees

6. drop table emp5

7. alter table employees2 rename to emp5

8. alter table dept add column test_column int

9. alter table emp5 drop column dept_id

'''P118'''
常见的数值类型
数值型：
    整型
    小数：
        定点数
        浮点数

字符型：
    较短的文本：char varchar
    较长的文本：text blob

日期型：


一、整型
    分类：
        tinyint samllint mediumint int/integer bigint
    特点：
        1. 如果不设置无符号，默认是有符号，希望要无符号，需要加入关键字unsigned
        2. 如果插入的数值超出了整型的范围，会报out of range异常，并且插入临界值
        3. 如果不设置长度，会有默认的长度
            长度代表了显示的最大宽度，如果不够会用0填充，填充使用zerofill关键字填充



1. 如何设置无符号和右符号
create table tab_int(
    t1 int
    t2 int unsigned
)

insert into tab_int values(-11,-11);

二、小数
    1. 浮点型
    float(M,D)
    double(M,D)
    2. 定点型
    dec(M,D)
    decimal(M,D)

    特点：
    1. M和D
    M：整数部位和小数部位
    D：小数部位
    如果超出范围，则插入临界值

    2. M和D都可以省略
    如果是decimal，则M默认为10，D默认为0
    如果是float和double，则会根据插入的数值精度来决定精度

    3. 定典型的精确度较高，如果要求插入的数值精度较高，如货币运算，则考虑使用

    原则：
        所选择的类型越简单越好，能保存的数值类型越小越好

三、字符型
    较短的文本：
        char
        varchar
    其他：
    binary和varbinary用于保存较短的二进制
    较长的文本：
        text
        blob(较大的二进制)

    特点：

                写法         M的意思                             特点          空间的耗费      效率
    char       char(M)     最大的字符数，可以省略，默认为1    固定长度的字符   比较耗费          高
   varchar   varchar(M)    最大的字符数，不可以省略          可变长度的字符   比较节省          低
   # 一般遇到不变的，比如sex，用char，可变的用varchar

   补充：
   1. enum: 插入的类型必须在范围中
   create table tab(
       c1 enum('a','b','c')
   )

    insert into tab values('m')，插入失败

    2. set：插入的类型必须在范围中，不过可以插入多个值
    create table tab(
        s1 set('a','b','c','d')
    );
        insert into tab values('a');
        insert into tab values('a','b');
        insert into tab values('a','b','c');

四、日期型
    分类：
    date 只保存日期
    time 只保存时间
    year 只保存年

    datetime 保存日期+时间
    timestamp 保存日期+时间

    特点：
                    字节        范围        时区等的影响
    datetime          8        1000-9999    不受 
    timestamp         4        1970-2038     受

create table tab(
    t1 datetime,
    t2 timestamp
)

insert into tab values(now(),now());

'''P124'''
[复习课]跳过

'''P125'''
约束
    含义：一种限制，用于限制表中的数据，为了保证表中的数据的准确和可靠性

    分类：六大约束
        not null：非空，用于保证该字段的值不能为空
            比如姓名、学号等
        default：默认，用于保证该字段有默认值
            比如性别(男生多的班级)
        primary key：主键，用于保证该字段的值具有唯一性，非空
            比如学号、员工编号等
        unique：唯一，用于保证该字段的值具有唯一性，可以为空
            比如座位号
        check：检查【mysql中不支持】
            比如年龄、性别
        foreign koy：外键约束，用于限制两个表的关系，用于保证该表的字段值必须来自于主表的关联列的值
            在从表添加外键约束，用于引用主表中某列的值
            比如学生表的专业编号，员工表的部门编号，员工表的工种编号

    添加约束的时间：
        1. 创建表时
        2. 修改表时

    约束的添加分类：
        1. 列级约束：
            六大约束语法上都支持，但是外键约束没有效果

        2. 表级约束：
            除了非空、默认，其他的都支持

    列级约束和表级约束pk：
                        位置                支持的约束类型          是否可以起约约束名
        列级约束：      列的后面        语法都支持，外键没效果          不可以
        表级约束：      所有列的下面    默认和非空不支持，其他支持      可以(主键没有效果)

    主键和唯一的大对比：
                保证唯一性      是否允许为空        一个表中可以有多少个    是否允许组合
        主键        yes             no                 至多有一个         允许，不推荐
        唯一        yes            yes                 可以有多个         允许，不推荐
        
    外键：
        1. 在从表设置外键关系
        2. 从表的外键列的类型和主表的关联列的类型要求一致或兼容
        3. 主表的关联列必须是一个key(一般是主键)
        4. 插入数据时，先插入主表，再插入从表
        5. 删除数据时，先删除从表，再删除主表

        insert into major values(1,'java')
        insert into major values(2,'h5')
常见约束
create table 表名(
    字段名  字段类型  约束
    字段名  字段类型，
    表级约束
)

一、创建表时添加约束
    1. 添加列级约束
    语法：
        直接在字段名和类型后面追加约束类型即可
        只支持：默认、非空、主键、唯一
        可以添加多个列级约束，用空格隔开
    create database students;
    use students;

    create table stuinfo(
        id int primary key,
        stuName varchar(20) not null,
        gender char(1) check(gender='男'or gender = '女'),
        seat int unique,
        age int default 18,
        majorid int references major(id)
    );

    create table major(
        id int primary key,
        majorName varchar(20)
    );

    show index from stuinfo
    查看stuinfo表中所有的索引，包括主键，外键，唯一

    2. 添加表级约束
    语法：
        【constraint 约束名】 约束类型(字段名)
    drop table if exists stuinfo;
    create table stuinfo(
        id int,
        stuname varchar(20),
        gender char(1),
        seat int,
        age int,
        majorid int,
        constraint pk primary key(id),
        constraint uq unique(seat),
        constraint ck chech(gender = '男' or gender = '女'),
        constraint fk_stuinfo_major foreign key(majorid) references major(id)
    )

    通用写法：
    create table if not exists stuinfo(
        id int primary key,
        stuname varchar(20) not nill,
        sex char(1),
        age int default 18,
        seat int unique,
        majorid int,
        constraint fk_stuinfo_major foreign key(majorid) references major(id)
    )

    二、修改表时添加约束
    1. 添加列级约束
    alter table 表名 modify colunm 字段名 字段类型 新约束;
    2. 添加表级约束
    alter table 表名 add 【constraint 约束名】 约束类型(字段名) 外键的引用;

    drop table if exists stuinfo;
    create table stuinfo(
        id int,
        stuname varchar(20),
        gender char(1),
        seat int,
        age int,
        majorid int
    )
    1. 添加非空约束
    alter table stuinfo modify column stuname varchar(20) not null;
    删除非空约束：
    alter table stuinfo modify column stuname varchar(20) null;
    2. 添加默认约束
    alter table stuinfo modify column age int default 18;
    3. 添加主键
        1. 列级约束
    alter table stuinfo modify column id int primary key;
        2. 表级约束
    alter table stuinfo add primary key(id);
    4. 添加唯一键
        1. 列级约束
    alter table stuinfo modify column seat int unique;
        2. 表级约束
    alter table stuinfo add unique(seat);
    5. 添加外键
    alter table stuinfo add constraint fk_stuinfo_major foreign key(majorid) references major(id)
   
    三、修改表时删除约束
    1. 删除非空约束
    alter table stuinfo modify column stuname varcahr(20) null;
    2. 删除默认约束
    alter table stuinfo modify column age int;
    3. 删除主键
    alter table stuinfo drop primary key;
    4. 删除唯一
    alter table stuinfo drop index seat;
    5. 删除外键
    alter table stuinfo drop foreign key fk_stuinfo_major;

    show index from stuinfo 查找键的名字

'''P132'''
[test]
1. alter table emp2 add constraint my_dept_id_pk id int primary key
alter table emp2 modify column id int primary key

3. alter tabke emp2 add column dept_id int
alter table emp2 add constraint fk_emp2_dept2 foreign key(dept_id) references dept2(id);

'''P133'''
标识列
    又称为自增长列
    含义：可以不用手动的插入值，系统提供默认的序列值

    特点：
    1. 标识列必须和主键搭配吗？不一定，但要求有一个key
    2. 一个表可以有几个标识列？至多一个
    3. 标识列的类型只能是数值型
    4. 标识列可以通过set auto_increment_increment=3;设置步长
       也可以通过手动设置值设置起始值: alter table test auto_increment = 140


一、创建表时设置标识列
drop table if exists tab_identity
create table tab_identity(
    id int primary key auto_increment,
    name varchar(20)
)
insert into tab_identity values(null,'john')

二、修改表时设置标识列
alter table tab_identity modify column id int primary key auto_increment

三、修改表示删除标识列
alter table tab_identity modify column id int primary key;

'''P134'''
TCL 事务控制语言
    事务：
    一个或者一组SQL语句组成一个执行单元，这个单元要么全部执行，要么全部不执行
    案例：转账
    张三丰 1000
    郭襄   1000
    update 表 set 张三丰余额=500 where name = '张三丰'
    update 表 set 郭襄余额=500 where name = '郭襄'

    show engines;显示存储引擎
    innodb支持事务，myisam,memory不支持事务

    事务的ACID属性
    1. 原子性(A)
    原子性是指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。
    2. 一致性(C)
    事务必须使数据库从一个一致性状态变换到另外一个一致性状态
    3. 隔离性(I)
    一个事务的执行不能被其他事务干扰
    4. 持久性(D)
    一个事务一旦被提交，对数据库的改变是永久性的

1. 事务的创建
隐式事务：事务没有明显的开启和结束的标记
比如insert、update、delete语句

显式事务：事务具有明显的开启和结束的标记
前提：必须先设置自动提交功能为禁用

set autocommit=0;

步骤1：开启事务
set autocommit=0;
start transaction;可选的
步骤2：编写事务的sql语句(select insert update delete)
语句1;
语句2;
……
步骤3：结束事务
commit; 提交事务
rollback; 回滚事务

savepoint 节点名;设置保存点

drop table if exists account;
create table account(
    id int primary key auto_increment,
    username varchar(20),
    balance double
);
insert into account(username,balance)
values('张无忌',1000),('赵敏',1000);
演示事务的使用步骤
1. 开启事务
set autocommit=0;
start transaction;
2. 编写一组事务的语句
update account set balance=500 where username='张无忌';
update account set balance=1500 where username='赵敏';
3. 结束事务
commit;

2. delete 和truncate 在事务使用时的区别
truncate 不能回滚，delete 可以回滚

演示delete
    set autocommit=0;
    start transaction;
    delete from account;
    rollback;
可以回滚

演示truncate
    set autocommit=0;
    start transaction;
    truncate from account;
    rollback;
不能回滚

'''P137'''
隔离级别
查看当前的隔离级别：select @@tx_isolation;
设置当前的隔离级别：set transaction isolation level read commited;
设置全局的隔离级别：set global transaction isolation level read commited;

                        脏读        不可重复读         幻读
read uncommited:        yes             yes             yes
read commited:          no              yes             yes
repeated read:          no              no              yes 
serializable:           no              no              no
mysql中默认第三个隔离级别repeatable read
oracle中默认第二个隔离级别read commited
查看隔离级别
select @@tx_isolation;
设置隔离级别
set session|global transaction;

3. 演示savepoint的使用
set autocommit=0;
start transaction;
delete from account where id=25;
savepoint a;
delete from account where id=28;
rollback to a;

a之前的删除
a之后的不删除

'''P139'''
视图
    含义：虚拟表，和普通表一样使用
    mysql5.1版本出现的新特性，是通过表动态生成的数据                使用

            创建语法的关键字   是否实际占有物理空间     增删改查，一般不能增删改
    视图     create view        只是保存了sql逻辑               增删改查
    表       create table           保存了数据
example1: 查询姓张的学生名和专业名
use students;
select stuname，majorname
from stuinfo as s,major as m
where stuname like '张%' and s.majorid=m.id

create view v1
as 
select stuname，majorname
from stuinfo as s,major as m
where s.majorid=m.id

一、创建视图
语法：
create view 视图名 as 
查询语句；

use myemployees;

example1. 查询姓名中包含a字符的员工名、部门名和工种信息
create view v1
as
select last_name,department_name
from employees as e,departments as d
where e.department_id = d.department_id;
select * from v1
where last_name like '%a%';

exmaple2. 查询各部门的平均工资级别
create view v2
as 
select department_id,avg(salary) as 平均工资
from employees as e,job_grades as j
group by department_id;
select v2.department_id,j.grade_level
from v2,job_grades as j
where v2.平均工资 between j.lowest_sal and j.highest_sal;

example3. 查询平均工资最低的部门信息
select *
from departments as d
where d.department_id=(
    select department_id
    from v2
    order by 平均工资 limit 1;
)
example4. 查询平均工资最低的部门名和工资
select d.department_name,v2.平均工资
from v2,departments as d
order by 平均工资 ASC limit 1;

二、视图的修改
    方式一：
    create or replace view 视图名
    as
    查询语句;

方式二：
    语法：
    alter view 视图名
    as 
    查询语句;

三、删除视图
    语法：
    drop view 视图名，视图名

drop view v1,v2,v3

四、查看视图
desc v3;

[test]
1. 创建视图emp_v1,要求查询电话号码以'011'开头的员工姓名和工资、邮箱
create view emp_v1
as
select last_name,salary,email
from employees as e
where phone_number like '011%';

2. 创建视图exp_v2,要求查询部门的最高工资高于12000的部门信息
create view emp_v2
as
select *
from departments as d
where d.department_id in (
    select department_id
    from employees as e
    group by department_id
    having max(salary)>12000  
)

五、视图的更新
create or replace view myv1
as 
select last_name,email,salary*12*(1+ifnull(commission_pct,0)) as 'annual salary'
from employees;

select * from myv1;
select * from employees;


1. 插入
insert into myv1 values('张飞','qqq','1000000')

2. 修改
update myv1 set last_name = '张无忌'
where last_name = '张飞'

3. 删除
delete from myv1 where last_name = '张无忌'

具备以下特点的视图是不允许更新的：
    1. 包含以下关键词的sql语句：分组函数、distinct、group by、having、union或者union all
    create or replace view myv1
    as

    select max(salary),department_id
    from employees
    group by department_id;
    
    selct * from myv1;
    update myv1 set m=9000 where department=10;

    2. 常量视图
    create or replace view myv2
    as 
    select 'lyp' name;
    select * from myv2;

    update myv2 set name='lucy';

    3. select中包含子查询
    create or replace view myv3
    as 
    select department_id,(select max(salary) from employees)
    from departments;

    select * from myv3;
    update myv3 set 最高工资=100000;

    4. join
    create or replace view myv4
    as
    select last_name,department_name
    from employees as e
    join department d
    on e.department_id=d.department_id

    select * from myv4;
    update myv4 set last_name = '张飞' where last_name = 'Whalean'

    5. from 一个不能更新的视图
    create or replace view myv5
    as
    select * from myv3;

    select * from myv5;
    update myv5 set 最高工资=10000 where department_id=60;

    6. where 子句的子查询引用了from子句中的表
    create or replace view myv6
    as
    select last_name,email,salary
    from employees
    where employee_id in (
        select employee_id
        from employees
        where manager_id is not null
    )

    select * from myv6;
    update myv6 set salary = 100000 wherer last_name = 'K_ing'

'''P147'''
[test]
1. 创建表Book表，字段如下：
bid 整型，要求主键
bname 字符型，要求设置唯一键，并非空
price 浮点型，要求有默认值10
brypeid 类型编号，要求引用booktype表的id字段 
create table Book(
    bid int primary key,
    bname char unique not null,
    price float default 10,
    bryeid int,
    foreign key(btypeid) reference bookType(id)
    )

2. 开启事务
向表中插入1行数据，并结束
set autocommit=0;
start transaction;
insert into book(bid,bname,price,btypeid)
values();

3. 创建视图，实现查询价格大于100的书名和类型名
create view v1
as 
select bookname,typename
from books
where price > 100;

4. 修改视图，实现查询价格在90-120 之间的书名和价格
create or replace view myv1
as
select bname,price 
from books as b
where price between 90 and 129;

5. 删除刚才建的视图
delete view myv1;

'''P149'''
变量
    系统变量：
        全局变量
        会话变量
    自定义变量：
        用户变量
        局部变量

一、系统变量
说明：变量由系统提供，不是用户自定义，属于服务器层面
使用的语法：
1. 查看所有的系统变量
show global/【session】 variables;

2. 查看满足条件的部分系统变量
show global/【session】 variables like '%char%';

3. 查看指定的某个系统变量的值
select @@global/【session】.系统变量名;

4. 为某个具体的系统变量赋值
方式一：
set global/session 系统变量名=值
方式二：
set @@global/【session】.系统变量名=值

注意：
如果是全局级别，则需要加global,如果是会话级别，则需要加session，如果不写，则默认session 

1. 全局变量
    作用域：服务器每次启动将为所有的全局变量赋初始值，针对于所有的会话和连接有效，但是不能跨重启(重启后不能生效)

    1. 查看所有的全局变量
    show golbal variables

    2. 查看部分的全局变量
    show global variables like '%char%';

    3. 查看指定的全局变量的值
    select @@global.autocommit;
    select @@tx_isolation;
    查看隔离级别

    4. 为某个指定的全局变量赋值
    set @@global.autocommit=0;

2. 会话变量
    作用域：仅仅针对于当前会话(连接)有效

    1. 查看所有的会话变量
    show variables;
    show session variables;

    2. 查看部分的会话变量
    show variables like '%char%';
    show session variables like '%char%';

    3. 查看指定的某个会话变量
    select @@tx_isolation;
    select @@session.tx_isolation;

    4. 为某个会话比那辆赋值
    方式一：
        set @@session.tx_isolation='read-uncommited';
    方式二：
        set session tx_isolation ='read-commited';

二、自定义变量
    说明：变量是用户自定义的，不是由系统的
    使用步骤：
    声明
    赋值
    使用(查看、比较、运算)

    1. 用户变量
    作用域：针对于当前会话(连接)有效，同于会话变量的作用域
    应用在任何地方，也就是begin end里面或者begin end外面
        赋值的操作符：=或者:=
        1. 声明并初始化
        set @用户变量名=值;
        set @用户变量名:=值;
        select @用户变量名:=值;

        2. 赋值(更新用户变量的值)
        方式一：通过set 或者select 
            set @用户变量名=值;
            set @用户变量名:=值;
            select @用户变量名:=值;
        方式二：通过select into 
            select 字段 into @变量名
            from 表

        3. 使用(查看用户变量的值)
        select @用户变量名
        example1: 
            set @count =1;
            # 赋值
            select count(*) into @count
            from employees

            select @count;
            # 查看

    2. 局部变量
    作用域：仅仅在它的begin end中有效
    应用在begin end中的第一句话
        1. 声明
        declare 变量名 类型;
        declare 变量名 类型 default 值;

        2. 赋值
        方式一：通过set 或者select
            set @用户变量名=值;或
            set @用户变量名:=值;或
            select @用户变量名:=值;        
        
        方式二：通过select into
            select 字段 into 局部变量名
            from 表;

        3. 使用
        select 局部变量名;

    对比用户变量和局部变量：
    
                作用域          定义和使用的位置                        语法
    用户变量    当前会话            会话中任何地方                  必须加@符号，不用限定类型
    局部变量    begin end中     只能在begin end中，且为第一句话     一般不用加@符号，需要限定类型

    example：声明两个变量并赋出事值，求和，并打印
        1. 用户变量
        set @m=1;
        set @n=2;
        set @sum=@m+@n;
        select @sum;

        2. 局部变量
        declare m int default 1;
        declare n int default 2;
        declare sum int;
        set sum=m+n;
        select sum;

三、存储过程和函数
    存储过程和函数：类似于java 中的方法
    好处：
    1. 提高代码的重用性
    2. 简化操作


存储过程
# 存储的过程，视图是存储的结果
    含义：一组预先编译好的sql语句的集合，理解成批处理语句
    1. 提高代码的重用性
    2. 简化操作
    3. 减少了编译次数并且减少了和数据库服务器的连接次数，提高了效率



一、创建语法
create procedure 存储过程名(参数列表)
begin 
存储过程体(一组合法的sql语句)
end

注意：
    1. 参数列表包括三部分
    参数模式    参数名  参数类型
    举例：
    in stuname varchar(20)

    参数模式：
    in：该参数可以作为输入，也就是该参数需要调用方传入值
    out：该参数可以作为输出，也就是该参数可以作为返回值
    inout：该参数既可以作为输入，又可以作为输出

    2. 如果存储过程体仅仅只有一句话，begin end可以省略

    3. 存储过程体中的每条sql语句的结果要求必须加分号
       存储过程的结尾可以使用delimiter 重新设置
       语法：
       delimiter 结束标记

       example：
       delimiter $

二、调用语法
call 存储过程名(实参列表);

三、[test]
1. 实参列表
example1: 插入到admin表中五条记录

delimeter $
create procedure myp1()
begin
    insert into admin(username,password)
    values('lyp','0000'),('zll','2222');
end $

调用
call myp1()$

2. 创建带in模式参数的存储过程
example1: 穿件存储过程实现 根据女神名查询对应的男神信息
create procedure myp2(in beautyname varchar(20))
begin
    select bo.*
    from boys bo
    right join beauty b on bo.id=b.boyfriend_id
    where b.name=beautyname;

end $


'''P165'''
函数
    含义：一组预先编译好的sql语句的集合，理解成批处理语句
    1. 提高代码的重用性
    2. 简化操作
    3. 减少了编译次数并且减少了和数据库服务器的连接次数，提高了效率

    区别：
    存储过程：可以有0个返回，也可以有多个返回，适合做批量插入、批量更新
    函数：必须只能有1个返回，适合做处理数据后返回一个结果

一、创建语法
create function 函数名(参数列表) returns 返回类型
begin 
    函数体
end

注意：
1. 参数列表包含两部分：
参数名 参数类型

2. 函数体：肯定会有return 语句，如果没有会报错
如果return 语句没有放在函数体的最后不会报错，但是不建议

return 值;

3. 函数体中只有一句话，可以省略begin end

4. 使用delimiter 语句设置结束标记

delimiter $;

二、调用语法
select 函数名(参数列表)

example1: 无参数有返回
返回公司的员工个数
create function myf1() returns int
begin
    declare c int default 0;
    select count(*) into c
    from employees;
    return c;
end $

select myfa()$

2. 有参数有返回
example1: 根据员工名返回他的工资

create function myf2(empName varchar(20)) returns double 
begin
    set @sal=0;
    select salary into @sal
    from employees
    where last_name=empname;

end $

'''P170'''
流程控制结构
    顺序结构：程序从上往下一次执行
    分支结构：程序从两条或者多条路径中选择一条去执行
    循环结构：程序在满足一定条件的基础上，重复执行一段代码


一、分支结构
1. if函数
    功能：实现简单的双分支
    语法：
    select if(表达式1,表达式2,表达式3)
    执行顺序：
    如果表达式1成立，则函数返回表达式2的值，否则返回表达式3的值

    应用：任何地方

2. case结构
情况1：用于实现等值判断
语法：
    case 变量/表达式/字段
    when 要判断的值 then 返回的值1
    when 要判断的值 then 返回的值2
    ……
    else 要返回的值n
    end




情况2：用于实现区间判断
语法：
    case 变量/表达式/字段
    when 要判断的条件1 then 返回的值1或语句1;
    when 要判断的条件2 then 返回的值2或语句2;
    ……
    else 要返回的值n或语句n;
    end case

特点：
1. 
    可以作为表达式，嵌套在其他语句中使用，可以放在任何地方，begin end中或begin end的外面
    可以作为独立的语句去使用，只能放在begin end中

2. 
    如果when中的值满足或者语句成立，则执行对应的then后面的语句，并且结束case
    如果都不满足，则执行else中的语句或值

3. 
    else可以省略，如果else省略了，并且所有when条件都不满足，则返回null

exmaple:
创建存储过程，根据传入的成绩，来显示等级，比如传入的成绩在90-100 区间，显示A，80-90 显示B，60-80 显示C，否则显示D

create procedure test_case(in score int)
begin
    case
    when scoure>=90 and score<=100 then select 'A';
    when score>=80 then select 'B'
    when score>=60 then select 'C'
    else select 'D';
    end case; 
end $



时间转换函数
SELECT DATE_FORMAT(NOW(),'%y%m%d')

窗口函数

    排序
    row_number()/rank()/dense_rank() over(partition by order by ) as 

    累加
    sum() over(partition by order by)
    sum() over(partition by order by
        rows between unbounded preceding and current row/unbounded following) as 
    # 这里最好进行排序，不然会出错

    偏移
    lag/lead
    lag/lead(名称,偏移量,默认值) over(partition by order by ) as 
    lag是向上偏移,lead是向下偏移

    first_value/last_value(名称) over(partition by order by ) as 
    last_value默认是到当前行的值，也就是 over(partition by order by rows between unbounded preceding and current row)，如果需要修改为全部值需要改为
                                    over(partition by order by rows between unbounded preceding and unbounded following)

Case when
不能在前一句对一个值进行命名，之后case when 直接调用这个数值，必须重新建表使用此数值
eg: select () as a,case when a …… 
这样是不允许的


如果列表中存在null时，不能使用判断语句 A >/</<> B 等，应该使用 A >/</<> B or A is null

平方：power(x,n) = x**n

order 排序：(多条件排序用','隔开)

select customer_number
from(
select customer_number,count(*) sum
from orders o
group by customer_number
order by sum desc limit 1) s

等于

select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1

leetcode 1322
点击率
select ad_id,
ifnull(round(sum(action="Clicked")/sum(action<>"Ignored")*100,2),0.00) as ctr
from ads
group by ad_id
order by ctr desc,ad_id 

MySQL中sum和count用法总结

1.sum
（1）sum()函数里面的参数是列名的时候，是计算列名的值的相加，而不是有值项的总数。
（2）sum(条件表达式)，如果记录满足条件表达式就加1，统计满足条件的行数
（3）如果想要计算一列中符合条件的数量，可以sum(if(a=b,1,0))计算数量
（4）多条件判断：
    having sum(if(order_date between '2020-06-01' and '2020-06-30',p.price*o.quantity,0))>=100
    and sum(if(order_date between '2020-07-01' and '2020-07-31',p.price*o.quantity,0))>=100
2.count
（1）COUNT()函数里面的参数是列名的的时候,那么会计算有值项的次数。（NULL 不计入， 但是''值计入）
（2）COUNT(*)可以计算出行数，包括null
（3）COUNT(1)也可以计算出行数，1在这里代表一行
（4）COUNT(column)对特定的列的值具有的行数进行计算，不包含NULL值
（5）COUNT(条件表达式)，不管记录是否满足条件表达式，只要非NULL就加1

对比

select s.buyer_id
from product p, sales s
where p.product_id = s.product_id
group by s.buyer_id
having sum(p.product_name='S8') > 0 and sum(p.product_name='iphone') < 1

select buyer_id
from sales s
where buyer_id in(select buyer_id from sales s1 join product p1 on s1.product_id=p1.product_id where p1.product_name='S8') 
and buyer_id not in(select buyer_id from sales s1 join product p1 on s1.product_id=p1.product_id where p1.product_name='iPhone')
group by buyer_id



筛选出最大值有多个的情况(使用Having)
select project_id
from Project
group by  project_id
having count(employee_id)>=all(select count(employee_id) from Project group by  project_id)


取字符串
substr(code,1,n)
