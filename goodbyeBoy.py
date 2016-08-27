# -*- coding: utf-8 -*-  


if __name__ == '__main__':
    

    
    import cv2  
    video_src = cv2.VideoCapture('template/template.mp4')
    fps = video_src.get(cv2.cv.CV_CAP_PROP_FPS)  
    size = (int(video_src.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),   
            int(video_src.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))) 
    video_tar = cv2.VideoWriter('temp_output.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)  

    #读帧  
    success, frame = video_src.read()  

    src_img = cv2.imread("src.jpg")#读取用户图像
    src_hei, src_width = src_img.shape[:2]#读取用户图像高度宽度
    ratio_src = src_width*1.0/src_hei# 比例

    top_left_pos=(80,80)#视频中图片左上角位置 (y,x)
    photo_width = 329#视频中图片宽
    photo_height = 249#视频中图片高
    ratio_photo = photo_width*1.0/photo_height# 比例

    #计算贴图宽高以及位置
    if ratio_src<=ratio_photo:#用户图像更窄,限制高度
        tar_height=photo_height
        tar_width=int(1.0*tar_height*ratio_src)
        #计算需要贴图的左上角位置
        top_left_pos_tar=( top_left_pos[0], top_left_pos[1]+(photo_width-tar_width)/2 )
    else:
        tar_width=photo_width
        tar_height=int(1.0*tar_width/ratio_src)
        #计算需要贴图的左上角位置
        top_left_pos_tar=( top_left_pos[0]+(photo_height-tar_height)/2, top_left_pos[1] )

    #缩放贴图
    img2=cv2.resize(src_img,(tar_width,tar_height),interpolation=cv2.INTER_CUBIC)

    frame_ind = 0#帧号，便于定位
    while success:

        if frame_ind>=45 and frame_ind<=475:
            frame[79:340,79:408]=0#加黑边
            frame[top_left_pos_tar[0]:top_left_pos_tar[0]+tar_height,
                  top_left_pos_tar[1]:top_left_pos_tar[1]+tar_width]=img2
        frame_ind=frame_ind+1
        print u"处理中...%%%.2f " % (100.0*frame_ind/645)
        video_tar.write(frame) #写视频帧  
        success, frame = video_src.read() #获取下一帧

    cv2.destroyAllWindows()
    video_src.release()
    video_tar.release()

    import os,datetime
    final_output_filename=datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H_%M_%S.mp4')#最终视频文件名
    os.system('ffmpeg.win32.exe -i template/template.mp3  -i temp_output.avi '+final_output_filename)#音频视频混流
    os.system('del temp_output.avi')#删除中间文件
    print u"完成！"




