
#Created by: Alireza Teimoori
#Created on: 21 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit 1-03
#This program calculates area and perimeter of the values that user gives

import ui

def calculate_button_touch_up_inside(sender):
    # calculate area and perimeter
    
    # input
    length = int(view['length_textbox'].text)
    width = int(view['width_textbox'].text)
    
    # process
    area = length * width
    perimeter = 2 * (length + width)
    
    # output
    view['area_answer_label'].text = 'The area is: ' + str(area) + ' cm^2'
    view['perimeter_answer_label'].text = 'The perimeter is: ' + str(perimeter) + ' cm'
    
view = ui.load_view()
view.present('sheet')
