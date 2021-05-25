import cv2
import glob


def read_video():
    """
    逐帧读取视频文件
    """
    video = './video/input/library.mp4'
    capture = cv2.VideoCapture(video)
    if capture.isOpened():
        while True:
            ret, img = capture.read()  # img 就是一帧图片
            if not ret:
                break  # 当获取完最后一帧就结束
    else:
        print('视频打开失败！')


def write_video():
    """
    将图片拼接成视频输出
    """
    video = './video/output/library.mp4'
    writer = cv2.VideoWriter(video)
    img_paths = glob.glob('./pic/*.jpg')
    for path in img_paths:
        print(path)
        img = cv2.imread(path)
        writer.write(img)  # 读取图片后一帧帧写入到视频中
    writer.release()


def make_video():
    """
    逐帧读取视频并对帧图片进行处理
    将处理后的帧图片重新拼接成视频输出
    """
    video_input = './video/input/library.mp4'
    video_output = './video/output/library.avi'
    capture = cv2.VideoCapture(video_input)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    writer = None
    if capture.isOpened():
        while True:
            ret, img = capture.read()  # img 就是一帧图片
            if writer is None:
                writer = cv2.VideoWriter(video_output, fourcc, 30.0, (720, 1280), True)
            if not ret:
                break  # 当获取完最后一帧就结束
            img_out = op_img(img)
            writer.write(img_out)
    else:
        print('视频打开失败！')
    capture.release()
    writer.release()


def op_img(img):
    """
    图片处理方法
    :param img: 图片
    :return: 处理后的图片
    """
    x = 204
    y = 54
    height = img.shape[0]
    width = img.shape[1]
    x0 = x + width // 2
    y0 = y + height // 2
    cv2.rectangle(img, (x0 - 20, y0 - 20), (x0 + 20, y0 + 20), (0, 0, 255), 5)
    cv2.imwrite('./pic/test.jpg', img)
    return img


make_video()
