from pprint import pprint
import csv
import re

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substitution = r'+7(\2)\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def update(address_book):
  updated_list = list()
  for person in address_book:
    updated_name = ' '.join(person[:3]).split(' ')
    result = [updated_name[0], updated_name[1], updated_name[2], person[3], person[4],
              re.sub(pattern, substitution, person[5]), person[6]]
    updated_list.append(result)
  pprint(updated_list)




if __name__ == '__main__':
  # pprint(contacts_list)
  update(contacts_list)
