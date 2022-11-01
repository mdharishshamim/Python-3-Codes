from __future__ import print_function


class RailwayForm():
    formtype = "RailwayForm"
    def printData(self):
        print(f"the name is {self.name}")
        print(f"the train is {self.train}")
        print(f"the doj is {self.doj}")




haarishApplication = RailwayForm()
haarishApplication.name = " haarish shamim"
haarishApplication.train = " rajdhani express"
haarishApplication.doj = "29 November 2022"
haarishApplication.printData()