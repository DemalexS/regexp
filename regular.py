from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
def format_contact(contacts_list):
  pattern = r'(\+7|8)\s*\(?(\d{3})\)?(\s?|-)*(\d{3})\-*(\d{2})\-*(\d{2})\s?(\(?)(доб\.\s\d+)?(\)?)?'
  regex = re.compile(pattern)
  format_contact_list = []
  for people in contacts_list:
    f_numb = regex.sub(r"+7(\2)\4-\5-\6 \8", people[5])
    f_lname = people[0].split(' ')
    f_fname = people[1].split(' ')
    f_format = []
    if len(f_lname) > 1 or len(f_fname) > 1:
      if len(f_lname) > 1:
        if len(f_lname) > 2:
          f_format = [f_lname[0], f_lname[1], f_lname[2], people[3], people[4], f_numb, people[6]]
        else:
          f_format = [f_lname[0], f_lname[1], people[2], people[3], people[4], f_numb, people[6]]
      if len(f_fname) > 1:
        f_format = [people[0], f_fname[0], f_fname[1], people[3], people[4], f_numb, people[6]]
    else:
      f_format = [people[0], people[1], people[2], people[3], people[4], f_numb, people[6]]

    format_contact_list.append(f_format)
  return format_contact_list

def delete_duplicates_contact(format_contact_list):
  phone_book = dict()
  for contact in format_contact_list:
    if contact[0] in phone_book:
      contact_value = phone_book[contact[0]]
      for i in range(len(contact_value)):
        if contact[i]:
          contact_value[i] = contact[i]
    else:
      phone_book[contact[0]] = contact
  return list(phone_book.values())

new_phonebook = delete_duplicates_contact(format_contact(contacts_list))
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_phonebook)