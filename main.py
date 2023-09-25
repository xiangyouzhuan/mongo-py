import argparse
import configparser

import pymongo
from happy_python import HappyLog, HappyConfigParser
from mongo_tool.insert import insertOne
from sys import argv

dfg = configparser.ConfigParser()
dfg.read('conf/config.ini')
ip = dfg['mongo']['ip']
port = int(dfg['mongo']['port'])

client = pymongo.MongoClient(host=ip, port=port)


def main():
    parser = argparse.ArgumentParser(prog='mongo_tool',
                                     description='mongo工具',
                                     usage='%(prog)s [-n] [-i file] [-d file] [-u file] [-q file]')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-i',
                       '--insert',
                       help='插入file',
                       required=False,
                       nargs=1,
                       action='store',
                       metavar='file',
                       dest='insert')

    group.add_argument('-u',
                       '--update',
                       help='更改数据',
                       required=False,
                       nargs=1,
                       action='store',
                       metavar='file',
                       dest='update')

    group.add_argument('-q',
                       '--query',
                       help='查询数据库数据',
                       required=False,
                       nargs=1,
                       action='store',
                       metavar=('file'),
                       dest='query')

    group.add_argument('-d',
                       '--delete',
                       help='从mongodb下载文件',
                       required=False,
                       nargs=1,
                       action='store',
                       metavar=('file'),
                       dest='delete')

    parser.add_argument('-v',
                        '--version',
                        help='显示版本信息',
                        action='version',
                        version='%(prog)s v1.0.0')

    args = parser.parse_args()

    if args.insert:  # 完成
        print('insert；')
        insertOne(argv[2])
        # directive = 'list %s' % ('' if args.insert == '__default__' else args.list)
        pass
    elif args.delete:  # 完成
        print('delete')
        pass
    elif args.update:  # 完成
        print('update')
        pass
    elif args.query:  # 完成
        print('query:')
        # query
        pass
    # elif args.download:#完成
    #     directive = 'download %s %s' % (args.download[0], args.download[1])
    #     pass
    else:
        print('命令行参数错误，请查看使用说明')
        parser.print_help()
        exit(1)

    # client.run(directive=directive, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
