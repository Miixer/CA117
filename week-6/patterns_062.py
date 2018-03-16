from re import findall
import sys

date = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2}"
phone = r"\b\d{2}[-\s]\d{7}\b"
email = r"\b\S*@\S*\b"
ldate = r"\b\d{2}\s[a-zA-Z]*\s\d{2}"

def main():
   assert(len(date) < 30)
   assert(len(phone) < 30)
   assert(len(email) < 40)
   assert(len(ldate) < 80)

   s = sys.stdin.read()

   datelist = findall(date, s)
   print("Dates: {}".format(datelist))

   phonelist = findall(phone, s)
   print('Phones: {}'.format(phonelist))

   emaillist = findall(email, s)
   print('Emails: {}'.format(emaillist))

   ldatelist = findall(ldate, s)
   print('Long dates: {}'.format(ldatelist))

if __name__ == '__main__':
   main()