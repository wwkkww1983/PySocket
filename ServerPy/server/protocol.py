#****************************************************
# 作者：YYC
# 功能：通信协议号
# 日期：2017-10-28
#****************************************************

INVALID = -1        #无用协议

class PROTOCOL:
    LOGINREQUEST  = 0  # 登陆请求
    LOGINDATA     = 1  # 服务器数据
    CLOSESOCKET   = 2  # 关闭套接字
    PERSONINFOREQ = 3  # 个人信息请求
    PERSONINFO    = 4  # 个人信息数据
    SAVEPERSONREQ = 5  # 保存个人信息

    #*************   好友相关   *************
    FRIENDLISTREQ = 10     # 好友列表请求
    FRIENDLISTINFO = 11    # 好友列表信息
    SELECTFRIENDREQ = 12   # 查找好友
    SELECTFRIENDINFO = 13  # 查找好友信息
    ADDFRIENDREQ  = 14     # 添加好友
    ADDFRIENDINFO = 15     # 添加好友回馈
    AGREERIENDREQ = 16     # 同意好友请求
    AGREERIENDINFO = 17    # 同意好友信息
    SUBFRIENDREQ  = 18     # 删除好友
    SUBFRIENDINFO = 19     # 删除好友回馈
    SENDMESSAGEREQ = 20    # 发送消息请求
    SENDMESSAGEINFO = 21   # 发送消息信息


