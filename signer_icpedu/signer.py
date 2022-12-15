import sys
import datetime
import re
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from endesive.pdf import pdf
from endesive.pdf import cms


class Sign:

    def __init__(self, email, password, filePath, certificatePath):
        self.email = email
        self.password = password
        self.filePath = filePath
        self.certificatePath = certificatePath

        isValidEmail = self.setEmail(email)
        isValidPassword = self.setPassword(password)
        if (not isValidEmail) or (not isValidPassword):
            print("ALGO ERRADO")
            raise Exception("Email inválido")


    # def initialize(self, email, password, filePath, certificatePath):
    #     isValidEmail = self.setEmail(email)
    #     isValidPassword = self.setPassword(password)
    #     self.filePath = filePath
    #     self.certificatePath = certificatePath

    #     if (not isValidEmail) or (not isValidPassword):
    #         print("ALGO ERRADO")
    #         raise Exception("Email inválido")


    def setEmail(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            print("Valid Email")
            self.email = email
            return True
        else:
            print("Invalid Email")
            # raise Exception("Email inválido")
            return False    
    
    def setPassword(self, password):
        if len(password) > 0: 
            print("Valid Input")
            self.password = password
            return True
        else:
            print("Invalid Input")
            return False

   


    # def certificadoContainsExtension(certificatePath):
    #     if('.p12' in certificatePath):
    #         return certificatePath
    #     else:
    #         return certificatePath + '.p12'

    # def pdfContainsExtension(pdfPath):
    #     if('.pdf' in pdfPath):
    #         return pdfPath
    #     else:
    #         return pdfPath + '.pdf'

    # def signFile(email, password, filePath, certificatePath):
        
    #     certificatePath = certificadoContainsExtension(certificatePath)
    #     filePath = pdfContainsExtension(filePath)

    #     date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
    #     date = date.strftime('%Y%m%d%H%M%S+00\'00\'')

    #     dct = {
    #         "aligned": 0,
    #         "sigflags": 3,
    #         "sigflagsft": 132,
    #         "sigpage": 0,
    #         "sigbutton": True,
    #         "sigfield": "Signature1",
    #         "auto_sigfield": True,
    #         "sigandcertify": True,
    #     # "signaturebox": (5, 805, 35, 835),
    #     # "signature_img": "selo.jpg",
    #         'contact': email,
    #         'location': 'Brazil',
    #         'signingdate': date,
    #         'reason': 'Autoria do documento',
    #         "password": password,
    #     }

    #     with open(certificatePath, 'rb') as fp:
    #         p12 = pkcs12.load_key_and_certificates(
    #             fp.read(), 
    #             password.encode("ascii"), 
    #             backends.default_backend()
    #         )
            
    #     datau = open(filePath, "rb").read()
    #     datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
    #     with open('arquivo-assinado.pdf', "wb") as fp:
    #         fp.write(datau)
    #         fp.write(datas)


def main():
    sign = Sign("kemuel@sal.com", "20sasd0", "asasds", "sadsda")
    print(sign.email)
        
main()