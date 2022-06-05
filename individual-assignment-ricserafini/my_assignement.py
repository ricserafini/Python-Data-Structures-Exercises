import csv

def parse_csv_to_graph(path):
	try:
		graph = {}
		with open(path, 'r') as file:
			csv_iterator = csv.reader(file)

			for row in csv_iterator:
				if row[0] == 'source':
					continue

				if row[0] not in graph:
					graph[row[0]] = []		
				graph[row[0]].append(row[1])

		return graph

	except:
		return None

print(parse_csv_to_graph('comedians.csv'))





	
	