
class HSSecuTradeSpi:
    def __init__(self, api):
        self.api = api

    def OnFrontConnected(self):
        print("OnFrontConnected")
        

    def OnFrontDisconnected(self, ret_code):
        print("OnFrontDisconnected")

    def OnRspAuthenticate(self, rsp_authenticate, rsp_info, request_id, is_last):
        print("OnRspAuthenticate==============", rsp_authenticate, rsp_info, request_id, is_last, flush=True)
        
        
        if rsp_info['ErrorID'] == 0:
            print('''
            --------------------------------
            |           注册成功            |
            --------------------------------\n''')
            


    def OnRspUserLogin(self, rsp_user_login, rsp_info, request_id, is_last):
        print("OnRspUserLogin==============", rsp_user_login, rsp_info, request_id, is_last, flush=True)
        if rsp_info['ErrorID'] == 0:
            print('''
            --------------------------------
            |           登录成功            |
            --------------------------------\n''')
            

    def OnRspOrderInsert(self, rsp_order_insert, rsp_info, request_id, is_last):
        print("OnRspOrderInsert=============", rsp_order_insert, rsp_info, request_id, is_last, flush=True)
        if rsp_info['ErrorID'] == 0:
            print('''
            --------------------------------
            |           委托成功:{}         |
            --------------------------------\n'''.format(rsp_order_insert['OrderRef']))
            self.api.order_info = rsp_order_insert

    def OnRspOrderAction(self, rsp_order_action, rsp_info, request_id, is_last):
        print("OnRspOrderAction=============", rsp_order_action, rsp_info, request_id, is_last, flush=True)
        if rsp_info['ErrorID'] == 0:
            print('''
            --------------------------------
            |           撤单成功:{}         |
            --------------------------------\n'''.format(rsp_order_action['OrigOrderRef']))

    def OnRspQryHold(self, rsp_qry_hold, rsp_info, request_id, is_last):
        print("OnRspQryHold=============", rsp_qry_hold, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询持仓成功         |
            --------------------------------\n''')

    def OnRspQryFund(self, rsp_qry_fund, rsp_info, request_id, is_last):
        print("OnRspQryFund=============", rsp_qry_fund, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询资金成功         |
            --------------------------------\n''')

    def OnRspQryOrder(self, rsp_qry_order, rsp_info, request_id, is_last):
        print("OnRspQryOrder=============", rsp_qry_order, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询委托成功         |
            --------------------------------\n''')

    def OnRspQryTrade(self, rsp_qry_trade, rsp_info, request_id, is_last):
        print("OnRspQryTrade=============", rsp_qry_trade, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询成交成功         |
            --------------------------------\n''')

    def OnRtnOrder(self, rtn_order):
        print("OnRtnOrder============", rtn_order)#下单回调结果

    def OnRtnTrade(self, rtn_order):
        print("OnRtnTrade============", rtn_order)#成交回调结果
        
    def OnRspQryStkcode(self, rsp_qry_stkcode, rsp_info, request_id, is_last):
        print("OnRspQryStkcode=============", rsp_qry_stkcode, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询证券代码成功       |
            --------------------------------\n''')

    def OnRspQryStkAcct(self, rsp_qry_stkcacct, rsp_info, request_id, is_last):
        print("OnRspQryStkAcct=============", rsp_qry_stkcacct, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询证券账户成功       |
            --------------------------------\n''')

    def OnRspQryEquity(self, rsp_qry_equity, rsp_info, request_id, is_last):
        print("OnRspQryEquity=============", rsp_qry_equity, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询新股额度成功       |
            --------------------------------\n''')

    def OnRspQryEtfcode(self, rsp_qry_etfcode, rsp_info, request_id, is_last):
        print("OnRspQryEtfcode=============", rsp_qry_etfcode, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询ETF代码成功       |
            --------------------------------\n''')

    def OnRspQryEtfcomponent(self, rsp_qry_etfcomponent, rsp_info, request_id, is_last):
        print("OnRspQryEtfcomponent=============", rsp_qry_etfcomponent, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          查询ETF成分股成功      |
            --------------------------------\n''')   
            
    def OnRspUserPasswordUpdate(self, rsp_passwd_update, rsp_info, request_id, is_last):
        print("OnRspUserPasswordUpdate=============", rsp_passwd_update, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |          密码更改成功      |
            --------------------------------\n''')

    def OnRspFundTrans(self, rsp_fund_trans, rsp_info, request_id, is_last):
        print("OnRspFundTrans=============", rsp_fund_trans, rsp_info, request_id, is_last,flush=True)

        if is_last:
            print('''
            --------------------------------
            |          资金调拨成功      |
            --------------------------------\n''')

    def OnRspStockTrans(self, rsp_qry_stock_tranas, rsp_info, request_id, is_last):
        print("OnRspStockTrans=============", rsp_qry_stock_tranas, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |          股份调拨成功      |
            --------------------------------\n''')
            
    def OnRspQryImpawnDetail(self, rsp_stock_impawndetail, rsp_info, request_id, is_last):
        print("OnRspQryImpawnDetail=============", rsp_stock_impawndetail, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |     质押入库债券明细查询成功    |
            --------------------------------\n''')

    def OnRspQryBondImpawnConc(self, rsp_qry_bondImpawnconc, rsp_info, request_id, is_last):
        print("OnRspQryBondImpawnConc======！！=======", rsp_qry_bondImpawnconc, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |        债券入库集中度查询      |
            --------------------------------\n''')

    def OnRspTransfer(self, rsp_transfer, rsp_info, request_id, is_last):
        print("OnRspTransfer=============", rsp_transfer, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |          银证转账完成         |
            --------------------------------\n''')

    def OnRspQryFundUF20(self, rsp_qry_fund_uf20, rsp_info, request_id, is_last):
        print("OnRspQryFundUF20=============", rsp_qry_fund_uf20, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |        主柜台资金查询完成       |
            --------------------------------\n''')

    def OnRspQryFundRealJour(self, rsp_qry_fund_real_jour, rsp_info, request_id, is_last):
        print("OnRspQryFundRealJour=============", rsp_qry_fund_real_jour, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |        资金流水查询完成       |
            --------------------------------\n''')

    def OnRspQryCompactRealJour(self, rsp_qry_compact_real_jour, rsp_info, request_id, is_last):
        print("OnRspQryCompactRealJour=============", rsp_qry_compact_real_jour, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |       实时合约流水查询完成      |
            --------------------------------\n''')


    def OnRspQryMaxEntradeNum(self, rsp_qry_max_entrade_num, rsp_info, request_id, is_last):
        print("OnRspQryMaxEntradeNum=============", rsp_qry_max_entrade_num, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |       可买卖数量请求完成      |
            --------------------------------\n''')


    def OnRspQryStockRealJour(self, rsp_qry_stock_real_jour, rsp_info, request_id, is_last):
        print("OnRspQryStockRealJour=============", rsp_qry_stock_real_jour, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |         股份流水查询完成       |
            --------------------------------\n''')

    def OnRspQryHKSecurate(self, rsp_qry_HKSecurate, rsp_info, request_id, is_last):
        print("OnRspQryHKSecurate=============", rsp_qry_HKSecurate, rsp_info, request_id, is_last,flush=True)
        if is_last:
            print('''
            --------------------------------
            |     港股通客户个人交易汇率查询    |
            --------------------------------\n''')

    def OnRspQryFundPeer(self, rsp_qry_fund_peer, rsp_info, request_id, is_last):
        print("OnRspQryFundPeer=============", rsp_qry_fund_peer, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |   对端快速交易中心资金查询完成    |
            --------------------------------\n''')

    def OnRspQryTransfer(self, rsp_qry_transfer, rsp_info, request_id, is_last):
        print("OnRspQryTransfer=============", rsp_qry_transfer, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |        银行转账查询完成         |
            --------------------------------\n''')

    def OnRspQryBankBalance(self, rsp_qry_bank_balance, rsp_info, request_id, is_last):
        print("OnRspQryBankBalance=============", rsp_qry_bank_balance, rsp_info, request_id, is_last, flush=True)
        if is_last:
            print('''
            --------------------------------
            |         银行余额查询完成        |
            --------------------------------\n''')