import blur
import black_white
import brightness
import contrast


def main():

    image_name = input("Görüntü Adi: ")
    secim = int(input("Efect Secimi: "))

    if secim == 1:    # bulaniklastirma
        blur.bulanik(image_name)

    elif secim == 2:  # grilestirme
        black_white.gri(image_name)

    elif secim == 3:  # parlaklık
        brightness.parlaklik(image_name)

    elif secim == 4:  # konstrat
        contrast.contrast(image_name)

main()