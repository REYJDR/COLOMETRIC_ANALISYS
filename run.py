from main import * 

#Init Program Properties
Program = App()
Program.load()

#start default vire
#Program.openView('SAP.se16.view')
#Program.openView('Invoices.createView.view')
Program.openView('Invoices.listView.view')
#Run program
Program.run()