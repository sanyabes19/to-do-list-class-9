import datetime

task_depository = 0
def unique_identifier():
    global task_depository
    task_depository += 1
    return task_depository

def length_identifier(variable):
    '''Cut string length if it is longer than expected'''
    if len(variable) > 50:
        variable = variable[:length]
    return variable

def priority_check(priority):
    '''Check is priority is valid and in range'''
    try:
        if 1 > int(priority) or int(priority) > 10:
            print('Specified wrong number. Please, write 1 to 10')
    except ValueError:
        print('Wrong value. Priority is thus empty')
        priority = 0
    return priority

def description_as_title(title, description):
    '''If description is empty, substitute with title'''
    if description == '':
        description = title
    return description

def check_if_done(done):
    if done != '':
        done = 'Done'
    else:
        done = 'False'
    return done

def due_date(due_date):
    date_format = '%d/%m/%y %H:%M'
    try:
        due_date = datetime.datetime.strptime(due_date, date_format)
    except ValueError:
        print('Wrong format of due date')
        due_date = 'Due date not specified'
    return due_date

print(due_date('a'))