from collections import deque

def yandex_funny_tester():
    '''
    This program is carry out Ctrl+X, Ctrl+V for strings in givven test and Down/Up for cursor 
    Separator for test and comands is '                '
    
    My\nprogram\nis awesome\nMy\nis awful\n                \nDown\nDown\nDown\nCtrl=X\nUp\nCtrl=X\nUp\nUp\nCntrl+V
    
    '''
    
    
    input_text = input('''please imput your comands''')
    input_list = input_text.split('\\n')
    sep = input_list.index('                ')
    text_file = input_list[:sep+1]
    cmd_list = input_list[sep+1:]
    text_linked = deque(text_file)
    start_index = 0
    buffer = None

    for i in cmd_list:
        if i == 'Down' and start_index < len(text_linked) - 1:
            start_index += 1
        if i == 'Up' and start_index > 0:
            start_index -= 1
        if i == 'Ctrl+X' and start_index < len(text_linked) - 1:
            buffer = text_linked[start_index]
            del text_linked[start_index]
        if i == 'Ctrl+V' and buffer != None:
            text_linked.insert(start_index, buffer)
    
    for i in text_linked:
        print(i)

