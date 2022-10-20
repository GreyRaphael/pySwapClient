import sys
import time
sys.path.append(r'..')
import HSSecuTradeSpi, HSSecuTradeApi
import threading
'''

�޸�����	 �޸İ汾      �޸���	    �޸ĵ�				 �޸�����
20220329     V6.1.0.6      ���Ƿ�       M202203240130,M202203240130 1��API֧������ת�˲�ѯ2��API֧����������ѯ
20220114     V6.1.0.5      ʩ  ��	    M202109070653       API֧�ֿͻ��˱������
20211229     V6.1.0.4      ���Ƿ�		M202111300009		API֧��˫���ĶԶ˿��ٽ��������ʽ��ѯ�ӿ�
20211213     V6.1.0.3      ������		M202111080567		����¼��ṹ��CHSSecuReqOrderInsertField����SecuPassword�ֶ�����
20210729     V6.1.0.2      ���Ƿ�		M202110251852		API֧�ָ۹�ͨ���˻��ʲ�ѯ
20210729     V6.1.0.1      ʩ  ��		 M202107012886		 �ֲֲ�ѯ������ֵ�ֶ����
20210608	 V6.1.0.0      ��ʢ־		 �ڲ�				  ͳһ�汾��V6.1.0.0
'''

#ȫ�ֱ���
class GlobalValue:
    # ���ӵ�½��Ϣ
    pszFrontAddress = "tcp://10.20.31.73:23572"     #����ǰ�õ�ip��ַ�Ͷ˿ں�
    pszFensAddress = "fens://10.20.31.73:33337"     #����Fens��ip��ַ�Ͷ˿ں�
    AccountID = "36000110"                           #�ʽ��˺�
    AppID = "1"                                     #�ͻ���ID
    AuthCode = "1234"                               #��֤��
    Password = "111111"                             #��������
    UserStationInfo = "1"                           #�û�վ����Ϣ
    UserApplicationType = '1'                       #Ͷ���߶�Ӧ�����
    iSubType = 1                                    #ע�ᶩ��ģʽ
    isSucceed = -1                                  #�Ƿ��¼�ɹ�

    retConnetRegt=None                        #���ӷ��ؽ��
    OrderInfoList = {}                        #���ί����Ϣ
    iRetFrontConnected=None                   #���ӻص����
    iResAuthen=None                           #��֤�ص����
    iRetLogin=None                            #��¼�ص����
    OrderRef = 1

class HSSecuTradeApiImpl (HSSecuTradeApi.HSSecuTradeApi):
    pass

class HSSecuTradeSpiImpl (HSSecuTradeSpi.HSSecuTradeSpi):
    def OnFrontConnected(self):
        super().OnFrontConnected()
        GlobalValue.iRetFrontConnected=0
        print("GlobalValue.iRetFrontConnected",GlobalValue.iRetFrontConnected)

    def OnFrontDisconnected(self, nResult):
        super().OnFrontDisconnected(nResult)
        GlobalValue.iRetFrontConnected = -1

    def OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast):
        super().OnRspAuthenticate(pRspAuthenticate, pRspInfo, nRequestID, bIsLast)
        GlobalValue.iResAuthen=pRspInfo

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        super().OnRspUserLogin(pRspUserLogin, pRspInfo, nRequestID, bIsLast)
        GlobalValue.iRetLogin=pRspInfo

    def OnRspOrderInsert(self, pRspOrderInsert, pRspInfo, nRequestID, bIsLast):
        super(HSSecuTradeSpiImpl, self).OnRspOrderInsert(pRspOrderInsert, pRspInfo, nRequestID, bIsLast)
        GlobalValue.OrderInfoList[nRequestID] = pRspOrderInsert

print(HSSecuTradeApi.GetSecuTradeApiVersion())
api = HSSecuTradeApiImpl("d:/")
spi = HSSecuTradeSpiImpl(api)
api.RegisterSpi(spi)

