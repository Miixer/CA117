class Contact(object):

   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return ("{} {} {}".format(self.name, self.phone, self.email))

class ContactList(object):

   def __init__(self):
      self.d = {}

   def add_contact(self, contact):
      self.d[contact.name] = contact

   def del_contact(self, contact):
      if contact in self.d:
         del self.d[contact]

   def get_contact(self, contact):
      if contact in self.d:
         return self.d[contact]
      else:
         return ("{} : No such contact".format(contact))

   def __str__(self):
      string = "Contact list\n------------"
      for key in sorted((self.d).keys()):
         string += "\n{}".format(self.d[key])
      return string

import sys

def main():
   cl = ContactList()
   for line in sys.stdin:
      [name, phone, email] = line.strip().split()
      c = Contact(name, phone, email)
      cl.add_contact(c)

   print(cl.get_contact('Jimmy'))
   print(cl.get_contact('Mary'))

   print(cl)
   cl.del_contact('Maggie')
   cl.del_contact('Maggie')

   c = Contact('Sue', '087-6442378', 'sue@eircom.net')
   cl.add_contact(c)
   c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
   cl.add_contact(c)
   print(cl)

if __name__ == '__main__':
   main()