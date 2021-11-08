import cloudpickle
import pickle
import spark
import numpy as np
import cv2 as cv

#Obtención del vector solución

pickle_file = open('hint_object.p','rb')
todo = pickle.load(pickle_file)
vector_fila=todo.rowsums
vector_columna=todo.colsums
vector=np.zeros(1089) 
for i in range(len(vector)):
	distancia=todo.compute_hamming(vector)
	vector[i]=1
	distancia2=todo.compute_hamming(vector)
	if distancia2 > distancia:
		vector[i]=0
	
#Obtención del QR

qr_array=vector
width=33 #Ancho del QR en cuadrados
sq_size=10 #Ancho en px de cada cuadrado

def draw_square(img, color, index):
    startPoint = ((index % width)*sq_size, int(index/width)*sq_size)
    endPoint = ((index % width + 1) * sq_size, (int(index/width) + 1)*sq_size)
    cv.rectangle(img, startPoint, endPoint,(255*(int(color)),255*(int(color)),255*(int(color))), thickness = -1)


if __name__ == "__main__":
    qr_window = "QR"
    size = sq_size*width, sq_size*width, 3
    qr_image = np.zeros(size, dtype=np.uint8)
    qr_image.fill(255)
    for i in range(len(qr_array)):
        draw_square(qr_image,qr_array[i],i)
        
    cv.imshow(qr_window, qr_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


			


