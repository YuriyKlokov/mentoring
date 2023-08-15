input_text = input('''please input your commands''')
cmd_list = input_text.split('\\n')

class Wagon():
    def __init__(self, number, _next_wagon=None, _prev_wagon=None):
        self.number = number
        self._next_wagon = _next_wagon
        self._prev_wagon = _prev_wagon

def Make_Train(cmd_list):
    first_wagon = None 
    last_wagon = None
    train_length = 0
    left_reduce = 0 
    right_reduce = 0
    
    for i in cmd_list:
        
        if first_wagon is None and last_wagon is None:
            first_wagon = Wagon(number=int(i[-1]))
            last_wagon = first_wagon
            train_length += 1
            continue
        
        if i[0] == '-' and int(i[-1]) >= train_length:
            first_wagon = None
            last_wagon = None
            train_length = 0
            left_reduce = 0 
            right_reduce = 0
        
        if i[:5] == '+left':
            first_wagon = Wagon(number=int(i[-1]), _next_wagon=first_wagon)
            if first_wagon._next_wagon:
                first_wagon._next_wagon._prev_wagon = first_wagon
            train_length += 1
         
        if i[:6] == '+right':
            last_wagon =  Wagon(number=int(i[-1]), _prev_wagon=last_wagon)
            if last_wagon._prev_wagon:
                last_wagon._prev_wagon._next_wagon = last_wagon
            train_length += 1
        
        if i[:5] == '-left':
            left_reduce += int(i[-1])
            
        if i[:6] == '-right':
            right_reduce += int(i[-1])
        
    while right_reduce > 0:
        last_wagon._prev_wagon._next_wagon = None
        last_wagon = last_wagon._prev_wagon
        right_reduce -= 1   
        

    while left_reduce > 0:
        first_wagon._next_wagon._prev_wagon = None 
        first_wagon = first_wagon._next_wagon
        left_reduce -= 1
        
    current_el = first_wagon
    while current_el:
        print(current_el.number)
        current_el = current_el._next_wagon

Make_Train(cmd_list)

+left 1\n+right 2\n+left 3\n-right 1

