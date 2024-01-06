
# FOTOGRAF SIYAH_BEYAZ(GRI) YAPMA

import cv2
import numpy as np

def gri(image_path):
    # resim yukleme
    img = cv2.imread(image_path)

    # resim boyutlari
    yeni_yukseklik, yeni_genislik = 500, 500
    yukseklik, genislik = img.shape[:2]
    yukseklik_orani, genislik_orani = yeni_yukseklik / yukseklik, yeni_genislik / genislik
    olcek_matrix = np.float32([[genislik_orani, 0, 0],
                              [0, yukseklik_orani, 0]])
    boyulandirilmis_goruntu = cv2.warpAffine(img, olcek_matrix, (yeni_genislik, yeni_yukseklik))

    # gri tonlama donusturmesi yap
    gri = cv2.cvtColor(boyulandirilmis_goruntu, cv2.COLOR_BGR2GRAY)

    # resimleri yanyana koy
    birlestirilmis_goruntu = np.hstack((boyulandirilmis_goruntu, cv2.cvtColor(gri, cv2.COLOR_GRAY2BGR)))

    # resimleri goster
    cv2.imshow("yeni foto", birlestirilmis_goruntu)

    # Bekle ve pencereyi kapat
    cv2.waitKey(0)
    cv2.destroyAllWindows()
