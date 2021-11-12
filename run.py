from main import * 

#Init Program Properties
Program = App()
Program.load()

#start default vire
Program.openView('Invoices.createView.view')
# Program.openView('Products.listView.view')
#Run program
Program.run()