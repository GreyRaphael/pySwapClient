import sys
import time
sys.path.append(r'..')
import HSSecuTradeSpi, HSSecuTradeApi
import threading
'''

修改日期	 修改版本      修改人	    修改单				 修改内容
20220329     V6.1.0.6      常亚凤       M202203240130,M202203240130 1、API支持银行转账查询2、API支持银行余额查询
20220114     V6.1.0.5      施  凯	    M202109070653       API支持客户端报单编号
20211229     V6.1.0.4      常亚凤		M202111300009		API支持双中心对端快速交易中心资金查询接口
20211213     V6.1.0.3      吴鹏飞		M202111080567		报单录入结构体CHSSecuReqOrderInsertField新增SecuPassword字段输入
20210729     V6.1.0.2      常亚凤		M202110251852		API支持港股通个人汇率查询
20210729     V6.1.0.1      施  凯		 M202107012886		 持仓查询增加市值字段输出
20210608	 V6.1.0.0      陈盛志		 内部				  统一版本到V6.1.0.0
'''

#全局变量
class GlobalValue:
    # 连接登陆信息
    pszFrontAddress = "tcp://10.20.31.73:23572"     #连接前置的ip地址和端口号
    pszFensAddress = "fens://10.20.31.73:33337"     #连接Fens的ip地址和端口号
    AccountID = "36000110"                           #资金账号
    AppID = "1"                                     #客户端ID
    AuthCode = "1234"                               #认证码
    Password = "111111"                             #交易密码
    UserStationInfo = "1"                           #用户站点信息
    UserApplicationType = '1'                       #投资者端应用类别
    iSubType = 1                                    #注册订阅模式
    isSucceed = -1                                  #是否登录成功

    retConnetRegt=None                        #连接返回结果
    OrderInfoList = {}                        #存放委托信息
    iRetFrontConnected=None                   #连接回调结果
    iResAuthen=None                           #认证回调结果
    iRetLogin=None                            #登录回调结果
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
        GlobalValue.retConnetRegt = api.RegisterFensServer(GlobalValue.pszFensAddress, GlobalValue.AccountID)  #连接fens
    else:
        GlobalValue.retConnetRegt = api.RegisterFront(GlobalValue.pszFrontAddress)  #连接前置

    api.RegisterSubModel(GlobalValue.iSubType)                                      #注册订阅模式
    retInit = api.Init("license.dat")

    if (GlobalValue.retConnetRegt != 0 | retInit != 0):
        print("发送连接请求失败！")
        return GlobalValue.isSucceed
    else:
        print("发送连接请求成功!")

def Authenticate():
    while True:
        if GlobalValue.iRetFrontConnected !=None:                           #循环等待连接成功
            if GlobalValue.iRetFrontConnected==0:
                auth = HSSecuTradeApi.CHSSecuReqAuthenticateField()         #接入认证应答
                auth.AccountID = GlobalValue.AccountID
                auth.AppID = GlobalValue.AppID
                auth.AuthCode = GlobalValue.AuthCode
                ret=api.ReqAuthenticate(auth, 2)
                if (ret != 0):
                    print("发送接入认证请求失败，错误码：", ret)
                    return GlobalValue.isSucceed
                else:
                    print("发送接入认证请求成功!")
                break
            else:
                print("连接超时。。。")
                return GlobalValue.isSucceed

def login():
    while True:
        if GlobalValue.iResAuthen !=None:
            if GlobalValue.iResAuthen['ErrorID'] == 0:                      #循环等待认证成功
                # 客户登录
                login_field = HSSecuTradeApi.CHSSecuReqUserLoginField()
                login_field.AccountID = GlobalValue.AccountID
                login_field.Password = GlobalValue.Password
                login_field.UserStationInfo = GlobalValue.UserStationInfo
                login_field.UserApplicationType = GlobalValue.UserApplicationType
                ret=api.ReqUserLogin(login_field, 3)
                if(ret!=0):
                    print("发送登录请求失败，错误码：", ret)
                    return GlobalValue.isSucceed
                else:
                    print("发送登录请求成功!")
                break
            else:
                print("接入认证失败,错误信息：",GlobalValue.iResAuthen['ErrorMsg'])
                return GlobalValue.isSucceed

    while True:
        if GlobalValue.iRetLogin != None:                                   #循环等待登录成功
            if GlobalValue.iRetLogin['ErrorID'] == 0:
                isSucceed = 0
                return isSucceed
            else:
                print("登录失败,错误信息：", GlobalValue.iRetLogin['ErrorMsg'])
                return GlobalValue.isSucceed
    return isSucceed


