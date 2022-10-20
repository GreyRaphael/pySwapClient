import PyHSSecuTradeApi
import time

# 接入认证应答
class CHSSecuReqAuthenticateField:
    def __init__(self):
        self.AccountID = None
        self.AppID = None
        self.AuthCode = None

# 客户登录
class CHSSecuReqUserLoginField:
    def __init__(self):
        self.AccountID = None
        self.Password = None
        self.UserApplicationType = None
        self.HSUserApplicationInfo = None
        self.MacAddress = None
        self.IPAddress = None
        self.UserStationInfo = None

# 报单录入请求
class CHSSecuReqOrderInsertField:
    def __init__(self):
        self.ExchangeID = None
        self.StockCode = None
        self.OrderCommand = None
        self.Direction = None
        self.OrderPrice = None
        self.OrderVolume = None
        self.StockAccount = None
        self.OrderRef = None
        self.CashGroupProp = None
        self.CompactID = None
        self.BatchNo = None
        self.ChannelType = None
        self.StockProperty = None
        self.ClientOrderID = None
        self.SecuPassword = None

# 报单撤单请求
class CHSSecuReqOrderActionField:
    def __init__(self):
        self.OrderPartition = None
        self.BrokerOrderID = None
        self.SessionID = None
        self.OrderRef = None
        self.ClientOrderID = None

# 资金查询
class CHSSecuReqQryFundField:
    def __init__(self):
        self.CurrencyID = None

# 持仓查询
class CHSSecuReqQryHoldField:
    def __init__(self):
        self.ExchangeID = None
        self.StockCode = None

# 报单查询
class CHSSecuReqQryOrderField:
    def __init__(self):
        self.OrderPartition = None
        self.BrokerOrderID = None
        self.SessionID = None
        self.OrderRef = None
        self.ClientOrderID = None

# 成交查询
class CHSSecuReqQryTradeField:
    def __init__(self):
        self.OrderPartition = None
        self.BrokerOrderID = None
        self.SessionID = None
        self.OrderRef = None
        self.ClientOrderID = None

# 证券账户信息查询
class CHSSecuReqQryStkAcctField:
    def __init__(self):
        self.ExchangeID = None

# 证券代码查询请求
class CHSSecuReqQryStkcodeField:
    def __init__(self):
        self.ExchangeID = None
        self.StockCode = None

# 新股申购额度查询请求
class CHSSecuReqQryEquityField:
    def __init__(self):
	    self.ExchangeID = None

# ETF代码信息查询
class CHSSecuReqQryEtfcodeField:
    def __init__(self):
        self.ExchangeID = None
        self.EtfCode = None
        self.PurRedStockCode = None

# ETF成分股信息查询请求
class CHSSecuReqQryEtfcomponentField:
    def __init__(self):
        self.ExchangeID = None
        self.PurRedStockCode = None
        self.EtfComponentCode = None

# 密码更改
class CHSSecuReqUserPasswordUpdateField:
    def __init__(self):
        self.PasswordType = None
        self.Password = None
        self.NewPassword = None

# 快速交易与集中交易之间资金调拨
class CHSSecuReqFundTransField:
    def __init__(self):
        self.TransDirection = None
        self.CurrencyID = None
        self.OccurBalance = None

# 快速交易与集中交易之间股份调拨请求
class CHSSecuReqStockTransField:
    def __init__(self):
        self.TransDirection = None
        self.StockAccount = None
        self.ExchangeID = None
        self.StockCode = None
        self.OccurVolume = None

# 质押入库债券明细查询请求
class CHSSecuReqQryImpawnDetailField:
    def __init__(self):
        self.StockAccount = None
        self.ExchangeID = None
        self.StockCode = None

# 债券入库集中度查询请求
class CHSSecuReqQryBondImpawnConcField:
    def __init__(self):
        self.ExchangeID = None
        self.StockCode = None


# 银行转账
class CHSSecuReqTransferField:
    def __init__(self):
        self.BankID  = None
        self.TransferType = None
        self.OccurBalance = None
        self.FundPassword = None
        self.BankPassword = None
        self.CurrencyID = None
        self.TransferOccasion = None

# 主柜台资金查询
class CHSSecuReqQryFundUF20Field:
    def __init__(self):
        self.CurrencyID = None


