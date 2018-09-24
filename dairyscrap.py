from selenium import webdriver
import time
import xlwt
names=[]
numbers=[]
chrome_path=r"C:\Users\Vaisansar\Desktop\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
#driver.get('https://www.justdial.com/Mumbai/Dairy-Shops')
#Change url with correct page number here
driver.get('https://www.justdial.com/Mumbai/Dairy-Product-Retailers/nct-10152687/page-2')

for i in range(10):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#Wait for it to load. Till then, paste the paste.js content in console
#Replace Each span class with correct value since its name changes dynamically
time.sleep(10)
print("Send stuff")
time.sleep(10)
a=driver.find_elements_by_class_name('lng_cont_name')
#Get All Names

for x in a:
	names.append(x.text)
b=driver.find_elements_by_css_selector('.contact-info a')
for y in b:
	numbers.append(y.text)



workbook=xlwt.Workbook(encoding='utf-8')
sheet=workbook.add_sheet('Content')
row=0
sheet.write(row,0,"Name")
sheet.write(row,1,"Number")
row=row+1
#This writes to a file called contacts2.xls
#it will only have data for that particular page. Copy it later to contacts.xls
#Because contents of contacts2.xls will be overwritten next time you run the script
#So keep copy-pasting to a big file.
for i in range(0,len(names)):
	sheet.write(row,0,names[i])
	sheet.write(row,1,numbers[i])
	row=row+1
workbook.save("contacts2.xls")