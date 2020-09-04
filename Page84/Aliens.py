# Caleb
# This will be page 84 assignment.

alien_color = 'red'

# green 5 
# yellow 10
# red 15

def get_points(killed_color):
    earned_points = 0

    if killed_color == 'green':
        earned_points = 5
    elif killed_color == 'yellow':
        earned_points = 10
    elif killed_color == 'red':
        earned_points = 15
    elif killed_color == 'blue':
        earned_points = 3

    return earned_points

if __name__ == "__main__":
    assert get_points('red') == 15
    assert get_points('yellow') == 10
    assert get_points('green') == 5
    assert get_points('blue') == 3