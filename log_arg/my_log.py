import logging
import datetime
import argparse


logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
#logging.debug('this is debug')
#logging.info('this is info')
#logging.warning('this is warning')

def get_args():
    parser = argparse.ArgumentParser(description="ARGS MACHINE")
    #parser.add_argument('-n', dest='host_name',  required=True, help='Enter hostname')
    parser.add_argument('-l', dest='log_it', default='off')
    #parser.add_argument('-u', dest='login_user', required=True, help='Enter User ID')
    #parser.add_argument('-p', dest='login_pass', required=True, help='Enter password')
    return parser.parse_args()

def do_log(mess):
    if log_flag == 'on':
        logging.info(mess)
        return
    else:
        pass


def try_me():
    note = "This is my note"
    snap = datetime.datetime.now()
    #logging.info(str(snap) + ': %' + note)
    do_log(str(snap) + ': %' + note)
    return




if __name__ == '__main__':
    args = get_args()
    log_flag = args.log_it
    try_me()