def OrderInsertAction():
    # 委托1
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

    # 委托2
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

    # 委托3
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

    # 撤单1
    while 40 not in GlobalValue.OrderInfoList.keys():  # 循环等待委托成功
        time.sleep(1)

    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.OrderRef = GlobalValue.OrderInfoList[40]['OrderRef']
    action_field.SessionID = GlobalValue.OrderInfoList[40]['SessionID']
    api.ReqOrderAction(action_field, 50)

    # 撤单2
    while 41 not in GlobalValue.OrderInfoList.keys():  # 循环等待
        time.sleep(1)

    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.BrokerOrderID = GlobalValue.OrderInfoList[41]['BrokerOrderID']
    action_field.OrderPartition = GlobalValue.OrderInfoList[41]['OrderPartition']
    api.ReqOrderAction(action_field, 51)

    
    ## 撤单3
    while 42 not in GlobalValue.OrderInfoList.keys():  # 循环等待委托成功
        time.sleep(1)
    
    action_field = HSSecuTradeApi.CHSSecuReqOrderActionField()
    action_field.ClientOrderID = GlobalValue.OrderInfoList[42]['ClientOrderID']
    api.ReqOrderAction(action_field, 52)

def QryHold():
    # 查询持仓
    pReqQryHold = HSSecuTradeApi.CHSSecuReqQryHoldField()
    api.ReqQryHold(pReqQryHold, 6)
    time.sleep(1)

def QryFund():
    # 资金查询
    pReqQryFund = HSSecuTradeApi.CHSSecuReqQryFundField()
    api.ReqQryFund(pReqQryFund, 7)
    time.sleep(1)

def QryOrder():
    # 委托查询
    pReqQryOrder = HSSecuTradeApi.CHSSecuReqQryOrderField()
    api.ReqQryOrder(pReqQryOrder, 8)
    time.sleep(1)

def QryTrade():
    # 成交查询
    pReqQryTrade = HSSecuTradeApi.CHSSecuReqQryTradeField()
    pReqQryTrade.OrderRef = GlobalValue.OrderInfoList[41]['OrderRef']
    pReqQryTrade.SessionID = GlobalValue.OrderInfoList[41]['SessionID']
    api.ReqQryTrade(pReqQryTrade, 9)
    time.sleep(1)

def QryStkAcct():
    # 证券账户查询
    pReqQryStkAcct = HSSecuTradeApi.CHSSecuReqQryStkAcctField()
    api.ReqQryStkAcct(pReqQryStkAcct, 10)
    time.sleep(1)

def QryStkcode():
    # 证券代码查询
    pReqQryStkcode = HSSecuTradeApi.CHSSecuReqQryStkcodeField()
    pReqQryStkcode.StockCode = '600570'
    api.ReqQryStkcode(pReqQryStkcode, 11)
    time.sleep(1)

def QryFundUF20():
    # 主柜台资金查询
    pReqQryFundUF20 = HSSecuTradeApi.CHSSecuReqQryFundUF20Field()
    api.ReqQryFundUF20(pReqQryFundUF20, 12)
    time.sleep(1)

def QryFundRealJour():
    # 资金流水查询
    pReqQryFundRealJour = HSSecuTradeApi.CHSSecuReqQryFundRealJourField()
    api.ReqQryFundRealJour(pReqQryFundRealJour, 13)
    time.sleep(1)

