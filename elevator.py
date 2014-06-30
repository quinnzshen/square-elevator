# Handler for the elevator object. The front-end will actually move the elevator
# div around the page; this class encapsulates the behavior of the elevator.
# It receives three different methods when different events occur (arrive,
# hall_call, and car_call), and is responsible for tracking its own internal
# state. The only state it exposes is its current direction, which can be "up",
# "down", or "stopped". The front-end uses this information to manage the
# elevator div.
#
# For all methods, floors are assumed to start at 1. The initializer receives
# a number equal to the top floor (or the total number of floors). It can be
# assumed that the elevator is initialized on the first floor.
#
# Passengers will typically press the correct hall button depending on the floor
# they intend to go to. Some "confused" passengers will press the incorrect
# hall button (they will have a question mark in their speech bubble). No
# passenger will ever intend to go to the floor they are currently on.

class Elevator(object):
  def __init__(self, landings):
    self.landings = landings
    self.position = 1
    self.heading = "stopped"
    self.hall_tasks = {"up": set(), "down": set(), "stopped": set()}
    self.car_tasks = set()

  # Called when an elevator arrives at a floor, or passes through a floor.
  # This method should return true if the elevator should stop and open its
  # doors, or false if the elevator should continue past the floor.

  def arrive(self, landing):
    self.position = landing

    # if sum([len(x) for x in self.hall_tasks.values()]) + len(car_tasks) == 0:
    #   self.heading = "stopped"
    # elif len(car_tasks) != 0:
    #   if self.position > car_tasks

    if self.position == 1:
      self.heading = "up"
    elif self.position == self.landings:
      self.heading = "down"

    if landing in self.car_tasks:
      self.car_tasks.remove(landing)
      return True
    elif landing in self.hall_tasks[self.heading]:
      self.hall_tasks[self.heading].remove(landing)
      return True
    return False

  # Called when someone outside the elevator presses a call button. Receives
  # the floor on which the button was pressed, and "up" or "down" depending
  # on which button was pressed. It can be assumed that this method will
  # never be called with the bottom floor and "down", or the top floor and
  # "up". The return value is ignored.

  def hall_call(self, landing, direction):
    self.hall_tasks[direction].add(landing)
    print "HALL CALL: ", self.hall_tasks
    pass

  # Called when someone inside the elevator presses a floor button. The return
  # value is ignored. You can, but do not need to, handle the case where
  # someone calls the floor they are currently on.

  def car_call(self, landing):
    self.car_tasks.add(landing)
    print "CAR CALL"
    pass

  # This method should return the current elevator direction: "up", "down",
  # or "stopped". The front-end uses this to properly animate the elevator.

  def direction(self):
    return self.heading
