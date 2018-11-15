import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    print('email sent')
    server.quit()
    return problems
    server.quit()
    sendemail(from_addr    = '', #your email address
              to_addr_list = [''],# end recipient 
              cc_addr_list = [''], # cc address
              subject      = 'Test', 
              message      = 'Test', 
              login        = '', #enter google login
              password     = '') # enter google password
