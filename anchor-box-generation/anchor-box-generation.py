import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride_len = image_size/feature_size
    anchor_boxes=[]
    
    for i in range(feature_size): 
        for j in range(feature_size):
            for scale in scales:
                for ratio in aspect_ratios:
                    centroid_y = i*stride_len+0.5*stride_len
                    centroid_x = j*stride_len+0.5*stride_len
                    width=scale*math.sqrt(ratio)
                    height= scale/math.sqrt(ratio) if ratio >= 1 else scale*math.sqrt(1/ratio)
                    anchor_boxes.append([centroid_x-width/2,centroid_y-height/2,centroid_x+width/2,centroid_y+height/2])
    return anchor_boxes

                




            


    
