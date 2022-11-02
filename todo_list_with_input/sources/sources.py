import datetime
import helpers.helpers

entry_dict = {'id':'','title':'','description':'','priority':'','due_date':'','done':''}

entry_dict['id'] = helpers.helpers.unique_identifier()
entry_dict['title'] = helpers.helpers.length_identifier(input('Write title:'))
entry_dict['description'] = helpers.helpers.description_as_title(entry_dict['title'],
                            input('Describe your task:'))
entry_dict['priority'] = helpers.helpers.priority_check(input('Specify priority:'))
entry_dict['due_date'] = helpers.helpers.due_date(input('Specify due date as dd/mm/yy hh:mm'))
entry_dict['done'] = helpers.helpers.check_if_done(input('If done, write anything:'))

print(entry_dict)







