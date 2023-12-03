1、介绍下项目的总体结构。
首先base包里面放的是底层需要调用的类BaseActivity和UniteApp，里面都是继承父类和接口后重写了方法。ContentURL就是我们调用的接口类，里面是获取URL的方法。

bean包都是实体集，HIstoryBean是【历史上的今天】实体集，HIstoryDescBean是【详细信息】实体集，LaoHuangliBean是【老黄历】实体集，你可以把bean理解为数据库里面一张表的设计，就是一个类它所有的私有属性以及get/set方法。

下面的HistoryActivity就是二级页面的活动文件，HistoryAdapter是适配器文件，用来把从网络上获取的数据显示到列表中，有列表那肯定有adapter，可以把它理解为容器，ListView装上adapter就可以显示了。

HistoryDescActivity是三级页面的活动文件，它不是列表显示，所以不需要adapter。最后就是MainActivity了，作为所有Android项目都有的活动文件，这里它起到的还是列表的作用，从上到下展示内容，我们下面会讲到。

2、获取网络数据的URL
这里的key值是我自己申请的，如果你运行项目出现没有数据的情况，应该是使用次数到达每日上限，方便起见，可以自己去【聚合数据】官网申请这两个key，一个是【老黄历】，还有一个是【历史上的今天】，然后替换掉下面三个方法中对应的key值，第一个和第三个需要替换【历史上的今天】的key值，第二个需要替换【老黄历】的key值。
![image](https://github.com/Drifterpc/se_course_project_2/assets/140794349/e6d9f545-e461-469d-847f-6564f0d3ff11)
运行环境要保证电脑是联网的，不然key值有用，也不会显示数据。