def QryStockRealJour():
    # 股份流水查询
    pReqQryStockRealJour = HSSecuTradeApi.CHSSecuReqQryStockRealJourField()
    api.ReqQryStockRealJour(pReqQryStockRealJour, 14)
    time.sleep(1)

def Transfer():
    # 银证转账
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
    # 港股通客户个人交易汇率查询
    pReqHKSecurate = HSSecuTradeApi.CHSSecuReqQryHKSecurateField()
    pReqHKSecurate.ExchangeID = "!"
    api.ReqQryHKSecurate(pReqHKSecurate, 16)
    time.sleep(1)

def QryFundPeer():
    # 对端快速交易中心资金查询
    pReqQryFundPeer = HSSecuTradeApi.CHSSecuReqQryFundPeerField()
    pReqQryFundPeer.SysnodeID = 0
    pReqQryFundPeer.CurrencyID = '0'
    api.ReqQryFundPeer(pReqQryFundPeer, 17)
    time.sleep(1)

def QryTransfer():
    # 银行转账查询
    pReqQryTransfer = HSSecuTradeApi.CHSSecuReqQryTransferField()
    pReqQryTransfer.BankID = ''
    pReqQryTransfer.TransferSerialID = 0
    api.ReqQryTransfer(pReqQryTransfer, 18)
    time.sleep(1)

def QryBankBalance():
    # 银行转账查询
    pReqQryBankBalance = HSSecuTradeApi.CHSSecuReqQryBankBalanceField()
    pReqQryBankBalance.BankID = '0008'
    pReqQryBankBalance.FundPassword = ''
    pReqQryBankBalance.BankPassword = ''
    pReqQryBankBalance.CurrencyID = '0'
    api.ReqQryBankBalance(pReqQryBankBalance, 19)
    time.sleep(1)

def QryDefault():
    print('输入的编号不正确！')

def DealBusiness():
    while True:
        print('''
            请选择功能：
            [1]Front连接
            [2]Fens连接
            [3]接入注册
            [4]登陆
            [5]委托撤单
            [6]查询持仓
            [7]资金查询
            [8]委托查询
            [9]成交查询
            [10]证券账户查询
            [11]证券代码查询
            [12]主柜台资金查询
            [13]资金流水查询
            [14]股份流水查询
            [15]银证转账
            [16]港股通交易汇率查询
            [17]对端快速交易中心资金查询
            [18]银行转账查询
            [19]银行余额查询
            [0]退出程序
            ''')

        cmd = input()
        if cmd=='1':Connect(False)          #Front连接
        elif cmd=='2':Connect(True)         #Fens连接
        elif cmd=='3':Authenticate()        #接入注册
        elif cmd=='4': login()              #登陆
        elif cmd=='5': OrderInsertAction()  #委托撤单
        elif cmd=='6': QryHold()            #查询持仓
        elif cmd=='7': QryFund()            #资金查询
        elif cmd=='8': QryOrder()           #委托查询
        elif cmd=='9': QryTrade()           #成交查询
        elif cmd=='10': QryStkAcct()        #证券账户查询
        elif cmd=='11': QryStkcode()        #证券代码查询
        elif cmd=='12': QryFundUF20()       #主柜台资金查询
        elif cmd=='13': QryFundRealJour()   #资金流水查询
        elif cmd=='14': QryStockRealJour()  #股份流水查询
        elif cmd=='15': Transfer()          #银证转账
        elif cmd=='16': QryHKSecurate()     #港股通交易汇率查询
        elif cmd=='17': QryFundPeer()       #对端快速交易中心资金查询
        elif cmd == '18':QryTransfer()      #银行转账查询
        elif cmd == '19':QryBankBalance()   #银行余额查询
        elif cmd=='0': return
        else:QryDefault()

def QuitDemo():
    print("程序已退出！")

def main():
    qryThread = threading.Thread(target=DealBusiness)
    qryThread.start()
    qryThread.join()
    QuitDemo()

if __name__ == '__main__':
   main()