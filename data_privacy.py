''' To hide the person in an image '''

# Import necessary stuff
# PIL IS Python Image Library
from PIL import Image, ImageDraw
import face_recognition
import math

# Loading Image (Make sure your code and image are in same folder else you have to specify the whole path of image)
image = face_recognition.load_image_file("gal.jpg")

# The below code identifies all the faces in a picture and length of the list gives the number of faces(In this case it is one)
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)

# To draw on the image
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

# Iterating through all faces in face_landmarks_list(In this case, only one face)
for face_landmarks in face_landmarks_list:
     le = face_landmarks.get('left_eye')
     re = face_landmarks.get('right_eye')
     #le gives co-ordinates of six points around left eye and re gives six points around right eye 
     x1 = le[1][0] # x-coordinate of first point
     x2 = le[4][0] # x-coordinate of fourth point
     y1 = le[1][1] # y-coordinate of first point
     y2 = le[4][1] # y-coordinate of fourth point
     # calculate distance between two points
     dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
     d.line((le[0],re[3]),width=int(dist))
pil_image.show()