# 资金流水查询
class CHSSecuReqQryFundRealJourField:
    def __init__(self):
        self.CurrencyID = None


# 实时合约流水查询
class CHSSecuReqQryCompactRealJourField:
    def __init__(self):
        self.StockCode = None
        self.CompactSource = None
        self.CompactType = None
        self.CompactId = None
        self.BrokerOrderID = None

# 可买卖数量请求
class CHSSecuReqQryMaxEntradeNumField:
    def __init__(self):
        self.ExchangeID = None
        self.StockCode = None 
        self.OrderCommand = None
        self.Direction = None
        self.OrderPrice = None
        self.CashGroupProp = None

# 股份流水查询
class CHSSecuReqQryStockRealJourField:
    def __init__(self):
        self.ExchangeType = None;
        self.AccountID = None;

# 港股通客户个人交易汇率查询
class CHSSecuReqQryHKSecurateField:
    def __init__(self):
        self.ExchangeID = None;

# 对端快速交易中心资金查询
class CHSSecuReqQryFundPeerField:
    def __init__(self):
        self.SysnodeID = None
        self.CurrencyID = None

# 银行转账查询
class CHSSecuReqQryTransferField:
    def __init__(self):
        self.BankID = None
        self.TransferSerialID = None

# 银行余额查询
class CHSSecuReqQryBankBalanceField:
    def __init__(self):
        self.BankID = None
        self.FundPassword = None
        self.BankPassword = None
        self.CurrencyID = None

