from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv('USER')
PRINTER = os.getenv('PRINTER')

END_FILE = '.pdf'

FOLDER_PATH = f"/home/{USER}/Pessoal/Certificados/"

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith(END_FILE):
        filepath = os.path.join(FOLDER_PATH, filename)
        
        print('Print file:', filename)
        
        os.system(f"lp -d {PRINTER} {filepath}")