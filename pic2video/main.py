import cv2
import glob
import numpy as np


class VideoMaker:
    def __init__(self):
        self.f = 3  # 焦距，单位cm
        self.dpi = 96 / 2.54  # 每cm像素点个数，常见 96/300
        self.get_xy()

    def get_xy(self):
        # 每帧对应的xyz坐标，当有多个目标时将其变为多维数组
        self.x3d = []
        self.y3d = []
        self.z3d = []
        # 每帧对应的xy坐标，当有多个目标时将其变为多维数组
        self.x = []
        self.y = []
        frame = 300  # 视频总帧数，和坐标数组长度保持一致
        for i in range(frame):
            matrix_1 = np.array([[self.f, 0, 0], [0, self.f, 0], [0, 0, 1]])
            matrix_2 = np.array([[self.x3d[i] / self.z3d[i]], [self.y3d[i] / self.z3d[i]], [1]])
            # 转换公式
            two_multi_res = np.dot(matrix_1, matrix_2)
            self.x.append(two_multi_res[0][0] * self.dpi)
            self.y.append(two_multi_res[1][0] * self.dpi)

    @staticmethod
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

    @staticmethod
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

    def make_video(self):
        """
        逐帧读取视频并对帧图片进行处理
        将处理后的帧图片重新拼接成视频输出
        """
        video_input = './video/input/library.mp4'
        video_output = './video/output/library.avi'
        capture = cv2.VideoCapture(video_input)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        writer = None
        frame = 0
        if capture.isOpened():
            while True:
                ret, img = capture.read()  # img 就是一帧图片
                if writer is None:
                    writer = cv2.VideoWriter(video_output, fourcc, 30.0, (img.shape[1], img.shape[0]), True)
                if not ret:
                    break  # 当获取完最后一帧就结束
                img_out = self.op_img(img, frame)  # 图像处理
                writer.write(img_out)  # 图像输出
                frame += 1
                # 注意视频真实帧数和坐标数组长度保持一致
                # if frame >= 300:
                #     break
        else:
            print('视频打开失败！')
        capture.release()
        writer.release()

    def op_img(self, img, frame):
        """
        图片处理方法
        :param img: 图片
        :param frame: 当前为第几帧
        :return: 处理后的图片
        """
        text = '(' + str(round(self.x3d[frame])) + ', ' + str(round(self.y3d[frame])) + ', ' + str(
            self.z3d[frame]) + ')'
        x = round(self.x[frame])  # 取整
        y = round(self.y[frame])  # 取整
        height = img.shape[0]
        width = img.shape[1]
        x = x + width // 2
        y = y + height // 2
        cv2.rectangle(img, (x - 20, y - 20), (x + 20, y + 20), (0, 0, 255), 5)  # 绘制矩形
        cv2.putText(img, text, (x - 20, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)  # 写字
        return img


video_maker = VideoMaker()
video_maker.make_video()
