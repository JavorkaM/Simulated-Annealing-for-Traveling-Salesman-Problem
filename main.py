from random import randint
import random
from graphics import *



TEMPERATURE_AT_START = 100
TEMPERATURE_DECREASE = 1  #in percentage form
MIN_TEMPERATURE = 0.001

NUM_OF_ITERATIONS_FOR_TEMPERATURE = 1000
TYPE_OF_NEIGHBOURHOOD_GENERATION = 0
# 0 - random per cycle
# 1 - swap
# 2 - insertion
# 3 - reversion

NUM_OF_CITIES = 40
GRID_SIZE_X = 300
GRID_SIZE_Y = 300

e = 2.718281828459045

VISUALIZE_SOLUTION = True

VISUAL_WINDOW_SCALE = 3


class city:
    def __init__(self, x_pos, y_pos, ):
        self.x = x_pos
        self.y = y_pos


def is_city_duplicate(list, x, y):
    for i in range(0, len(list)):
        if(list[i].x == x and list[i].y == y):
            return True
    return False


def create_list_of_cities():
    temp_list = []

    temp_x = 0
    temp_y = 0
    for i in range(0, NUM_OF_CITIES):
        duplicate = True
        while(duplicate):
            duplicate = False
            temp_x = randint(1, GRID_SIZE_X)
            temp_y = randint(1, GRID_SIZE_Y)
            duplicate = is_city_duplicate(temp_list, temp_x, temp_y)
        temp_city =city(temp_x, temp_y)
        temp_list.append(temp_city)
    return temp_list



def get_cities_distance(city_1, city_2):
    #                                                |\
    #                                                |  \
    # Pythagoras Theorem                           b |    \ c
    #            ___________________________         |      \
    #    c  =  \/ (a2 - a1)^2 - (b2 - b1)^2          |________\
    #                                                    a
    return ((((city_2.x - city_1.x) ** 2) + ((city_2.y - city_1.y) ** 2)) ** 0.5)


def create_city_distance_table(list_of_cities):
    distance_table = [[0 for i in range(0, NUM_OF_CITIES)] for j in range(0, NUM_OF_CITIES)]
    for i in range(0, len(list_of_cities)):
        for j in range(0, len(list_of_cities)):
            temp = get_cities_distance(list_of_cities[i],list_of_cities[j])
            distance_table[i][j]  = temp
            distance_table[j][i]  = temp

    return distance_table


def print_cities(list):
    for i in range(0, len(list)):
        print("City no.", i, " - ", list[i].x,",", list[i].y)

def is_duplicate(list, city_num):
    for i in range(0,len(list)):
        if(list[i] == city_num):
            return True
    return False


def generate_first():
    temp_list = []
    temp = 0
    for i in range(0, NUM_OF_CITIES):
        duplicate = True
        while(duplicate):
            duplicate = False
            temp = randint(0,NUM_OF_CITIES - 1)
            duplicate = is_duplicate(temp_list, temp)
        temp_list.append(temp)
    temp_list.append(temp_list[0])
    return temp_list


## SWAP
def generate_neighbour_swap(city_order):
    city_order.pop(len(city_order) - 1)
    temp_1 = -1
    temp_2 = -1
    while(temp_1 == temp_2):
        temp_1 = randint(0,NUM_OF_CITIES - 1)
        temp_2 = randint(0,NUM_OF_CITIES - 1)

    temp = city_order[temp_1]
    city_order[temp_1] = city_order[temp_2]
    city_order[temp_2] = temp
    city_order.append(city_order[0])
    return city_order

## REVERSION
def generate_neighbour_reversion(city_order):
    city_order.pop(len(city_order) - 1)
    temp_1 = -1
    temp_2 = -1
    while (temp_1 == temp_2):
        temp_1 = randint(0, NUM_OF_CITIES - 1)
        temp_2 = randint(0, NUM_OF_CITIES - 1)

    if(temp_1 > temp_2):
        temp = temp_1
        temp_1 = temp_2
        temp2 = temp

    city_order[temp_1:temp_2] = city_order[temp_1:temp_2][::-1]
    city_order.append(city_order[0])
    return city_order

## INSERTION
def generate_neighbour_insertion(city_order):
    city_order.pop(len(city_order) - 1)
    temp_1 = -1
    temp_2 = -1
    while (temp_1 == temp_2):
        temp_1 = randint(0, NUM_OF_CITIES - 1)
        temp_2 = randint(0, NUM_OF_CITIES - 1)

    temp_city = city_order[temp_1]
    city_order.pop(temp_1)
    city_order.insert(temp_2, temp_city)
    city_order.append(city_order[0])
    return city_order

