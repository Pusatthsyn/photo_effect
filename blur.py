
# FOTOGRAF BULANIKLASTIRMA

import cv2
import numpy as np

def bulanik(image_name):
    # fotografi bellege yükle
    image = cv2.imread(image_name)

    # Resim boyutları alınır
    # resmin yüksekliği, genisligi ve kanal sayisini dondur
    yukseklik, genislik = image.shape[:2]

    # Yeni boyutlar icin olcek faktorleri hesaplama
    yeni_yukseklik = 500
    yeni_genislik = 500
    yukseklik_orani = yeni_yukseklik / yukseklik
    genislik_orani = yeni_genislik / genislik

    # Olceklendirme matrisi oluşturma
    # "cv2.warpAffine" fonksiyonu kullanarak fotografa uygula ve boyutlandirilmis bir goruntu olustur
    olcek_matrix = np.float32([[genislik_orani, 0, 0],
                              [0, yukseklik_orani, 0]])

    # Olceklendirme matrisini resme uygulama
    boyulandirilmis_goruntu = cv2.warpAffine(image, olcek_matrix, (yeni_genislik, yeni_yukseklik))

    # Yeniden boyutlandirilmis resme Gauss bulaniklastirma uygulama
    bulaniklik_boyutu = 7
    bulaniklik_boyutu2 = 25

    # "cv2.GaussianBlur" bir goruntuyu belirli bir boyutta bulaniklastirir
    bulanik_foto = cv2.GaussianBlur(boyulandirilmis_goruntu,
                                    (bulaniklik_boyutu, bulaniklik_boyutu), 0)
    bulanik_max_image = cv2.GaussianBlur(boyulandirilmis_goruntu,
                                        (bulaniklik_boyutu2, bulaniklik_boyutu2), 0)

    # Yeniden boyutlandirilmis ve bulaniklastirilmis resimler yatay olarak birlestirme
    birlestirilmis_goruntu = np.concatenate((boyulandirilmis_goruntu, bulanik_foto, bulanik_max_image), axis=1)

    # Fotograflari yanyana gosterme
    cv2.imshow('yeni foto', birlestirilmis_goruntu)
    #cv2.imwrite("bulanik.jpg", blurred_max_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
