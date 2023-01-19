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
    
    # Verificador do formato do email 
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
    
    # Verificador se a senha está em branco
    def setPassword(self, password):
        if len(password) > 0: 
            print("Valid Input")
            self.password = password
            return True
        else:
            print("Invalid Input")
            return False

    def certificadoContainsExtension(self):
        if('.p12' in self.certificatePath):
            return self.certificatePath
        else:
            return self.certificatePath + '.p12'

    def pdfContainsExtension(self):
        if('.pdf' in self.filePath):
            return self.filePath
        else:
            return self.filePath + '.pdf'

    def signFile(self):
        # 
        certificatePath = self.certificadoContainsExtension()
        filePath = self.pdfContainsExtension()

        date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
        date = date.strftime('%Y%m%d%H%M%S+00\'00\'')

        dct = {
            "aligned": 0,
            "sigflags": 3,
            "sigflagsft": 132,
            "sigpage": 0,
            "sigbutton": True,
            "sigfield": "Signature1",
            "auto_sigfield": True,
            "sigandcertify": True,
            # "signaturebox": (470, 840, 570, 640),
            # "signature": "Assinado digitalmente por: \n\n  ",
            # "signature_img": "selo.jpg",
            'contact': self.email,
            'location': 'Brazil',
            'signingdate': date,
            'reason': 'Autoria do documento',
            "password": self.password,
        }

        with open(certificatePath, 'rb') as fp:
            p12 = pkcs12.load_key_and_certificates(
                fp.read(), 
                self.password.encode("ascii"), 
                backends.default_backend()
            )
            
        datau = open(filePath, "rb").read()
        datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
        with open('arquivo-assinado.pdf', "wb") as fp:
            fp.write(datau)
            fp.write(datas)

    # def verifySignature(self):
    #     certificatePath = self.certificadoContainsExtension()
    #     trusted_cert_pems = (
    #         open(certificatePath, 'rb').read(),
    #     )
    #     data = open("arquivo-assinado.pdf", "rb").read()
        
    #     no = 0
    #     for (hashok, signatureok, certok) in pdf.verify(
    #         data, trusted_cert_pems, "/etc/ssl/certs"
    #     ):
    #         print("*" * 10, "signature no:", no)
    #         print("signature ok?", signatureok)
    #         print("hash ok?", hashok)
    #         print("cert ok?", certok)


    # def verificar_assinatura_string(self, message, signature):
    #         public_key = self.certificado.key.public_key()
    #         return public_key.verify(
    #             signature,
    #             message,
    #             padding.PSS(
    #                 mgf=padding.MGF1(hashes.SHA1()),
    #                 salt_length=padding.PSS.MAX_LENGTH
    #             ),
    #             hashes.SHA1()
    #         )


def main():
    sign = Sign("kemuel@gmail.com", "Kemuel20", "pdf", "kemuel")
    sign.signFile()
    
        
main()