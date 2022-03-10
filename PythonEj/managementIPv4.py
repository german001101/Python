#!/usr/bin /env python3

class cargaListaIpv4():
    def __init__(self):
        self.listaIpv4 = ["29.204.192.0", "29.204.224.0", "29.205.0.0", "29.205.32.0", "29.205.64.0", "29.205.96.0", "29.205.128.0", "29.205.160.0", "29.205.192.0", "29.205.224.0"]
        self.mascara = "255.255.224.0"
        self.nombreScope = "VOZ4_JALISCO_"
        self.nombrePolicy = "OLT_JaliscoMGM4"
        self.cantScope = 0
        self.ligw=[]
        self.liFh=[]
        self.liMh=[]
        self.liLh=[]
        self.liRange=[]
    def countScope(self):
        for x in range(len(self.listaIpv4)):
            self.cantScope += 1
    def gateway(self):
        for x in self.listaIpv4:
            separadorGw = "."
            separadorGw = x.split(separadorGw)
            separadorGw[3] = int(separadorGw[3])+1
            separadorGw[3] = str(separadorGw[3])
            separadorGw = '.'.join(separadorGw)
            self.ligw.append(separadorGw)
        return self.ligw
    #########################Rango##############################
    def firstHost(self):
        for x in self.listaIpv4:
            separadorFh = "."
            separadorFh = x.split(separadorFh)
            separadorFh[3]= int(separadorFh[3])+4
            separadorFh[3]=str(separadorFh[3])
            separadorFh = ".".join(separadorFh)
            self.liFh.append(separadorFh)
        return self.liFh
    def mediumHost(self):
        for x in self.listaIpv4:
            separadorMh = "."
            separadorMh = x.split(separadorMh)
            separadorMh[2] = int(separadorMh[2])+3
            separadorMh[2] = str(separadorMh[2])
            separadorMh = ".".join(separadorMh)
            self.liMh.append(separadorMh)    
        return self.liMh
    def lastHost(self):
        for x in self.liMh:
            separadorLh = "."
            separadorLh = x.split(separadorLh)
            separadorLh[3] = int(separadorLh[3])+254
            separadorLh[3] = str(separadorLh[3])
            separadorLh = ".".join(separadorLh)
            self.liLh.append(separadorLh)
        return self.liLh
    #########################FIN RANGO##############################
    def rangeScope(self):
        for x in range(self.cantScope):
            print("#################################################################################################")
            print("###########################NETWORK {}{} IPv4#####################################".format(self.nombreScope,x+1))
            print("#################################################################################################")
            print("scope {}{} create {} {}".format(self.nombreScope,x+1,self.listaIpv4[x],self.mascara))
            print("scope {}{} addRange {} {}".format(self.nombreScope,x+1,self.liFh[x],self.liLh[x]))
            print("scope {}{} unset primary-subnet".format(self.nombreScope,x+1))
            print("scope {}{} set policy={}".format(self.nombreScope,x+1,self.nombrePolicy))
            print("scope {}{} set selection-tag-list={}{}".format(self.nombreScope,x+1,self.nombreScope,x+1))
            print("scope-policy {}{} setOption routers {}".format(self.nombreScope,x+1,self.ligw[x]))

# bloque principal
listaScope = cargaListaIpv4()
listaScope.countScope()
listaScope.gateway()
listaScope.firstHost()
listaScope.mediumHost()
listaScope.lastHost()
listaScope.rangeScope()