def Connect(isFens):
    if isFens:
        GlobalValue.retConnetRegt = api.RegisterFensServer(GlobalValue.pszFensAddress, GlobalValue.AccountID)  #����fens
    else:
        GlobalValue.retConnetRegt = api.RegisterFront(GlobalValue.pszFrontAddress)  #����ǰ��

    api.RegisterSubModel(GlobalValue.iSubType)                                      #ע�ᶩ��ģʽ
    retInit = api.Init("license.dat")

    if (GlobalValue.retConnetRegt != 0 | retInit != 0):
        print("������������ʧ�ܣ�")
        return GlobalValue.isSucceed
    else:
        print("������������ɹ�!")

def Authenticate():
    while True:
        if GlobalValue.iRetFrontConnected !=None:                           #ѭ���ȴ����ӳɹ�
            if GlobalValue.iRetFrontConnected==0:
                auth = HSSecuTradeApi.CHSSecuReqAuthenticateField()         #������֤Ӧ��
                auth.AccountID = GlobalValue.AccountID
                auth.AppID = GlobalValue.AppID
                auth.AuthCode = GlobalValue.AuthCode
                ret=api.ReqAuthenticate(auth, 2)
                if (ret != 0):
                    print("���ͽ�����֤����ʧ�ܣ������룺", ret)
                    return GlobalValue.isSucceed
                else:
                    print("���ͽ�����֤����ɹ�!")
                break
            else:
                print("���ӳ�ʱ������")
                return GlobalValue.isSucceed

def login():
    while True:
        if GlobalValue.iResAuthen !=None:
            if GlobalValue.iResAuthen['ErrorID'] == 0:                      #ѭ���ȴ���֤�ɹ�
                # �ͻ���¼
                login_field = HSSecuTradeApi.CHSSecuReqUserLoginField()
                login_field.AccountID = GlobalValue.AccountID
                login_field.Password = GlobalValue.Password
                login_field.UserStationInfo = GlobalValue.UserStationInfo
                login_field.UserApplicationType = GlobalValue.UserApplicationType
                ret=api.ReqUserLogin(login_field, 3)
                if(ret!=0):
                    print("���͵�¼����ʧ�ܣ������룺", ret)
                    return GlobalValue.isSucceed
                else:
                    print("���͵�¼����ɹ�!")
                break
            else:
                print("������֤ʧ��,������Ϣ��",GlobalValue.iResAuthen['ErrorMsg'])
                return GlobalValue.isSucceed

    while True:
        if GlobalValue.iRetLogin != None:                                   #ѭ���ȴ���¼�ɹ�
            if GlobalValue.iRetLogin['ErrorID'] == 0:
                isSucceed = 0
                return isSucceed
            else:
                print("��¼ʧ��,������Ϣ��", GlobalValue.iRetLogin['ErrorMsg'])
                return GlobalValue.isSucceed
    return isSucceed


def OrderInsertAction():
    # ί��1
    order_field = HSSecuTradeApi.CHSSecuReqOrderInsertField()
    order_field.ExchangeID = "1"
    order_field.StockCode = "600486"
    order_field.OrderPrice = 1.15
    order_field.OrderVolume = 200
    order_field.Direction = 1
    order_field.OrderRef = '%d' %GlobalValue.OrderRef
    GlobalValue.OrderRef +=1
    order_field.OrderCommand = 1
    order_field.CashGroupProp = '0'
    api.ReqOrderInsert(order_field, 40)

    # ί��2
    order_field = HSSecuTradeApi.CHSSecuReqOrderInsertField()
    order_field.ExchangeID = "1"
    order_field.StockCode = "600570"
    order_field.OrderPrice = 2
    order_field.OrderVolume = 200
    order_field.Direction = 1
    order_field.OrderRef = '%d' %GlobalValue.OrderRef
    GlobalValue.OrderRef += 1
    order_field.OrderCommand = 1
    order_field.CashGroupProp = '0'
    api.ReqOrderInsert(order_field, 41)

    # ί��3
    order_field = HSSecuTradeApi.CHSSecuReqOrderInsertField()
    order_field.ExchangeID = "1"
    order_field.StockCode = "600570"
    order_field.OrderPrice = 2
    order_field.OrderVolume = 200
    order_field.Direction = 1
    order_field.OrderRef = '%d' %GlobalValue.OrderRef
    GlobalValue.OrderRef += 1
    order_field.OrderCommand = 1
    order_field.CashGroupProp = '0'
    api.ReqOrderInsert(order_field, 42)

    # ����1
    while 40 not in GlobalValue.OrderInfoList.keys():  # ѭ���ȴ�ί�гɹ�
        time.sleep(1)

    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.OrderRef = GlobalValue.OrderInfoList[40]['OrderRef']
    action_field.SessionID = GlobalValue.OrderInfoList[40]['SessionID']
    api.ReqOrderAction(action_field, 50)

    # ����2
    while 41 not in GlobalValue.OrderInfoList.keys():  # ѭ���ȴ�
        time.sleep(1)

    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.BrokerOrderID = GlobalValue.OrderInfoList[41]['BrokerOrderID']
    action_field.OrderPartition = GlobalValue.OrderInfoList[41]['OrderPartition']
    api.ReqOrderAction(action_field, 51)

    
    ## ����3
    while 42 not in GlobalValue.OrderInfoList.keys():  # ѭ���ȴ�ί�гɹ�
        time.sleep(1)
    
    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.ClientOrderID = GlobalValue.OrderInfoList[42]['ClientOrderID']
    api.ReqOrderAction(action_field, 52)

