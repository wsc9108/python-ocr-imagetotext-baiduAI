from aip import AipOcr

APP_ID = '18613139'
API_KEY = 'MaVDi4OblgqdAMP4PIA1mXb1'
SECRET_KEY = 'BMmp2OBIRiAGn2vjAZl2YLB9UCeBgmtk'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

def get_file_content(filePath):
	with open(filePath, 'rb' )as fp:
		return fp.read()
	
image = get_file_content("C:\Users\jwang\Desktop\test2.jpg")

result = client.basicGeneral(image);
print (result)

for item in result['words_result']:
	print(item['words'])
