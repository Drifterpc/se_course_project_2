新增功能：历史上的今天
1、用户可以查看当天的老黄历信息![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/dd4eaa1b-33d9-456c-8c3c-17781d39672e)
2、用户可以查看当天在历史上发生的著名事件![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/55db86f1-3991-4188-b14f-71f4daf6633e)
还可以点击下方的“点击加载更多”显示更多的事件![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/a1507691-346c-4ff1-9332-405790ef14e5)
3、每一个事件可以点击进入，从而查看事件详情![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/2bb1a059-3102-40be-870c-00b65d0b866d)
4、还可以点击右下角的日历控件切换日期![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/19f2c400-d450-423d-8c1f-738964a199bb)
如下为切换日期后显示的信息![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/358e111c-063a-48d3-8126-b4e6245c52f5)

1、介绍下项目的总体结构。
首先base包里面放的是底层需要调用的类BaseActivity和UniteApp，里面都是继承父类和接口后重写了方法。ContentURL就是我们调用的接口类，里面是获取URL的方法。


bean包都是实体集，HIstoryBean是【历史上的今天】实体集，HIstoryDescBean是【详细信息】实体集，LaoHuangliBean是【老黄历】实体集，你可以把bean理解为数据库里面一张表的设计，就是一个类它所有的私有属性以及get/set方法。

下面的HistoryActivity就是二级页面的活动文件，HistoryAdapter是适配器文件，用来把从网络上获取的数据显示到列表中，有列表那肯定有adapter，可以把它理解为容器，ListView装上adapter就可以显示了。

HistoryDescActivity是三级页面的活动文件，它不是列表显示，所以不需要adapter。最后就是MainActivity了，作为所有Android项目都有的活动文件，这里它起到的还是列表的作用，从上到下展示内容，我们下面会讲到。

2、获取网络数据的URL
这里的key值是我自己申请的，如果你运行项目出现没有数据的情况，应该是使用次数到达每日上限，方便起见，可以自己去【聚合数据】官网申请这两个key，一个是【老黄历】，还有一个是【历史上的今天】，然后替换掉下面三个方法中对应的key值，第一个和第三个需要替换【历史上的今天】的key值，第二个需要替换【老黄历】的key值。

运行环境要保证电脑是联网的，不然key值有用，也不会显示数据。