def QryHold():
    # ��ѯ�ֲ�
    pReqQryHold = HSSecuTradeApi.CHSSecuReqQryHoldField()
    api.ReqQryHold(pReqQryHold, 6)
    time.sleep(1)

def QryFund():
    # �ʽ��ѯ
    pReqQryFund = HSSecuTradeApi.CHSSecuReqQryFundField()
    api.ReqQryFund(pReqQryFund, 7)
    time.sleep(1)

def QryOrder():
    # ί�в�ѯ
    pReqQryOrder = HSSecuTradeApi.CHSSecuReqQryOrderField()
    api.ReqQryOrder(pReqQryOrder, 8)
    time.sleep(1)

def QryTrade():
    # �ɽ���ѯ
    pReqQryTrade = HSSecuTradeApi.CHSSecuReqQryTradeField()
    pReqQryTrade.OrderRef = GlobalValue.OrderInfoList[41]['OrderRef']
    pReqQryTrade.SessionID = GlobalValue.OrderInfoList[41]['SessionID']
    api.ReqQryTrade(pReqQryTrade, 9)
    time.sleep(1)

def QryStkAcct():
    # ֤ȯ�˻���ѯ
    pReqQryStkAcct = HSSecuTradeApi.CHSSecuReqQryStkAcctField()
    api.ReqQryStkAcct(pReqQryStkAcct, 10)
    time.sleep(1)

def QryStkcode():
    # ֤ȯ�����ѯ
    pReqQryStkcode = HSSecuTradeApi.CHSSecuReqQryStkcodeField()
    pReqQryStkcode.StockCode = '600570'
    api.ReqQryStkcode(pReqQryStkcode, 11)
    time.sleep(1)

def QryFundUF20():
    # ����̨�ʽ��ѯ
    pReqQryFundUF20 = HSSecuTradeApi.CHSSecuReqQryFundUF20Field()
    api.ReqQryFundUF20(pReqQryFundUF20, 12)
    time.sleep(1)

def QryFundRealJour():
    # �ʽ���ˮ��ѯ
    pReqQryFundRealJour = HSSecuTradeApi.CHSSecuReqQryFundRealJourField()
    api.ReqQryFundRealJour(pReqQryFundRealJour, 13)
    time.sleep(1)

def QryStockRealJour():
    # �ɷ���ˮ��ѯ
    pReqQryStockRealJour = HSSecuTradeApi.CHSSecuReqQryStockRealJourField()
    api.ReqQryStockRealJour(pReqQryStockRealJour, 14)
    time.sleep(1)

def Transfer():
    # ��֤ת��
    pReqTransfer = HSSecuTradeApi.CHSSecuReqTransferField()
    pReqTransfer.BankID = '0008'
    pReqTransfer.TransferType = '1'
    pReqTransfer.OccurBalance = 11111
    pReqTransfer.FundPassword = '111111'
    pReqTransfer.CurrencyID = '0'
    pReqTransfer.TransferOccasion = '13445'
    api.ReqTransfer(pReqTransfer, 15)
    time.sleep(1)

