import csv


with open("course_schedule.csv", "r", newline="", encoding="UTF-8") as ifp, \
open("Trinities.csv", "w", newline="", encoding="UTF-8") as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	headers = next(reader)
	for i, row in enumerate(reader):
		for j, header in enumerate(headers):
			writer.writerow([i+1, header, row[j]])


with open("Trinities.csv", "r", newline="", encoding="UTF-8") as ifp, \
open("prefix_Trinities.csv", "w", newline="", encoding="UTF-8") as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    for row in reader:
        if row[1] in ["Ημέρα", "Ώρα έναρξης", "Ώρα λήξης"]:
            label = "l:"
        else:
            label = "u:"
        writer.writerow(["b:"+row[0], row[1], label+row[2]])


with open('prefix_Trinities.csv', 'r', newline = '') as ifp, open('URIs_Trinities.csv', 'w', newline = '') as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	convertions = {" ": "%20"}
	for s,p,o in reader:
		for special_char, conv in convertions.items():
			p = 'http://host/sw//myvocab#' + p.replace(special_char, conv)
		if o[0] == 'u':
			o = 'http://host/sw/you/resource/' + o.replace(" ", "%20")[2:]
		writer.writerow([s,p,o])


with open('URIs_Trinities.csv', 'r', encoding="UTF-8", newline='') as ifp, open('new_URIs_Trinities.csv', 'w', encoding="UTF-8", newline = '') as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for s,p,o in reader:
		new_s = s.replace("b", "_")
		new_p = "<" + p + ">"
		new_p = new_p.replace("//", "/you/", 2).replace("/you/", "//", 1)
		new_o = ""
		if o.startswith("l:"):
			content  = o.split("l:")[1]
			if "#Start%20time" in p or "#End%20time" in p:
				time = '"' + content + ':00"'
				new_o = time + "^^" + "<" + "http://www.w3.org/2001/XMLSchema" +"#time" +">"
			else:
				new_o = '"' + content + '"'
		elif o.startswith("http://"):
			new_o = '<' + o + '>'
		else:
			new_o = '"' + o + '"'
		print("{} {} {} .".format(new_s, new_p, new_o))
