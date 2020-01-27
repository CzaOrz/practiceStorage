### [GIT](#GIT)
* [Git](#Git)

----------

#### Git
* 安装git的流程
    * sudo apt-get install git<br>
    git config --global user.name "czaorz"<br>
    git config --global user.email "972542655@qq.com"<br>
    ssh-keygen -t rsa -C "youremail@example.com"
* 创建仓库的流程
    * git init --bare<br>
* 添加远程仓库
    * git remote add origin git@github.com:michaelliao/learngit.git
* 指令含义
    * git add  -- 将修改添加到暂存区
    * git commit  -- 将暂存区的修改，提交到分支
    * git push  -- 将当前分支信息，推到远程分支
* 版本回退
    * 没有add的情况下回退某个文件filename
        * git checkout -- filename
    * add 的情况下回退这个文件filename
        * git reset HEAD filename
    * commit 的情况下回退这个文件filename
        * git reset --hard HEAD^
    * 回退版本
        * HEAD表示当前版本，上一个版本用HEAD^表示，上上版本则用HEAD^^表示，而前100各版本用HEAD~100
        * git reset --hard HEAD^
        * git reset --hard commit_id
    * 当你回退了版本，但是又后悔了，想退到没退之前的版本
        * 使用 git reflog 可以查看历史命令，用这个主要就是查看提交版本的 commit_id 是多少
        * 然后直接使用 git reset --hard commit_id