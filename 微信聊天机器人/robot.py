import itchat
from wxpy import *  # 导入wxpy库

@itchat.msg_register(TEXT)   # @是函数的修饰，作用：如果收到是纯文字信息，则执行下面的函数
def text_reply(msg):
    print(msg.text)
    reply_text = msg.text.replace('吗？', '!')
    print(reply_text)
    return reply_text

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    print(msg)
    msg.download(msg.fileName)  # 以fileNmae命名 存到Python文件所在的文件夹下



bot = Bot()  # 登录微信web
xiaobin = bot.mps().search('小栤机器人')[0]  # 机器人设为小栤机器人, 关注微信公众号：小栤机器人
group = bot.groups()  # 找出所有群聊，为避免小冰跑到群里说话
chat = 0
@bot.register()  # 接受所有消息
def forward_others(msg):
    global chat
    global group
    # if msg.chat != xiaobin and msg.chat not in group:  # 消息不是小冰的，也不是群消息，则转发给小冰，意思就和好友聊天
    if msg.chat != xiaobin :
        chat = msg.chat  # 说话的人
        msg.forward(xiaobin)  # 转发消息给小冰
    else:
        if msg.chat == xiaobin:  # 说话对象是小冰
            msg.forward(chat, suffix='--彬彬机器人')  # 转发消息给，对你说话的好友，并且在小冰的消息后面加上‘--XX’

bot.join()

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()   # 保证在一直运行

