## 创建仓库

- git init

##  创建文件

1.touch test.py(新建文件）

2.git status(查看状态）

3.git add test.py(添加文件到暂存区）

4.git commit -m 'add test.py'（添加文件到仓库中）

## 修改文件

1.vi test.py（编辑器修文件）

2.git status(查看状态）

3.git add test.py(添加文件到暂存区）

4.git commit -m '这里写关于文件修改的描述'（提交文件到仓库中）

## 删除文件

1.rm -rf test.py(删除文件）

2.git rm test.py(从git中删除文件）

3.git commit -m '这里写关于文件删除的描述'（提交操作）

## 下载

git clone https://github.com/konglhui/titanic-translate.git(从github中下载项目到本地）

修改文件（步骤同修改文件一样）

## 将本地文件提交到github云仓库中

1.git remote add origin git@github.com:konglhui/仓库名.git


2.git pull --rebase origin master（在github仓库中可能在本地没有，这一步将GitHub的文件下载到本地，否则无法推送）

3.git push -u origin master （这样就可以正确的推动到github中了）