class HSSecuTradeApi:
    def __init__(self, path):
        '''
        创建交易接口
        :param flow_path: 缓存路径,str
        '''
        self.api = PyHSSecuTradeApi.PyHSSecuTradeApi(path)

    def RegisterSpi(self, pSpi):
        '''
        注册回调接口,要求实现以下函数
        :param pSpi:回调接口类的实例
        :return:
        '''
        return self.api.RegisterSpi(OnFrontConnected = pSpi.OnFrontConnected,
                                    OnFrontDisconnected = pSpi.OnFrontDisconnected,
                                    OnRspAuthenticate = pSpi.OnRspAuthenticate,
                                    OnRspUserLogin = pSpi.OnRspUserLogin,
                                    OnRspOrderInsert = pSpi.OnRspOrderInsert,
                                    OnRspOrderAction = pSpi.OnRspOrderAction,
                                    OnRspQryHold = pSpi.OnRspQryHold,
                                    OnRspQryFund = pSpi.OnRspQryFund,
                                    OnRspQryOrder = pSpi.OnRspQryOrder,
                                    OnRspQryTrade = pSpi.OnRspQryTrade,
                                    OnRspQryStkcode = pSpi.OnRspQryStkcode,
                                    OnRspQryStkAcct = pSpi.OnRspQryStkAcct,
                                    OnRspQryEquity = pSpi.OnRspQryEquity,
                                    OnRspQryEtfcode = pSpi.OnRspQryEtfcode,
                                    OnRspQryEtfcomponent = pSpi.OnRspQryEtfcomponent,
                                    OnRspUserPasswordUpdate = pSpi.OnRspUserPasswordUpdate,
                                    OnRspFundTrans = pSpi.OnRspFundTrans,
                                    OnRspStockTrans = pSpi.OnRspStockTrans,
                                    OnRspQryImpawnDetail = pSpi.OnRspQryImpawnDetail,
                                    OnRspQryBondImpawnConc = pSpi.OnRspQryBondImpawnConc,
                                    OnRspTransfer = pSpi.OnRspTransfer,
                                    OnRspQryFundUF20 = pSpi.OnRspQryFundUF20,
                                    OnRspQryFundRealJour = pSpi.OnRspQryFundRealJour,
                                    OnRspQryCompactRealJour = pSpi.OnRspQryCompactRealJour,
                                    OnRspQryMaxEntradeNum = pSpi.OnRspQryMaxEntradeNum,
                                    OnRspQryStockRealJour = pSpi.OnRspQryStockRealJour,
                                    OnRspQryHKSecurate=pSpi.OnRspQryHKSecurate,
                                    OnRspQryFundPeer=pSpi.OnRspQryFundPeer,
                                    OnRspQryTransfer=pSpi.OnRspQryTransfer,
                                    OnRspQryBankBalance=pSpi.OnRspQryBankBalance,
                                    OnRtnOrder = pSpi.OnRtnOrder,
                                    OnRtnTrade = pSpi.OnRtnTrade)

    def RegisterFront(self, pszFrontAddress):
        '''
        注册前置机网络地址
        :param pszFrontAddress: str类型；前置机网络地址,格式："tcp://" + Ip_Address + ":" + Port。
        :return:
        '''
        return self.api.RegisterFront(pszFrontAddress)

    def RegisterFensServer(self, pszFensAddress, pszAccountID):
        '''
        注册Fens网络地址
        :param pszFensAddress: str类型；Fens网络地址，格式："fens://" + Ip_Address + ":" + Port。
               pszAccountID: str类型；账号
        :return:
        '''
        return self.api.RegisterFensServer(pszFensAddress, pszAccountID)

    def Init(self, pszLicFile, pszSafeLevel  = "", pszPwd  = "", pszSslFile  = "", pszSslPwd  = ""):
        '''
        初始化连接
        :param pszLicFile:通讯证书,str
        :param pszSafeLevel :安全级别,str
        :param pszPwd :通讯密码,str
        :param pszSslFile :SSL证书,str
        :param pszSslPwd :SSL密码,str
        :return:
        '''
        return self.api.Init(pszLicFile, pszSafeLevel, pszPwd, pszSslFile, pszSslPwd)

    def Wait(self):
        '''
        等待
        :return:
        '''
        time.sleep(999999)

    def ReqAuthenticate(self, pReqAuthenticate, nRequestID):
        '''
        接入认证
        :param pReqAuthenticate: 接入认证信息,CHSSecuReqAuthenticateField类型
        :param nRequestID:请求号
        :return:
        '''
        return  self.api.ReqAuthenticate(pReqAuthenticate.__dict__, nRequestID)

    def ReqUserLogin(self, pReqUserLogin, nRequestID):
        '''
        客户登录
        :param pReqUserLogin:客户登录信息,CHSSecuReqUserLoginField类型
        :param nRequestID:请求号
        :return:
        '''
        print("ReqUserLogin", pReqUserLogin.__dict__)
        return  self.api.ReqUserLogin(pReqUserLogin.__dict__, nRequestID)

    def ReqOrderInsert(self, pReqOrderInsert, nRequestID):
        '''
        报单录入
        :param pReqOrderInsert:报单信息,CHSSecuReqOrderInsertField类型
        :param nRequestID:
        :return:
        '''
        print("ReqOrderInsert", pReqOrderInsert.__dict__)
        return self.api.ReqOrderInsert(pReqOrderInsert.__dict__, nRequestID)

    def ReqOrderAction(self, pReqOrderAction, nRequestID):
        '''
        报单撤单
        :param pReqOrderAction:撤单信息,CHSSecuReqOrderActionField类型
        :param nRequestID:
        :return:
        '''
        print("ReqOrderAction", pReqOrderAction.__dict__)
        return self.api.ReqOrderAction(pReqOrderAction.__dict__, nRequestID)

    def ReqQryHold(self, pReqQryHold, nRequestID):
        '''
        持仓查询
        :param pReqQryHold:持仓查询信息，CHSSecuReqQryHoldField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryHold", pReqQryHold.__dict__)
        return self.api.ReqQryHold(pReqQryHold.__dict__, nRequestID)

    def ReqQryFund(self, pReqQryFund, nRequestID):
        '''
        资金查询
        :param pReqQryFund:资金查询信息，CHSSecuReqQryFundField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryFund", pReqQryFund.__dict__)
        return self.api.ReqQryFund(pReqQryFund.__dict__, nRequestID)

    def ReqQryOrder(self, pReqQryOrder, nRequestID):
        '''
        报单查询
        :param req_qry_order:报单查询信息，CHSSecuReqQryOrderField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryOrder", pReqQryOrder.__dict__)
        return self.api.ReqQryOrder(pReqQryOrder.__dict__, nRequestID)

    def ReqQryTrade(self, pReqQryTrade, nRequestID):
        '''
        成交查询
        :param pReqQryTrade:成交查询信息，CHSSecuReqQryTradeField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryTrade", pReqQryTrade.__dict__)
        return self.api.ReqQryTrade(pReqQryTrade.__dict__, nRequestID)

    def ReqQryStkAcct(self, pReqQryStkAcct, nRequestID):
        '''
        股东号查询
        :param pReqQryStkAcct:
        :param nRequestID:
        :return:
        '''
        print("ReqQryStkAcct", pReqQryStkAcct.__dict__)
        return self.api.ReqQryStkAcct(pReqQryStkAcct.__dict__, nRequestID)

    def ReqQryStkcode(self, pReqQryStkcode, nRequestID):
        '''
        证券代码查询
        :param pReqQryStkcode:
        :param nRequestID:
        :return:
        '''
        print("ReqQryStkcode", pReqQryStkcode.__dict__)
        return self.api.ReqQryStkcode(pReqQryStkcode.__dict__, nRequestID)

    def ReqQryEquity(self, pReqQryEquity, nRequestID):
        '''
        新股申购额度查询
        :param pReqQryEquity:
        :param nRequestID:
        :return:
        '''
        print("ReqQryEquity", pReqQryEquity.__dict__)
        return self.api.ReqQryEquity(pReqQryEquity.__dict__, nRequestID)

    def ReqQryEtfcode(self, pReqQryEtfcode, nRequestID):
        '''
        ETF代码查询
        :param pReqQryEtfcode:
        :param nRequestID:
        :return:
        '''
        print("ReqQryEtfcode", pReqQryEtfcode.__dict__)
        return self.api.ReqQryEtfcode(pReqQryEtfcode.__dict__, nRequestID)

    def ReqQryEtfcomponent(self, pReqQryEtfcomponent, nRequestID):
        '''
        ETF成分股查询
        :param pReqQryEtfcomponent:
        :param nRequestID:
        :return:
        '''
        print("ReqQryEtfcomponent", pReqQryEtfcomponent.__dict__)
        return self.api.ReqQryEtfcomponent(pReqQryEtfcomponent.__dict__, nRequestID)


    def ReqUserPasswordUpdate(self, pReqUserPasswordUpdate, nRequestID):
        '''
        密码修改
        :param pReqUserPasswordUpdate:
        :param nRequestID:
        :return:
        '''
        print("ReqUserPasswordUpdate", pReqUserPasswordUpdate.__dict__)
        return self.api.ReqUserPasswordUpdate(pReqUserPasswordUpdate.__dict__, nRequestID)

    def ReqFundTrans(self, pReqFundTrans, nRequestID):
        '''
        快速交易与集中交易之间资金调拨
        :param pReqFundTrans:
        :param nRequestID:
        :return:
        '''
        print("ReqFundTrans", pReqFundTrans.__dict__)
        return self.api.ReqFundTrans(pReqFundTrans.__dict__, nRequestID)

    def ReqStockTrans(self, pReqStockTrans, nRequestID):
        '''
        快速交易与集中交易之间股份调拨
        :param pReqStockTrans:
        :param nRequestID:
        :return:
        '''
        print("ReqStockTrans", pReqStockTrans.__dict__)
        return self.api.ReqStockTrans(pReqStockTrans.__dict__, nRequestID)

    def ReqQryImpawnDetail(self, pReqQryImpawnDetail, nRequestID):
        '''
        质押入库债券明细查询
        :param pReqQryImpawnDetail:
        :param nRequestID:
        :return:
        '''
        print("ReqQryImpawnDetail", pReqQryImpawnDetail.__dict__)
        return self.api.ReqQryImpawnDetail(pReqQryImpawnDetail.__dict__, nRequestID)

    def ReqQryBondImpawnConc(self, pReqQryBondImpawnConc, nRequestID):
        '''
        债券入库集中度查询
        :param pReqQryBondImpawnConc:
        :param nRequestID:
        :return:
        '''
        print("ReqQryBondImpawnConc", pReqQryBondImpawnConc.__dict__)
        return self.api.ReqQryBondImpawnConc(pReqQryBondImpawnConc.__dict__, nRequestID)

    def RegisterSubModel(self,pszSubModel):
        '''
        注册订阅模式
        :param pszSubModel:订阅方式，整数型
            0-从本交易日开始重传
            1-从上次收到的续传
            2-从登录后最新的开始传
        :return:
        '''
        print("RegisterSubModel", pszSubModel)
        return self.api.RegisterSubModel(pszSubModel)

    def ReqTransfer(self,pReqTransfer, nRequestID):
        '''
        银证转账
        :param pReqTransfer:
        :param nRequestID:
        :return:
        '''
        print("ReqTransfer", pReqTransfer)
        return self.api.ReqTransfer(pReqTransfer.__dict__, nRequestID)

    def ReqQryFundUF20(self,pReqQryFundUF20, nRequestID):
        '''
        主柜台资金查询
        :param pReqQryFundUF20:主柜台资金查询参数,CHSSecuReqQryFundUF20Field类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryFundUF20", pReqQryFundUF20)
        return self.api.ReqQryFundUF20(pReqQryFundUF20.__dict__, nRequestID)

    def ReqQryFundRealJour(self, pReqQryFundRealJour, nRequestID):
        '''
        资金流水查询
        :param pReqQryFundRealJour:资金流水查询参数,CHSSecuReqQryFundRealJourField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryFundRealJour", pReqQryFundRealJour)
        return self.api.ReqQryFundRealJour(pReqQryFundRealJour.__dict__, nRequestID)
        
    def ReqQryCompactRealJour(self, pReqQryCompactRealJour, nRequestID):
        '''
        合约流水表查询
        :param pReqQryCompactRealJour:合约流水表查询参数,CHSSecuReqQryCompactRealJourField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryCompactRealJour", pReqQryCompactRealJour)
        return self.api.ReqQryCompactRealJour(pReqQryCompactRealJour.__dict__, nRequestID)

    def ReqQryMaxEntradeNum(self, pReqQryMaxEntradeNum, nRequestID):
        '''
        可买卖数量请求
        :param pReqQryMaxEntradeNum:可买卖数量请求参数,CHSSecuReqQryMaxEntradeNumField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryMaxEntradeNum", pReqQryMaxEntradeNum)
        return self.api.ReqQryMaxEntradeNum(pReqQryMaxEntradeNum.__dict__, nRequestID)        

    def ReqQryStockRealJour(self, pReqQryStockRealJour, nRequestID):
        '''
        股份流水查询
        :param pReqQryStockRealJour:股份流水查询参数,CHSSecuReqQryStockRealJourField类型
        :param nRequestID:
        :return:
        '''
        print("pReqQryStockRealJour", pReqQryStockRealJour)
        return self.api.ReqQryStockRealJour(pReqQryStockRealJour.__dict__, nRequestID)

    def ReqQryHKSecurate(self, pReqQryHKSecurate, nRequestID):
        '''
        港股通客户交易汇率查询
        :param pReqQryHKSecurate:港股通客户个人交易汇率查询,CHSSecuReqQryHKSecurateField类型
        :param nRequestID:
        :return:
        '''
        print("港股通客户交易汇率查询pReqQryHKSecurate", pReqQryHKSecurate)
        return self.api.ReqQryHKSecurate(pReqQryHKSecurate.__dict__, nRequestID)

    def ReqQryFundPeer(self, pReqQryFundPeer, nRequestID):
        '''
        对端快速交易中心资金查询
        :param pReqQryFundPeer:对端快速交易中心资金查询,CHSSecuReqQryFundPeerField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryFundPeer", pReqQryFundPeer)
        return self.api.ReqQryFundPeer(pReqQryFundPeer.__dict__, nRequestID)


    def ReqQryTransfer(self,pReqQryTransfer, nRequestID):
        '''
        银行转账查询
        :param pReqQryTransfer:银行转账查询参数,CHSSecuReqQryTransferField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryTransfer", pReqQryTransfer)
        return self.api.ReqQryTransfer(pReqQryTransfer.__dict__, nRequestID)

    def ReqQryBankBalance(self,pReqQryBankBalance, nRequestID):
        '''
        银行余额查询
        :param pReqQryBankBalance:银行余额查询参数,CHSSecuReqQryBankBalanceField类型
        :param nRequestID:
        :return:
        '''
        print("ReqQryBankBalance", pReqQryBankBalance)
        return self.api.ReqQryBankBalance(pReqQryBankBalance.__dict__, nRequestID)

def GetSecuTradeApiVersion():
    '''
    :return:
    '''
    return PyHSSecuTradeApi.GetSecuTradeApiVersion()

def SetLogCallBack(func):
    '''
    设置日志回调，函数要求只有一个参数str
    :return:
    '''
    return PyHSSecuTradeApi.SetLogCallBack(OnLogCallBack = func)