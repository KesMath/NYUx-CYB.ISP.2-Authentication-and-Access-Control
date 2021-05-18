import os
import stat

def chnge_group_perms():
    '''
    assuming error handling is taken care of
    to revert permissions to mirror ones in directory: 'chmod 644 testfile.txt'
    '''
    os.chmod("lab_soln/testfile.txt", stat.S_IWGRP | stat.S_IXGRP)



if __name__ == '__main__':
    chnge_group_perms()