from customtkinter import *
from CTkTable import *

#https://github.com/Akascape/CTkTable



window = CTk()
window.title("BUDGET")
window.geometry("600x400") #fml
window.resizable(0,0) #disable resize
set_appearance_mode("light")




#++++++++++++++++++++++++++++++ {PAGES} ++++++++++++++++++++++++++++++++++++++


# Create frames for each page
TABFRAME = CTkFrame(window, height=51, width=600, fg_color="#1E1E1E", corner_radius=0)
TABFRAME.pack(anchor=CENTER, fill=X)


#These are the individual pages, or rather, the frames
TransactionsPage = CTkFrame(window)
TransactionsPage.pack(fill=BOTH, expand=True)




# Create a list to hold all the pages
pages = [TransactionsPage]


# Function to show a page
def show_page(page):
    page.pack(fill=BOTH, expand=True)
    window.update_idletasks()  # Update the UI
    if page == TransactionsPage:
        transactionpage(TransactionsPage)
       


         
#++++++++++++++++++++++++++++++ {PAGE FUNCTIONS} ++++++++++++++++++++++++++++++++++++++
#DO NOT EDIT SPACE, WILL USE SPACE FOR THE OTHER PAGES


#def clientpage(page):
#def assetpage(page):
#def calculator(page):





TitleFont = CTkFont(family="Oswald", size=15, weight='bold')
EditFont = CTkFont(family="Oswald", size=15, weight='bold')
BTNFont = CTkFont(family="Oswald", size=13)
ErrorFont = CTkFont( size=10)
TransactionsPagePost = 0 #so the page only posts once and not multiple times

