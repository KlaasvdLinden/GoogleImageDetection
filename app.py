import requests
import webbrowser
import cv2

# init cam
cam = cv2.VideoCapture(2)  # 0 = webcam, 2 = External USB cam like smartphone

cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 32:
        # SPACE pressed
        img_name = "img.png"
        cv2.imwrite(img_name, frame)
        print("Picture taken!")
        break

cam.release()

cv2.destroyAllWindows()

filePath = 'img.png'
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']

webbrowser.open(fetchUrl)





