# 动车站信息管理系统
 实现基于RBAC(Role Based Access Control，基于角色的访问控制)用户角色和权限管理。

主要采用Django用作后端框架，前端用flask框架搭建前端服务器，用作返回页面，数据库采用mysql，即构成一个前后端分离应用。

用户可分为两种类型：
一种是普通旅客，可以在平台上进行留言，以及之后的增删改查。
一种是站点管理员，可以在平台上进行日常站点的信息管理操作，以及之后的增删改查。
管理员可分为四大类，可登录平台后台进行操作分别为：
旅客反馈处理组（负责处理旅客的信息留言）
站点信息核对组（负责核对动车站日常的信心管理）
人事组（负责管理用户信息，包括普通旅客及管理员）
超级管理员（拥有最高权限）

以上用户及管理员的身份之差异及管理员之间身份的差区别都体现了“用户-角色-权限”的含义。


