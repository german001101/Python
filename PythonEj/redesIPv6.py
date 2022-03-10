#!/usr/bin/env python3
class cargaListaIPv6():
    def __init__(self):
        self.nombreLinkMGM = "MGN6_OLT_ZTE_Ontario_"
        self.nombreLinkHSD = "HSD6_OLT_ZTE_Ontario_"
        self.nombreLinkIPTV = "IPTV6_OLT_ZTE_Ontario_"
        self.nombrePolicy = "OLT_Jalisco_4_6"
        self.prefixMangement = ["2806:310:18::/48", "2806:310:1b::/48", "2806:310:1e::/48", "2806:310:21::/48", "2806:310:24::/48", "2806:310:27::/48", "2806:310:2a::/48", "2806:310:2d::/48", "2806:310:30::/48", "2806:310:33::/48"]
        self.prefixIanaHsd = ["2806:310:19::/96", "2806:310:1c::/96", "2806:310:1f::/96", "2806:310:22::/96", "2806:310:25::/96", "2806:310:28::/96", "2806:310:2b::/96", "2806:310:2e::/96", "2806:310:31::/96", "2806:310:34::/96"]
        self.prefixIapdHsd = ["2806:310:19:8000::/49", "2806:310:1c:8000::/49", "2806:310:1f:8000::/49", "2806:310:22:8000::/49", "2806:310:25:8000::/49", "2806:310:28:8000::/49", "2806:310:2b:8000::/49", "2806:310:2e:8000::/49", "2806:310:31:8000::/49", "2806:310:34:8000::/49"]
        self.prefixIanaIpt = ["2806:310:1a::/96", "2806:310:1d::/96", "2806:310:20::/96", "2806:310:23::/96", "2806:310:26::/96", "2806:310:29::/96", "2806:310:2c::/96", "2806:310:2f::/96", "2806:310:32::/96", "2806:310:35::/96"]
        self.prefixIapdIptv = ["2806:310:1a:8000::/49", "2806:310:1d:8000::/49", "2806:310:20:8000::/49", "2806:310:23:8000::/49", "2806:310:26:8000::/49", "2806:310:29:8000::/49", "2806:310:2c:8000::/49", "2806:310:2f:8000::/49", "2806:310:32:8000::/49", "2806:310:35:8000::/49"]
        self.liNomMGM = []
        self.liNomHSD = []
        self.liNomIPTV = []
        self.cantPrefix = 0
    
    def countPrefix(self):
        for x in range(len(self.prefixMangement)):
            self.cantPrefix += 1

    def createLink(self):
        for x in range(self.cantPrefix):
            listaMGM="link {}{} create".format(self.nombreLinkMGM,x+1)
            listaHSD="link {}{} create".format(self.nombreLinkHSD,x+1)
            listaIPTV="link {}{} create".format(self.nombreLinkIPTV,x+1)
            print("link {}{} create".format(self.nombreLinkMGM,x+1))
            print("link {}{} create".format(self.nombreLinkHSD,x+1))
            print("link {}{} create".format(self.nombreLinkIPTV,x+1))
            self.liNomMGM.append(listaMGM)
            self.liNomHSD.append(listaHSD)
            self.liNomIPTV.append(listaIPTV)
        return (self.liNomMGM,self.liNomHSD,self.liNomIPTV)
    
    def ipv6Prefix(self):
        
        for x in range(len(self.prefixMangement)):
            print("######################################################################################")
            print("##################################MANAGEMENT OLT_{}####################################".format(x+1))
            print("######################################################################################")
            print("prefix {}{} create {}".format(self.nombreLinkMGM,x+1,self.prefixMangement[x]))
            print("prefix {}{} set range={}".format(self.nombreLinkMGM,x+1,self.prefixMangement[x]))
            print("prefix {}{} set dhcp-type=dhcp".format(self.nombreLinkMGM,x+1,self.nombreLinkMGM,x+1))
            print("prefix {}{} set link={}".format(self.nombreLinkMGM,x+1,self.liNomMGM[x]))
            print("prefix {}{} set policy={}".format(self.nombreLinkMGM,x+1,self.nombrePolicy))
            print("######################################################################################")
            print("#######################################HSD OLT_{}######################################".format(x+1))
            print("######################################################################################")
            print("prefix {}IANA_{} create {}".format(self.nombreLinkHSD,x+1,self.prefixIanaHsd[x]))
            print("prefix {}IANA_{} set range={}".format(self.nombreLinkHSD,x+1,self.prefixIanaHsd[x]))
            print("prefix {}IANA_{} set dhcp-type=dhcp".format(self.nombreLinkHSD,x+1))
            print("prefix {}IANA_{} set link={}".format(self.nombreLinkHSD,x+1,self.liNomHSD[x]))
            print("prefix {}IANA_{} set policy={}".format(self.nombreLinkHSD,x+1,self.nombrePolicy))

            print("prefix {}IAPD_{} create {}".format(self.nombreLinkHSD,x+1,self.prefixIapdHsd[x]))
            print("prefix {}IAPD_{} set range={}".format(self.nombreLinkHSD,x+1,self.prefixIapdHsd[x]))
            print("prefix {}IAPD_{} set dhcp-type=prefix-delegation".format(self.nombreLinkHSD,x+1))
            print("prefix {}IAPD_{} set link={}".format(self.nombreLinkHSD,x+1,self.nombreLinkHSD,x+1))
            print("prefix {}IAPD_{} set policy={}".format(self.nombreLinkHSD,x+1,self.nombrePolicy))

            print("######################################################################################")
            print("#######################################IPTV OLT_{}#####################################".format(x+1))
            print("######################################################################################")
            print("prefix {}IANA_{} create {}".format(self.nombreLinkIPTV,x+1,self.prefixIanaIpt[x]))
            print("prefix {}IANA_{} set range={}".format(self.nombreLinkIPTV,x+1,self.prefixIanaIpt[x]))
            print("prefix {}IANA_{} set dhcp-type=dhcp".format(self.nombreLinkIPTV,x+1))
            print("prefix {}IANA_{} set link={}".format(self.nombreLinkIPTV,x+1,self.liNomIPTV[x]))
            print("prefix {}IANA_{} set policy={}".format(self.nombreLinkIPTV,x+1,self.nombrePolicy))

            print("prefix {}IAPD_{} create {}".format(self.nombreLinkIPTV,x+1,self.prefixIapdIptv[x]))
            print("prefix {}IAPD_{} set range={}".format(self.nombreLinkIPTV,x+1,self.prefixIapdIptv[x]))
            print("prefix {}IAPD_{} set dhcp-type=prefix-delegation".format(self.nombreLinkIPTV,x+1))
            print("prefix {}IAPD_{} set link={}".format(self.nombreLinkIPTV,x+1,self.nombreLinkIPTV,x+1))
            print("prefix {}IAPD_{} set policy={}".format(self.nombreLinkIPTV,x+1,self.nombrePolicy))

#Bloque Principal
listaPrefix = cargaListaIPv6()
listaPrefix.countPrefix()
listaPrefix.createLink()
listaPrefix.ipv6Prefix()
