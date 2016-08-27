# goodbyeboy

##效果

上传用户头像，产生《非诚勿扰》节目全灭灯的恶搞视频，可用于QQ、微信聊天等场景（可用微信PC版上传视频）。

##用法

将头像拷贝到当前文件夹下，重命名为src.jpg，双击运行main.py，完成后会在当前目录生成final_output.mp4。

##配置步骤

由于代码依赖openCV，因此需要做：

1. 把 opencv\python\2.7\x86 下的 cv2.pyd 拷贝到 C:\Python27\Lib\site-packages 中。
2. 环境变量增加 当前路径\opencv\ffmpeg


