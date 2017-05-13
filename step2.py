import MySQLdb
#连接
conn=MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='1',
    db='student',
    charset='utf8'
)
cursor=conn.cursor()

#building的数据录入
d1="INSERT department VALUES('computer','Building_A',12000)";
d2="INSERT department VALUES('biology','Building_B',24000)";
d3="INSERT department VALUES('physics','Building_C' ,28000)";
d4="INSERT department VALUES('new', 'Building_D', 8000)";
d5="INSERT department VALUES('math', 'Buding_E', 35000)";

cursor.execute(d1)
cursor.execute(d2)
cursor.execute(d3)
cursor.execute(d4)
cursor.execute(d5)

#student的数据录入
s1="INSERT student VALUES(1,'廉萱妍','f',19,'loving','computer')";
s2="INSERT student VALUES(2,'荀良运','m',17,'single','computer')";
s3="INSERT student VALUES(3,'尹枫起','m',14,'loving','computer')";
s4="INSERT student VALUES(4,'皇甫梦心','f',13,'loving','computer')";
s5="INSERT student VALUES(5,'司马海禧','m',24,'loving','computer')";
s6="INSERT student VALUES(6,'薛珊柏','f',21,'single','biology')";
s7="INSERT student VALUES(7,'皇甫驰钊','m',21,'single','physics')";
s8="INSERT student VALUES(8,'骆谷震','m',23,'single','computer')";
s9="INSERT student VALUES(9,'吕禧逸','m',18,'single','biology')";
s10="INSERT student VALUES(10,'公孙子晨','m',20,'loving','physics')";
s11="INSERT student VALUES(11,'王凡康','m',21,'loving','physics')";
s12="INSERT student VALUES(12,'谢婷桃','f',21,'single','computer')";
s13="INSERT student VALUES(13,'寿雨华','f',20,'single','physics')";
s14="INSERT student VALUES(14,'昌菲婧','f',19,'loving','new')";
s15="INSERT student VALUES(15,'赵梓梓','m',22,'loving','biology')";
s16="INSERT student VALUES(16,'尉迟彩鑫','f',22,'single','new')";
s17="INSERT student VALUES(17,'毛骏钊','m',23,'single','new')";
s18="INSERT student VALUES(18,'吴腾梁','m',17,'loving','math')";
s19="INSERT student VALUES(19,'庞德骏','m',23,'loving','math')";
s20="INSERT student VALUES(20,'梅昭凡','f',18,'single','computer')";

cursor.execute(s1)
cursor.execute(s2)
cursor.execute(s3)
cursor.execute(s4)
cursor.execute(s5)
cursor.execute(s6)
cursor.execute(s7)
cursor.execute(s8)
cursor.execute(s9)
cursor.execute(s10)
cursor.execute(s11)
cursor.execute(s12)
cursor.execute(s13)
cursor.execute(s14)
cursor.execute(s15)
cursor.execute(s16)
cursor.execute(s17)
cursor.execute(s18)
cursor.execute(s19)
cursor.execute(s20)

