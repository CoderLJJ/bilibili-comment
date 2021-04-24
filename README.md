### b站自动化评论程序

| 获取视频列表网址  | get-video-list.py   |
| ----------------- | ------------------- |
| 遍历视频列表网址  | bilibili-comment.py |
| 合并多个excel文件 | hebing-xlsx.py      |

### 准备材料

1. Chrome浏览器
2. Chromedriver驱动
3. python开发环境

### 开始运行

1. 运行get-video-list.py获取搜索结果视频列表，生成对应的excel文件
2. 修改bilibili-comment里面读取对应的excel文件名，修改要发送的评论内容
3. option.add_argument('--user-data-dir =你的谷歌浏览器个人资料路径')，可以通过chrome://version查看
4. 运行一次，然后登录一次b站，浏览器记住cookie，就可以实现免登录了

