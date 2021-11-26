from model import CharcoalProductionMap
import cv2
import numpy as np

#from .portrayal import portrayCell
#from .model import CharcoalProductionMap

class ModelImage():
    def __init__(self,model, model_height = 20, model_width = 20, cell_size_pixels = 5):
        image_width = model_width * (cell_size_pixels + 1)
        image_height = model_height * (cell_size_pixels + 1)
        self.image = 255 * np.ones(shape=[image_height, image_width, 3], dtype=np.uint8)
        self.model = model
        self.cell_size_pixels = cell_size_pixels
    
    def get_image(self):
        return self.image

    #def display_forest_cell(cell_y, cell_x)
    
    def display_model(self):
        for cell_list in self.model.grid.__iter__():
            cell = cell_list[0]
            if len(cell_list)>0:
                cell_layer_0 = None
                cell_layer_1 = None                
                for counter in range(0 , len(cell_list)):
                    if cell_list[counter].type == "forest":
                        cell = cell_list[counter]
                        image_cell_x = cell.x * (cell_size_pixels + 1)
                        image_cell_y = cell.y * (cell_size_pixels + 1)
                        self.image[image_cell_y:image_cell_y + cell_size_pixels,image_cell_x:image_cell_x + cell_size_pixels] = cell.getColorNumber()
            else:

                image_cell_x = cell.x * (cell_size_pixels + 1)
                image_cell_y = cell.y * (cell_size_pixels + 1)
                self.image[image_cell_y:image_cell_y + cell_size_pixels,image_cell_x:image_cell_x + cell_size_pixels] = cell.getColorNumber()


# https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/
# https://pupli.net/2019/03/create-blank-image-using-opencv-python/
#def __init__(self, height=50, width=50, required_charcoal_loads_per_year=2, cells_cut_for_charcoal_hearth=3,collection_radius=3, forest_age_maturity=30):

model_height = 15
model_width = 15
model_map = CharcoalProductionMap(model_height,model_width,4,4,3,20, False)

cell_size_pixels = 20


map_image = ModelImage(model_map, model_height,model_width,cell_size_pixels)
map_image.display_model()
while True:
    
    # print(blank_image.shape)
    cv2.imshow("map_image", map_image.get_image())
    # white blank image
    cv2.moveWindow("map_image", 10,10)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        break
    if key == ord("+"):
        model_map.step()
        map_image.display_model()
        cv2.imshow("map_image", map_image.get_image())
cv2.destroyAllWindows()