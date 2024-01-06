
# FOTOGRAF KONSTRAT

import cv2
import numpy as np

def contrast(image_name):
    img = cv2.imread(image_name)
    image = cv2.resize(img, (500, 500))

    # Kontrast arttırma ve azaltma değerlerini hesaplayıp gerekli işlemleri yapma
    kontrast_deger1 = 80 # int(input("kontrast arttırma değerini giriniz (%): "))
    kontrast_deger2 = 50 # int(input("kontrast azaltma değerini giriniz (%): "))

    kontrast1 = int(((kontrast_deger1 + 64) * (64 + 64) / (100 + 100)) - 64)
    kontrast2 = int(((kontrast_deger2 + 64) * (64 + 64) / (100 + 100)) - 64)

    # konsrast arttirma
    if kontrast1 != 0:
        f1 = 131 * (kontrast1 + 127) / (127 * (131 - kontrast1))
        alpha_a = f1
        gamma_a = 127 * (1 - f1)
        image1 = cv2.addWeighted(image, alpha_a, image, 0, gamma_a)
    else:
        image1 = image.copy()

    #  kontrast arttirma ve azaltma islemleri icin kullanildi

    # konsrast azaltma
    if kontrast2 != 0:
        f2 = 131 * (kontrast2 - 127) / (127 * (131 + kontrast2))
        alpha_b = f2
        gamma_b = 127 * (1 - f2)
        image2 = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    else:
        image2 = image.copy()

    birlestirilmis_goruntu = np.concatenate((image, image1, image2), axis=1)
    cv2.imshow('yeni foto', birlestirilmis_goruntu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
