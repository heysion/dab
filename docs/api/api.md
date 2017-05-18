# 接口

## -w path 指定config.json文件所在的路径

## config.json 内容
```
{
"name":"deepin-server",
"tag":"15.1",
"arch":"mips64el",
"task":30,
"workbase":"/work/task/30",
"preseed":"preseed.cfg",
"include":"include.list",
"exclude":"exclude.list",
"output":"/work/mkiso",
"cache":"/work/cache",
"repo":"/work/mips64el",
"debian_cd":"/work/data/debian-cd"
}
```
### config 字段
name 定义项目名称用于ISO名字前缀

tag 项目的tag名字，用于ISO名字中缀

arch 架构名字

task 任务ID build id 全局唯一

workbase 任务执行工作目录

preseed preseed 文件路径

include 包含软件列清单

exclude 排除软件列表清单

output ISO输出目录

cache 公共cache共享目录

repo 仓库目录

debian_cd debian-cd的路径



