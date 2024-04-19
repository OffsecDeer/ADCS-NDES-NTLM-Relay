# ADCS-NDES-NTLM-Relay

Recover ADCS NDES OTPs and enrollment passwords

Clone impacket and replace the original `impacket/examples/ntlmrelayx/attacks/httpattack.py` with this one, update the package:
```text
pip3 install .
```

Run like so:

```text
ntlmrelayx.py -t https://srv-ndes/certsrv/mscep_admin/ -smb2support
```

![image](https://github.com/OffsecDeer/ADCS-NDES-NTLM-Relay/assets/21975499/6ba7e9b2-4630-4b31-9bc2-93115db3f0d7)

If the NDES certificate has a client authentication EKU (as they usually do) and no policy modules are in place we can submit the RA a CSR to impersonate arbitrary users. Details on my [Medium](https://medium.com/@offsecdeer/abusing-adcs-ndes-for-privilege-escalation-e4d306c9ca97).
If the server uses a non-default `PasswordVDir` the URL needs to be changed manually from the source AND specified in the command line.
