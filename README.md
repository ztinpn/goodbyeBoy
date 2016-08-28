# goodbyeBoy 用python生成《非诚勿扰》恶搞微信好友头像的视频

起因是微信好友发了一个搞笑视频：非诚勿扰节目里屏幕出现一人头像然后慢慢全灭灯响起可惜不是你，我一看兴致来了，希望把里面的头像换成任意好友的头像，然后发给他们，或者在微信群里恶搞。感觉思路比较清晰，修改视频里的几帧就行，难点是openCV库没有音频视频混流的功能，后来用python调用ffmpeg解决了。

##效果

上传用户头像，产生《非诚勿扰》节目全灭灯的恶搞视频，仅1MB左右的大小，可方便地用于QQ、微信聊天等场景（可用微信PC版上传视频）。
可下载 https://github.com/ztinpn/goodbyeboy/blob/master/template/template.mp4?raw=true 查看示例。

##用法

将头像拷贝到当前文件夹下，重命名为src.jpg，双击运行goodbyeBoy.py，完成后会在当前目录生成 日期时间.mp4。

##配置步骤

由于代码依赖openCV和numpy，因此需要做（windows 10, python 2.7.12下测试通过，其他情况请自行修改。）：

1. 把 opencv\python\2.7\x86 下的 cv2.pyd 拷贝到 C:\Python27\Lib\site-packages 中；
2. windows系统环境变量增加 当前路径\opencv\ffmpeg；
3. 去https://sourceforge.net/projects/numpy/files/NumPy/1.9.2/ 下载numpy-1.9.2-win32-superpack-python2.7.exe并安装。



