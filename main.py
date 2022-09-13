import sys
sys.path.append('./')

from movies_duration.graphic import mcu_movies_duration_graphic
from movies_duration.graphic import mcu_phase_duration_graphic

def main():
    mcu_movies_duration_graphic.show()
    mcu_phase_duration_graphic.show()
    
if __name__ == '__main__':
    main()