#exam的数据插入
sql11="insert exam values(1,'FirstExam',62)"
sql12="INSERT exam VALUES(1,'SecondExam',70)"
sql13="INSERT exam VALUES(1,'ThirdExam',98)"
sql14="INSERT exam VALUES(1,'FinalExam',93)"
sql21="insert exam values(2,'FirstExam',46)"
sql22="INSERT exam VALUES(2,'SecondExam',97)"
sql23="INSERT exam VALUES(2,'ThirdExam',68)"
sql24="INSERT exam VALUES(2,'FinalExam',60)"
sql31="insert exam values(3,'FirstExam',64)"
sql32="INSERT exam VALUES(3,'SecondExam',48)"
sql33="INSERT exam VALUES(3,'ThirdExam',94)"
sql34="INSERT exam VALUES(3,'FinalExam',68)"
sql41="insert exam values(4,'FirstExam',69)"
sql42="INSERT exam VALUES(4,'SecondExam',100)"
sql43="INSERT exam VALUES(4,'ThirdExam',97)"
sql44="INSERT exam VALUES(4,'FinalExam',56)"
sql51="insert exam values(5,'FirstExam',91)"
sql52="INSERT exam VALUES(5,'SecondExam',86)"
sql53="INSERT exam VALUES(5,'ThirdExam',58)"
sql54="INSERT exam VALUES(5,'FinalExam',81)"
sql61="insert exam values(6,'FirstExam',81)"
sql62="INSERT exam VALUES(6,'SecondExam',70)"
sql63="INSERT exam VALUES(6,'ThirdExam',98)"
sql64="INSERT exam VALUES(6,'FinalExam',93)"
sql71="insert exam values(7,'FirstExam',60)"
sql72="INSERT exam VALUES(7,'SecondExam',48)"
sql73="INSERT exam VALUES(7,'ThirdExam',63)"
sql74="INSERT exam VALUES(7,'FinalExam',74)"
sql81="insert exam values(8,'FirstExam',86)"
sql82="INSERT exam VALUES(8,'SecondExam',99)"
sql83="INSERT exam VALUES(8,'ThirdExam',73)"
sql84="INSERT exam VALUES(8,'FinalExam',79)"
sql91="insert exam values(9,'FirstExam',94)"
sql92="INSERT exam VALUES(9,'SecondExam',61)"
sql93="INSERT exam VALUES(9,'ThirdExam',49)"
sql94="INSERT exam VALUES(9,'FinalExam',72)"
sql101="insert exam values(10,'FirstExam',62)"
sql102="INSERT exam VALUES(10,'SecondExam',67)"
sql103="INSERT exam VALUES(10,'ThirdExam',68)"
sql104="INSERT exam VALUES(10,'FinalExam',78)"
sql111="insert exam values(11,'FirstExam',94)"
sql112="INSERT exam VALUES(11,'SecondExam',60)"
sql113="INSERT exam VALUES(11,'ThirdExam',93)"
sql114="INSERT exam VALUES(11,'FinalExam',60)"
sql121="insert exam values(12,'FirstExam',98)"
sql122="INSERT exam VALUES(12,'SecondExam',48)"
sql123="INSERT exam VALUES(12,'ThirdExam',69)"
sql124="INSERT exam VALUES(12,'FinalExam',86)"
sql131="insert exam values(13,'FirstExam',46)"
sql132="INSERT exam VALUES(13,'SecondExam',84)"
sql133="INSERT exam VALUES(13,'ThirdExam',47)"
sql134="INSERT exam VALUES(13,'FinalExam',83)"
sql141="insert exam values(14,'FirstExam',52)"
sql142="INSERT exam VALUES(14,'SecondExam',97)"
sql143="INSERT exam VALUES(14,'ThirdExam',91)"
sql144="INSERT exam VALUES(14,'FinalExam',84)"
sql151="insert exam values(15,'FirstExam',85)"
sql152="INSERT exam VALUES(15,'SecondExam',68)"
sql153="INSERT exam VALUES(15,'ThirdExam',100)"
sql154="INSERT exam VALUES(15,'FinalExam',52)"
sql161="insert exam values(16,'FirstExam',59)"
sql162="INSERT exam VALUES(16,'SecondExam',58)"
sql163="INSERT exam VALUES(16,'ThirdExam',95)"
sql164="INSERT exam VALUES(16,'FinalExam',58)"
sql171="insert exam values(17,'FirstExam',92)"
sql172="INSERT exam VALUES(17,'SecondExam',93)"
sql173="INSERT exam VALUES(17,'ThirdExam',100)"
sql174="INSERT exam VALUES(17,'FinalExam',49)"
sql181="insert exam values(18,'FirstExam',87)"
sql182="INSERT exam VALUES(18,'SecondExam',81)"
sql183="INSERT exam VALUES(18,'ThirdExam',93)"
sql184="INSERT exam VALUES(18,'FinalExam',58)"
sql191="insert exam values(19,'FirstExam',85)"
sql192="INSERT exam VALUES(19,'SecondExam',88)"
sql193="INSERT exam VALUES(19,'ThirdExam',91)"
sql194="INSERT exam VALUES(19,'FinalExam',62)"
sql201="INSERT exam values(20,'FirstExam',88)"
sql202="INSERT exam VALUES(20,'SecondExam',78)"
sql203="INSERT exam VALUES(20,'ThirdExam',94)"
sql204="INSERT exam VALUES(20,'FinalExam',100)"

cursor.execute(sql11)
cursor.execute(sql12)
cursor.execute(sql13)
cursor.execute(sql14)
cursor.execute(sql21)
cursor.execute(sql22)
cursor.execute(sql23)
cursor.execute(sql24)
cursor.execute(sql31)
cursor.execute(sql32)
cursor.execute(sql33)
cursor.execute(sql34)
cursor.execute(sql41)
cursor.execute(sql42)
cursor.execute(sql43)
cursor.execute(sql44)
cursor.execute(sql51)
cursor.execute(sql52)
cursor.execute(sql53)
cursor.execute(sql54)
cursor.execute(sql61)
cursor.execute(sql62)
cursor.execute(sql63)
cursor.execute(sql64)
cursor.execute(sql71)
cursor.execute(sql72)
cursor.execute(sql73)
cursor.execute(sql74)
cursor.execute(sql81)
cursor.execute(sql82)
cursor.execute(sql83)
cursor.execute(sql84)
cursor.execute(sql91)
cursor.execute(sql92)
cursor.execute(sql93)
cursor.execute(sql94)
cursor.execute(sql101)
cursor.execute(sql102)
cursor.execute(sql103)
cursor.execute(sql104)
cursor.execute(sql111)
cursor.execute(sql112)
cursor.execute(sql113)
cursor.execute(sql114)
cursor.execute(sql121)
cursor.execute(sql122)
cursor.execute(sql123)
cursor.execute(sql124)
cursor.execute(sql131)
cursor.execute(sql132)
cursor.execute(sql133)
cursor.execute(sql144)
cursor.execute(sql151)
cursor.execute(sql152)
cursor.execute(sql153)
cursor.execute(sql154)
cursor.execute(sql161)
cursor.execute(sql162)
cursor.execute(sql163)
cursor.execute(sql164)
cursor.execute(sql171)
cursor.execute(sql172)
cursor.execute(sql173)
cursor.execute(sql174)
cursor.execute(sql181)
cursor.execute(sql182)
cursor.execute(sql183)
cursor.execute(sql184)
cursor.execute(sql191)
cursor.execute(sql192)
cursor.execute(sql193)
cursor.execute(sql194)
cursor.execute(sql201)
cursor.execute(sql202)
cursor.execute(sql203)
cursor.execute(sql204)

#上传
conn.commit()


cursor.close()
conn.close()