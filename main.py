import sys
sys.path.append('./')

from dc_mcu.graphic import hair_graphic, eye_graphic

def main():
    hair_graphic.show()
    eye_graphic.show()

if __name__ == '__main__':
    main()