def calculate_fitness(city_order, distance_table):
    fitness = 0
    for i in range(0, len(city_order) - 1 ):
        fitness += distance_table[city_order[i]][city_order[i+1]]
    return fitness

def calculate_chance(temperature, temp_fitness, current_fitness):
    if( e**((current_fitness - temp_fitness) / temperature ) > random.uniform(0, 1) ):

    ####################################################################
    #      ( fitness change)
    #      (  -----------  )
    #      (  temperature  )    >  random floating point between 0 and 1
    #    e^
    ####################################################################
        return True
    return False

def visualize_path(window,path, list_of_cities):
    for city in list_of_cities:
        point = Point(city.x * VISUAL_WINDOW_SCALE, city.y * VISUAL_WINDOW_SCALE)
        cir = Circle(point, 5)
        cir.setOutline(color_rgb(255,255,255))
        cir.draw(window)
    i = 0
    for i in range(0, len(path) - 2):
        point1 = Point(list_of_cities[path[i]].x * VISUAL_WINDOW_SCALE, list_of_cities[path[i]].y * VISUAL_WINDOW_SCALE)
        point2 = Point(list_of_cities[path[i+1]].x * VISUAL_WINDOW_SCALE, list_of_cities[path[i+1]].y * VISUAL_WINDOW_SCALE)
        line = Line(point1,point2)
        line.setWidth(2)
        line.setFill(color_rgb(255,255,255))
        line.draw(window)

    point1 = Point(list_of_cities[path[len(path) - 1]].x * VISUAL_WINDOW_SCALE,
                   list_of_cities[path[len(path) - 1]].y * VISUAL_WINDOW_SCALE)
    point2 = Point(list_of_cities[path[0]].x * VISUAL_WINDOW_SCALE,
                   list_of_cities[path[0]].y * VISUAL_WINDOW_SCALE)
    line = Line(point1, point2)
    line.setWidth(2)
    line.setFill(color_rgb(255, 255, 255))
    line.draw(window)


def clear_window(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def print_solution(solution,fitness, list_of_cities):
    first = True
    for i in solution:
        print("(",list_of_cities[i].x,",", list_of_cities[i].y, ")" , end="")
        if(i != solution[len(solution) - 1] or first):
            print(" -> ",end="")
        temp = False

    print("")
    print("Lenght of path = ", fitness )

    if(VISUALIZE_SOLUTION):
        window = GraphWin("Window", VISUAL_WINDOW_SCALE * GRID_SIZE_X, VISUAL_WINDOW_SCALE * GRID_SIZE_Y)
        window.setBackground(color_rgb(0, 0, 0))
        visualize_path(window,solution,list_of_cities)
        window.getMouse()
        window.close()


def simulated_annealing(type_of_neighbour_generation,list):
    distance_table = create_city_distance_table(list)

    current = generate_first()
    current_fitness = calculate_fitness(current, distance_table)
    temperature = TEMPERATURE_AT_START
    window_s = GraphWin("Window", VISUAL_WINDOW_SCALE * GRID_SIZE_X, VISUAL_WINDOW_SCALE * GRID_SIZE_Y)
    window_s.setBackground(color_rgb(0, 0, 0))
    i = 0
    while(temperature > MIN_TEMPERATURE):
        for i in range(0, NUM_OF_ITERATIONS_FOR_TEMPERATURE):
            temp = current[:]
            if(type_of_neighbour_generation == 0):
                type = randint(1,3)
            else:
                type = type_of_neighbour_generation
            if(type == 1):
                temp = generate_neighbour_swap(temp)
            elif(type == 2):
                temp = generate_neighbour_insertion(temp)
            elif(type == 3):
                temp = generate_neighbour_reversion(temp)
            else:
                print("Invalid type of neighbour generation!")
                return 1

            temp_fitness = calculate_fitness(temp, distance_table)
            if(temp_fitness < current_fitness or calculate_chance(temperature, temp_fitness, current_fitness)):
                current = temp
                current_fitness = temp_fitness
                break
        temperature *= 1 - (TEMPERATURE_DECREASE/100)
        if(i == NUM_OF_ITERATIONS_FOR_TEMPERATURE - 1 ):
            break
        for item in window_s.items[:]:
            item.undraw()
        window_s.update()
        visualize_path(window_s,current, list)


    print_solution(current,current_fitness,list)



if __name__ == '__main__':
    list_of_cities = create_list_of_cities()
    simulated_annealing(TYPE_OF_NEIGHBOURHOOD_GENERATION,list_of_cities)
