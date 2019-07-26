import imaplib

def geimail(host, port, mail, password):
    M = imaplib.IMAP4_SSL(host, port)
    print(M)
    try:
        try:
            M.login(mail, password)
            print('成功登陆邮箱')
        except Exception as e:
            print('登陆错误: %s' % e)
            M.close()
        # 选取收件箱
        M.select('INBOX')
        # 获取未读邮件信息
        unseen = M.search(None, 'Unseen')
        unseen_list = unseen[1][0].split()
        print('未读邮件数：', len(unseen_list))
        # 想获取最新一封:
        typ, data = M.search(None, 'ALL')
        msglist = data[0].split()
        print('已读邮件数：', len(msglist))
    except Exception as e:
        print('imap error: %s' % e)
        M.close()
    M.logout()

if __name__ == "__main__":
    Email = input('Email: ')
    Password = input('Password: ')
    IMAP_server = input('IMAP server: ')
    IMAP_port = input('IMAP port: ')
    print('开始获取')
    geimail(IMAP_server, IMAP_port, Email, Password)
