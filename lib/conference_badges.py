def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # badge_messages = []
    # for name in names:
    #     badge_messages.append(f'Hello, my name is {name}.')
    # return badge_messages
   
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    # room_assignments = []

    # for i, name in enumerate(names, start = 1):
    #     room_assignments.append(f"Hello, {name}! You'll be assigned to room {i}!")
    # return room_assignments

    room_assignments = [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(names, start = 1)]
    return room_assignments

def printer(names):
   badge_messages = batch_badge_creator(names)
   for message in badge_messages:
       print(message)


   room_assignments = assign_rooms(names)
   for assignment in room_assignments:
       print(assignment)
       


        
