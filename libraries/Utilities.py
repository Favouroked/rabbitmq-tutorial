import pdfkit
import requests

from .Config import config


def convert_to_pdf(txt_path, name):
    options = {'page-size': 'Letter', 'margin-left': '0.75in', 'margin-bottom': '0.75in', 'margin-top': '0.75in',
               'encoding': 'UTF-8', 'margin-right': '0.75in', 'quiet': ''}
    pdf_path = "pdf-files/{}.pdf".format(name)
    pdfkit.from_file(txt_path, pdf_path, options=options)
    print("[x] Finished converting {} to pdf".format(name))
    return pdf_path


def send_email(pdf_path, book_name, email):
    print('[x] Sending e-mail to {} for book {}'.format(email, book_name))
    domain = config['mailgun']['domain']
    apiKey = config['mailgun']['apiKey']
    url = "https://api.mailgun.net/v3/{}/messages".format(domain)
    req = requests.post(
        url,
        auth=("api", apiKey),
        files=[("attachment", ('{}.pdf'.format(book_name), open(pdf_path, 'rb').read()))],
        data={"from": 'no-reply@favournifemi.me',
              "to": email,
              "subject": "Your {} pdf from wuxiaworld-crawler".format(book_name),
              "text": "The {} novel has been crawled and is attached to this mail. Thank you for using our service"
                  .format(book_name)
              }
    )
    print(req.json())
