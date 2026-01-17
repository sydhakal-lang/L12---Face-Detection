import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../L11 - Fun with filters/example.jpg')
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.putText(imagergb, "Hi, Hello", (100, 500 ), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 155, 5 ), 10 )
plt.imshow(imagergb)
plt.show()

