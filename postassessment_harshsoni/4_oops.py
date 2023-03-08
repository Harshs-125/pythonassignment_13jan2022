class Country():
    def __init__(self,name):
        self.name=name
        self.states=[]
    def add_states(self,state):
        self.states.append(state.name)
    def print_country(self):
        print("country:",self.name)
        print("states:",self.states)
       
class State(Country):
    def __init__(self,name):
        self.name=name
        self.districts=[]
        self.cities=[]
    def add_district(self,district):
        self.districts.append(district.name)
    def add_cities(self,city):
        self.cities.append(city.name)
    def print_state(self):
        print("State:",self.name)
        print("districts:",self.districts)
        print("cities:",self.cities)

class District(State):
    def __init__(self,name):
        self.name=name
    def print_district(self):
        print("District:",self.name)
class City(State):
    def __init__(self,name):
        self.name=name
    def print_city(self):
        print("City:",self.name)
class Unionterritory():
    def __init__(self,name):
        self.name=name
        self.cities=[]
    def add_city(self,city):
        self.cities.append(city.name)
    def print_ut(self):
        print("UnionTerritory:",self.name)
        print("cities:",self.cities)

india_country=Country("India")
mp_state=State("Madhya Pradesh")
askn=District("Ashoknagar")
india_country.add_states(mp_state)
mp_state.add_district(askn)
ind=City("Indore")
mp_state.add_cities(ind)
delhi=Unionterritory("Delhi")
newdelhi=City("New Delhi")
delhi.add_city(newdelhi)

india_country.print_country()
mp_state.print_state()
askn.print_district()
ind.print_city()
delhi.print_ut()