def transactionpage(page): #TO BE UPDATED
    global TransactionsPagePost, OutputEditContent
    if TransactionsPagePost==0:
        
        #START MASTER 
        PageMargin = CTkFrame(page)
        PageMargin.pack(expand=True)
        RequestPadding = CTkFrame(PageMargin, width=170, height=330, fg_color="#dbdbdb", corner_radius=0, border_color='#000000', border_width=1)
        OutputPadding = CTkFrame(PageMargin, width=410, height=330, fg_color="#dbdbdb", corner_radius=0, border_color='#000000', border_width=1)
        RequestPadding.grid_propagate(0)
        OutputPadding.grid_propagate(0)
        
        RequestPadding.grid(row=0, column=0)
        OutputPadding.grid(row=0, column=1) 

        #Requested Content
        SearchRequestContent = CTkFrame(RequestPadding, width=170, height=165, fg_color="#FFFFFF", corner_radius=0, border_color='#000000', border_width=1)
        SearchRequestContent.grid_propagate(0)
        
        EditsRequestContent = CTkFrame(RequestPadding, width=170, height=165, fg_color="#FFFFFF", corner_radius=0, border_color='#000000', border_width=1)
        EditsRequestContent.grid_propagate(0)
        
        SearchRequestContent.grid(row=0, column=0)
        EditsRequestContent.grid(row=1, column=0) 
        
        #Fixes all Buttons
        for i in range(1):
            EditsRequestContent.grid_columnconfigure(i, weight=1, uniform="column")
            EditsRequestContent.grid_rowconfigure(0, minsize=51)
        
        for i in range(1):
            SearchRequestContent.grid_columnconfigure(i, weight=1, uniform="column")
            SearchRequestContent.grid_rowconfigure(0, minsize=51)
        
        
        

        #Output Content
        OutputEditContent = CTkFrame(OutputPadding, width=410, height=115, fg_color="#FFFFFF", corner_radius=0, border_color='#000000', border_width=1)
        OutputEditContent.grid(row = 0, column = 0)
        LabelTransactionAdd = CTkLabel(OutputEditContent, text="TRANSACTIONS",font = EditFont)
        LabelTransactionAdd.place(x=5, y=1)
        

        OutputTableContent = CTkFrame(OutputPadding, width=410, height=215, fg_color="#a6a6a6", corner_radius=0, border_color='#000000', border_width=1)
        OutputTableContent.grid(row = 1, column = 0) 
        OutputEditContent.grid_propagate(0)
        
        
        OutputTableScrollbarContent = CTkFrame(OutputTableContent, width=410, height=215)
        OutputTableScrollbarContent.pack(fill="both", expand=True)
        
        canvas = CTkCanvas(OutputTableScrollbarContent, width=410, height=215, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = CTkScrollableFrame(canvas, width =387)
        scrollbar.grid(rowspan=100, row = 0, column = 0, sticky='nsew')

        EditLabelRequest = CTkLabel(EditsRequestContent, text="EDITS", font=EditFont)
        EditLabelRequest.grid(row=0, column=0, )
        
        
        #important buttons for requesting
        AddButtonRequest = CTkButton(EditsRequestContent, text="ADD",corner_radius=0, command=lambda: outputContentGivenButtons(OutputEditContent, 1),font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#e6e6e6')
        AddButtonRequest.grid(row=1,column=0,padx = 10, pady = 4, sticky='nsew')
        
        EditButtonRequest = CTkButton(EditsRequestContent, text="EDIT",corner_radius=0, command=lambda: outputContentGivenButtons(OutputEditContent, 2), font=BTNFont, fg_color='#FFFFFF', text_color='#000000', border_color='#000000', border_width=1, hover_color='#e6e6e6')
        EditButtonRequest.grid(row=2,column=0,padx = 10, pady = 1, sticky='nsew')
        
        DeleteButtonRequest = CTkButton(EditsRequestContent, text="DELETE",  corner_radius=0,command=lambda: outputContentGivenButtons(OutputEditContent, 3), font=BTNFont, fg_color='#FFFFFF', text_color='#000000', border_color='#000000', border_width=1, hover_color='#e6e6e6')
        DeleteButtonRequest.grid(row=3,column=0,padx = 10, pady = 2, sticky='nsew')
        
        #SearchRequestContentItemsg
        
        SearchLabel = CTkLabel(SearchRequestContent, text="TRANSACTIONS", font=EditFont)
        SearchLabel.grid(row=0, column=0, padx = 10, pady = 0,)
        
        SearchEntry = CTkEntry(SearchRequestContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Search")
        SearchEntry.grid(row=1, column=0, padx = 10, pady = 4,)
        
        SearchButton = CTkButton(SearchRequestContent, text="Search", fg_color='#0053A0', corner_radius=0, text_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#0051ff', command= lambda: TransactionSearch())
        SearchButton.grid(row=2,column=0, padx = 10, pady = 1,)

        comboVal = StringVar(value="Select")
        SearchComboChoices = CTkComboBox(SearchRequestContent, values=["Items", "Cash", "Date"], command=TransactionSearch_ComboCallback, variable=comboVal, corner_radius=1)
        SearchComboChoices.set("Select")
        SearchComboChoices.grid(row = 3, column=0, padx=10,pady=2)
        SearchComboChoices.configure(state="readonly")
        TransactionsPagePost=1
    else:
        print("printed!")

def TransactionSearch():
    print("y")
def TransactionSearch_ComboCallback():
    print("y")


vieweditemflag = False
A_vieweditemflag = 0
E_vieweditemflag = 0
D_vieweditemflag = 0

viewederror = 0

ErrorBoolean = False

sucessful_transaction = False

currentmode = ""

TransAddExist = False
TransEditExist = False
TransDeleteExist = False

def outputContentGivenButtons(OutputEditContent, value): 
    global vieweditemflag, A_vieweditemflag, E_vieweditemflag, D_vieweditemflag, currentmode, mode
    if value == 1:
        mode = "add"
        print(A_vieweditemflag)

    elif value == 2:
        mode = "edit"
        

    elif value == 3:
        mode = "delete"
    
    if currentmode == mode:
        return
    
    clearcurrentmode ()

    if currentmode == "":
        vieweditemflag = 0
    print(mode)
    
    if mode == "add":
        addmodeui()
    elif mode == "edit":
        editmodeui()
    elif mode == "delete":
        deletemodeui()

    currentmode = mode
    

def clearcurrentmode ():
    global TransAddExist, TransEditExist, TransDeleteExist, diffvalue, viewederror, ErrorBoolean

    # Destroy Add mode widgets if they exist
    if TransAddExist:
        try:
            TransactionNameBoxFrom.place_forget()
            TransactionNameBoxTo.place_forget()
            Transaction_combobox.place_forget()
        except Exception as e:
            print(f"Add is not working. Error: {e}" )
        try:
            if ErrorBoolean==True:
                Error.destroy()
                viewederror=0
                ErrorBoolean = False
        except Exception as e:
            print(f"Deletion Error not working. Error: {e}" )
        
        try:
            if diffvalue == 0:
                print("y")
            elif diffvalue == 1:
                AddDateEntryBox.place_forget()
            elif diffvalue == 2:
                AddGoodsEntryBox.place_forget()
            elif diffvalue == 3:
                typebox.place_forget()
                amtinput.place_forget()
            elif diffvalue == 4:
                AddBranchEntryBox.place_forget()
            if diffvalue > 0:
                AddSearchBoxEnter.destroy()
            if ErrorBoolean == True:
                Error.destroy()
        except Exception as e:
            print(f"Not working. Error: {e}")

        TransAddExist = False
    # Destroy Edit mode widgets if they exist
    if TransEditExist:
        try:
            TransactionIDEdit.destroy()
            Transaction_combobox.destroy()
        except Exception as e:
            print(f"Error destroying Transaction_combobox and TransactionIDEdit: {e}")
        try:
            if ErrorBoolean==True:
                Error.destroy()
                viewederror=0
                ErrorBoolean = False
        except Exception as e:
            print(f"Deletion Error not working. Error: {e}" )

        try:
            if diffvalue == 0:
                print("has not used combobox yet")
            elif diffvalue == 1:
                EditDateEntryBox.place_forget()
            elif diffvalue == 2:
                print(str(diffvalue) + " is set")
                EditGoodsEntryBox.place_forget()
            elif diffvalue == 3:
                typebox.place_forget()
                amtinputEdit.place_forget()
            elif diffvalue == 4:
                EditBranchEntryBox.place_forget()
            elif diffvalue == 5:
                PartyToEntryBox.place_forget()
                PartyForEntryBox.place_forget()
            if diffvalue > 0:
                EditSearchBoxEnter.place_forget() 
            if ErrorBoolean == True:
                Error.destroy()
        except Exception as e:
            print("ERROR")
        
        TransEditExist = False

    if TransDeleteExist:
        TransactionIDDelete.destroy()
        TransDeleteExist = False

    # Destroy the common input button if it exists
    try:
        Transaction_inputbutton.destroy()
    except NameError:
        pass  # Handle case where button isn't created yet

        
    
   
def addmodeui():
    vieweditemflag = 1
    
    global TransAddExist, TransactionNameBoxFrom, TransactionNameBoxTo, Transaction_inputbutton, Transaction_combobox, sucessful_transaction 
    global DateHolder, GoodsHolder, BranchHolder, TypeHolder, AmountHolder, PartyToHolder, PartyForHolder, StatusHolder
    DateHolder=""
    GoodsHolder=""
    BranchHolder=""
    TypeHolder="Item"
    AmountHolder = ""
    StatusHolder = ""
    PartyToHolder=""
    PartyForHolder=""
    sucessful_transaction = False
    
    #All Flags
    global Trans_DateFlag, Trans_GoodsFlag, Trans_TypeFlag, Trans_BranchFlag
    Trans_DateFlag=False
    Trans_GoodsFlag=False
    Trans_TypeFlag=False
    Trans_BranchFlag=False

    global TypeChecker, typewaschecked
    TypeChecker = True #whether item or cash
    typewaschecked = False #checks whether or not type in combo box was checked or not

    global enteronce, diffvalue, enteronceforcombo

    enteronce = 0
    diffvalue = 0 #to findout which combo is working orn ot
    enteronceforcombo = 0 

    


    # Create Add-specific widgets
    TransactionNameBoxFrom = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Transaction From", width=190, height=25)
    TransactionNameBoxFrom.place(x=5, y=25)

    TransactionNameBoxTo = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Transaction To", width=190, height=25)
    TransactionNameBoxTo.place(x=205, y=25)

    comboVal = StringVar(value="Select")
    Transaction_combobox = CTkComboBox(OutputEditContent, values=["Date", "Inventory ID", "Type", "Branch ID"], command=callback, variable=comboVal, height = 25, corner_radius=1, width=110)
    Transaction_combobox.set("Select")
    Transaction_combobox.place(x=5, y = 53)
    Transaction_combobox.configure(state="readonly")
    
    Transaction_inputbutton = CTkButton(OutputEditContent, text="Add", corner_radius=0, font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1,hover_color='#e6e6e6', width=100, height=27,command= lambda: handleaddtrans())
    Transaction_inputbutton.place(x=295, y=82)
    

    TransAddExist = True  # Mark Add mode as active

def editmodeui():
    
    vieweditemflag = 1
    global TransEditExist, TransactionIDEdit, Transaction_combobox, Transaction_inputbutton, sucessful_transaction
    global DateHolder, GoodsHolder, BranchHolder, TypeHolder, AmountHolder, PartyToHolder, PartyForHolder, StatusHolder
    DateHolder=""
    GoodsHolder=""
    BranchHolder=""
    TypeHolder="Item"
    AmountHolder = ""
    PartyToHolder=""
    PartyForHolder=""
    StatusHolder =""
    sucessful_transaction = False

    #All Flags
    global Trans_DateFlag, Trans_GoodsFlag, Trans_TypeFlag, Trans_BranchFlag, Trans_IDFlag, Trans_PartyFlag
    Trans_DateFlag=False
    Trans_GoodsFlag=False
    Trans_TypeFlag=False
    Trans_BranchFlag=False
    Trans_IDFlag = False
    Trans_PartyFlag = False
    
    global TypeChecker, typewaschecked
    TypeChecker = True #whether item or cash
    typewaschecked = False #checks whether or not type in combo box was checked or not

    global enteronce, diffvalue, enteronceforcombo
    enteronce = 0
    diffvalue = 0 #to findout which combo is working orn ot
    enteronceforcombo = 0 

    # Create Edit specific widgets
    TransactionIDEdit = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Transaction ID", width=390, height=25)
    TransactionIDEdit.place(x=5, y=25)

    comboVal = StringVar(value="Select")
    Transaction_combobox = CTkComboBox(OutputEditContent, values=["Date", "Inventory ID", "Type", "Branch ID", "Parties"], command=callback, variable=comboVal, height = 25, corner_radius=1, width=110)
    Transaction_combobox.set("Select")
    Transaction_combobox.place(x=5, y = 53)
    Transaction_combobox.configure(state="readonly")

    Transaction_inputbutton = CTkButton(OutputEditContent, text="Edit", corner_radius=0, font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#e6e6e6', width=100, height=27, command=lambda: handleedittrans())
    Transaction_inputbutton.place(x=295, y=82)
    


    TransEditExist = True  # Mark Edit mode as active

def deletemodeui():
    global TransactionIDDelete, Transaction_inputbutton, TransDeleteExist
    TransactionIDDelete = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="enter Transaction ID to delete", width=390, height = 25)
    TransactionIDDelete.place(x=5,y=25)

    Transaction_inputbutton = CTkButton(OutputEditContent, text = "Delete", command = lambda: handledeletetrans(TransactionIDDelete, Transaction_inputbutton), corner_radius=0,font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#e6e6e6', width=100, height = 27)
    Transaction_inputbutton.place (x=295, y = 82)
    TransDeleteExist = True


            
            

def handledeletetrans(TransactionIDDelete, deleteinputbutton):
    global deletebuttonrequestchecker
    ItemToDelete = TransactionIDDelete.get()
    if ItemToDelete != "":
        print("Item is deleted. Transaction =" + str(ItemToDelete))
        clearcurrentmode()
        
    else:
        print("Please enter correct field properly.")
        
def callback(choice): #COMBO BOX FUNCTIONALITIES
    global enteronce, enteronceforcombo, diffvalue, typebox,  DateHolder, GoodsHolder, BranchHolder, TypeHolder, AmountHolder, typewaschecked
    enteronce = enteronce + 1
    enteronceforcombo = enteronceforcombo + 1
    
    if mode == "add": #ADD============================COMBO
        global AddDateEntryBox, AddGoodsEntryBox, AddBranchEntryBox, amtinput, AddSearchBoxEnter, ErrorBoolean, Error
    
        
        print (enteronce)
        if enteronce > 1:
            AddSearchBoxEnter.destroy()
            enteronce = 1
            print (enteronce)
            
            
        if enteronce == 1:
            AddSearchBoxEnter = CTkButton(OutputEditContent, text = "Confirm", corner_radius=0,font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#e6e6e6', width=100, height = 27, command=lambda: confirmyourchoice(choice, AddSearchBoxEnter))
            AddSearchBoxEnter.place(x=190,y=82)

        if enteronceforcombo>1:
            if diffvalue == 1:
                AddDateEntryBox.place_forget()
            elif diffvalue == 2:
                AddGoodsEntryBox.place_forget()
            elif diffvalue == 3:
                typebox.place_forget()
                amtinput.place_forget()
            elif diffvalue == 4:
                AddBranchEntryBox.place_forget()

            enteronceforcombo = 1
            print (enteronceforcombo)

        if enteronceforcombo == 1:
            if choice == "Date": #For DATE
                diffvalue = 1
                AddDateEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Date of Transaction", width=275, height = 25)
                AddDateEntryBox.place(x=120, y = 53)
                AddDateEntryBox.configure(state="normal")
                AddDateEntryBox.insert(0,DateHolder)
                
                
            elif choice == "Inventory ID": #for Inventory
                diffvalue = 2
                AddGoodsEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Inventory Id", width=275, height = 25)
                AddGoodsEntryBox.place(x=120, y = 53)
                AddGoodsEntryBox.configure(state="normal")
                AddGoodsEntryBox.insert(0,GoodsHolder)
                
                
            elif choice == "Type": #for TYPE
                diffvalue = 3
                typewaschecked = True #this means that type was checked in terms of viewed is true, hence it will:
                comboVal = StringVar(value="Item") #set combo select to item as initial
                typebox = CTkComboBox(OutputEditContent, values=["Item", "Cash"], command=boolfortypecheck, variable=comboVal, height = 25, corner_radius=1, width=275) #whether item or cash 
                typebox.place(x=120, y = 53)
                
                amtinput = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Enter Amount", width=110, height = 27)
                amtinput.place(x=5, y = 82)
                amtinput.insert(0, AmountHolder)

                typebox.set(TypeHolder)
                typebox.configure(state="readonly")
                
            elif choice == "Branch ID": #certain BRANCH
                diffvalue = 4
                AddBranchEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Branch Id", width=275, height = 25)
                AddBranchEntryBox.place(x=120, y = 53)
                AddBranchEntryBox.insert(0,BranchHolder)

        if typewaschecked == True and choice != "Type": 
            amtinput.destroy()
            typewaschecked = False
        
        print ("diffvalue: " + str(diffvalue))
        
        if BranchHolder == "" or DateHolder == "" or GoodsHolder == "" or AmountHolder == "": #if one of these is empty, then:
            if DateHolder ==""and diffvalue == 1: #if its date holder is empty and its on the same
                AddDateEntryBox.delete(0, END)
                AddDateEntryBox.configure(placeholder_text="Date of Transaction")
            elif GoodsHolder ==""and diffvalue == 2:
                AddGoodsEntryBox.delete(0, END)
                AddGoodsEntryBox.configure(placeholder_text="Inventory Id")
            elif TypeHolder == ""and diffvalue == 3:
                typebox.delete(0, END)
                amtinput.delete(0, END)
                amtinput.configure(placeholder_text="Enter Amount")
            elif BranchHolder == "" and diffvalue == 4:
                AddBranchEntryBox.delete(0, END)
                AddBranchEntryBox.configure(placeholder_text="Branch Id")
            
        else:
            if BranchHolder != "" and diffvalue==4:
                AddBranchEntryBox.insert(0,BranchHolder)
            elif DateHolder !="" and diffvalue ==1:
                AddDateEntryBox.insert(0,DateHolder)
            elif GoodsHolder !=""and diffvalue == 2:
                AddGoodsEntryBox.insert(0, GoodsHolder)
            elif TypeHolder != "" and diffvalue==3:
                typebox.insert(0, TypeHolder)
                amtinput.insert(0, AmountHolder)
    else: #EDIT============================COMBO
        global PartyForEntryBox, PartyToEntryBox, EditDateEntryBox, EditGoodsEntryBox, EditBranchEntryBox, amtinputEdit, PartyForHolder, PartyToHolder,  EditSearchBoxEnter
        
        
        print (enteronce)
        if enteronce > 1:
            EditSearchBoxEnter.destroy()
            enteronce = 1
            print (enteronce)
            
        
        if enteronce == 1:
            EditSearchBoxEnter = CTkButton(OutputEditContent, text = "Confirm", corner_radius=0,font=BTNFont, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', border_width=1, hover_color='#e6e6e6', width=100, height = 27, command=lambda: confirmyourchoice(choice, EditSearchBoxEnter))
            EditSearchBoxEnter.place(x=190,y=82)

        if enteronceforcombo>1:
            if diffvalue == 1:
                EditDateEntryBox.destroy()
            elif diffvalue == 2:
                EditGoodsEntryBox.destroy()
            elif diffvalue == 3:
                typebox.destroy()
                amtinputEdit.destroy()
            elif diffvalue == 4:
                EditBranchEntryBox.destroy()
            elif diffvalue == 5:
                PartyToEntryBox.destroy()
                PartyForEntryBox.destroy()

            enteronceforcombo = 1
            print (enteronceforcombo)

        if enteronceforcombo == 1:
            if choice == "Date": #For DATE
                diffvalue = 1
                EditDateEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Date of Transaction", width=275, height = 25)
                EditDateEntryBox.place(x=120, y = 53)
                EditDateEntryBox.configure(state="normal")
                EditDateEntryBox.insert(0,DateHolder)
                
                
            elif choice == "Inventory ID": #for GOODS
                diffvalue = 2
                EditGoodsEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Inventory Id", width=275, height = 25)
                EditGoodsEntryBox.place(x=120, y = 53)
                EditGoodsEntryBox.configure(state="normal")
                EditGoodsEntryBox.insert(0,GoodsHolder)
                
                
            elif choice == "Type": #for TYPE
                diffvalue = 3
                comboVal = StringVar(value="Item")
                typebox = CTkComboBox(OutputEditContent, values=["Item", "Cash"], command=boolfortypecheck, variable=comboVal, height = 25, corner_radius=1, width=275)
                typebox.place(x=120, y = 53)
                
                amtinputEdit = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Enter Amount", width=120, height = 27)
                amtinputEdit.place(x=5, y = 82)
                amtinputEdit.insert(0, AmountHolder)

                typebox.set(TypeHolder)
                typebox.configure(state="readonly")
                
            elif choice == "Branch ID": #certain BRANCH
                diffvalue = 4
                EditBranchEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Branch Id", width=275, height = 25)
                EditBranchEntryBox.place(x=120, y = 53)
                EditBranchEntryBox.insert(0,BranchHolder)
            elif choice == "Parties": #EDITS WHO SENT AND WHOS SENDING TRANSACTION
                diffvalue = 5
                PartyForEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Transaction For", width=132, height = 25)
                PartyForEntryBox.place(x=120, y = 53)
                PartyForEntryBox.insert(0,PartyForHolder)
                PartyToEntryBox = CTkEntry(OutputEditContent, corner_radius=0, border_color='#000000', border_width=1, placeholder_text="Transaction To", width=132, height = 25)
                PartyToEntryBox.place(x=260, y = 53)
                PartyToEntryBox.insert(0,PartyToHolder)

        if typewaschecked == True and choice != "Type":
            amtinputEdit.destroy()
            typewaschecked = False
        
            
        if BranchHolder == "" or DateHolder == "" or GoodsHolder == "" or AmountHolder == "" or PartyForHolder == "" or PartyToHolder == "": #if blank is empty, then delete items in it
            if DateHolder ==""and diffvalue == 1:
                EditDateEntryBox.delete(0, END)
                EditDateEntryBox.configure(placeholder_text="Date of Transaction")
            elif GoodsHolder ==""and diffvalue == 2:
                EditGoodsEntryBox.delete(0, END)
                EditGoodsEntryBox.configure(placeholder_text="Inventory Id")
            elif TypeHolder == ""and diffvalue == 3:
                amtinputEdit.delete(0, END)
                amtinputEdit.configure(placeholder_text="Enter Amount")
            elif BranchHolder == "" and diffvalue == 4:
                EditBranchEntryBox.delete(0, END)
                EditBranchEntryBox.configure(placeholder_text="Branch Id")
            elif diffvalue == 5:
                if PartyForHolder == "" and PartyToHolder == "":
                    PartyForEntryBox.delete(0, END)
                    PartyForEntryBox.configure(placeholder_text="Transaction From")
                if PartyToHolder == "":
                    PartyToEntryBox.delete(0, END)
                    PartyToEntryBox.configure(placeholder_text="Transaction To")
        else: #basically checks if blank is not empty, input item already in it
            
            if DateHolder !="" and diffvalue ==1:
                EditDateEntryBox.insert(0,DateHolder)
            elif GoodsHolder !=""and diffvalue == 2:
                EditGoodsEntryBox.insert(0, GoodsHolder)
            elif TypeHolder != "" and diffvalue==3:
                typebox.insert(0, TypeHolder)
                amtinputEdit.insert(0, AmountHolder)
            elif BranchHolder != "" and diffvalue==4: 
                EditBranchEntryBox.insert(0,BranchHolder)
            elif PartyToHolder != "" and diffvalue == 5:
                PartyToEntryBox.insert(0,PartyToHolder)
            elif PartyForHolder != "" and diffvalue == 5:
                PartyForEntryBox.insert(0,PartyForHolder)
            
        
        print ("diffvalue: " + str(diffvalue))



def confirmyourchoice(choice, AddSearchBoxEnter): #CONFIRMS THE CHOICE

    global DateHolder, GoodsHolder, BranchHolder, TypeChecker, TypeHolder, typebox, AmountHolder, PartyForHolder, PartyToHolder, Trans_PartyFlag, StatusHolder
    global Trans_DateFlag, Trans_GoodsFlag, Trans_TypeFlag, Trans_BranchFlag, Trans_IDFlag
    if mode == "add":
        AddSearchBoxEnter.destroy()
        if choice == "Date" and AddDateEntryBox.get() != "":
            DateHolder = AddDateEntryBox.get()
            print (DateHolder)
            Trans_DateFlag = True
            AddDateEntryBox.configure(state="readonly")
            
        elif choice == "Inventory ID" and AddGoodsEntryBox.get() != "":
            GoodsHolder = AddGoodsEntryBox.get()
            print (GoodsHolder)
            Trans_GoodsFlag = True
            AddGoodsEntryBox.configure(state="readonly")
            
        elif choice == "Branch ID" and AddBranchEntryBox.get() != "": #im the new yanderedev
            BranchHolder = AddBranchEntryBox.get()
            print (BranchHolder)
            Trans_BranchFlag = True
            AddBranchEntryBox.configure(state="readonly")

        elif choice == "Type" and TypeHolder != "":
            if TypeChecker == True:
                TypeHolder = "Item"
            else:
                TypeHolder = "Cash"
            print (TypeHolder)
            Trans_TypeFlag = True
            AmountHolder = amtinput.get()
            amtinput.configure(state="readonly")
    elif mode=="edit": #CONFIRM EDIT CHOICE
        EditSearchBoxEnter.destroy()
        if choice == "Date" and EditDateEntryBox.get() != "": #DATE
            DateHolder = EditDateEntryBox.get()
            print (DateHolder)
            Trans_DateFlag = True
            EditDateEntryBox.configure(state="readonly")
            
        elif choice == "Inventory ID" and EditGoodsEntryBox.get() != "": #INV
            GoodsHolder = EditGoodsEntryBox.get()
            print (GoodsHolder)
            Trans_GoodsFlag = True
            EditGoodsEntryBox.configure(state="readonly")
            
        elif choice == "Branch ID" and EditBranchEntryBox.get() != "": #BRANCH
            BranchHolder = EditBranchEntryBox.get()
            print (BranchHolder)
            Trans_BranchFlag = True
            EditBranchEntryBox.configure(state="readonly")

        elif choice == "Type" and TypeHolder != "": #TYPE
            if TypeChecker == True: #if its true then its an item
                TypeHolder = "Item"
            else:
                TypeHolder = "Cash"
            print (TypeHolder)
            Trans_TypeFlag = True #checks if confirmed then flag is true
            AmountHolder = amtinputEdit.get()
            amtinputEdit.configure(state="readonly")
        elif choice == "Parties": #PARTIES
           if PartyForEntryBox.get != "" and PartyToEntryBox.get != "":
                PartyForHolder = PartyForEntryBox.get() #gets and puts
                print(PartyForHolder)
                PartyToHolder = PartyToEntryBox.get()#gets and puts
                print(PartyToHolder)

                PartyForEntryBox.configure(state="readonly")
                PartyToEntryBox.configure(state="readonly")
                
                Trans_PartyFlag = True



            
def handleaddtrans():
    global ErrorBoolean, Error, viewederror, amountedit
    global Trans_DateFlag, Trans_GoodsFlag, Trans_TypeFlag, Trans_BranchFlag
       
    global TransAddExist, TransactionNameBoxFrom, TransactionNameBoxTo, Transaction_inputbutton, Transaction_combobox, sucessful_transaction 
    
    TransactorTo =  TransactionNameBoxTo.get()
    TransactorFrom = TransactionNameBoxFrom.get()

    if TransactorTo and TransactorFrom != "": #if the transactor to and transactor from is NOT empty, then it'll post as true.
        TransactionNameForFlag = True
        TransactionNameToFlag = True
    print ("Name= " + str(Trans_DateFlag) + ", Goods= " + str(Trans_GoodsFlag) + ", Type= " + str(Trans_TypeFlag) + ", Branch= " + str(Trans_BranchFlag)) 

    if (Trans_DateFlag == True and Trans_GoodsFlag== True and Trans_TypeFlag == True and Trans_BranchFlag == True and TransactionNameToFlag == True and TransactionNameForFlag == True and AmountHolder.isnumeric()): #CHECKS IF ALL ARE TRUE AND CORRECTLY INPUTTED!!
        print("Sucessfully Submitted.")
        print("Transactor From: " + TransactorFrom)
        print("Transactor To: " + TransactorTo)
        print("Date: " + DateHolder)
        print("Goods: " + GoodsHolder)
        print("Branch ID: " + BranchHolder) 
        print("Type: " + TypeHolder)
        print("amount of type: " + AmountHolder)
        
        TransactionNameBoxTo.destroy()
        TransactionNameBoxFrom.destroy()
        Transaction_combobox.destroy()
        Transaction_inputbutton.destroy()
        
        AddBranchEntryBox.destroy()
        AddDateEntryBox.destroy()
        AddGoodsEntryBox.destroy()
        typebox.destroy()
        amtinput.destroy()
 
        if ErrorBoolean==True:
            Error.destroy()
            viewederror=0
            ErrorBoolean = False
            

    else: #prints an error
        if viewederror == 0 and not viewederror > 1:
            print("Please Input ALL entries.")
            ErrorBoolean = True
            Error = CTkLabel(OutputEditContent, text="Please Input ALL entries correctly.", text_color="red", height=13)
            Error.place(x=200, y=3)
            viewederror = 1

def handleedittrans():
    global Trans_DateFlag, Trans_GoodsFlag, Trans_TypeFlag, Trans_BranchFlag, Trans_IDFlag, Trans_PartyFlag, amountedit, diffvalue
    global amountedit, ErrorBoolean, Error, viewederror, sucessful_transaction,Transaction_inputbutton
    TransactorFrom = TransactionIDEdit.get()

    if TransactionIDEdit.get() != "": #if the transactor to and transactor from is NOT empty, then it'll post as true.
        Trans_IDFlag = True
    
    if diffvalue == 3:
        if AmountHolder.isnumeric() and Trans_TypeFlag == True:
            amountedit = True

    print ("Date= " + str(Trans_DateFlag) + ", Inventory= " + str(Trans_GoodsFlag) + ", Type= " + str(Trans_TypeFlag) + ", Branch= " + str(Trans_BranchFlag)) 
    
    if diffvalue > 0:
        if (Trans_DateFlag or Trans_GoodsFlag or Trans_TypeFlag or Trans_BranchFlag or amountedit) and Trans_IDFlag:  # CHECKS IF ALL ARE TRUE AND CORRECTLY INPUTTED!!
            print("Successfully Submitted.")
            print("TransactionID : " + TransactorFrom)
            print("Date: " + DateHolder)
            print("Goods: " + GoodsHolder)
            print("Branch ID: " + BranchHolder) 
            print("Type: " + TypeHolder)
            print("Amount of type: " + AmountHolder)
            if ErrorBoolean==True:
                Error.destroy()
                viewederror=0
                ErrorBoolean = False
            sucessful_transaction = True
            
            if Transaction_inputbutton.winfo_exists():
                Transaction_inputbutton.destroy()
            try:
                TransactionIDEdit.place_forget()
                Transaction_combobox.destroy()
            except Exception as e:
                print(f"Error destroying Transaction_combobox and TransactionIDEdit: {e}")

            try:
                if diffvalue == 0:
                    print("has not used combobox yet")
                elif diffvalue == 1:
                    EditDateEntryBox.place_forget()
                elif diffvalue == 2:
                    print(str(diffvalue) + " is set")
                    EditGoodsEntryBox.place_forget()
                elif diffvalue == 3:
                    typebox.place_forget()
                    amtinputEdit.place_forget()
                elif diffvalue == 4:
                    EditBranchEntryBox.place_forget()
                elif diffvalue == 5:
                    PartyToEntryBox.place_forget()
                    PartyForEntryBox.place_forget()
                if diffvalue > 0:
                    EditSearchBoxEnter.place_forget() 
                if ErrorBoolean == True:
                    Error.destroy()
            except Exception as e:
                print("ERROR")
            

            
            
    else: #prints an error
                print("Please Input an entry.")
                ErrorBoolean = True
                Error = CTkLabel(OutputEditContent, text="Please Input an entry.", text_color="red", height=13)
                Error.place(x=200, y=3)
                viewederror = viewederror + 1
                print(viewederror)

        
        



#FOR BOOLEAN
def boolfortypecheck(choice):
    global TypeChecker, Trans_TypeFlag
    if choice == "Item":
        TypeChecker=True
        print("Item")
    elif choice == "Cash":
        TypeChecker=False
        print("Cash")

        




# Function to handle button clicks
def button_event(page):
    salespage(page)
SalesTab = CTkButton(TABFRAME, text="Sales", width=20)
SalesTab.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")
SalesTab.configure(command=lambda: button_event(TransactionsPage))
# Show the first page by default
show_page(TransactionsPage)    
window.mainloop()

