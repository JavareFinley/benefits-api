from django.utils.translation import gettext as _
from decouple import config
import sendgrid
import csv
from io import StringIO
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition
import base64
from screener.views import eligibility_results, eligibility_results_translation


def email_pdf(target_email, screen_id, language):
    raw_data = eligibility_results(screen_id)
    data = eligibility_results_translation(raw_data, language)

    data_reduced = []
    for item in data:
        item.pop('legal_status_required', None)
        item.pop('failed_tests', None)
        item.pop('passed_tests', None)
        item.pop('short_name', None)
        item.pop('apply_button_link', None)
        if item['eligible']:
            item.pop('eligible', None)
            data_reduced.append(item)
    data_reduced = sorted(data_reduced, key=lambda x: x['estimated_value'], reverse=True)
    col_names = list(data_reduced[0].keys())
    cell_text = []
    cell_text.append(col_names)
    for item in data_reduced:
        cell_text.append(list(item.values()))

    f = StringIO()
    csv.writer(f).writerows(cell_text)
    encoded = base64.b64encode(f.getvalue().encode())
    encoded = str(encoded, 'utf-8')
    sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID'))
    from_email = Email("screener@garycommunity.org")  # Change to your verified sender
    to_email = To(target_email)  # Change to your recipient
    subject = _("Screener Results from My Friend Ben")
    content = Content("text/plain", _("Thank you for using our benefits screener. Your results are attached as a csv file that can be opened in any spreadsheet software."))
    mail = Mail(from_email, to_email, subject, content)
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('text/csv')
    attachment.file_name = FileName('results.csv')
    attachment.disposition = Disposition('attachment')
    mail.add_attachment(attachment)

    sg.client.mail.send.post(request_body=mail.get())
