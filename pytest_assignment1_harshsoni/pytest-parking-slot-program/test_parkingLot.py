import pytest
from ParkingLot import *

p=ParkingLot()

def test_create_parking_lot():
    assert p.create_parking_lot(5)==p.capacity

def test_get_empty_slot():
    slot = p.get_empty_slot()
    assert p.slots[slot]==-1

def test_park():
    slot_id1=p.park(121,"red")
    slot_id2=p.park(122,"green")
    slot_id3=p.park(123,"blue")
    slot_id4=p.park(124,"white")
    assert p.slots[slot_id1]!=-1
    assert p.slots[slot_id2]!=-1
    slot_id5=p.park(125,"black")
    assert p.park(126,"red")==-1
    assert slot_id1-slot_id2!=0
    assert slot_id2-slot_id3!=0
    assert slot_id3-slot_id4!=0
    assert slot_id4-slot_id5!=0

def test_leave_slot():
    assert p.park(127,"red")==-1
    assert p.leave_slot(1)==True
    assert p.leave_slot(1)==False
    assert p.park(127,"red")==1
    assert p.leave_slot(2)==True
    assert p.leave_slot(3)==True
    assert p.slots[2]==-1
    assert p.slots[2]==-1
    

def test_get_slotno_from_regno():
    slot_id8=p.park(128,"red")
    assert p.get_slotno_from_regno(128)==slot_id8
    slot_id9=p.park(129,"black")
    assert p.get_slotno_from_regno(129)!=slot_id8
    
def test_get_slotno_from_color():
    slot_nos=p.get_slotno_from_color("red")
    assert slot_nos!=[]
    slot_nos2=p.get_slotno_from_color("pink")
    assert slot_nos2==[]

def test_get_regno_from_color():
    reg_nos=p.get_regno_from_color("red")
    assert reg_nos!=[]
    reg_nos2=p.get_regno_from_color("pink")
    assert reg_nos2==[]