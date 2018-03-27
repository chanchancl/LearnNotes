
# 一个统计文件中所有blance的程序，
# 每个记录以换行符分割，数据可能出现不能转换为float的内容
# 数据在 carddata.txt, 日志在cardlog.txt


def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError) as diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError:
        log.write('no txns this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachline in txns:
        result = safe_float(eachline)
        if isinstance(result, float):
            total += result
            log.write('data ... processed\n')
        else:
            log.write('ignored: %s\n' % result)
    print('$%.2f (new blance)' % total)
    log.close()


if __name__ == '__main__':
    main()
