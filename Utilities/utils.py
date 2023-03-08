
class Utils:
    #get the list and print the list one by one
    def printListItemText(self,list):
        print(len(list))
        for alltitles in list:
            print(alltitles.text)

     # get the title that doesnot have 'searchinput' in it
    def assertInListItemText(self, lists, textassert):
        for alltitles in lists:
            if (textassert)  in alltitles.text:
                print("Titles that have " + textassert + " in it: ", alltitles.text)

    #get the title that doesnot have 'searchinput' in it
    def assertNotInListItemText(self,lists,textassert):
        for alltitles in lists:
            if (textassert) not in alltitles.text:
                print("Titles that doesnot have " + textassert+ " in it: " , alltitles.text)






