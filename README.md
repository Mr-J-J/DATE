# 每日早安推送给女朋友
这个项目借鉴summercozyrock，在其基础上进行了封装优化，使不用懂代码也能制作每日早安推送
> 我会起一个仓库，用于友好交流，用于真正零代码做一个早安的推送


效果如图。当然，文字是可以修改的。
![5e72e89fd7ff692a0bfa62010517c0c](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-3928d054-65f7-4202-bdda-94a4bc56495a/aaab908c-24c9-4ecc-b0f4-c935433fe415.jpg)


之前看到有点朋友用action定时触发，刚开始我也是后来发现不准时，然后我采用阿里云函数

首先用想被推送的微信扫码然后找我要user-id
![5e72e89fd7ff692a0bfa62010517c0c](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-3928d054-65f7-4202-bdda-94a4bc56495a/30ace4fa-7300-462d-9b3a-779a5de1af1b.png)

然后打开网址填写信息，注意只需要填写一次，不重复提交，不然会多次推送，效果不好
https://static-3928d054-65f7-4202-bdda-94a4bc56495a.bspapp.com
![5e72e89fd7ff692a0bfa62010517c0c](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-3928d054-65f7-4202-bdda-94a4bc56495a/7baea4e1-c885-40bc-974b-d32b99fdf64b.png)

这样就可以啦

这个定时任务是每天早晨8点推送，有想法的话可以找我提提意见我会改一改～

Github 的右上角可以点击 star 给我点鼓励吧亲

点点关注，点点赞，有什么好玩的东西可以at我，我来教我来做
