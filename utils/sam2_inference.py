import cv2
import numpy as np

class SAM2Model:
    def __init__(self, model_path):
        # 初始化，这里可以留空，后续可以替换为真正的SAM模型加载
        pass
    
    def segment_person(self, image):
        # 简化版的分割逻辑，实际使用时需要根据SAM模型的API进行调整
        # 这里使用OpenCV的背景分割作为临时解决方案
        # 后续需要替换为真正的SAM模型推理
        
        # 使用GrabCut进行背景分割
        mask = np.zeros(image.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        
        # 假设人像在图像中心
        rect = (50, 50, image.shape[1]-50, image.shape[0]-50)
        cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        
        # 创建掩码
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        mask = mask2 * 255
        
        # 只保留最大的连通区域（假设是人像）
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            mask = np.zeros_like(mask)
            cv2.drawContours(mask, [largest_contour], -1, 255, -1)
        
        return mask
