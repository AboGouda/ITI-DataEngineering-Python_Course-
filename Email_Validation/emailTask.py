import csv
import json
def email_is_valid(email):
    try:
        if '@' not in email:
            return False

        user, domain = email.split('@')

        if not user or not domain:
            return False

        if '..' in domain:
            return False

        domain_parts = domain.split('.')

        if len(domain_parts) < 2 or any(part.strip() == '' for part in domain_parts):
            return False

        return True
    except:
        return False


with open(r'c:\Users\Abo Gouda\Downloads\dummy_emails_unique_names.csv', mode='r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

filtered_data = list(filter(lambda x: email_is_valid(x['Email']), data))


domains = [x['Email'].split('@')[1] for x in filtered_data]
unique_domains = set(domains)


with open(r'altr.json', mode='w', encoding='utf-8') as json_file:
    json.dump(filtered_data, json_file, indent=4)