def QryHKSecurate():
    # �۹�ͨ�ͻ����˽��׻��ʲ�ѯ
    pReqHKSecurate = HSSecuTradeApi.CHSSecuReqQryHKSecurateField()
    pReqHKSecurate.ExchangeID = "!"
    api.ReqQryHKSecurate(pReqHKSecurate, 16)
    time.sleep(1)

def QryFundPeer():
    # �Զ˿��ٽ��������ʽ��ѯ
    pReqQryFundPeer = HSSecuTradeApi.CHSSecuReqQryFundPeerField()
    pReqQryFundPeer.SysnodeID = 0
    pReqQryFundPeer.CurrencyID = '0'
    api.ReqQryFundPeer(pReqQryFundPeer, 17)
    time.sleep(1)

def QryTransfer():
    # ����ת�˲�ѯ
    pReqQryTransfer = HSSecuTradeApi.CHSSecuReqQryTransferField()
    pReqQryTransfer.BankID = ''
    pReqQryTransfer.TransferSerialID = 0
    api.ReqQryTransfer(pReqQryTransfer, 18)
    time.sleep(1)

def QryBankBalance():
    # ����ת�˲�ѯ
    pReqQryBankBalance = HSSecuTradeApi.CHSSecuReqQryBankBalanceField()
    pReqQryBankBalance.BankID = '0008'
    pReqQryBankBalance.FundPassword = ''
    pReqQryBankBalance.BankPassword = ''
    pReqQryBankBalance.CurrencyID = '0'
    api.ReqQryBankBalance(pReqQryBankBalance, 19)
    time.sleep(1)

def QryDefault():
    print('����ı�Ų���ȷ��')

def DealBusiness():
    while True:
        print('''
            ��ѡ���ܣ�
            [1]Front����
            [2]Fens����
            [3]����ע��
            [4]��½
            [5]ί�г���
            [6]��ѯ�ֲ�
            [7]�ʽ��ѯ
            [8]ί�в�ѯ
            [9]�ɽ���ѯ
            [10]֤ȯ�˻���ѯ
            [11]֤ȯ�����ѯ
            [12]����̨�ʽ��ѯ
            [13]�ʽ���ˮ��ѯ
            [14]�ɷ���ˮ��ѯ
            [15]��֤ת��
            [16]�۹�ͨ���׻��ʲ�ѯ
            [17]�Զ˿��ٽ��������ʽ��ѯ
            [18]����ת�˲�ѯ
            [19]��������ѯ
            [0]�˳�����
            ''')

        cmd = input()
        if cmd=='1':Connect(False)          #Front����
        elif cmd=='2':Connect(True)         #Fens����
        elif cmd=='3':Authenticate()        #����ע��
        elif cmd=='4': login()              #��½
        elif cmd=='5': OrderInsertAction()  #ί�г���
        elif cmd=='6': QryHold()            #��ѯ�ֲ�
        elif cmd=='7': QryFund()            #�ʽ��ѯ
        elif cmd=='8': QryOrder()           #ί�в�ѯ
        elif cmd=='9': QryTrade()           #�ɽ���ѯ
        elif cmd=='10': QryStkAcct()        #֤ȯ�˻���ѯ
        elif cmd=='11': QryStkcode()        #֤ȯ�����ѯ
        elif cmd=='12': QryFundUF20()       #����̨�ʽ��ѯ
        elif cmd=='13': QryFundRealJour()   #�ʽ���ˮ��ѯ
        elif cmd=='14': QryStockRealJour()  #�ɷ���ˮ��ѯ
        elif cmd=='15': Transfer()          #��֤ת��
        elif cmd=='16': QryHKSecurate()     #�۹�ͨ���׻��ʲ�ѯ
        elif cmd=='17': QryFundPeer()       #�Զ˿��ٽ��������ʽ��ѯ
        elif cmd == '18':QryTransfer()      #����ת�˲�ѯ
        elif cmd == '19':QryBankBalance()   #��������ѯ
        elif cmd=='0': return
        else:QryDefault()

def QuitDemo():
    print("�������˳���")

def main():
    qryThread = threading.Thread(target=DealBusiness)
    qryThread.start()
    qryThread.join()
    QuitDemo()

if __name__ == '__main__':
   main()