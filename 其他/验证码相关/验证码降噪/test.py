# -*- coding: utf-8 -*-
import cv2
import pytesseract
"""
如何过滤掉正余弦
data:image/jpeg;base64,
"""
# 灰度，二值化
def _get_dynamic_binary_image(img_name):
    im = cv2.imread(img_name)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    cv2.imwrite('cza.jpg', th1)  # 保留原始初始值
    return th1

#去除边框
def clear_border(img):
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if x < 2 or x > h - 2:
                img[x, y] = 255
    return img,h,w
# 干扰线降噪
def interference_line(img,h,w):
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            if img[x, y - 1] > 245:
                count = count + 1
            if img[x, y + 1] > 245:
                count = count + 1
            if img[x - 1, y] > 245:
                count = count + 1
            if img[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                img[x, y] = 255
    return img
#点降噪
def interference_point(img,img_name):
    # todo 判断图片的长宽度下限
    x = 0
    y = 0
    filename ='3.jpg'
    cur_pixel = img[x, y]# 当前像素点的值
    height,width = img.shape[:2]
    for y in range(0, width - 1):
      for x in range(0, height - 1):
        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,4邻域
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右上顶点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最上非顶点,6邻域
                sum = int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        elif y == width - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x, y - 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右下顶点
                sum = int(cur_pixel) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y - 1])

                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最下非顶点,6邻域
                sum = int(cur_pixel) \
                      + int(img[x - 1, y]) \
                      + int(img[x + 1, y]) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x + 1, y - 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])

                if sum <= 3 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])

                if sum <= 3 * 245:
                  img[x, y] = 0
            else:  # 具备9领域条件的
                sum = int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 4 * 245:
                  img[x, y] = 0
    cv2.imwrite(filename, img)
    return img
#字符的切割问题，涉及到算法，以后研究
def test(img):
    """
    0    黑色
    255  白色
    """
    h, w = img.shape
    for y in range(1, w-1):
        for x in range(1, h-1):
            if not img[x, y] and not img[x, y-1] and not img[x, y+1] and not img[x-1, y] and not img[x+1, y]:
                img[x, y] = img[x, y-1] = img[x, y+1] = img[x+1, y] = img[x-1, y] = 1
                # img[x, y] = 1
    for y in range(1, w-1):
        for x in range(1, h-1):
            if img[x, y] == 0:
                img[x, y] = 255
    cv2.imwrite('test1_img.jpg', img)  # 保留原始初始值


def show(img):
    cv2.namedWindow("Image")
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = './722h4a.jpg'  # h47c2c 856835 722h4a
    im = _get_dynamic_binary_image(img)  # 二值化
    Im, h, w = clear_border(im)  # 去边框?
    # im =interference_line(Im, h, w)  # 去直线?
    # IM = interference_point(im,img)  # 去点?
    # text = pytesseract.image_to_string(IM, lang='eng')
    # print(text, '?????')
    test(im)
    # image=show(im)

    # from minitools.baidu.ocr import BaiDuOcr
    # aa = BaiDuOcr()
    # with open('test1_img.jpg', 'rb') as f:  # h47c2c 856835 test1_img
    #     print(aa.webImage2word(f.read()))



