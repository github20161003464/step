#3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句.
SELECT * FROM peoples where school IS NOT ‘GDUFS’;

#3-2.查找计算机系每次考试所有学生的平均成绩(最终显示考试名称, 平均分)。
SELECT exam.exam_name,avg(exam.grade) FROM exam WHERE student.dept_name = 'computer';

#3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
SELECT student.name,avg(exam.grade) FROM student,exam WHERE avg(exam.grade)>=80;

#3-4.找出人数最少的院系以及其年度预算。
select department.dept_name,department.budget from department where min(count(student.name));

#3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
alter table student change  column computer comp.sci where dept_name=’computer’;

#3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
update department set budget = count(student.name)*2000+department.budget where dept_name = ‘computer’;

#3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
update department set dept_name = avg_budget,building = NULL,budget = avg(budget);

#3-8. 删除计算机系中考试成绩平均分低于70的学生.
Delete from student,exam where student.dept_name=’computer’,avg(exam.grade)<70;

#3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
update student set student.emotion_state=’single’ where student.emotion_state=’loving’,avg(exam.grade<75);

#3-10(选做). 对每个学生, 往exam表格中插入名为Avg_Exam的考试, 考试分数为之前学生参加过考试的平均分.
alter table exam add  column Avg_Exam varchar(20);
for x in range(count(student.name)):
	insert into exam(Avg_Exam) values(avg(exam.grade));