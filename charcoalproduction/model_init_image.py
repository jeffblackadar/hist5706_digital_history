import cv2
import numpy as np

#from .portrayal import portrayCell
#from .model import CharcoalProductionMap

class ModelImage():
    def __init__(self,model_height=20, model_width = 20, cell_size_pixels = 5):
        image_width = model_width * (cell_size_pixels + 1)
        image_height = model_height * (cell_size_pixels + 1)
        self.image = 255 * np.ones(shape=[image_height, image_width, 3], dtype=np.uint8)
        self.matrix = np.zeros((model_height, model_width))
        
    
    def get_image(self):
        return self.image
    
    def display_model(self):
        for y in range(0,self.matrix.shape[0]):
            for x in range(0,self.matrix.shape[1]):
                image_cell_x = x * (cell_size_pixels + 1)
                image_cell_y = y * (cell_size_pixels + 1)
                color_number = (0,0,0)
                if self.matrix[y,x] == 1:
                    color_number = (0,90,0)
                if self.matrix[y,x] == 0:
                    color_number = (50,50,50)
                self.image[image_cell_y:image_cell_y + cell_size_pixels,image_cell_x:image_cell_x + cell_size_pixels] = color_number
                

model_height = 10
model_width = 15

cell_size_pixels = 20


map_image = ModelImage( model_height,model_width,cell_size_pixels)
map_image.display_model()

center_y = model_height // 2
center_x = model_width // 2


 
    
# print(blank_image.shape)
cv2.imshow("map_image", map_image.get_image())
# white blank image
cv2.moveWindow("map_image", 10,10)
#    key = cv2.waitKey(1) & 0xFF
#    if key == ord("c"):
#        break
#    if key == ord("+"):
y_plus = center_y 
y_minus = center_y 
x_plus = center_x
x_minus = center_x 
print("Type + to advance. Type c to cancel. (the letter c on the keyboard.)")        
while y_plus <= map_image.matrix.shape[0] or y_minus >= 0 or x_plus <= map_image.matrix.shape[1] or x_minus >= 0:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        break
    if key == ord("+"):
        y_plus = y_plus + 1
        y_minus = y_minus - 1
        x_plus = x_plus + 1
        x_minus = x_minus - 1
        print(y_minus, y_plus,x_minus, x_plus)
            
        if y_minus >= 0:                
            x_low = x_minus
            if x_minus < 0:
                x_low = 0
            x_high = x_plus +1
            if x_high > map_image.matrix.shape[1]:
                x_high = map_image.matrix.shape[1]
            for xcounter in range(x_low,x_high):
                if map_image.matrix[y_minus,xcounter] > 0:
                    print("error1",y_minus,xcounter)
                else:
                    map_image.matrix[y_minus,xcounter] = 1
        if y_plus < map_image.matrix.shape[0]:                
            x_low = x_minus
            if x_minus < 0:
                x_low = 0
            x_high = x_plus +1
            if x_high > map_image.matrix.shape[1]:
                x_high = map_image.matrix.shape[1]
            for xcounter in range(x_low,x_high):
                if map_image.matrix[y_plus,xcounter] > 0:
                    print("error2",y_plus,xcounter)
                else:
                    map_image.matrix[y_plus,xcounter] = 1
        if x_minus >= 0:                
            y_low = y_minus + 1
            if y_low < 0:
                y_low = 0
            y_high = y_plus 
            if y_high > map_image.matrix.shape[0]:
                y_high = map_image.matrix.shape[0]
            for ycounter in range(y_low,y_high):
                if map_image.matrix[ycounter,x_minus] > 0:
                    print("error3",ycounter,x_minus)
                else:
                    map_image.matrix[ycounter,x_minus] = 1
                    
        if x_plus < map_image.matrix.shape[1]:
            y_low = y_minus + 1
            if y_low < 0:
                y_low = 0
            y_high = y_plus 
            if y_high > map_image.matrix.shape[0]:
                y_high = map_image.matrix.shape[0]
            for ycounter in range(y_low,y_high):
                #print(ycounter,x_plus)
                if map_image.matrix[ycounter,x_plus] > 0:
                    print("error4",ycounter,x_plus)
                else:
                    map_image.matrix[ycounter,x_plus] = 1 
            
        map_image.display_model()
        cv2.imshow("map_image", map_image.get_image())
print("Done loop. Type c (the letter c on the keyboard.)")
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        cv2.destroyAllWindows()
        break