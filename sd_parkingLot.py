from queue import PriorityQueue
from queue import Queue


class Vehicle:
    def __init__(self, plate):
        self.plate = plate
        self.lot = None

    def assignLot(self, lot):
        self.lot = lot


class Lot:
    def __init__(self, id):
        self.avail = True
        self.id = id


class Management:
    def __init__(self, num):
        self.lots = {}
        self.vehicles = {}
        self.availableLots = PriorityQueue()
        self.waitingList = Queue()
        for i in range(num):
            l = Lot(i)
            self.lots[i] = l
            self.availableLots.put((i, l))

    def add(self, vehicle):

        self.vehicles[vehicle.plate] = vehicle
        if(not self.availableLots.empty()):
            id, lot = self.availableLots.get()
            vehicle.assignLot(lot)
        else:
            self.waitingList.put(vehicle)

    def remove(self, vehicle):
        del self.vehicles[vehicle.plate]
        self.availableLots.put((vehicle.lot.id, vehicle.lot))

        if(not self.waitingList.empty()):
            self.add(self.waitingList.get())

    def searchLot(self, id):
        pass

    def searchVehicle(self, plate):
        pass


class FrontDesk:
    def __init__(self, num):
        self.management = Management(num)

    def checkIn(self, vehicle):
        self.management.add(vehicle)

    def checkout(self, vehicle):
        self.management.remove(vehicle)


v1 = Vehicle(1)
v2 = Vehicle(2)

fd = FrontDesk(1)

fd.checkIn(v1)

fd.checkIn(v2)

print(v1.lot.id)
if(v2.lot is not None):
    print(v2.lot.id)

fd.checkout(v1)

if(v2.lot is not None):
    print(v2.lot.id)
