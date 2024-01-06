
# FOTOGRAF PARLAKLIK

import cv2
import numpy as np

def parlaklik(image_name):

    img = cv2.imread(image_name)
    image = cv2.resize(img, (500, 500))

    parlaklik_degeri1 = 75
    parlaklik_degeri2 = 75

    # Parlaklık değerlerine göre parlaklık ayarı yap
    parlaklik1 = int(((parlaklik_degeri1 + 127) * (127 + 127) / (100 + 100)) - 127)
    parlaklik2 = int(((parlaklik_degeri2 + 127) * (127 + 127) / (100 + 100)) - 127)

    # Parlaklık ayarlamasına göre gölgeler ve vurgular belirle
    if parlaklik1 > 0:
        golge = parlaklik1
        yuksek_isik = 255
    else:
        golge = 0
        yuksek_isik = 255 + parlaklik1

    # Parlaklık ayarlaması yap
    alpha_a = (yuksek_isik - golge) / 255
    gamma_a = golge

    # Ayarlanmış parlakligi resim uzerine uygula
    image2 = cv2.addWeighted(image, alpha_a, image, 0, gamma_a)

    # Parlaklik azaltma islemi
    if parlaklik2 < 0:
        yuksek_isik2 = 0
        golge2 = 255
    else:
        yuksek_isik2 = 255 - parlaklik2
        golge2 = 0

    alpha_b3 = (yuksek_isik2 - golge2) / 255
    gamma_b3 = golge2
    image3 = cv2.addWeighted(image, alpha_b3, image, 0, gamma_b3)
    cv2.waitKey(0)

    # iki resmi birlestir ve ekranda goster
    birlestirilmis_goruntu = np.concatenate((image, image2, image3), axis=1)
    cv2.imshow('yeni foto', birlestirilmis_goruntu)
    cv2.waitKey(0)