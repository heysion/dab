Target
pakages 
source build
task host channel

# dabctl
dabctrl newtarget --name=testtarget --arch=amd64 --codename=testing
dabctrl new-pkg --name=deepin-auto-build --target=testtarget
dabctl set-build-depends --name=deepin-auto-build --build-depends=python,tornado,postgresql
dabctrl upload-src deepin-auto-build_0.1.dsc --package=deepin-auto-build
dabctrl new-build --package=deepin-auto-build 
dabctrl new-task deepin-auto-build_0.1.dsc --package=deepin-auto-build --arch=amd64
dabctrl update-repo --target=testtarget
dabctrl repo-del --target=testtarget --package=deepin-auto-build
dabctrl pkg-del --name=deepin-auto-build --all #source build repo
dabctrl pkg-rename dab --name=deepin-auto-build --wait # update build source repo && check depends 
dabctrl update-src deepin-auto-build_0.2.dsc --package=deepin-auto-build

#web api
list all task 
list all target 
list all package
select package build
select package source
select package task


提交source 后，newtask 将 source 添加到 task表中。然后通过 将build 注册到 task中。 
首先将dsc 文件信息写入到 source (package + version)表中，然后通过 build-name 去查询 build信息。没有就初始化build （package + version ) 信息。
同时下发 task 任务。
task任务执行完。将task任务标记完成。并更新 build表，（将debctl信息写入 build表中，并标记build成功）

updaterepo 的时候，更加仓库规则去拉去最新的 build信息（debctl信息，通过package查询）同时使用reporepo 工具创建仓库，将仓库last连接链向 当前仓库。

newrepo 创建仓库规则，并拉去最新build包，创建仓库。

00

http://www.evil0x.com/posts/9780.html