import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        # flag, ajpg = cv2.imencode("img_q90.jpg", a, [cv2.IMWRITE_JPEG_QUALITY, 90])
        # http://www.programcreek.com/python/example/70396/cv2.imencode
        # #encode to jpeg format
        # encode param image quality 0 to 100. default:95
        # if you want to shrink data size, choose low image quality.
        ret, jpeg = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 60])
        return jpeg.tobytes()
