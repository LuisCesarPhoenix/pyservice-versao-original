from src.utils.owncloud_utils import download_file, upload_file
from src.services.file_service import process_csv
from src.services.report_service import generate_pdf_report

def process_message(file_path):
    """Processa o arquivo recebido da fila"""
    local_file = download_file(file_path)
    processed_file = process_csv(local_file)

    report_pdf = processed_file.replace(".xlsx", ".pdf")
    generate_pdf_report(processed_file, report_pdf)

    upload_file(processed_file, "dados_enriquecidos.xlsx")
    upload_file(report_pdf, "relatorio.pdf")
