from modelisationOfLLL import modelisationOfLLL

class ModelisationCFG:

    def __init__(self,ci_list):
        self.ci_list = ci_list
        self.application = modelisationOfLLL(2000,800,1)
        self.application.creation_frame(self.ci_list)
        self.iterator = 0
        self.list_i =[0]

    def setCiList(self,list):
        self.ci_list =list

    def update(self,i,alpha,continu):
        self.iterator += 1
        self.list_i.append(i+1)
        self.application.update_frame(self.ci_list,i,self.list_i,self.iterator,alpha,continu)



