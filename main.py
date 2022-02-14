from pprint import pprint
import csv
import re

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substitution = r'+7(\2)\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def update_phones(address_book):
  updated_list = list()
  for person in address_book:
    updated_name = ' '.join(person[:3]).split(' ')
    result = [updated_name[0], updated_name[1], updated_name[2], person[3], person[4],
              re.sub(pattern, substitution, person[5]), person[6]]
    updated_list.append(result)
  # pprint(updated_list)
  return updated_list


def exlude_odd_names(new_contacts_list):
  phone_book = dict()
  for contact in new_contacts_list:
    if contact[0] and contact[1] in phone_book:
      contact_value = phone_book[contact[0]+contact[1]]
      for i in range(len(contact_value)):
        if contact[i]:
          contact_value[i] = contact[i]
    else:
      phone_book[contact[0]+contact[1]] = contact
  return list(phone_book.values())




if __name__ == '__main__':
  # pprint(contacts_list)
  new_phone_book = exlude_odd_names(update_phones(contacts_list))
  # pprint(new_phone_book)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_phone_book)